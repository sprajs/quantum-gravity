"""Two clocks on one Einstein–Rosen null face, in units R=1 and bracket/G."""

from functools import lru_cache
from math import fsum, isclose, sqrt

EPSILON = 3 / 4
# Eight-point Gauss-Legendre integration, using the positive nodes.
RULE = ((0.1834346424956498, 0.3626837833783620),
        (0.5255324099163290, 0.3137066458778873),
        (0.7966664774136267, 0.2223810344533745),
        (0.9602898564975363, 0.1012285362903763))


def integrate(fn, lo, hi):
    if hi <= lo:
        return 0.0
    midpoint, half = (hi + lo) / 2, (hi - lo) / 2
    return half * fsum(w * (fn(midpoint - half * x) + fn(midpoint + half * x))
                       for x, w in RULE)


def piecewise(fn, knots, lo, hi):
    edges = [lo, *sorted({x for x in knots if lo < x < hi}), hi]
    return fsum(integrate(fn, left, right) for left, right in zip(edges, edges[1:]))


def jump(parameter):
    """Complete elliptic integral K(m)/pi by the arithmetic-geometric mean."""
    assert 0 <= parameter < 1
    a, b = 1.0, sqrt(1 - parameter)
    for _ in range(5):
        a, b = (a + b) / 2, sqrt(a * b)
    return 1 / (2 * a)


def cap_response(h):
    """Density in v and signed clock source in y=sqrt(r), divided by sqrt(r)."""
    lo, hi = EPSILON - h, EPSILON + h

    def density(v):
        x = (v - EPSILON) / h
        return 15 / (16 * h) * (1 - x * x)**2 if abs(x) < 1 else 0.0

    @lru_cache(maxsize=4096)
    def source(y):
        bulk = integrate(lambda v: density(v) / v, lo, min(y, hi))
        return density(y) * (1 - y*y) / (y*y) - 2 * bulk

    return density, source


def later_clock_bracket(h, delay):
    """Angular-integrated retarded propagator on the two displaced null faces."""
    assert delay > 0
    lo, hi = EPSILON - h, EPSILON + h
    _, source = cap_response(h)

    def row(y):
        radius = y*y

        def integrand(z):
            other = z*z
            parameter = delay * (2 * (other - radius) + delay) / (4 * radius * other)
            return source(z) * jump(max(0.0, parameter))

        start = max(lo, sqrt(max(0, radius - delay / 2)))
        return source(y) * piecewise(integrand, [hi], start, 1.0)

    crossings = [hi, *(sqrt(y*y + delay / 2) for y in (lo, hi))]
    return piecewise(row, crossings, lo, 1.0)


def main():
    moment = ((1 - EPSILON) / EPSILON)**2
    atom = (1 - EPSILON**2) / EPSILON**2
    positive_slow_cap = moment**2 / 4
    positive_fast_cap = (moment**2 + atom**2) / 4
    # The two signs are sampled with probabilities 3/4 and 1/4.
    assert isclose(positive_slow_cap / 2, 1 / 648)
    assert isclose(positive_fast_cap / 2, 25 / 324)

    eta = 1 / 256
    slow_h, fast_h = eta, eta**3
    slow = later_clock_bracket(slow_h, eta**3)
    fast = later_clock_bracket(fast_h, eta)
    assert abs(slow - positive_slow_cap) < 2e-5
    assert abs(fast - positive_fast_cap) < 0.002
    for h, delay, expected in ((slow_h / 2, (eta / 2)**3, positive_slow_cap),
                               ((eta / 2)**3, eta / 2, positive_fast_cap)):
        error = abs(later_clock_bracket(h, delay) - expected)
        previous = abs((slow if h > delay else fast) - expected)
        assert error < 0.6 * previous

    # Smooth probe X psi = t on the domain. Its constant initial velocity
    # can be continued with compact support outside the local domain of dependence.
    h = 1 / 512
    density, source = cap_response(h)
    lo, hi = EPSILON - h, EPSILON + h
    smeared = piecewise(lambda y: source(y) * y * (y*y - 1), [hi], lo, 1)
    cap_average = integrate(lambda v: -density(v) * (1-v*v)**2 / (2*v), lo, hi)
    assert isclose(smeared, cap_average, abs_tol=2e-12)
    assert abs(smeared + 49/384) < 2e-6
    print(f"Later clock, broad cap collar: {slow:.8f}; limit {positive_slow_cap:.8f}")
    print(f"Later clock, narrow cap collar: {fast:.8f}; limit {positive_fast_cap:.8f}")
    print("Centered skew timing, limiting brackets / G: 1/648 and 25/324")
    print(f"Smooth-probe variation: {smeared:.8f}; limit {-49/384:.8f}")


if __name__ == "__main__":
    main()
