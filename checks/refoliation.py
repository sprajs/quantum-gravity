"""Two cut tests in the free, plane-polarized graviton sector.

Run with python3 checks/refoliation.py. Only the Python standard library is used.
"""

import cmath
import math
from fractions import Fraction


def cap_pairing(m, n, amplitude, use_normal=True, points=2048):
    """Integrate the two positive-frequency solutions on t=a(1-cos z)."""
    summands = []
    for j in range(points):
        z = math.tau * j / points
        cut_time = amplitude * (1 - math.cos(z))
        cut_slope = amplitude * math.sin(z)
        weight = 1 - cut_slope if use_normal else 1
        summands.append(weight * cmath.exp(1j * (n - m) * (z - cut_time)))
    integral_mean = complex(
        math.fsum(v.real for v in summands), math.fsum(v.imag for v in summands)
    ) / points
    return (m + n) * integral_mean / (2 * math.sqrt(m * n))


def vacuum_descendant_norm(level):
    """Squared norm of L[-level]|0> from distinct two-oscillator states."""
    squared_norm = Fraction()
    for left in range(1, level // 2 + 1):
        right = level - left
        if left == right:
            # Coefficient 1/2, with two identical creation operators.
            squared_norm += Fraction(left * left, 2)
        else:
            # Two ordered terms, each with coefficient 1/2.
            squared_norm += left * right
    return squared_norm


def main():
    error = max(
        abs(cap_pairing(m, n, 0.6) - int(m == n))
        for m in range(1, 9) for n in range(1, 9)
    )
    wrong_overlap = abs(cap_pairing(1, 2, 0.6, use_normal=False))
    assert error < 1e-12
    assert 0.303 < wrong_overlap < 0.305
    print(f"Max pairing error for modes 1 through 8: {error:.3g}")
    print(f"Mode 1,2 overlap magnitude if the tilt is omitted: {wrong_overlap:.6f}")
    for level in (2, 3):
        right_chiral_norm = vacuum_descendant_norm(level)
        left_chiral_norm = vacuum_descendant_norm(level)
        normal_normal = right_chiral_norm - left_chiral_norm
        mixed = right_chiral_norm + left_chiral_norm
        assert normal_normal == 0
        assert mixed == Fraction(level**3 - level, 6)
        print(f"Level {level} vacuum commutators: normal-normal {normal_normal}, mixed {mixed}")


if __name__ == "__main__":
    main()
