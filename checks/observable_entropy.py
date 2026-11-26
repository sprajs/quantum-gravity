"""Conditional Schwarzschild entropy checks. Run with standard-library Python 3."""
from fractions import Fraction
from math import exp, isclose, log, log1p, pi, sqrt


def emission_log_weights(s, alpha, x):
    """Entropy difference from losing the fraction x of the initial energy."""
    return s * (-2 * x + x * x) + 2 * alpha * log1p(-x)


def two_loss_terms(s, alpha, x, y):
    """Separate the area and logarithm in the mixed second difference."""
    area_term = 2 * s * x * y
    log_term = 2 * alpha * log1p(-x * y / ((1 - x) * (1 - y)))
    return area_term, log_term


def simpson(function, lower, upper, steps=4096):
    width = (upper - lower) / steps
    middle = sum((4 if i % 2 else 2) * function(lower + i * width)
                 for i in range(1, steps))
    return (function(lower) + middle + function(upper)) * width / 3


def main():
    # Power of s in the spin-summed density per unit mass after removing exp(s).
    alpha = Fraction(106, 45)
    clock_powers = (alpha + Fraction(1, 2), alpha + 1)
    for k in clock_powers:
        # Independent quadrature of each proposed normalized measure.
        half_area = simpson(lambda z: z ** (float(k) - 1), 0, 0.5)
        all_areas = simpson(lambda z: z ** (float(k) - 1), 0, 1)
        assert isclose(all_areas, 1 / float(k), rel_tol=1e-10)
        probability = half_area / all_areas
        assert isclose(probability, 2 ** -float(k), rel_tol=1e-10)
        mean_clock_fraction = simpson(lambda z: sqrt(z) * z ** (float(k) - 1), 0, 1) / all_areas
        q = 2 * k / (1 + 2 * k)
        assert isclose(mean_clock_fraction, float(q), rel_tol=1e-10)
        print(f"clock exponent {k}, P(half area) = {probability:.6f}, q = {q}")

    # Check the Jacobian on a fixed interval in a moderate-size toy spectrum.
    # In this check only, m is a dimensionless mass normalized so that s = m^2.
    density_s = lambda s: exp(s) * s ** (float(alpha) - 0.5)
    area_count = simpson(density_s, 4, 9)
    mass_count = simpson(lambda m: 2 * m * density_s(m * m), 2, 3)
    assert isclose(area_count, mass_count, rel_tol=1e-11)
    print(f"matched mass-bin / area-bin count = {mass_count / area_count:.12f}")

    # Direct finite differences at a moderate test area check signs and factors.
    s_test, x, y = 80.0, 0.03, 0.07
    delta = (emission_log_weights(s_test, alpha, x + y)
             - emission_log_weights(s_test, alpha, x)
             - emission_log_weights(s_test, alpha, y))
    assert isclose(delta, sum(two_loss_terms(s_test, alpha, x, y)), rel_tol=1e-13)

    # SI constants and one illustrative mass of about ten solar masses.
    G, c, k_B = 6.67430e-11, 299792458, 1.380649e-23
    hbar = 6.62607015e-34 / (2 * pi)
    M = 1.98847e31
    planck_mass = sqrt(hbar * c / G)
    s = 4 * pi * (M / planck_mass) ** 2
    T_H = hbar * c**3 / (8 * pi * G * M * k_B)
    x = k_B * T_H / (M * c**2)
    assert isclose(x, 1 / (2 * s))
    fractional_shift = -float(alpha) / (s + float(alpha))
    area_term, log_term = two_loss_terms(s, alpha, x, x)
    print(f"s = {s:.4e}, alpha log(s) = {float(alpha) * log(s):.3f}")
    print(f"T_H = {T_H:.4e} K, dT/T_H = {fractional_shift:.4e}, dT = {T_H * fractional_shift:.4e} K")
    print(f"two thermal quanta: area term = {area_term:.4e}, log term = {log_term:.4e}")


if __name__ == "__main__":
    main()
