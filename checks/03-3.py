"""Exterior derivative of (A.14) on an exact polynomial family, using rational arithmetic."""

from fractions import Fraction as F


def jet(v, x, y):
    """Field and first two derivatives of z=x(1-v)^2+y(1-v)^3."""
    t = 1 - v
    return x*t**2 + y*t**3, -2*x*t - 3*y*t**2, 2*x + 6*y*t


def omega(cap, area, x, y, first, second):
    """One branch, per solid angle, multiplied by 16 pi G."""
    def variation(v, vector):
        da, dx, dy = vector
        z, dz, _ = jet(v, dx, dy)
        _, p, dp = jet(v, x, y)
        c = da / (2 * area)
        return z - v*c*p, dz - c*(p + v*dp)

    def integrand(v):
        h, dh = variation(v, first)
        k, dk = variation(v, second)
        return area * v**2 * (dh*k - dk*h)

    # Both z(1) and z'(1) vanish, so the mixed corner term is zero.
    # The integrand has degree at most seven on this family. The closed
    # seven-node Newton-Cotes rule integrates each coefficient exactly.
    weights = [41, 216, 27, 272, 27, 216, 41]
    return (cap-1) * sum(
        w*integrand(1+(cap-1)*i/6) for i, w in enumerate(weights)
    ) / 840


def exterior_derivative(cap):
    ea, ex, ey = [tuple(F(i == j) for i in range(3)) for j in range(3)]
    # Each evaluated component is affine in the differentiated parameter.
    return (
        omega(cap, F(2), 0, 0, ex, ey) - omega(cap, F(1), 0, 0, ex, ey)
        + omega(cap, F(1), 1, 0, ey, ea) - omega(cap, F(1), 0, 0, ey, ea)
        + omega(cap, F(1), 0, 1, ea, ex) - omega(cap, F(1), 0, 0, ea, ex)
    )


if __name__ == "__main__":
    for cap in [F(0), F(1, 4), F(1, 2), F(3, 4)]:
        result = exterior_derivative(cap)
        expected = cap**3 * (1-cap)**4 / 2
        assert result == expected, (cap, result, expected)
        print(f"b = {cap}, 16 pi G times dOmega(dA, dx, dy) = {result}")
