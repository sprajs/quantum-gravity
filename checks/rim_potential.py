"""Check the finite-sheet potential, moving rim and angular endpoint charge."""

import cmath
from itertools import combinations
from math import cos, pi, sin


def integrate(function, lower, upper, intervals=128):
    """Composite Simpson quadrature, also on complex deformations of the rim."""
    step = (upper - lower) / intervals
    values = [function(lower + i * step) for i in range(intervals + 1)]
    return step / 3 * (values[0] + values[-1] + 4 * sum(values[1:-1:2])
                       + 2 * sum(values[2:-1:2]))


def profile(v, a, c):
    """Both components of z, z' and z'' for a family on the hyperbolic target."""
    return ((a * v + c * v**2, a * v**3 - c * v),
            (a + 2 * c * v, 3 * a * v**2 - c),
            (2 * c, 6 * a * v))


def add(first, second, factor):
    return tuple(u + factor * w for u, w in zip(first, second))


def pairing(z, first, second):
    return first[0] * second[0] + cmath.exp(2 * z[0]) * first[1] * second[1]


def sheet_potential(fields, direction):
    """(A.9) in fixed x ∈ [0,1], V(0)=b and V(1)=1, oriented from 1 to 0."""
    r, b, a, c = fields
    dr, db, da, dc = direction
    w = 1 - b

    def flux(x):
        v = b + w * x
        dv = (1 - x) * db
        z, p, _ = profile(v, a, c)
        dz = add(profile(v, da, dc)[0], p, dv)
        shear_term = w * pairing(z, p, dz)
        expansion = 2 * w / v
        kappa = w * v * pairing(z, p, p) / 4
        dlog_area = dr / r + 2 * dv / v
        return r * v**2 * (shear_term - (2 * kappa + expansion) * dlog_area)

    return integrate(flux, 1, 0) + 2 * ((b**2 - 1) * dr + 2 * r * b * db)


def printed_and_rim(fields, first, second):
    """(A.14) integral including target Christoffels, plus explicit rim terms."""
    r, b, a, c = fields

    def mixed(v, direction):
        dr, _, da, dc = direction
        z, p, pp = profile(v, a, c)
        dz, dp, _ = profile(v, da, dc)
        x = add(dz, p, -v * dr / (2 * r))
        xp = add(add(dp, p, -dr / (2 * r)), pp, -v * dr / (2 * r))
        connection = (-cmath.exp(2 * z[0]) * p[1] * x[1],
                      p[0] * x[1] + p[1] * x[0])
        return x, add(xp, connection, 1)

    def bulk(v):
        z = profile(v, a, c)[0]
        x, xp = mixed(v, first)
        y, yp = mixed(v, second)
        return r * v**2 * (pairing(z, xp, y) - pairing(z, yp, x))

    def endpoint(v, direction, move):
        _, db, da, dc = direction
        z, p, _ = profile(v, a, c)
        return pairing(z, p, add(profile(v, da, dc)[0], p, db if move else 0))

    def area(direction):
        return b**2 * direction[0] + 2 * r * b * direction[1]

    corner = -(first[0] * endpoint(1, second, False)
               - second[0] * endpoint(1, first, False)) / 2
    printed = corner + integrate(bulk, 1, b)
    rim = b / 2 * (area(first) * endpoint(b, second, True)
                   - area(second) * endpoint(b, first, True))
    frame = 2 * (first[0] * second[1] - second[0] * first[1])
    return printed, rim, frame


def differential(fields, first, second):
    step = 1e-20
    d_first = sheet_potential(add(fields, first, 1j * step), second).imag / step
    d_second = sheet_potential(add(fields, second, 1j * step), first).imag / step
    return d_first - d_second


def angular_test():
    """A periodic angular patch with nonzero shear, twist and cut displacement."""
    a, r, b = 0.7, 1.3, 0.4

    def evaluate(v, angle):
        s, c = sin(angle), cos(angle)
        zv = a * c
        zy = -a * v * s
        y = (1 - v) * (s + sin(2 * angle))
        dy = (1 - v) * (c + 2 * cos(2 * angle))
        velocity = -(s + sin(2 * angle))
        density = r * v**2
        twist_density = r * (a * v**3 * s / 6 - a**2 * v**4 * s * c / 4)
        angular_flux = (density * (zv * (zy * y + dy)
                        - (v * zv**2 / 2 + 2 / v) * dy)
                        + 2 * twist_density * velocity)
        return angular_flux, 2 * twist_density * y

    def mean(v, index):
        return sum(evaluate(v, 2 * pi * j / 24)[index] for j in range(24)) / 24

    flux = integrate(lambda v: mean(v, 0), 1, b)
    charge = mean(b, 1) - mean(1, 1)
    assert abs(flux - charge) < 1e-10 and abs(charge) > 1e-3, (flux, charge)
    print(f"Angular flux and endpoint charge (cut average): {charge:.8f}")


if __name__ == "__main__":
    basis = [tuple(int(i == j) for j in range(4)) for i in range(4)]
    for fields in ((1.7, 0.4, 0.3, -0.2), (0.8, 0.7, -0.2, 0.5)):
        residuals = []
        for first, second in combinations(basis, 2):
            parts = printed_and_rim(fields, first, second)
            residuals.append(abs(differential(fields, first, second) - sum(parts)))
        assert max(residuals) < 2e-8, residuals
        print(f"b={fields[1]}: six two-form components agree within 2e-8")
    angular_test()
