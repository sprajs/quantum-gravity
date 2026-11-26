"""Average the exact optical bracket for Gaussian exposures separated by lambda*h."""

from fractions import Fraction
from math import erf, exp, fsum, isclose, pi, sqrt

from weak_clock_contact import (
    CAP, OMEGA, build_sections, cross_bracket, evaluate, integrate, product,
)


def contact_slope(sections, jump):
    regular = [(lo, hi, {n-1: n*c for n, c in z.items() if n})
               for lo, hi, z in sections]
    bulk = sum(integrate(product(v, v), lo, hi) for lo, hi, v in regular)
    traces = sum(evaluate(v, CAP) for lo, hi, v in regular if CAP in (lo, hi))
    return OMEGA * (bulk + jump*traces) / 2


def delayed_samples(sections, jump, h, panels):
    # The density difference in the integrand vanishes at x=0, where the
    # sharp bracket has two traces. The omitted Gaussian tails start at x=18.
    step = Fraction(18, panels)
    samples = []
    for i in range(1, panels+1):
        x = i*step
        weight = 1 if i == panels else (4 if i % 2 else 2)
        bracket = cross_bracket(sections, jump, h*x)
        samples.append((float(x), float(weight*step*bracket/3)))
    return samples


def gaussian_average(samples, separation):
    def density(x):
        return exp(-(x-separation)**2/4) / sqrt(4*pi)

    return fsum(weight*(density(x)-density(-x)) for x, weight in samples)


def main():
    sections, jump = build_sections()
    slope = contact_slope(sections, jump)
    assert slope == Fraction(535896929, 29327760)
    h = Fraction(1, 100000)
    coarse = delayed_samples(sections, jump, h, 192)
    fine = delayed_samples(sections, jump, h, 384)
    assert gaussian_average(fine, 0) == 0
    for separation in (0.5, 2.0):
        bracket = gaussian_average(fine, separation)
        assert gaussian_average(fine, -separation) == -bracket
        assert isclose(bracket, gaussian_average(coarse, separation), abs_tol=3e-9)
        limiting = erf(separation/2)/30
        measured_slope = (bracket-limiting)/(separation*float(h))
        assert isclose(measured_slope, float(slope), rel_tol=1e-4)
        print(f"lambda={separation:.1f}: B_h={bracket:.9f}, "
              f"balanced added variance={bracket/2:.9f}, limit={limiting/2:.9f}")
    print(f"One-sided regular slope {slope} (G_N=hbar=1)")


if __name__ == "__main__":
    main()
