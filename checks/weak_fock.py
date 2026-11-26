"""Measure the Minkowski one-particle weight per octave from the clock Hessian."""

from cmath import exp
from math import comb, factorial, isclose, pi

from joint_spherical_hessian import falling


CAP = 1 / 3
WIDTH = 1 / 6
NEWTON = 1.0
CURRENT = 3 / (5120 * NEWTON)


def master_jet(y, order):
    # f_W = (16a/5!) width^5 y^5 (1-y)^12 (1+y)^12, |y| < 1.
    # The factored evaluation preserves the high-order zero at the outer end.
    value = 0.0
    for i in range(order + 1):
        for j in range(order - i + 1):
            k = order - i - j
            value += (comb(order, i) * comb(order-i, j) * (-1)**j
                      * falling(5, i) * falling(12, j) * falling(12, k)
                      * y**(5-i) * (1-y)**(12-j) * (1+y)**(12-k))
    return 16 * CAP * WIDTH**(5-order) * value / factorial(5)


def slope_terms(s):
    # Coefficients of f^(j) for j=2,3,4,5 in the optical slope G'_f.
    return -3/(4*s**4), 3/(4*s**3), -5/(16*s**2), 1/(16*s)


def hessian_samples(panels):
    samples = []
    for i in range(panels + 1):
        y = i / panels
        s = CAP + WIDTH*y
        terms = slope_terms(s)
        slope = sum(c * master_jet(y, j) for j, c in enumerate(terms, 2))
        if i == 0:
            assert isclose(slope, 1)
        weight = 1 if i in (0, panels) else (4 if i % 2 else 2)
        measure = weight * WIDTH / (3*panels) * (3/20) * s*(1-s) * slope
        samples.append((WIDTH*y, *(measure*c for c in terms)))
    return samples


def spectral_weight(k, samples):
    # H(k) is the original mixed Hessian on exp(-ik(s-a)), with a smooth
    # test cutoff equal to one on this reference's support. Divide by k^4
    # before accumulating the dimensionless weight d mu / d log k.
    z = -1j*k
    coeff = [z**j / k**4 for j in range(2, 6)]
    h = sum(exp(z*x) * (b2*coeff[0] + b3*coeff[1] + b4*coeff[2] + b5*coeff[3])
            for x, b2, b3, b4, b5 in samples)
    return abs(h)**2 / (pi*CURRENT)


def octave_weight(lo, samples):
    # Simpson in log k, returning the band norm divided by log 2.
    panels = 16
    values = [spectral_weight(lo*2**(i/panels), samples) for i in range(panels + 1)]
    return (values[0] + values[-1] + 4*sum(values[1:-1:2])
            + 2*sum(values[2:-1:2])) / (3*panels)


def main():
    coefficient = 3*NEWTON*(1-CAP)**2 / (20*pi)
    assert isclose(coefficient, 1/(15*pi))
    samples = hessian_samples(4096)
    for lo in (256, 512, 1024, 2048, 4096):
        weight = octave_weight(lo, samples)
        print(f"[{lo}, {2*lo}]  one-particle weight / log(2) = {weight:.9f}")
    refined = octave_weight(lo, hessian_samples(8192))
    assert isclose(weight, refined, rel_tol=3e-4)
    assert isclose(refined, coefficient, rel_tol=2e-3)
    print(f"Sharp rim coefficient 1/(15 pi) = {coefficient:.9f}")


if __name__ == '__main__':
    main()
