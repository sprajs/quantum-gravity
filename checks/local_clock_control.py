#!/usr/bin/env python3
"""Check the single-emitter epoch comparison in audit/local-clock-control.md."""

from fractions import Fraction as Q

from joint_jacobi import dot, exponents, matched_excess, sky


def optics(b, age, radius, cap=0.5):
    """Matched-waist excess at fixed launch age, restored to length units."""
    return age * matched_excess(b, radius / age, cap)


def launch_age(radius, cap):
    """Find the stored Kasner launch age giving proper midpoint T=1."""
    p = exponents(2)
    half_duration = radius
    for _ in range(8):
        emission = 1 - half_duration
        waist, _ = sky(p, half_duration / emission, cap)
        error = radius - emission * waist
        if abs(error) < 2e-14:
            return emission
        half_duration += error
    raise AssertionError("nested midpoint matching failed")


def main():
    b = Q(2)
    p = exponents(b)
    denominator = 1 + b + b**2
    dp = [(slope * denominator - value * (1 + 2 * b)) / denominator**2
          for slope, value in zip((-1, 1, 1 + 2 * b), (-b, 1 + b, b * (1 + b)))]
    electric = [v * (1 - v) for v in p]
    tidal = dot(electric, electric)
    tidal_b = sum(2 * e * (1 - 2 * v) * dv for e, v, dv in zip(electric, p, dp))
    bracket = dp[0] / (p[0] * dot(dp, dp))
    assert bracket == -Q(21, 4)

    def cap_weight(e):
        return (1 - 5 * e**4 + 4 * e**5) / 225

    common = -4 * bracket * tidal * tidal_b * cap_weight(Q(1, 2))**2
    nested = -4 * bracket * tidal * tidal_b * cap_weight(Q(1, 3)) * cap_weight(Q(1, 2)) / 5**5
    margin = Q(1, 3) - Q(1, 5)
    assert common == -Q(169, 29412250)
    assert nested == -Q(24128, 11167463671875)
    assert margin == Q(2, 15)
    print(f"Common-window single-emitter coefficient {common}")
    print(f"Nested clock bracket difference {nested}; flat separation margin {margin}")

    # Independent shooting for both faces. Vary the shape at fixed launch age,
    # then the physical launch age at fixed matched radius and torus shape.
    h_b, h_t = 0.02, 0.005
    estimates = []
    for radius in (0.04, 0.02):
        ub = (optics(2 + h_b, 1, radius) - optics(2 - h_b, 1, radius)) / (2 * h_b)
        ut = (optics(2, 1 + h_t, radius) - optics(2, 1 - h_t, radius)) / (2 * h_t)
        measured = float(bracket) * ub * ut / radius**10
        estimates.append(measured)
        print(f"R/T={radius:.2f} normalized common-window limit {measured:.6e}")
    extrapolation = 2 * estimates[1] - estimates[0]
    assert all(common < x < 0 for x in estimates)
    assert abs(estimates[1] - common) < abs(estimates[0] - common)
    assert abs(extrapolation / common - 1) < 0.06

    for radius in (0.14, 0.08):
        t1, t2 = launch_age(radius, 1 / 3), launch_age(radius / 5, 0.5)
        ub = (optics(2 + h_b, t1, radius, 1 / 3)
              - optics(2 - h_b, t1, radius, 1 / 3)) / (2 * h_b)
        ut = (optics(2, t2 + h_t, radius / 5)
              - optics(2, t2 - h_t, radius / 5)) / (2 * h_t)
        measured = float(bracket) * ub * ut / radius**10
        print(f"R/T={radius:.2f} normalized nested difference {measured:.6e}")
        assert 1 < measured / nested < 1.15


if __name__ == "__main__":
    main()
