"""Spherical wave kernel and coincident electric Weyl curvature readings."""

from fractions import Fraction
from math import atan, comb, factorial, pi


def normalized_shell_kernel(delay, radius, second_radius, width):
    """8 pi r s times the causal kernel, with Fourier multiplier exp(-width |k|)."""
    difference = radius - second_radius
    total = radius + second_radius
    return (atan((delay + difference) / width) + atan((delay - difference) / width)
            - atan((delay + total) / width) - atan((delay - total) / width)) / pi


def integrate_simpson(function, lower, upper, panels):
    step = (upper - lower) / panels
    odd = sum(function(lower + i * step) for i in range(1, panels, 2))
    even = sum(function(lower + i * step) for i in range(2, panels, 2))
    return step * (function(lower) + 4 * odd + 2 * even + function(upper)) / 3


def contact_test_fourth(delay):
    # Fourth derivative of t^3 (1-t^2)^8 / 6, extended by zero beyond [-1,1].
    result = 0
    for j in range(1, 9):
        degree = 3 + 2 * j
        result += ((-1)**j * comb(8, j) * factorial(degree)
                   / (6 * factorial(degree - 4))) * delay**(degree - 4)
    return result


def power_profile(power):
    """Coefficients of the compact polynomial (1-t^2)^power on [-1,1]."""
    return {2 * j: Fraction((-1)**j * comb(power, j)) for j in range(power + 1)}


def derivative(poly, order):
    return {degree - order: coefficient * factorial(degree) / factorial(degree - order)
            for degree, coefficient in poly.items() if degree >= order}


def pair(poly, other):
    return sum(a * b * Fraction(2, i + j + 1) for i, a in poly.items()
               for j, b in other.items() if (i + j) % 2 == 0)


def check_centered_profiles():
    first = power_profile(10)
    mass = pair(first, {0: 1})
    first = {i: coefficient / mass for i, coefficient in first.items()}
    seed = power_profile(14)
    second = first.copy()
    amplitude = Fraction(1, 100000)
    for i, coefficient in derivative(seed, 3).items():
        second[i] = second.get(i, 0) + amplitude * coefficient
    # |seed'''| <= 19656 (1-t^2)^10, so the second detector is nonnegative.
    assert amplitude * 19656 < 1 / mass
    for moment in range(3):
        assert pair(first, {moment: 1}) == pair(second, {moment: 1})
    weight = -pair(first, derivative(second, 3))
    assert weight == -amplitude * pair(derivative(first, 6), seed)
    assert weight != 0 and pair(first, derivative(first, 3)) == 0
    return float(weight)


if __name__ == "__main__":
    width = 1e-7
    assert abs(normalized_shell_kernel(0.01, 1, 1, width) - 1) < 1e-5
    assert abs(normalized_shell_kernel(-0.01, 1, 1, width) + 1) < 1e-5
    assert abs(normalized_shell_kernel(1.01, 0.4, 0.6, width)) < 1e-5
    assert abs(normalized_shell_kernel(0.99, 0.4, 0.6, width) - 1) < 1e-5
    # Sky norm of the screen projection of diag(-1/2,-1/2,1).
    projected_norm = integrate_simpson(lambda mu: 9 * (1 - mu**2)**2 / 16,
                                       -1, 1, 1000)
    assert abs(projected_norm - 3 / 5) < 1e-10
    # Integrate the independent Fourier expression against the fourth derivative
    # of a compact test; the limiting contact distribution gives -test'''(0).
    contact = integrate_simpson(
        lambda t: normalized_shell_kernel(t, 1, 1, 0.0001) * contact_test_fourth(t) / 2,
        -1, 1, 12000)
    assert abs(contact + 1) < 0.003
    print("Fourier shell kernel gives both one-sided cut limits and both antipodal limits")
    print(f"TT projection on the sphere: {projected_norm:.6f}")
    print(f"Normalized curvature contact on cubic test: {contact:.6f} (limit -1)")
    print(f"Equal-mean, equal-variance cross-bracket in units of its contact coefficient"
          f" times width^(-4): {check_centered_profiles():.6f}")
