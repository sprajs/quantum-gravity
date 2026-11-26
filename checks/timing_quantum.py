"""Evaluate the quantum clock's timing dependence from the full optical response."""

from cmath import exp as cexp
from math import exp, factorial, fsum, isclose, log, pi, sqrt

from weak_clock_contact import OMEGA, build_sections


def boundary_jets(sections):
    """Jumps of every classical derivative of z, including the exterior zeros."""
    jumps = {}
    for lower, upper, polynomial in sections:
        for position, sign in ((lower, 1), (upper, -1)):
            coefficients = jumps.setdefault(position, {})
            for degree, term in polynomial.items():
                for order in range(degree + 1):
                    jet = term * (factorial(degree) // factorial(degree-order))
                    jet *= position**(degree-order)
                    coefficients[order] = coefficients.get(order, 0) + sign * jet
    return [(float(position), [float(values.get(i, 0)) for i in range(max(values)+1)])
            for position, values in jumps.items()]


def spectral_weight(k, jets):
    # Repeated integration by parts on the polynomial pieces gives the exact
    # transform of the measure z', including its atom and its regular density.
    inv_ik = 1 / (1j*k)
    transformed = 0j
    for position, jumps in jets:
        endpoint = 0j
        for coefficient in reversed(jumps):
            endpoint = coefficient + inv_ik * endpoint
        transformed += cexp(-1j*k*position) * endpoint
    return float(OMEGA) * abs(transformed)**2 / pi


def detector(u):
    # Fourier transform of N(0,1) density times (1 + (t^3-3t)/3)^2 /(5/3).
    square = u*u
    real = 1 + (6 + square * (-18 + square*(9-square))) / 9
    return exp(-square/2) * complex(real, 2*u**3/3) / (5/3)


def check_timing_densities():
    # Direct time-domain probability and moments also check the ordering sign.
    panels = 16384
    step = 24 / panels
    moments = [[0.0]*3 for _ in range(2)]
    earlier_minus = 0.0
    later_bias = 0.0
    for i in range(panels):
        t = -12 + (i+0.5)*step
        h3 = (t**3 - 3*t) / 3
        weight = step * exp(-t*t/2) / (sqrt(2*pi) * (5/3))
        plus, minus = weight*(1+h3)**2, weight*(1-h3)**2
        for sums, mass in zip(moments, (plus, minus)):
            for order in range(3):
                sums[order] += mass * t**order
        later_bias += plus * (1 - 2*earlier_minus - minus)
        earlier_minus += minus
    for row in moments:
        for value, target in zip(row, (1, 0, 17/5)):
            assert isclose(value, target, abs_tol=1e-12)
    assert isclose(pi*later_bias/2, 23*sqrt(pi)/200, rel_tol=1e-6)


def integrate_filters(width, jets, panels):
    # u = k*width/2. The three integrands in d log u vanish at both ends.
    lower, upper = log(1e-6), log(16)
    step = (upper-lower) / panels
    octave, relative, bracket = [], [], []
    for i in range(panels + 1):
        u = exp(lower + i*step)
        weight = spectral_weight(2*u/width, jets)
        if i not in (0, panels):
            weight *= 4 if i % 2 else 2
        plus = detector(u)
        minus = plus.conjugate()  # the other profile is its time reflection
        octave.append(weight * (abs(detector(u/2))**2 - abs(plus)**2))
        relative.append(weight * abs(plus-minus)**2)
        bracket.append(weight * (plus*minus.conjugate()).imag)
    return [step*fsum(values)/3 for values in (octave, relative, bracket)]


def main():
    check_timing_densities()
    sections, _ = build_sections()
    jets = boundary_jets(sections)
    c = 1 / (15*pi)
    targets = (c*log(2), c*16/25, c*23*sqrt(pi)/200)
    for width in (1e-7, 1e-9):
        values = integrate_filters(width, jets, 2048)
        for value, target in zip(values, targets):
            assert isclose(value, target, rel_tol=2e-5)
        print(f"h={width:.0e}: one-particle octave {values[0]:.9f}, "
              f"relative norm squared {values[1]:.9f}, bracket {values[2]:.9f}")
    refined = integrate_filters(width, jets, 4096)
    for coarse, fine in zip(values, refined):
        assert isclose(coarse, fine, rel_tol=2e-7)
    print("Reflected equal-moment detectors: relative norm / C = 16/25, "
          "bracket / C = 23 sqrt(pi)/200")


if __name__ == "__main__":
    main()
