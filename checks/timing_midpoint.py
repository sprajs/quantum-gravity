"""Coincident proper-time filters for two distinct spherical clock Hessians."""

from fractions import Fraction as F
from math import factorial

from weak_clock_contact import (
    CAP, OMEGA, add, evaluate, integrate, product, scale, translate,
)


def derivative(p, order=1):
    return {i-order: c * (factorial(i) // factorial(i-order))
            for i, c in p.items() if i >= order}


def primitive(p):
    return {i+1: F(c, i+1) for i, c in p.items()}


def response(power, master_coefficient):
    """Terminal fifth primitive of the full optical source, in units G_N=1."""
    master = {power+6: master_coefficient}
    strain = add(scale(derivative(master, 4), F(1, 16), -1),
                 scale(derivative(master, 3), F(-1, 4), -2),
                 scale(derivative(master, 2), F(1, 4), -3))
    slope = derivative(strain)
    assert slope == {power: 1}
    weight = product(slope, {1: 1, 2: -1})

    def tail_moment(order):
        p = primitive(scale(weight, 1, -order))
        return add({0: evaluate(p, F(1))}, scale(p, -1))

    m2, m4 = tail_moment(2), tail_moment(4)
    before = {0: -16 * evaluate(m2, CAP), 2: 96 * evaluate(m4, CAP)}
    after = add(scale(m2, -16), scale(m4, 96, 2), scale(weight, -16, -1))
    assert evaluate(after, F(1)) == 0
    assert evaluate(after, CAP)-evaluate(before, CAP) == -16*(1-CAP)*CAP**power
    return [(F(0), CAP, before), (CAP, F(1), after)]


def traces(sections, position):
    left = right = F(0)
    for lo, hi, p in sections:
        if lo < position <= hi:
            left = evaluate(p, position)
        if lo <= position < hi:
            right = evaluate(p, position)
    return left, right


def branch_limits(first, second):
    value = -OMEGA * sum(
        integrate(product(derivative(p), q), lo, hi)
        for (lo, hi, p), (_, _, q) in zip(first, second)
    )
    later = earlier = value
    for position in (F(0), CAP, F(1)):
        left, right = traces(first, position)
        below, above = traces(second, position)
        later -= OMEGA * (right-left) * below
        earlier -= OMEGA * (right-left) * above
    return later, earlier


def cumulative_pieces(sections):
    total = F(0)
    pieces = []
    for lo, hi, p in sections:
        q = primitive(p)
        cumulative = add(q, {0: total-evaluate(q, lo)})
        pieces.append((lo, hi, cumulative))
        total = evaluate(cumulative, hi)
    return pieces, {0: total}


def smooth_box(sections, width):
    """Convolution with a unit-area box on [0,width] in the s master."""
    pieces, terminal = cumulative_pieces(sections)

    def at(point):
        for lo, hi, p in pieces:
            if lo < point < hi:
                return p
        return terminal if point > pieces[-1][1] else {}

    points = sorted({x+shift for lo, hi, _ in pieces
                     for x in (lo, hi) for shift in (0, width)})
    result = []
    for lo, hi in zip(points, points[1:]):
        midpoint = (lo+hi)/2
        difference = add(at(midpoint), scale(translate(at(midpoint-width), width), -1))
        result.append((lo, hi, scale(difference, 1/width)))
    return result


def filtered_bracket(first, second, width):
    a, b = smooth_box(first, width), smooth_box(second, width)
    for sections in (a, b):
        for x in {x for lo, hi, _ in sections for x in (lo, hi)}:
            left, right = traces(sections, x)
            assert left == right
    return -OMEGA * sum(integrate(product(derivative(p), q), lo, hi)
                        for (lo, hi, p), (_, _, q) in zip(a, b))


def ordering_bias(ratio):
    centers = ((-1, F(2, 3)), (2, F(1, 3)))
    assert sum(t*mass for t, mass in centers) == 0
    bias = F(0)
    for t, mass in centers:
        for u, other_mass in centers:
            delay = ratio*u-t
            # Independent bumps of radius 1/10 preserve each ordering.
            assert abs(delay) > (1+ratio)/10
            bias += mass*other_mass*(1 if delay > 0 else -1)
    return bias


def main():
    first = response(4, F(2, 1575))
    second = response(5, F(1, 1650))
    later, earlier = branch_limits(first, second)
    assert branch_limits(second, first) == (-earlier, -later)
    midpoint, half_jump = (later+earlier)/2, (later-earlier)/2
    assert midpoint == F(8126, 48715425)
    assert half_jump == F(2633, 22143375)
    assert branch_limits(first, first)[0] == -branch_limits(first, first)[1]
    assert ordering_bias(F(2)) == F(-1, 3)
    assert ordering_bias(F(1, 2)) == F(1, 3)
    print(f"Distinct clock limits (G_N=1): later {later}, earlier {earlier}")
    print(f"Synchronized midpoint {midpoint}, half-jump {half_jump}")
    for width in (F(1, 1000), F(1, 1000000)):
        value = filtered_bracket(first, second, width)
        assert filtered_bracket(second, first, width) == -value
        assert abs(value-midpoint) < width/1000
        print(f"Common box of master width {float(width):.6f}: {float(value):.12f}")


if __name__ == "__main__":
    main()
