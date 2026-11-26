"""Check the matched charges and common clock interval in audit/matter-boundary.md."""

from decimal import Decimal, localcontext
from fractions import Fraction
from math import sqrt

from matter_diamond import clock, locate_cap
from matter_state_count import simpson


def charge_density(x, w):
    """Return the pulled-back -star dφ density, normalized to unit total charge."""
    # sqrt(-g)/sin(theta) = w² x², -g^eta,eta = 1/w and phi'/s = 1/w.
    return 3 * (w**2 * x**2) / w / w


def charges_on_cut(d, x_cap):
    """Integrate the flux on a constant-time cap and on the adjoining null face."""
    w_cap = 1 - d * (1 - x_cap)

    def cap_density(x):
        return charge_density(x, w_cap)

    def face_density(x):
        return charge_density(x, 1 - d * (1 - x))

    def integrate_quadratic(density, start, end):
        middle = (start + end) / 2
        return (end - start) * (density(start) + 4 * density(middle) + density(end)) / 6

    return (integrate_quadratic(cap_density, Fraction(0), x_cap),
            integrate_quadratic(face_density, x_cap, Fraction(1)))


def check_charges():
    # d is negative on the future-tip face of the same expanding solution.
    cases = (
        ("past", Fraction(3, 4), Fraction(5, 12), Fraction(125, 1728), Fraction(1375, 9936)),
        ("future", Fraction(-3, 4), Fraction(1, 4), Fraction(1, 64), Fraction(5, 752)),
    )
    epsilon = Fraction(5, 16)
    for tip, d, x, expected_cap, expected_derivative in cases:
        w = 1 - d * (1 - x)
        assert x**2 * w == epsilon**2
        cap, face = charges_on_cut(d, x)
        assert cap == expected_cap and cap + face == 1

        # Differentiate x² w=epsilon² at fixed cap area, then P_cap=P x³.
        dx_dd = x * (1 - x) / (2 * w + d * x)
        cap_derivative = cap + 3 * d * x**2 * dx_dd
        assert cap_derivative == expected_derivative

        # Rebuild each entire cut at two nearby momenta, including both moving rims.
        step = Decimal('1e-9')
        d0 = Decimal(d.numerator) / d.denominator
        eps = Decimal(epsilon.numerator) / epsilon.denominator
        numerical_charges = []
        for delta in (-step, step):
            shifted = d0 + delta
            x_shifted, _ = locate_cap(shifted, eps)
            numerical_charges.append((shifted * x_shifted**3, shifted * (1 - x_shifted**3)))
        for i, expected in enumerate((cap_derivative, 1 - cap_derivative)):
            numerical = (numerical_charges[1][i] - numerical_charges[0][i]) / (2 * step)
            assert abs(numerical - Decimal(expected.numerator) / expected.denominator) < Decimal('1e-17')
        print(f"{tip} cap Q/P = {cap}, face = {face}, complete cut = {cap + face}, "
              f"dQ_cap/dP = {cap_derivative}")


def check_two_clocks():
    epsilon = Decimal('0.5')
    max_width = Decimal('0.25')
    d_max = float(max_width)
    bound = d_max**2 * (1 + d_max) / (8 * (1 - d_max)**2.5)
    assert bound < 0.021
    max_sampled = 0
    past_readings = []
    for i in range(-16, 17):
        signed_width = max_width * i / 16
        x_cap, y_cap = locate_cap(signed_width, epsilon)
        direct = float(clock(signed_width, x_cap, y_cap) - (1 - epsilon))
        x_c, d = float(x_cap), float(signed_width)

        def focus(x):
            w = 1 - d * (1 - x)
            affine_remaining = (1 - x) * (1 + w) / 2
            return 3 * d**2 * affine_remaining * x / (4 * w**2 * sqrt(w))

        excess = simpson(focus, x_c, 1.0)
        assert abs(excess - direct) < 1e-12
        assert 0 <= direct <= bound
        max_sampled = max(max_sampled, direct)
        if i > 0 and i % 2 == 0:
            past_readings.append(1 - float(epsilon) + direct)
    print(f"Both clocks: uniform excess bound {bound:.10f} R at |P/P0| <= 1/4, "
          f"largest sampled excess {max_sampled:.10f} R")
    separations = [right - left for left, right in zip(past_readings, past_readings[1:])]
    closest = min(separations)
    assert len(past_readings) == 8 and abs(closest - 0.00018637638) < 1e-12
    print(f"Eight past-clock readouts: minimum spacing {closest:.11f} R")


if __name__ == '__main__':
    with localcontext() as context:
        context.prec = 60
        check_charges()
        check_two_clocks()
