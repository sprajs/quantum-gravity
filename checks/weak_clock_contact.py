"""Time-translate the weak spherical quadrupole and pair its complete profiles."""

from fractions import Fraction as F
from math import comb, factorial


CAP = F(1, 3)
OMEGA = F(3, 5120)  # G_N = 1
HESSIAN = F(3, 20)


def add(*polys):
    summed = {}
    for p in polys:
        for i, coefficient in p.items():
            summed[i] = summed.get(i, 0) + coefficient
    return {i: value for i, value in summed.items() if value}


def scale(p, factor, degree=0):
    return {i + degree: factor * value for i, value in p.items()}


def product(p, q):
    return add(*(scale(p, value, i) for i, value in q.items()))


def translate(p, delay):
    """Coefficients of p(s-delay)."""
    return add(*({j: c * comb(i, j) * (-delay)**(i-j) for j in range(i+1)}
                 for i, c in p.items()))


def evaluate(p, position):
    return sum(c * position**i for i, c in p.items())


def integrate(p, lower, upper):
    return sum(c * (upper**(i+1) - lower**(i+1)) / (i+1)
               for i, c in p.items())


def primitive_piece(q, order):
    # Integral of q(z)*(s-z)^order/order! from z=CAP to z=s.
    terms = []
    for n, value in q.items():
        for j in range(order + 1):
            c = value * comb(order, j) * (-1)**j / (factorial(order) * (n+j+1))
            terms.append({order+n+1: c})
            terms.append({order-j: -c * CAP**(n+j+1)})
    return add(*terms)


def build_sections():
    # G'_W = p s^4 + q s^5 with unit rim slope and zero vertex fourth derivative.
    moment = [integrate({n-1: F(1), n: F(-1)}, CAP, F(1)) for n in (4, 5)]
    p = 1 / (CAP**4 - CAP**5 * moment[0] / moment[1])
    q = -p * moment[0] / moment[1]
    slope = {4: p, 5: q}
    weight = product(slope, {1: 1, 2: -1})
    assert evaluate(slope, CAP) == 1
    assert integrate(scale(weight, 1, -2), CAP, F(1)) == 0
    # Kernel for f_X^(4) from its fifth primitive. Second master derivative at
    # the vertex contributes 1/4 of the u-coordinate second derivative.
    vertex = HESSIAN * F(3, 4) * integrate(scale(weight, 1, -4), CAP, F(1))
    before = {2: vertex / (2 * OMEGA)}
    slope_weights = (F(-3, 4), F(3, 4), F(-5, 16), F(1, 16))
    weights = {j: scale(weight, c, j-6) for j, c in enumerate(slope_weights, 2)}
    ordinary = [scale(primitive_piece(weights[j], 4-j), (-1)**j) for j in (2, 3, 4)]
    after = add(before, scale(add(*ordinary, scale(weights[5], -1)), HESSIAN / OMEGA))
    # For s>1 the kernel is an ordinary polynomial of degree at most four.
    # Check independently that the optical and vertex moments cancel its tail.
    for s in range(2, 7):
        tail = evaluate(before, F(s))
        for j in (2, 3, 4):
            n = 4-j
            kernel = {i: F((-1)**(i+j) * comb(n, i) * s**(n-i), factorial(n))
                      for i in range(n+1)}
            tail += HESSIAN * integrate(product(weights[j], kernel), CAP, F(1)) / OMEGA
        assert tail == 0
    jump = evaluate(after, CAP) - evaluate(before, CAP)
    assert jump == -16 * (1-CAP) and evaluate(after, F(1)) == 0
    return [(F(0), CAP, before), (CAP, F(1), after)], jump


def cross_bracket(sections, jump, delay):
    # Positive delay places the translated experiment at later Minkowski time.
    # The master g=f_X^(4) translates by half the physical delay.
    shift = delay / 2
    result = F(0)
    for lower, upper, current in sections:
        regular = {j-1: j*c for j, c in current.items() if j}
        for other_lower, other_upper, other in sections:
            lo = max(lower, other_lower+shift)
            hi = min(upper, other_upper+shift)
            if lo < hi:
                result += integrate(product(regular, translate(other, shift)), lo, hi)
    for lo, hi, section in sections:
        if lo < CAP-shift < hi:
            result += jump * evaluate(section, CAP-shift)
    return -OMEGA * result


def main():
    sections, jump = build_sections()
    limit = OMEGA * jump**2 / 2
    assert limit == F(1, 30)
    for delay in (F(1, 1000), F(1, 100000), F(1, 10000000)):
        value = cross_bracket(sections, jump, delay)
        assert cross_bracket(sections, jump, -delay) == -value
        print(f"Proper-time delay {float(delay):.7f}: spherical clock bracket {float(value):.8f}")
    assert abs(value - limit) < F(1, 50000)
    # Two centered detectors with equal variances. Convolving every atom with
    # the same even compact bump of radius <1/8 preserves the ordering and moments.
    first = ((-1, F(1, 2)), (1, F(1, 2)))
    second = ((F(1, 2), F(4, 5)), (-2, F(1, 5)))
    for j in (0, 1, 2):
        assert sum(t**j*w for t, w in first) == sum(t**j*w for t, w in second)
    bias = sum(w*v*(1 if s>t else -1) for t,w in first for s,v in second)
    assert bias * limit == F(-1, 150)
    print(f"Later-time limit {limit}; equal-moment detector limit {bias*limit} (G_N=1)")


if __name__ == "__main__":
    main()
