"""Sharp brackets of cylindrical affine clocks, normalized by Newton's constant."""

from dataclasses import dataclass
from functools import lru_cache
from math import exp, fsum, sqrt

from joint_resolution import integrate, jump, piecewise


@dataclass(frozen=True)
class Clock:
    cap: float
    slope: float  # dq/dr on this face; the waist has r=1.

    def weight(self, r):
        a, k = self.cap, self.slope
        return exp(k * (r - a) + k*k * (r*r - a*a)/4) / (2*sqrt(a))

    @lru_cache(maxsize=12000)
    def remaining(self, r):
        return integrate(self.weight, r, 1)

    def sensitivity(self, r):
        return (1 + self.slope*r) * self.remaining(r)

    def density(self, r):
        """Smooth part of the clock source divided by sqrt(r)."""
        return ((1 + self.slope*r) * self.weight(r)
                - self.slope * self.remaining(r)) / sqrt(r)

    def atom(self):
        return -self.sensitivity(self.cap) / sqrt(self.cap)

    def moment(self, n):
        """Apply the unweighted source to r^(-1/2)((1-r)/r)^n by variation."""
        def response(r):
            ratio = (1 - r)/r
            derivative = -ratio**n / (2*r**1.5)
            if n:
                derivative -= n * ratio**(n-1) / r**2.5
            return self.sensitivity(r) * derivative

        return piecewise(response, [(1 + self.cap)/2], self.cap, 1)


def opposed_series(first, second):
    coefficient, terms = 1.0, []
    for n in range(16):
        terms.append(coefficient * first.moment(n) * second.moment(n))
        coefficient *= ((2*n + 1)/(2*n + 2))**2
    # c=1/(4G); K(m)/pi starts at 1/2.
    return 2 * fsum(terms)


def opposed_direct(first, second, delay=0.0):
    front = 1 + delay/2

    def kernel(r, s):
        parameter = (front-r)*(front-s)/(r*s)
        if parameter <= 0:
            return 0.0
        return jump(parameter) if r < front else -jump(parameter)

    def row(r):
        return (second.atom() * kernel(r, second.cap)
                + piecewise(lambda s: second.density(s) * kernel(r, s),
                            [front], second.cap, 1))

    return 4 * (first.atom() * row(first.cap)
                + piecewise(lambda r: first.density(r) * row(r), [front], first.cap, 1))


def delayed_same_face(first, second, delay):
    """Exact pre-axis kernel, split at its direct front, with separate cap atoms."""
    if delay < 0:
        return -delayed_same_face(second, first, -delay)
    assert 0 < delay < min(first.cap, second.cap)

    def row(r):
        def kernel(s):
            return jump(max(0, delay * (2*(s-r) + delay)/(4*r*s)))

        threshold = r - delay/2
        atom = second.atom()*kernel(second.cap) if second.cap > threshold else 0
        return atom + integrate(lambda s: second.density(s) * kernel(s),
                                max(second.cap, threshold), 1)

    bulk = piecewise(lambda r: first.density(r)*row(r),
                     [second.cap + delay/2, (1 + first.cap)/2], first.cap, 1)
    return 4 * (first.atom()*row(first.cap) + bulk)


def zero_mass_slope(cap):
    low, high = -1/cap, -1.0
    assert Clock(cap, low).moment(0) > 0 > Clock(cap, high).moment(0)
    for _ in range(54):
        middle = (low + high)/2
        if Clock(cap, middle).moment(0) > 0:
            low = middle
        else:
            high = middle
    return (low + high)/2


def main():
    # The signs of the slopes differ because the upper ray runs to the past.
    lower, upper = Clock(0.64, 0.5), Clock(0.81, -0.5)
    series = opposed_series(lower, upper)
    direct = opposed_direct(lower, upper)
    assert abs(series - direct) < 2e-12 and series > 0
    assert abs(direct - 0.0010258692) < 5e-11
    for sign in (-1, 1):
        coarse = opposed_direct(lower, upper, sign*1e-4)
        fine = opposed_direct(lower, upper, sign*1e-6)
        assert abs(fine-direct) < 0.02 * abs(coarse-direct)
    print(f"Opposite faces, curved vacuum: bracket / G = {direct:.10f}")

    a, b = 0.36, 0.81
    alpha = zero_mass_slope(a)
    first, second = Clock(a, alpha), Clock(b, alpha)
    assert abs(first.moment(0)) < 2e-14
    ratio = first.weight(b) / second.weight(b)
    expected = ratio * (second.atom()**2 - second.moment(0)**2)
    assert abs(expected - 0.0043908526) < 5e-11
    print(f"Same outgoing face, zero first mass at alpha*R = {alpha:.10f}")
    for delay in (1e-3, 1e-5, 1e-7):
        earlier = delayed_same_face(first, second, -delay)
        later = delayed_same_face(first, second, delay)
        assert max(abs(earlier-expected), abs(later-expected)) < delay/5 + 1e-10
        print(f"Delay +/-{delay:.0e}, earlier {earlier:.10f}, later {later:.10f}")
    print(f"Common sharp bracket / G = {expected:.10f}")

    # Without the calibration the two sides differ by M_a M_b / (2c).
    ordinary_first, ordinary_second = Clock(a, 0.5), Clock(b, 0.5)
    predicted = 2 * ordinary_first.moment(0) * ordinary_second.moment(0)
    later = delayed_same_face(ordinary_first, ordinary_second, 1e-8)
    earlier = delayed_same_face(ordinary_first, ordinary_second, -1e-8)
    assert abs(later - earlier - predicted) < 2e-8 and predicted > 0
    print(f"Uncalibrated same-face jump / G = {predicted:.10f}")


if __name__ == '__main__':
    main()
