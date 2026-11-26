"""Finite-cap TT wave. Exact piecewise integrals, with c=1 in the impulse example."""

from fractions import Fraction as Q


def hat(x, center):
    distance = x - center
    if abs(distance) >= 1:
        return 0, 0
    return 1 - abs(distance), (1 if distance < 0 else -1)


def wave(t, x, centers):
    # h=A(x-t)+B(x+t). Derivatives are sampled strictly within each piece.
    a, da = hat(x - t, centers[0])
    b, db = hat(x + t, centers[1])
    return a + b, db - da, da + db


def check_graph_flux():
    length = Q(1, 2)
    centers_x = (Q(-1, 4), Q(1, 3))
    centers_y = (Q(1, 4), Q(2, 3))

    def flux(left, right, slope, intercept):
        # On t=slope*x+intercept, collect all preimages of the kink positions.
        points = {left, right}
        for centers in (centers_x, centers_y):
            for center, sign in zip(centers, (-1, 1)):
                speed = 1 + sign * slope
                if speed:
                    for knot in (center - 1, center, center + 1):
                        x = (knot - sign * intercept) / speed
                        if left < x < right:
                            points.add(x)
        points = sorted(points)
        total = 0
        for lo, hi in zip(points, points[1:]):
            x = (lo + hi) / 2
            t = slope * x + intercept
            h, ht, hx = wave(t, x, centers_x)
            k, kt, kx = wave(t, x, centers_y)
            total += (hi - lo) * ((ht + slope * hx) * k - (kt + slope * kx) * h)
        return total

    left, right = Q(-4), Q(4)
    flat = flux(left, right, 0, 0)
    null = flux(Q(0), length, 1, 0)
    caps = flux(left, Q(0), 0, 0) + flux(length, right, 0, length)
    assert null and caps and flat == caps + null
    print(f"Mixed slice flux: caps {caps}, null {null}, total {flat}")


def check_weak_response():
    # f=2 on (0,1/2), beta=-3/2 at 0. Compare a sheet measurement with its
    # transferred Cauchy response on independent configuration and velocity tests.
    # The three tests are (q,p)=(1-4x,0), (0,2x), (x**2,1) on [0,1].
    # They can be extended with compact support outside that interval.
    def integral(coefficients, end):
        return sum((Q(a, i + 1) * end**(i + 1) for i, a in enumerate(coefficients)), Q(0))

    def evaluate(coefficients, x):
        return sum(a * x**i for i, a in enumerate(coefficients))

    for q, p, expected in (((1, -4), (), Q(-3, 2)),
                           ((), (0, 2), Q(1, 6)),
                           ((0, 0, 1), (1,), Q(5, 12))):
        q0 = evaluate(q, 0)

        def trace(s):
            return (q0 + evaluate(q, 2*s) + integral(p, 2*s)) / 2

        # Simpson's rule is exact for these polynomial sheet traces.
        original = (trace(Q(0)) + 4*trace(Q(1, 4)) + trace(Q(1, 2))) / 6 - Q(3, 2)*q0
        # Xp=-delta_0+1_(0,1)/2, Xq=-(1-x)*1_(0,1)/2.
        transferred = -q0 + integral(q, 1)/2 + (integral(p, 1) - integral((0, *p), 1))/2
        assert original == transferred == expected
    print("Clock test variation -3/2; independent Cauchy tests 1/6 and 5/12")


def check_one_sided_response():
    # Propagate (3) from t=0 and compare to approach from either side of the
    # null source. All observations avoid the characteristic discontinuity.
    def position(x):
        return (x - 1)/2 if 0 < x < 1 else Q(0)

    def solution(t, x):
        lo, hi = x - t, x + t
        bulk_length = max(0, min(hi, 1) - max(lo, 0))
        momentum_integral = Q(bulk_length, 2) - int(lo < 0 < hi)
        return (position(lo) + position(hi) + momentum_integral)/2

    s = Q(1, 4)
    for offset in (Q(1, 16), Q(1, 64)):
        assert solution(s + offset, s) == s - Q(3, 4) + offset/2
        assert solution(s - offset, s) == s - Q(1, 2) - offset/2
    print("One-sided field limits at s=1/4: -1/2 and -1/4")


def response_energy(width):
    # Convolution by the unit-mass box on [-width,width]. Each segment has
    # constant mollified delta and an affine mollified interval indicator.
    segments = ((2*width, 1/(2*width), 0, 1),
                (1 - 2*width, Q(0), 1, 1),
                (2*width, Q(0), 1, 0))
    total = 0
    for length, delta, left, right in segments:
        def density(indicator):
            momentum = Q(indicator, 2) - delta
            gradient = Q(indicator, 2) - delta/2
            return (momentum**2 + gradient**2) / 2

        middle = Q(left + right, 2)
        total += length * (density(left) + 4*density(middle) + density(right)) / 6
    return total


def check_resolution():
    for scale in (4, 16, 64, 256):
        width = Q(1, scale)
        energy = response_energy(width)
        assert energy == Q(5, 16)/width - Q(1, 8) - width/6
    print("Box-smoothed response: width * energy tends to 5/16")


if __name__ == "__main__":
    check_graph_flux()
    check_weak_response()
    check_one_sided_response()
    check_resolution()
