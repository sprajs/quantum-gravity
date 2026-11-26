"""Check the common-window weak-wave contact by polarization and time integration."""

from fractions import Fraction
from math import ceil, cos, exp, pi, sin, sqrt

from weak_curved import GAUSS


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def combine(a, x, b, y):
    return tuple(x * u + y * v for u, v in zip(a, b))


def polarizations(a, b):
    def plus(x, y):
        return (dot(a, x) * dot(a, y) - dot(b, x) * dot(b, y)) / sqrt(2)

    def cross(x, y):
        return (dot(a, x) * dot(b, y) + dot(b, x) * dot(a, y)) / sqrt(2)

    return plus, cross


def angular_mixed(q):
    # Rotate a unit plane-wave background; sum both unit TT test polarizations.
    # Its E and B have squared norms 1/4 each at unit frequency.
    x, y, z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    mu = 1 - q
    n = (sqrt(1 - mu**2), 0, mu)
    screen = ((mu, 0, -n[0]), y)
    test = polarizations(x, y)

    def tidal(direction, strain):
        difference = 1 - dot(direction, n)
        axes = [combine(e, difference, n, dot(direction, e)) for e in screen]
        return [strain(a, b) / 2 for a in axes for b in axes]

    test_tides = [tidal(z, f) for f in test]
    total = 0.0
    for u, weight in GAUSS:
        radial = sqrt(1 - u*u)
        for i in range(12):
            phi = (i + 0.5) * pi / 6
            d = (radial*cos(phi), radial*sin(phi), u)
            theta = (u*cos(phi), u*sin(phi), -radial)
            azimuth = (-sin(phi), cos(phi), 0)
            background = polarizations(theta, azimuth)
            for j, f in enumerate(background):
                # Hodge dual on the two polarizations sends + to x and x to -+.
                dual = background[1-j]
                bsign = 1 - 2*j
                btide = tidal(d, f)
                for k in (0, 1):
                    ep = (f(x, x) - f(y, y)) / sqrt(2) if k == 0 else sqrt(2)*f(x, y)
                    bp = sqrt(2)*dual(x, y) if k == 0 else -(dual(x, x)-dual(y, y))/sqrt(2)
                    point = (ep + bsign*bp) / 2
                    total += weight * point * dot(btide, test_tides[k]) / 48
    return total


def gauss(f, lower, upper):
    center = (upper + lower) / 2
    scale = (upper - lower) / 2
    return scale * sum(weight * f(center + scale*z) for z, weight in GAUSS)


def gaussian_mixed(cap, width):
    # Directly integrate the affine ray and angle variables. A unit normal
    # detector window has autocorrelation exp(-s^2/4)/(2 sqrt(pi)).
    def fifth(z):
        poly = -z**5 / 32 + 5*z**3 / 8 - 15*z / 8
        return exp(-z*z/4) * poly / (2*sqrt(pi))

    def ray(t):
        # Effective range z=qt/h <= 20; its remaining Gaussian tail is negligible.
        upper = min(2*t/width, 20)
        count = max(1, ceil(2*upper))
        angle = sum(gauss(lambda z: z**4*fifth(z), upper*i/count,
                          upper*(i+1)/count) for i in range(count))
        kernel = t*t*(1-max(t, cap))**2 / 6
        return -kernel * angle / (2*width*t**5)

    edges = {0, cap, 1}
    t = width / 2
    while t < 1:
        edges.add(t)
        t *= 2
    edges = sorted(edges)
    return sum(gauss(ray, l+(r-l)*i/4, l+(r-l)*(i+1)/4)
               for l, r in zip(edges, edges[1:]) for i in range(4))


def main():
    for q in (0.25, 1, 1.75):
        # w0=1/2 for the unit reference polarization.
        assert abs(angular_mixed(q) - q**4/20) < 1e-14
    print("Direct two-polarization contractions: w0 q^4/10")

    a, b = Fraction(1, 3), Fraction(1, 2)

    def c(s):
        return -(1-5*s**4+4*s**5)/225

    def u(s):
        return (1-s)**2/6

    coefficient = Fraction(16, 5) * (c(a)*u(b)-c(b)*u(a))
    assert coefficient == Fraction(238, 820125)
    print("Common-window h^(-3) contact / (G w0 R^7 eta''(0)):", coefficient)
    last_error = 1.0
    for h in (0.02, 0.01, 0.005):
        mixed = c(a)*gaussian_mixed(float(b), h) - c(b)*gaussian_mixed(float(a), h)
        ratio = (16/10)*h**3*mixed / (-float(coefficient)/(4*sqrt(pi)))
        err = abs(ratio - 1)
        assert err < 0.26 * last_error
        last_error = err
        print(f"Gaussian mixed term / leading contact, h={h:.3f}: {ratio:.8f}")
    assert last_error < 0.003


if __name__ == "__main__":
    main()
