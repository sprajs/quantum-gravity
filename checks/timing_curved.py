"""Check the Rosen time sweep and flat separation margins of the curved clocks."""
from fractions import Fraction
from math import cosh, fsum, isclose, sinh, tanh


def integrated_inverse_scale(kappa, start, end, panels=256):
    """Integrate a_1^{-2} along a Rosen ray by composite Simpson quadrature."""
    step = (end - start) / panels
    values = [1 / cosh(kappa * (start + i * step)) ** 2 for i in range(panels + 1)]
    return step * (values[0] + 4 * fsum(values[1:-1:2])
                   + 2 * fsum(values[2:-1:2]) + values[-1]) / 3


def event_times(radius, cap_fraction):
    return -radius, (2 * cap_fraction - 1) * radius, radius


def flat_separation(radius_a, cap_a, radius_b, cap_b, distance):
    return min(abs(distance - abs(t_a - t_b)) for t_a in event_times(radius_a, cap_a)
               for t_b in event_times(radius_b, cap_b))


def main():
    for kappa, length in ((1.0, 1.0), (0.02, 1.3), (1.0, 0.35)):
        max_squared_radius = length * tanh(kappa * length / 2) / kappa
        for i in range(33):
            u = length * i / 32
            incoming = integrated_inverse_scale(kappa, 0, u)
            returning = integrated_inverse_scale(kappa, u, length)
            cone_bound = 2 * length * cosh(kappa * u) ** 2
            cone_bound *= incoming * returning / (incoming + returning)
            analytic = (2 * length * sinh(kappa * u) * sinh(kappa * (length - u))
                        / (kappa * sinh(kappa * length)))
            assert isclose(cone_bound, analytic, abs_tol=1e-11)
            assert cone_bound <= max_squared_radius + 1e-11
            if i == 16:
                assert isclose(cone_bound, max_squared_radius, abs_tol=1e-11)
    print(f"Unit Rosen diamond: Killing norm upper bound {-1 + tanh(0.5) / 2:.8f}")

    radius, cap = Fraction(1), Fraction(1, 3)
    margin = flat_separation(radius, cap, radius, cap, radius)
    assert margin == Fraction(1, 3)
    print(f"Overlapping equal clocks: null-time separation margin {margin} in units of R")

    small_radius, small_cap = Fraction(1, 5), Fraction(2, 3)
    support_margin = min(abs(t) - small_radius for t in event_times(radius, cap))
    assert support_margin == Fraction(2, 15)
    assert flat_separation(radius, cap, small_radius, small_cap, Fraction(0)) >= support_margin
    print(f"Nested unequal clocks: smooth-neighborhood margin {support_margin} in units of R")


if __name__ == "__main__":
    main()
