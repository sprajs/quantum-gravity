"""Integrate angular and normal cap displacements on the unit Minkowski ball."""

from fractions import Fraction as F


def integral_unit_interval(polynomial):
    # Boole's rule is exact through degree five. All profiles below are even
    # in cos(theta), so the angular mean also uses the interval [0, 1].
    weights = [7, 32, 12, 32, 7]
    return sum(weight * polynomial(F(i, 4)) for i, weight in enumerate(weights)) / 90


def quadrupole(z):
    return (3 * z**2 - 1) / 2


def cap_volume_integrand(r, z):
    # h = 2 S, N = (r² - 1)(x S x)/2, tr S = 0.
    # S : Hess N = (r² - 1) tr S² + 4 r² n S² n.
    norm_squared = F(3, 2)
    normal_squared = (1 - z**2) / 4 + z**2
    contraction = (r**2 - 1) * norm_squared + 4 * r**2 * normal_squared
    # The angular mean absorbs 4 pi. The sign uses Omega(X, B_N).
    return -r**2 * contraction / 2


def main():
    # Set G = 1. Integral_C k times a scalar equals half its angular mean.
    cap_angular = -integral_unit_interval(lambda z: 9 * z**2 * (1 - z**2)) / 2
    joint_angular = -integral_unit_interval(lambda z: -6 * quadrupole(z)**2) / 2
    assert cap_angular == -F(3, 5) and cap_angular + joint_angular == 0
    print(f"Common angular displacement: {cap_angular} + {joint_angular} = 0")

    adm = integral_unit_interval(
        lambda r: integral_unit_interval(lambda z: cap_volume_integrand(r, z))
    )
    # At the rim, delta_B u = -Q and delta_X k / k = -Q.
    joint = integral_unit_interval(lambda z: quadrupole(z)**2) / 2
    assert adm == -F(1, 10) and adm + joint == 0
    print(f"Geometric cap tilt (ADM and joint): {adm} + {joint} = 0")


if __name__ == "__main__":
    main()
