#!/usr/bin/env python3
"""Vary both null faces of a compact Kasner diamond in audit/joint-jacobi.md."""

from math import cos, exp, log, pi, sin, sqrt
from fractions import Fraction

# Gauss-Legendre on [-1,1]. Four nodes suffice for the leading angular moment.
GAUSS = [
    (-0.8611363115940526, 0.3478548451374539),
    (-0.3399810435848563, 0.6521451548625461),
    (0.3399810435848563, 0.6521451548625461),
    (0.8611363115940526, 0.3478548451374539),
]


def nodes(lo, hi):
    return [((lo + hi + (hi - lo) * x) / 2, (hi - lo) * w / 2) for x, w in GAUSS]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def cross(x, y):
    return [x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2],
            x[0] * y[1] - x[1] * y[0]]


def unit(x):
    length = sqrt(dot(x, x))
    return [a / length for a in x]


def frame(n):
    axis = [0, 0, 1] if abs(n[2]) < 0.9 else [0, 1, 0]
    e = unit(cross(n, axis))
    return e, cross(n, e)


def exponents(b):
    den = 1 + b + b * b
    return [-b / den, (1 + b) / den, b * (1 + b) / den]


def velocity(t, p, n):
    """Coordinate ray velocity, affine lapse dt/ds, and inverse squared scales."""
    inverse = [t ** (-2 * a) for a in p]
    energy = sqrt(sum(d * ni * ni for d, ni in zip(inverse, n)))
    return [d * ni / energy for d, ni in zip(inverse, n)], energy, inverse


def ray(lo, hi, p, n, basis=()):
    """Integrate x(t) and its transverse derivatives with respect to momenta."""
    x = [0.0] * 3
    jac = [[0.0] * 3 for _ in basis]
    for t, w in nodes(lo, hi):
        v, energy, inv = velocity(t, p, n)
        for i in range(3):
            x[i] += w * v[i]
        for e, col in zip(basis, jac):
            ve = dot(v, e)
            for i in range(3):
                col[i] += w * (inv[i] * e[i] - v[i] * ve) / energy
    return x, jac


def waist(end, p, n):
    """Solve the three spatial matching equations for t and the return direction."""
    t = (1.0 + end) / 2
    m = n
    for _ in range(8):
        x, _ = ray(1.0, t, p, n)
        basis = frame(m)
        y, jac = ray(t, end, p, m, basis)
        residual = [a - b for a, b in zip(y, x)]
        if max(map(abs, residual)) < 4e-15:
            return t
        v, _, _ = velocity(t, p, n)
        w, _, _ = velocity(t, p, m)
        cols = [[a + b for a, b in zip(v, w)], [-c for c in jac[0]],
                [-c for c in jac[1]]]
        det = dot(cols[0], cross(cols[1], cols[2]))
        dt, dm, dn = [dot(residual, cross(cols[(i+1) % 3], cols[(i+2) % 3])) / det
                      for i in range(3)]
        t += dt
        m = unit([a + dm * e + dn * f for a, e, f in zip(m, *basis)])
    raise AssertionError("waist shooting failed")


def screen(t, p, n, basis):
    """Optical distance and affine derivative from the proper screen parallelogram."""
    _, jac = ray(1.0, t, p, n, basis)
    v, energy, inverse = velocity(t, p, n)
    axis = [t ** a for a in p]
    cols = [[s * value for s, value in zip(axis, col)] for col in jac]
    rates = []
    for e, col in zip(basis, cols):
        ve = dot(v, e)
        rates.append([a * c / t + s * (d * ei - vi * ve) / energy
                      for a, c, s, d, ei, vi in zip(p, col, axis, inverse, e, v)])
    area = cross(*cols)
    rate = [a + b for a, b in zip(cross(rates[0], cols[1]), cross(cols[0], rates[1]))]
    norm2 = dot(area, area)
    radius = norm2 ** 0.25
    return radius, energy * radius * dot(area, rate) / (2 * norm2)


def sky(p, length, epsilon):
    """Intersect both light cones, fix each cap, and average with the v1 weight."""
    sum_d = sum_d2 = sum_du = 0.0
    for mu, w in GAUSS:
        for j in range(8):
            phi = j * pi / 4
            n = [sqrt(1 - mu * mu) * cos(phi), sqrt(1 - mu * mu) * sin(phi), mu]
            basis = frame(n)
            stop = waist(1 + 2 * length, p, n)
            ds, _ = screen(stop, p, n, basis)
            cap = 1 + epsilon * (stop - 1)
            for _ in range(6):
                dc, slope = screen(cap, p, n, basis)
                difference = dc - epsilon * ds
                if abs(difference) < 4e-16:
                    break
                cap -= difference * velocity(cap, p, n)[1] / slope
            else:
                raise AssertionError("cap shooting failed")
            interval = sum(weight / velocity(t, p, n)[1] for t, weight in nodes(cap, stop))
            sum_d += w * ds
            sum_d2 += w * ds * ds
            sum_du += w * ds * slope * interval
    return sum_d2 / sum_d, sum_du / sum_d


def matched_excess(b, matched, epsilon):
    p = exponents(b)
    length = matched
    for _ in range(6):
        waist_mean, clock = sky(p, length, epsilon)
        if abs(matched - waist_mean) < 1e-14:
            return clock - (1 - epsilon) * waist_mean
        length += matched - waist_mean
    raise AssertionError("matched-waist preparation failed")


def main():
    b = Fraction(2)
    p = exponents(b)
    electric_norm = sum(a*a*(1-a)**2 for a in p)
    assert electric_norm == Fraction(72,343)
    # In units V_T/(8 pi G T)=1 the metric-modulus response is dual to db.
    dp = [Fraction(v, 49) for v in (3, -8, 5)]
    assert sum(dp) == dot(p, dp) == 0
    modulus = [d / dot(dp, dp) for d in dp]
    assert dot(modulus, dp) == 1
    assert sum(modulus) == dot(p, modulus) == 0
    delectric = sum(2 * a * (1-a) * (1-2*a) * da for a, da in zip(p, dp))
    assert delectric == Fraction(-240, 2401)

    # Integrate the retarded-minus-advanced kernel against an even bump
    # in log(s/T). Normalizing the discrete quadrature preserves its moments.
    pulse = [(u, w*exp(-1/(1-u*u))) for u, w in GAUSS]
    for t in (0.1, 0.9, 2.0, 10.0):
        ret = sum(w*max(log(t)-u, 0) for u, w in pulse)
        adv = sum(w*max(u-log(t), 0) for u, w in pulse)
        assert abs((ret-adv)/sum(w for _, w in pulse) - log(t)) < 1e-14

    epsilon = 0.5
    factor = 1 - 5 * epsilon**4 + 4 * epsilon**5
    leading = -16 * factor / 36015
    step = 0.02
    print(f"predicted normalized bracket {leading:.8f}")
    measured = []
    for matched in (0.06, 0.03):
        plus = matched_excess(2 + step, matched, epsilon)
        minus = matched_excess(2 - step, matched, epsilon)
        result = (plus - minus) / (2 * step * matched**5)
        measured.append(result)
        print(f"R/T={matched:.2f} normalized bracket {result:.8f}")
    extrapolated = 2 * measured[1] - measured[0]
    assert abs(extrapolated / leading - 1) < 0.02
    assert abs(measured[1] - leading) < abs(measured[0] - leading)
    print(f"linear extrapolation          {extrapolated:.8f}")


if __name__ == "__main__":
    main()
