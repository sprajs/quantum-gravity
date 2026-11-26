"""Leading semiclassical focusing from an s-wave of a real massless scalar."""
from cmath import phase, rect
from math import acos, atan, cos, exp, isclose, pi, sin, sqrt


def simpson(function, lower, upper, panels=1024):
    step = (upper - lower) / panels
    middle = sum((4 if i % 2 else 2) * function(lower + i * step)
                 for i in range(1, panels))
    return step * (function(lower) + middle + function(upper)) / 3


# Dimensionless integrals of the ray derivative for the half-radius cap.
PAST = ((1/8 + pi/16 - atan(2)/4) / pi**2, (23 - 11j) / (600 * pi**2))
FUTURE = ((3/8 - pi/16) / (5 * pi**2), (9 - 13j) / (600 * pi**2))
PAIR_AMPLITUDE = 0.1


def clock_coefficient(theta, diagonal, interference):
    amplitude = PAIR_AMPLITUDE
    number = 2 * amplitude**2 / (1 + amplitude**2)
    pairing = rect(sqrt(2) * amplitude / (1 + amplitude**2), theta)
    return 8 * pi * (number * diagonal + (pairing * interference).real)


def main():
    # Independent KG normalization in position space (r = a tan y).
    norm = simpson(lambda y: 16 * sin(y)**2 * cos(y)**2 / pi, 0, pi / 2)
    assert isclose(norm, 1.0, abs_tol=1e-12)
    # Independent frequency-space energy with a=1. The discarded tail is <1e-31.
    energy = simpson(lambda z: 4*z*z*exp(-2*z), 0, 45, panels=16384)
    assert isclose(energy, 1.0, abs_tol=5e-11)

    def past(x):
        return -2j / (pi * (1 + 2j*x)**2)

    def future(x):
        return 2j / (pi * (1 + 2j) * (1 + 2j*(1 - x))**2)

    print(f"KG norm {norm:.12f}; one-particle energy in units of 1/a: {energy:.10f}")
    check_cut("past", past, *PAST)
    check_cut("future", future, *FUTURE)


def check_cut(tip, g, exact_a, exact_b):
    def weight(x):
        return x * (1 - x)

    diagonal = simpson(lambda x: weight(x) * abs(g(x))**2, 0.5, 1)
    interference = simpson(lambda x: weight(x) * g(x)**2, 0.5, 1)
    assert abs(exact_a - diagonal) < 1e-13
    assert abs(exact_b - interference) < 1e-13
    amplitude = PAIR_AMPLITUDE
    number = 2 * amplitude**2 / (1 + amplitude**2)
    assert isclose(number, 2 / 101)
    for sign in (-1, 1):
        pairing = sign * sqrt(2) * amplitude / (1 + amplitude**2)

        def stress(x):
            return 2 * number * abs(g(x))**2 + 2 * (pairing * g(x)**2).real

        coefficient = 4 * pi * simpson(lambda x: weight(x) * stress(x), 0.5, 1)
        analytic = clock_coefficient(0 if sign > 0 else pi, exact_a, exact_b)
        assert isclose(coefficient, analytic, abs_tol=1e-12)
        assert sign * coefficient > 0
        print(f"{tip} tip, relative sign {sign:+d}, R times total energy {number:.9f}, "
              f"R times leading clock excess / G {coefficient:+.9f}")

    # Check the complex interference term away from the two real phases.
    test_phase = pi / 2
    pairing = rect(sqrt(2) * amplitude / (1 + amplitude**2), test_phase)
    quadrature = 8 * pi * (number * diagonal + (pairing * interference).real)
    assert isclose(quadrature, clock_coefficient(test_phase, exact_a, exact_b), abs_tol=1e-12)
    centre = pi - phase(exact_b)
    half_width = acos(number * exact_a / (abs(pairing) * abs(exact_b)))
    lower, upper = centre - half_width, centre + half_width
    for zero in (lower, upper):
        assert abs(clock_coefficient(zero, exact_a, exact_b)) < 1e-14
    assert lower < pi < upper
    print(f"{tip} tip, negative excess for phase/pi between {lower/pi:.6f} and {upper/pi:.6f}")


if __name__ == "__main__":
    main()
