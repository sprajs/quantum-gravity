#!/usr/bin/env python3
"""Check the two capped light cones in a massless-scalar FLRW spacetime."""

from decimal import Decimal, localcontext
from fractions import Fraction


def clock(signed_width, x, y):
    """Return U/R from the cap slope and the affine interval, with y=a_cap/a_S."""
    radius_slope = y + signed_width * x / (2 * y)
    affine_interval = (1 - x) * (1 + y**2) / 2
    return radius_slope * affine_interval / y**2


def focusing_excess(width, x, y):
    return width**2 * (1 - x)**2 * (x + 2 * y**2 / (1 + y)**2) / (4 * y**3)


def check_rational_caps():
    width = Fraction(3, 4)
    epsilon = Fraction(5, 16)
    cases = [
        ("past", width, Fraction(5, 12), Fraction(3, 4), Fraction(4025, 5184)),
        ("future", -width, Fraction(1, 4), Fraction(5, 4), Fraction(5781, 8000)),
    ]
    for tip, d, x, y, expected in cases:
        w = 1 - d * (1 - x)
        assert y**2 == w and x * y == epsilon
        assert clock(d, x, y) == expected
        assert expected - (1 - epsilon) == focusing_excess(width, x, y) > 0

        # In affine units dτ=w dx, test f''(τ)=-R_{ττ} f/2 for f=D/R.
        radius_x = y + d * x / (2 * y)
        radius_xx = d / y - d**2 * x / (4 * y**3)
        radius_tautau = (w * radius_xx - d * radius_x) / w**3
        ricci_tautau = 3 * d**2 / (2 * w**4)
        assert radius_tautau == -ricci_tautau * (x * y) / 2
        print(f"{tip} tip: U/R = {expected}, excess/R = {expected - (1 - epsilon)}")


def locate_cap(d, epsilon):
    """Invert the measured area fraction x²[1-d(1-x)]=epsilon² on the cone."""
    low, high = Decimal(0), Decimal(1)
    for _ in range(150):
        x = (low + high) / 2
        w = 1 - d * (1 - x)
        if x**2 * w < epsilon**2:
            low = x
        else:
            high = x
    x = (low + high) / 2
    return x, (1 - d * (1 - x)).sqrt()


def check_weak_limit():
    width = Decimal("1e-9")
    radar_over_radius = ((1 + width) * (1 + width).sqrt()
                         - (1 - width) * (1 - width).sqrt()) / (3 * width)
    assert abs((1 - radar_over_radius) / width**2 - Decimal(1) / 24) < Decimal("1e-18")
    for epsilon in map(Decimal, ("0.1", "0.5", "0.9")):
        coefficient = (1 - epsilon)**2 * (1 + 2 * epsilon) / 8
        for d in (width, -width):
            x, y = locate_cap(d, epsilon)
            reading = clock(d, x, y)
            above_area = (reading - (1 - epsilon)) / width**2
            above_flat = (reading - (1 - epsilon) * radar_over_radius) / width**2
            assert abs(above_area - coefficient) < Decimal("1e-9")
            assert abs(above_flat - coefficient - (1 - epsilon) / 24) < Decimal("1e-9")
        if epsilon == Decimal("0.5"):
            print(f"half-radius cap: weak area coefficient = {coefficient:.4f}, "
                  f"equal-radar coefficient = {coefficient + (1 - epsilon) / 24:.10f}")


if __name__ == "__main__":
    check_rational_caps()
    with localcontext() as context:
        context.prec = 70
        check_weak_limit()
