"""Pair different cap clocks on a single vacuum wave, in units G_N = R = 1."""

from fractions import Fraction as F
from math import prod

from weak_clock_contact import (
    HESSIAN, OMEGA, add, evaluate, integrate, product, scale, translate,
)


def derivative(p):
    return {n - 1: n * value for n, value in p.items() if n}


def integral_to_one(p):
    """Return the polynomial integral of p(t) from s to 1."""
    primitive = {n + 1: value / (n + 1) for n, value in p.items()}
    return add({0: evaluate(primitive, 1)}, scale(primitive, -1))


def sections(slope, cap):
    weight = product({1: 1, 2: -1}, slope)
    moment = integral_to_one(scale(weight, 1, -2))
    lower_jet = integral_to_one(scale(weight, 1, -4))
    before = {0: -16 * evaluate(moment, cap), 2: 96 * evaluate(lower_jet, cap)}
    after = add(scale(moment, -16), scale(lower_jet, 96, 2), scale(weight, -16, -1))
    assert evaluate(after, F(1)) == 0
    assert evaluate(after, cap) - evaluate(before, cap) == -16 * (1-cap) * evaluate(slope, cap)
    return [(F(0), cap, before), (cap, F(1), after)]


def source_check(slope, cap, profile):
    # Check the full-line weak equation on localized monomials that agree with
    # s^n on [0,1]. For n <= 6 the regular-vertex optical slope vanishes.
    weight = product({1: 1, 2: -1}, slope)
    for n in range(18):
        optical = F(0)
        if n > 6:
            coefficient = F(n * (n-1) * (n-3) * (n-5) * (n-6), 16)
            optical = HESSIAN * coefficient * integrate(scale(weight, 1, n-6), cap, F(1))
        pairing = F(0)
        if n >= 5:
            for lo, hi, z in profile:
                pairing -= OMEGA * prod(range(n-4, n+1)) * integrate(scale(z, 1, n-5), lo, hi)
        assert optical == pairing, (cap, n, optical, pairing)


def jumps(profile):
    result = {}
    for lo, hi, polynomial in profile:
        result[lo] = result.get(lo, 0) + evaluate(polynomial, lo)
        result[hi] = result.get(hi, 0) - evaluate(polynomial, hi)
    return {s: value for s, value in result.items() if value}


def trace_value(profile, s, side):
    left, right = F(0), F(0)
    for lo, hi, polynomial in profile:
        if lo < s < hi:
            return evaluate(polynomial, s)
        if s == lo:
            right = evaluate(polynomial, s)
        if s == hi:
            left = evaluate(polynomial, s)
    if side < 0:
        return left
    if side > 0:
        return right
    return (left + right) / 2


def bracket(first, second, delay, delay_side=0):
    # As the delay increases to a coincidence from below, s-delay/2
    # approaches from the right. At the midpoint use the mean of the traces.
    shift = delay / 2
    regular = F(0)
    for lo, hi, current in first:
        for left, right, other in second:
            start, stop = max(lo, left + shift), min(hi, right + shift)
            if start < stop:
                regular += integrate(product(derivative(current), translate(other, shift)), start, stop)
    atomic = sum(jump * trace_value(second, s-shift, -delay_side) for s, jump in jumps(first).items())
    return -OMEGA * (regular + atomic)


def test_vertex_contact(a, b):
    slope = {4: F(1)}
    first, second = (sections(slope, cap) for cap in (a, b))
    vertex_a, vertex_b = jumps(first)[0], jumps(second)[0]
    rim_b = jumps(second)[b]
    earlier = bracket(first, second, F(0), -1)
    later = bracket(first, second, F(0), 1)
    assert earlier == OMEGA * (rim_b**2 - vertex_b**2) / 2 == F(-207, 4096000)
    assert later == earlier + OMEGA * vertex_a * vertex_b == F(15949, 66355200)
    assert bracket(first, second, F(0)) == (earlier + later) / 2
    assert earlier == -bracket(second, first, F(0), 1)
    print(f"Untuned s^4, earlier/later limits / G_N: {earlier}, {later}")


def test_negative_wave(a, b):
    slope = {1: F(-48), 2: F(144), 3: F(-96)}
    moment = integral_to_one(product(slope, {-1: F(1), 0: F(-1)}))
    assert evaluate(moment, a) == evaluate(slope, b) == 0
    assert evaluate(moment, b) == F(1, 2)
    assert -16 * (1-a) * evaluate(slope, a) == F(1024, 27)
    negative = -OMEGA * (-16 * evaluate(moment, b))**2 / 2
    assert negative == F(-3, 160)
    # An independent higher-degree wave has the same three relevant jumps
    # e_a, e_b and d_b, and has polynomial master responses on both intervals.
    alternate = product({4: F(1)}, product({0: -b, 1: F(1)}, {0: F(1), 1: F(-679, 557)}))
    raw_moment = integrate(product(alternate, {-1: F(1), 0: F(-1)}), b, F(1))
    alternate = scale(alternate, 1 / (2 * raw_moment))
    first, second = (sections(alternate, cap) for cap in (a, b))
    assert set(jumps(first)) == {a} and jumps(second) == {0: F(-8)}
    for cap, profile in ((a, first), (b, second)):
        source_check(alternate, cap, profile)
    for side in (-1, 0, 1):
        assert bracket(first, second, F(0), side) == negative
        assert bracket(second, first, F(0), side) == -negative
    print(f"Inner vertex and outer rim canceled, both delay limits / G_N: {negative}")


def main():
    a, b = F(1, 3), F(1, 2)
    moments = [integrate({n-1: F(1), n: F(-1)}, b, F(1)) for n in (4, 5)]
    q = -moments[0] / moments[1]
    unscaled = {4: F(1), 5: q}
    slope = scale(unscaled, 1 / evaluate(unscaled, b))
    assert slope == {4: F(152, 3), 5: F(-208, 3)} and evaluate(slope, b) == 1
    first, second = (sections(slope, cap) for cap in (a, b))
    for cap, profile in ((a, first), (b, second)):
        source_check(slope, cap, profile)
    assert set(jumps(first)) == {0, a} and set(jumps(second)) == {b}
    print(f"Common wave slope (152/3) s^4 (1 + q s), q = {q}; outer rim slope = 1")
    print(f"Cap 1/3 jumps: {jumps(first)[0]}, {jumps(first)[a]} (vertex, rim)")
    print(f"Cap 1/2 jumps: 0, {jumps(second)[b]} (vertex, rim)")
    equal = bracket(first, second, F(0))
    assert equal == F(3, 160) == OMEGA * jumps(second)[b]**2 / 2
    assert equal == -bracket(second, first, F(0))
    for inner_cap in (F(1, 10), F(2, 5), F(49, 100)):
        assert bracket(sections(slope, inner_cap), second, F(0)) == equal
    assert equal * evaluate(unscaled, b)**2 == F(27, 3696640)
    print(f"Equal-time bracket / G_N = {equal} ({float(equal):.10g})")
    for delay in (F(1, 1000), F(1, 100000), F(1, 10000000)):
        values = [bracket(first, second, d) for d in (-delay, delay)]
        assert values == [-bracket(second, first, d) for d in (delay, -delay)]
        assert values[0] < equal < values[1] and max(abs(v-equal) for v in values) < 2 * delay
        print(f"At delay -/+{float(delay):.7f}: {float(values[0]):.10g}, {float(values[1]):.10g}")
    test_vertex_contact(a, b)
    test_negative_wave(a, b)


if __name__ == "__main__":
    main()
