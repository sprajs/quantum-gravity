"""Exact relative timing laws and translated spherical clock brackets. G_N=1."""

from collections import Counter
from fractions import Fraction as F
from functools import cache
from itertools import product

from weak_clock_contact import OMEGA, build_sections, cross_bracket


def independent_later(first, second, first_width, second_width, offset=0):
    """Each pulse has the same symmetric bump with support in (-1/8, 1/8)."""
    relative_radius = (first_width + second_width) * F(1, 8)
    probability = F(0)
    for (x, mass_x), (y, mass_y) in product(first, second):
        delay = offset + second_width * y - first_width * x
        assert abs(delay) > relative_radius
        if delay > 0:
            probability += mass_x * mass_y
    return probability


def phase_pairs(shift, bins):
    """The phase bins partition a uniform trigger. The rotation permutes them."""
    for i in range(bins):
        yield i, (i + shift) % bins


def main():
    sections, jump = build_sections()
    contact = OMEGA * jump**2 / 2
    assert contact == F(1, 30)

    @cache
    def bracket(delay):
        assert delay
        return cross_bracket(sections, jump, delay)

    symmetric = ((-1, F(1, 2)), (1, F(1, 2)))
    assert independent_later(symmetric, symmetric, 1, 2) == F(1, 2)
    assert independent_later(symmetric, symmetric, 1, 2, F(5, 2)) == F(3, 4)
    print("Centered even windows: midpoint at unequal widths")

    skew = ((-2, F(1, 5)), (F(1, 2), F(4, 5)))
    assert sum(x * mass for x, mass in skew) == 0
    later = independent_later(skew, skew, 1, 2)
    assert contact * (2 * later - 1) == F(1, 50)
    print("Centered skew window at double width: 1/50")

    narrow = F(1, 10**8)
    tolerance = F(1, 100000)
    bins = 12
    for steps, expected in (((3, 5), F(1, 90)), ((7, 9), -F(1, 90))):
        # A symmetric pair of phase shifts with mean 1/3 or 2/3.
        pairs = [pair for shift in steps for pair in phase_pairs(shift, bins)]
        assert Counter(i for i, _ in pairs) == Counter(j for _, j in pairs)
        assert all(i != j for i, j in pairs)
        later = F(sum(j > i for i, j in pairs), len(pairs))
        mean_shift = F(sum(steps), len(steps) * bins)
        assert later == 1 - mean_shift
        assert contact * (2 * later - 1) == expected
        # Center each trigger bin on its midpoint. Independent smooth bumps
        # narrower than half the physical bin spacing preserve all pair orders.
        actual = sum(bracket(narrow * (j-i) / bins) for i, j in pairs) / len(pairs)
        assert abs(actual - expected) < tolerance
    print("Identical marginals, paired cyclic triggers: 1/90 and -1/90")

    # Compare L_t with the readout (L_t + L_(t+d))/2. Its second component
    # contributes a continuous, nonzero term at zero nominal delay.
    separation = F(1, 1000)
    midpoint = bracket(separation) / 2
    assert midpoint > F(1, 50)
    for sign in (-1, 1):
        delay = sign * narrow
        value = (bracket(delay) + bracket(separation + delay)) / 2
        assert abs(value - (midpoint + sign * contact / 2)) < tolerance
    print("Distinct readouts: nonzero midpoint and half the calibrated jump")


if __name__ == "__main__":
    main()
