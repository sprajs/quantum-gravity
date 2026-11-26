"""Pair two full-line spherical clock covectors, including the point-vertex source."""

from fractions import Fraction as F

from joint_spherical_hessian import falling
from weak_clock_contact import (
    CAP, HESSIAN, OMEGA, add, evaluate, integrate, primitive_piece, product,
    scale, translate,
)


def response(slope):
    """Compute z = f_X'''' in units G_N=1 by integrating from the left."""
    weight = product(slope, {1: F(1), 2: F(-1)})
    vertex_four = -F(1, 16) * integrate(scale(weight, 1, -2), CAP, F(1))
    vertex_two = F(3, 4) * integrate(scale(weight, 1, -4), CAP, F(1))
    before = scale({0: vertex_four, 2: vertex_two / 2}, HESSIAN / OMEGA)
    coefficients = (F(-3, 4), F(3, 4), F(-5, 16), F(1, 16))
    weights = {j: scale(weight, c, j-6) for j, c in enumerate(coefficients, 2)}
    terms = [scale(primitive_piece(weights[j], 4-j), (-1)**j) for j in (2, 3, 4)]
    after = add(before, scale(add(*terms, scale(weights[5], -1)), HESSIAN / OMEGA))
    assert evaluate(after, CAP) - evaluate(before, CAP) == -16*(1-CAP)*evaluate(slope, CAP)
    assert evaluate(after, F(1)) == 0
    return [(F(0), CAP, before), (CAP, F(1), after)]


def strain_slope(power):
    """Vertex-normalized G' for the test master f(s)=s^power near [0,1]."""
    strain = (F(falling(power, 4), 16) - F(falling(power, 3), 4)
              + F(falling(power, 2), 4))
    return add({power-6: (power-5)*strain},
               {-4: F(3, 2)} if power == 2 else {},
               {-2: F(-3, 2)} if power == 4 else {})


def verify_source(sections, slope):
    # Compare -Omega*int z f^(5) with the original optical Hessian, including
    # tests that have nonvanishing jets at the vertex and at the waist.
    weight = product(slope, {1: F(1), 2: F(-1)})
    for power in range(17):
        fifth = {power-5: falling(power, 5)} if power >= 5 else {}
        from_master = -OMEGA * sum(integrate(product(z, fifth), lo, hi)
                                   for lo, hi, z in sections)
        optical = HESSIAN * integrate(product(weight, strain_slope(power)), CAP, F(1))
        assert from_master == optical


def jumps(sections):
    atoms = {}
    for lo, hi, z in sections:
        atoms[lo] = atoms.get(lo, 0) + evaluate(z, lo)
        atoms[hi] = atoms.get(hi, 0) - evaluate(z, hi)
    return {s: value for s, value in atoms.items() if value}


def bracket(first, second, delay, *, left_trace=True):
    """At a collision, left_trace selects the limit from positive proper delay."""
    shift = delay / 2
    result = F(0)
    for lo, hi, z in first:
        regular = {j-1: j*c for j, c in z.items() if j}
        for lower, upper, other in second:
            start, end = max(lo, lower+shift), min(hi, upper+shift)
            if start < end:
                result += integrate(product(regular, translate(other, shift)), start, end)
    for location, jump in jumps(first).items():
        pos = location - shift
        for lo, hi, other in second:
            in_piece = lo < pos <= hi if left_trace else lo <= pos < hi
            if in_piece:
                result += jump * evaluate(other, pos)
    return -OMEGA * result


def main():
    for power, amplitude in [(10, F(2, 1575)), (11, F(1, 1650))]:
        assert scale(strain_slope(power), amplitude) == {power-6: F(1)}
    slope4, slope5 = {4: F(1)}, {5: F(1)}
    first, second = response(slope4), response(slope5)
    verify_source(first, slope4)
    verify_source(second, slope5)
    later = bracket(first, second, F(0))
    earlier = bracket(first, second, F(0), left_trace=False)
    midpoint = (later + earlier) / 2
    assert later == F(69593, 243577125) and earlier == F(3889, 81192375)
    assert midpoint == F(8126, 48715425)
    assert bracket(second, first, F(0), left_trace=False) == -later
    assert bracket(second, first, F(0)) == -earlier
    d4, d5 = jumps(first), jumps(second)
    overlap = sum(value*d5[s] for s, value in d4.items())
    assert later - earlier == OMEGA * overlap
    for delay in (F(1, 1000), F(1, 100000), F(1, 10000000)):
        positive = bracket(first, second, delay)
        negative = bracket(first, second, -delay)
        assert positive == -bracket(second, first, -delay)
        assert negative == -bracket(second, first, delay)
        print(f"At delays +/-{float(delay):.7f}, B/G_N = {float(positive):.10f}, "
              f"{float(negative):.10f}")
    assert abs(positive-later) < F(1, 10**8) and abs(negative-earlier) < F(1, 10**8)
    print(f"Later {later}, earlier {earlier}, common-window midpoint {midpoint} (G_N=1)")

    coefficient = overlap / sum(v*v for v in d4.values())
    assert coefficient == F(2633, 3897)
    compensated = response(add(slope5, scale(slope4, -coefficient)))
    corrected_jumps = jumps(compensated)
    assert set(corrected_jumps) == {F(0), CAP}
    assert sum(v*corrected_jumps[s] for s, v in d4.items()) == 0
    for left_trace in (True, False):
        assert bracket(first, compensated, F(0), left_trace=left_trace) == midpoint
    print(f"For reference slope s^5 - ({coefficient})s^4, both limits = {midpoint}")


if __name__ == "__main__":
    main()
