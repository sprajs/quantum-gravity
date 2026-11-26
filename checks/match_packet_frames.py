"""Transport and clock checks for the spherical quadrupole. Standard library."""

from fractions import Fraction
from math import comb, factorial, fsum, isclose

from joint_spherical_hessian import falling, optical_mode, simpson
from match_packets import CAP, bump, reference


# A monomial (j, p, c) represents c F^(j)(t+r) / r^p.
RADIAL = [(2, 3, 6), (1, 4, -18), (0, 5, 18)]
MIXED = [(3, 2, 2), (2, 3, -6), (1, 4, 12), (0, 5, -12)]


def moment(terms, phase_slope, time_derivatives=0, radial_weight=0):
    """Transfer derivatives onto r^(-p) on an entire traversed lobe."""
    coefficients = {}
    for j, p, coefficient in terms:
        j += time_derivatives
        p -= radial_weight
        exponent = p + j
        rising = factorial(exponent - 1) // factorial(p - 1)
        value = Fraction(coefficient * rising, phase_slope ** j)
        coefficients[exponent] = coefficients.get(exponent, 0) + value
    return {p: c for p, c in coefficients.items() if c}


def filtered_hessian(width):
    """Evaluate the original Hessian on the outer lobe before integrations by parts."""
    a = float(CAP)

    def integrand(x):
        s = a + width * (2 + x)
        z = (2 * s - a) / a
        jets = []
        for j in range(7):
            terms = [comb(j, k) * falling(6, k) * (2 / a) ** k * z ** (6 - k)
                     * bump(x, j - k + 2) / width ** (j - k + 3)
                     for k in range(j + 1)]
            jets.append(fsum(terms) / 2 ** j)
        slope = optical_mode(s, jets)[1]
        reference_slope = optical_mode(s, reference(s, 2))[1]
        return 3 * width * s * (1 - s) * slope * reference_slope / 20

    return simpson(integrand, -1, 1, pieces=1600)


def check():
    difference = RADIAL + [(j, p, -c) for j, p, c in MIXED]
    for field in [RADIAL, MIXED, difference]:
        assert moment(field, 2) == {}
    assert moment(difference, 2, radial_weight=-1) == {}
    assert moment(RADIAL, 2, time_derivatives=1) == {}
    assert moment(RADIAL, 2, time_derivatives=1, radial_weight=1) == {}
    assert moment(MIXED, 2, time_derivatives=1) == {}
    for alpha in [Fraction(1, 3), 1, Fraction(3, 2), 3, 4]:
        assert moment(RADIAL, alpha) == {5: Fraction(18 * (alpha - 2) ** 2, alpha ** 2)}
        numerator = -60 * (alpha - 2) * (alpha ** 2 - 2 * alpha + 2)
        assert moment(MIXED, alpha, time_derivatives=1) == {6: Fraction(numerator, alpha ** 4)}
    speed_derivative = Fraction(-60 * (2 ** 2 - 2 * 2 + 2), 2 ** 4)
    assert speed_derivative == Fraction(-15, 2)
    print(f"Null endpoint transport vanishes; mixed time derivative coefficient = {speed_derivative}")

    assert moment(RADIAL, 1) == {5: 18}
    assert moment(RADIAL, 1, time_derivatives=1) == {6: 90}
    assert moment(RADIAL, 1, time_derivatives=1, radial_weight=1) == {}
    assert moment(MIXED, 1, time_derivatives=1) == {6: 60}
    assert moment(difference, 1, radial_weight=-1) == {}
    for p in (5, 6):
        # After substituting r=2s-a, two derivatives of r^(6-p) vanish.
        assert falling(6 - p, 2) == 0
    print("Filtered cap-radius moments of orders 5 and 6 vanish exactly.")

    bare_sheet_limit = -2 * 5 * CAP ** 2 * factorial(4) / (16 * CAP)
    assert bare_sheet_limit == -5
    print(f"One-sided radial Wronskian limit = {bare_sheet_limit}")
    limit = -Fraction(3, 20) * factorial(7) * (1 - CAP) / 16
    assert limit == Fraction(-63, 2)
    estimates = [filtered_hessian(1 / denominator) for denominator in (8192, 32768, 131072, 524288)]
    assert all(abs(y - limit) < abs(x - limit) for x, y in zip(estimates, estimates[1:]))
    assert isclose(estimates[-1], float(limit), abs_tol=0.025)
    print(f"Filtered clock Hessian = {estimates[-1]:.6f}, analytic limit = {limit}")


if __name__ == "__main__":
    check()
