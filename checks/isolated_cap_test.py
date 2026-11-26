"""Test the two optical moments of homogeneous quadrupole responses, R=G_N=1."""

from fractions import Fraction as F
from math import comb, perm

from timing_caps import bracket, sections, source_check
from weak_clock_contact import HESSIAN, add, evaluate, integrate, product, scale


A, B = F(1, 3), F(1, 2)


def moment(slope, exponent, lo, hi):
    return integrate(product(slope, {exponent: 1, exponent + 1: -1}), lo, hi)


def tidal_moments(slope, cap):
    return (21 * HESSIAN * moment(slope, 2, cap, F(1)),
            105 * HESSIAN * moment(slope, 3, cap, F(1)))


def determinant(first, second):
    return first[0] * second[1] - first[1] * second[0]


def calibrated_slope():
    """Solve the two outer-clock and two interval moment conditions."""
    powers = range(4, 8)
    basis = [{n: F(1)} for n in powers]
    matrix = [[evaluate(p, B) for p in basis] + [F(1)],
              [moment(p, -1, B, F(1)) for p in basis] + [F(0)],
              [moment(p, 2, A, B) for p in basis] + [F(0)],
              [moment(p, 3, A, B) for p in basis] + [F(0)]]
    for col in range(len(basis)):
        pivot = next(i for i in range(col, len(basis)) if matrix[i][col])
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        row = [x / matrix[col][col] for x in matrix[col]]
        matrix[col] = row
        for i in range(len(basis)):
            if i != col:
                multiple = matrix[i][col]
                matrix[i] = [x - multiple*y for x, y in zip(matrix[i], row)]
    return {n: row[-1] for n, row in zip(powers, matrix)}


def metric_components(degree, time_order):
    """Radial, radial-angular and trace-free screen coefficients at t=1."""
    jets = []
    for j in range(5):
        order = j + time_order
        remaining = degree - order
        factor = F(perm(degree, order), 2**degree)
        # Jets of [F(1+r) - (-1)^j F(1-r)] / r^(5-j), F(u)=(u/2)^degree.
        jets.append({i+j-5: 2*factor*comb(remaining, i)
                     for i in range(remaining+1) if (i+j) % 2})
    coefficients = ((18, -18, 6), (-12, 12, -6, 2), (3, -3, 3, -2, 1))
    return [add(*(scale(jet, k) for jet, k in zip(jets, row))) for row in coefficients]


def sky_contraction(first, second):
    weights = (F(3, 10), F(3, 5), F(3, 5))
    return add(*(scale(product(x, y), w) for x, y, w in zip(first, second, weights)))


def main():
    slope = calibrated_slope()
    assert evaluate(slope, B) == 1 and moment(slope, -1, B, F(1)) == 0
    assert tidal_moments(slope, A) == tidal_moments(slope, B)
    first, second = (sections(slope, c) for c in (A, B))
    for cap, profile in ((A, first), (B, second)):
        source_check(slope, cap, profile)
    for side in (-1, 0, 1):
        assert bracket(first, second, F(0), side) == F(3, 160)
        assert bracket(second, first, F(0), side) == F(-3, 160)
    print("Equal tidal moments at both caps; earlier and later brackets = 3/160")

    control = {4: F(152, 3), 5: F(-208, 3)}
    control_det = determinant(tidal_moments(control, A), tidal_moments(control, B))
    assert control_det == F(-4454779, 188956800)
    print(f"Control wave tidal determinant = {control_det}")

    h7, dt7 = metric_components(7, 0), metric_components(7, 1)
    h8, dt8 = metric_components(8, 0), metric_components(8, 1)
    adm = scale(add(sky_contraction(dt7, h8), scale(sky_contraction(h7, dt8), -1)), F(1, 8), 2)
    assert adm == {2: F(-3969, 64), 6: F(-8127, 320)}
    omega = integrate(adm, F(0), F(1))
    assert omega == F(-243, 10)
    reference = {1: F(21)}
    two_mode = -determinant(tidal_moments(reference, A), tidal_moments(reference, B)) / omega
    assert two_mode == F(146461, 1866240)
    print(f"Waist ADM product = {omega}; restricted two-mode bracket = {two_mode}")


if __name__ == "__main__":
    main()
