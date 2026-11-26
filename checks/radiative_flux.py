"""Exact finite-null-face and linearized graviton checks, using rational arithmetic."""

from fractions import Fraction as F
from math import comb


def derivative(coefficients):
    return [power * value for power, value in enumerate(coefficients) if power]


def evaluate(coefficients, point):
    return sum(value * point**power for power, value in enumerate(coefficients))


def integrated_product(first, second, lo, hi):
    return sum(
        F(a * b, i + j + 1) * (hi**(i + j + 1) - lo**(i + j + 1))
        for i, a in enumerate(first) for j, b in enumerate(second)
    )


def check_vacuum_balance():
    # The two Rosen scale factors are u**p and u**q. Substitute u=x**5
    # to integrate the shear and expansion terms exactly from u=1 to 32.
    p, q = F(3, 5), F(-1, 5)
    expansion = p + q
    ricci_coefficient = -(p * (p - 1) + q * (q - 1))
    shear_squared = (p - q)**2 / 2
    assert ricci_coefficient == 0 and shear_squared == F(8, 25)
    endpoint_power = 5 * (expansion - 1)
    assert endpoint_power == -3
    charge_change = expansion * (F(2)**endpoint_power - 1)
    # mu * (theta**2/2 - sigma**2) du has an x**(-4) density.
    integrated_flux = 5 * (expansion**2 / 2 - shear_squared) * (1 - F(1, 8)) / 3
    assert charge_change == integrated_flux == F(-7, 20)
    print(f"Vacuum Rosen cut-charge change and integrated flux: {charge_change}")


def check_profile():
    # h = u**5 (1-u)**5. Its derivatives through fourth order vanish
    # at both ends. The second perturbation in the flux test is h'.
    h = [0] * 5 + [(-1)**j * comb(5, j) for j in range(6)]
    hp = derivative(h)
    hpp = derivative(hp)
    jet = h
    for _ in range(5):
        assert evaluate(jet, 0) == evaluate(jet, 1) == 0
        jet = derivative(jet)
    flux = integrated_product(hp, hp, 0, 1) - integrated_product(hpp, h, 0, 1)
    assert flux == 2 * integrated_product(hp, hp, 0, 1) > 0
    print(f"Normalized symplectic flux for h and h': {flux}")

    # On a round cone of affine radius 1+u the weight is (1+u)**2.
    # Choose the second variation -u*h so the Wronskian is h**2.
    other = [0] + [-a for a in h]
    weighted_h = [a + b for a, b in zip(h + [0], [0] + h)]
    spherical_flux = 0
    for power, coefficient in enumerate((1, 2, 1)):
        weight = [0] * power
        spherical_flux += coefficient * (
            integrated_product(weight + hp, other, 0, 1)
            - integrated_product(weight + derivative(other), h, 0, 1)
        )
    assert spherical_flux == integrated_product(weighted_h, weighted_h, 0, 1) > 0
    print(f"Normalized round-cone symplectic flux: {spherical_flux}")

    # Vary h along k = h + h', so the total energy variation and the
    # individual rim terms are both nonzero.
    k = [a + b for a, b in zip(h, hp + [0])]
    kp = derivative(k)
    cut = F(1, 3)
    contractions = []
    rim_terms = []
    for lo, hi in ((0, cut), (cut, 1)):
        pairing = integrated_product(kp, hp, lo, hi)
        contraction = pairing - integrated_product(hpp, k, lo, hi)
        rim = evaluate(hp, hi) * evaluate(k, hi) - evaluate(hp, lo) * evaluate(k, lo)
        assert 2 * pairing == contraction + rim
        contractions.append(contraction)
        rim_terms.append(rim)
    assert rim_terms[0] == -rim_terms[1] != 0
    assert sum(contractions) == 2 * integrated_product(kp, hp, 0, 1) == flux
    print(f"Matched rim terms cancel: {sum(rim_terms)}")
    print(f"Whole-profile Hamiltonian variation: {sum(contractions)}")


if __name__ == "__main__":
    check_vacuum_balance()
    check_profile()
