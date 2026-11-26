#!/usr/bin/env python3
"""Check the same-midpoint pair of spherical Kasner clocks in audit/timing-kasner.md."""

from fractions import Fraction
from math import cos, pi, sin, sqrt

from joint_jacobi import GAUSS, dot, exponents, sky


def clock_coefficients(epsilon):
    fourth = 1 - 5 * epsilon**4 + 4 * epsilon**5
    fifth = 1 - 6 * epsilon**5 + 5 * epsilon**6
    return fourth / 225, 4 * fourth / 225 - 2 * fifth / 135


def tidal_moments(p):
    """Differentiate the exact directional squared tidal tensor along the ray."""
    electric = [v * (1 - v) for v in p]
    electric_squared = [v * v for v in electric]
    total = sum(electric_squared)
    mean = derivative = 0.0
    for mu, weight in GAUSS:
        for azimuth in range(8):
            angle = azimuth * pi / 4
            n2 = [(1 - mu**2) * cos(angle)**2, (1 - mu**2) * sin(angle)**2, mu**2]
            expansion = dot(p, n2)
            n2_prime = [2 * x * (expansion - v) for x, v in zip(n2, p)]
            en = dot(electric, n2)
            tidal = 4 * total - 8 * dot(electric_squared, n2) + 2 * en**2
            angular_rate = -8 * dot(electric_squared, n2_prime) + 4 * en * dot(electric, n2_prime)
            mean += weight * tidal / 16
            derivative += weight * (angular_rate - 4 * (1 + expansion) * tidal) / 32
    return mean, derivative


def centered_excess(b, midpoint, radius, epsilon):
    p = exponents(b)
    half_duration = radius
    for _ in range(8):
        emission = midpoint - half_duration
        # The ray integrator takes emission time as its time and length unit.
        waist, clock = sky(p, half_duration / emission, epsilon)
        error = radius - emission * waist
        if abs(error) < 2e-14:
            return emission * (clock - (1 - epsilon) * waist)
        half_duration += error
    raise AssertionError("centered waist matching failed")


def numerical_pair(radius):
    derivatives = []
    b_step, t_step = 0.025, 0.008
    for epsilon in (1 / 3, 1 / 2):
        db = (centered_excess(2 + b_step, 1, radius, epsilon)
              - centered_excess(2 - b_step, 1, radius, epsilon)) / (2 * b_step)
        dt = (centered_excess(2, 1 + t_step, radius, epsilon)
              - centered_excess(2, 1 - t_step, radius, epsilon)) / (2 * t_step)
        derivatives.append((db, dt))
    (db1, dt1), (db2, dt2) = derivatives
    return -21 / 4 * (db1 * dt2 - dt1 * db2) / radius**11


def main():
    p = exponents(Fraction(2))
    dp = [Fraction(v, 49) for v in (3, -8, 5)]
    electric = [v * (1 - v) for v in p]
    norm = dot(electric, electric)
    norm_prime = sum(2 * e * (1 - 2 * v) * dv for e, v, dv in zip(electric, p, dp))
    assert sum(v * e**2 for v, e in zip(p, electric)) == 0
    tidal, derivative = tidal_moments([float(v) for v in p])
    assert abs(tidal - 8 * norm / 5) < 1e-14
    assert abs(derivative + 16 * norm / 3) < 1e-14
    normed_epoch_bracket = dp[0] / (p[0] * dot(dp, dp))
    assert normed_epoch_bracket == Fraction(-21, 4)
    assert sum(dp) == 0  # The conjugate modulus preserves the volume epoch.
    a1, b1 = clock_coefficients(Fraction(1, 3))
    a2, b2 = clock_coefficients(Fraction(1, 2))
    coefficient = normed_epoch_bracket * norm * norm_prime * (b1 * a2 - a1 * b2)
    assert coefficient == Fraction(488, 1286491815)
    print(f"exact normalized pair coefficient  {coefficient}")
    values = []
    for radius in (0.10, 0.05):
        result = numerical_pair(radius)
        values.append(result)
        print(f"R/T={radius:.2f} normalized pair          {result:.3e}")
    extrapolated = 2 * values[1] - values[0]
    print(f"linear extrapolation               {extrapolated:.3e}")
    assert 0 < values[1] - coefficient < values[0] - coefficient
    assert abs(extrapolated / coefficient - 1) < 0.04


if __name__ == "__main__":
    main()
