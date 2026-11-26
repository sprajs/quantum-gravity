"""Invariant clock contacts on one and two real quadrupoles, and a Weyl phase."""

from fractions import Fraction
from itertools import combinations
from math import pi, sin

from weak_clock_contact import build_sections, cross_bracket


def quadrupole_action(axis):
    """Infinitesimal rotation on (Qxx, Qyy, Qxy, Qxz, Qyz), trace Q = 0."""
    rotation = [[0] * 3 for _ in range(3)]
    i, j = (axis + 1) % 3, (axis + 2) % 3
    rotation[i][j], rotation[j][i] = -1, 1
    columns = []
    for col in range(5):
        xx, yy, xy, xz, yz = (int(col == n) for n in range(5))
        tensor = ((xx, xy, xz), (xy, yy, yz), (xz, yz, -xx - yy))

        def variation(a, b):
            return sum(rotation[a][k] * tensor[k][b] - tensor[a][k] * rotation[k][b]
                       for k in range(3))

        columns.append([variation(a, b) for a, b in ((0, 0), (1, 1), (0, 1), (0, 2), (1, 2))])
    return list(zip(*columns))


def invariant_contact_dimension(copies):
    """Solve C(Ju,v) + C(u,Jv) = 0 for an alternating C by exact elimination."""
    dimension = 5 * copies
    pairs = list(combinations(range(dimension), 2))
    pivots = {}
    for axis in range(3):
        block = quadrupole_action(axis)
        rotation = [[block[i % 5][j % 5] if i // 5 == j // 5 else 0
                     for j in range(dimension)] for i in range(dimension)]
        for i, j in pairs:
            row = [Fraction(rotation[k][i] * (l == j) - rotation[l][i] * (k == j)
                            + (k == i) * rotation[l][j] - (l == i) * rotation[k][j])
                   for k, l in pairs]
            for index in range(len(row)):
                value = row[index]
                if not value:
                    continue
                if index not in pivots:
                    pivots[index] = [entry / value for entry in row]
                    break
                row = [entry - value * known for entry, known in zip(row, pivots[index])]
    return len(pairs) - len(pivots)


def main():
    # A separate detector family supplies a second copy of the spin-two data.
    dimensions = [invariant_contact_dimension(n) for n in (1, 2)]
    assert dimensions == [0, 1]
    print(f"Rotation-invariant alternating contacts, one and two quadrupole copies: {dimensions}")

    # In units hbar = G_N = 1 choose product of Weyl amplitudes 30*pi.
    # A strongly continuous time translate would have commutator distance 0.
    sections, jump = build_sections()
    bracket = cross_bracket(sections, jump, Fraction(1, 10_000_000))
    distance = 2 * abs(sin(15 * pi * float(bracket)))
    assert distance > 1.99999
    print(f"Weyl commutator distance from identity at delay 1e-7: {distance:.8f} (limit 2)")


if __name__ == "__main__":
    main()
