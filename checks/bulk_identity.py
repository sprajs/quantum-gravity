# /// script
# requires-python = ">=3.10"
# dependencies = ["sympy==1.14.0"]
# ///
"""Exact two-jet proof of the affine bulk density in arXiv:2611.34924v1, B.10–11."""

from functools import cache
from itertools import product

import sympy as sp


coordinates = sp.symbols("t r x y")
t, r, x, y = coordinates
angles = (x, y)
half = sp.Rational(1, 2)


def field(name):
    return sp.Function(name)(*coordinates)


F, Vx, Vy, qxx, qxy, qyy = map(field, ("F", "Vx", "Vy", "qxx", "qxy", "qyy"))
fields = (F, Vx, Vy, qxx, qxy, qyy)
q = sp.Matrix([[qxx, qxy], [qxy, qyy]])
V = sp.Matrix([Vx, Vy])
area = sp.sqrt(q.det())

# A constant angular frame change and angular velocity set q=I, V=0 at
# one point. A substitution must never differentiate these point values.
# Turn *each derivative* into a separate indeterminate before substituting.
derivatives = {}
for f in fields:
    for i, a in enumerate(coordinates):
        derivatives[f.diff(a)] = sp.Symbol(f"{f.func}_{a}")
        for b in coordinates[i:]:
            derivatives[f.diff(a, b)] = sp.Symbol(f"{f.func}_{a}{b}")
point_values = {qxx: 1, qxy: 0, qyy: 1, Vx: 0, Vy: 0, F: sp.Symbol("F0")}


def at_point(expr):
    return sp.sympify(expr).xreplace(derivatives).xreplace(point_values)


def ricci_scalar(metric, inverse, coords):
    """Coordinate contraction of the Riemann tensor, using both metric jets."""
    indices = range(len(coords))
    inv = inverse.applyfunc(at_point)

    @cache
    def dg(i, j, k):
        return at_point(metric[i, j].diff(coords[k]))

    @cache
    def ddg(i, j, k, m):
        return at_point(metric[i, j].diff(coords[k], coords[m]))

    @cache
    def dinv(i, j, k):
        return -sum(inv[i, a]*dg(a, b, k)*inv[b, j] for a, b in product(indices, repeat=2))

    @cache
    def lowered(a, i, j):
        return half*(dg(a, j, i) + dg(a, i, j) - dg(i, j, a))

    @cache
    def gamma(a, i, j):
        return sum(inv[a, b]*lowered(b, i, j) for b in indices)

    def dgamma(a, i, j, k):
        return sum(dinv(a, b, k)*lowered(b, i, j)
                   + half*inv[a, b]*(ddg(b, j, i, k) + ddg(b, i, j, k) - ddg(i, j, b, k))
                   for b in indices)

    def ricci(i, j):
        return sum(dgamma(k, i, j, k) - dgamma(k, i, k, j)
                   + sum(gamma(k, i, j)*gamma(l, k, l) - gamma(l, i, k)*gamma(k, j, l)
                         for l in indices) for k in indices)

    return sum(inv[i, j]*ricci(i, j) for i, j in product(indices, repeat=2) if inv[i, j])


def spacetime_scalar():
    # Build g independently of the expansions, shears and boundary current.
    shift_cov = q*V
    g = sp.Matrix([[-F + V.dot(shift_cov), -1, shift_cov[0], shift_cov[1]],
                   [-1, 0, 0, 0],
                   [shift_cov[0], 0, qxx, qxy],
                   [shift_cov[1], 0, qxy, qyy]])
    inv = sp.zeros(4)
    inv[0, 1] = inv[1, 0] = -1
    inv[1, 1] = F
    inv[1, 2:4], inv[2:4, 1] = V.T, V
    inv[2:4, 2:4] = q.inv()
    assert (g*inv - sp.eye(4)).applyfunc(sp.cancel) == sp.zeros(4)
    return ricci_scalar(g, inv, coordinates)


def printed_density():
    # A is an area density. Its Lie derivative is the full angular divergence.
    transported_area = area.diff(t) - sum((area*V[i]).diff(a) for i, a in enumerate(angles))
    theta_t = at_point(transported_area / area)
    theta_r = at_point(area.diff(r) / area)
    lie_q = sp.Matrix(2, 2, lambda i, j: sum(
        V[k]*q[i, j].diff(a) + q[k, j]*V[k].diff(angles[i])
        + q[i, k]*V[k].diff(angles[j]) for k, a in enumerate(angles)))
    sigma_t = half*((q.diff(t) - lie_q).applyfunc(at_point) - theta_t*sp.eye(2))
    sigma_r = half*(q.diff(r).applyfunc(at_point) - theta_r*sp.eye(2))
    w = (-half*q*V.diff(r)).applyfunc(at_point)
    cut_scalar = ricci_scalar(q, q.inv(), angles)
    bulk = 2*(sigma_t*sigma_r).trace() - theta_t*theta_r + cut_scalar + 2*w.dot(w)
    delta_bulk = at_point(area.diff(r)*F.diff(r) + F*area.diff(r)**2/(2*area)) \
        - at_point(F)*(sigma_r*sigma_r).trace()
    current_t = 2*area.diff(r)
    current_r = 2*transported_area - area*F.diff(r) - 2*F*area.diff(r)
    current_angular = -2*area.diff(r)*V
    divergence = current_t.diff(t) + current_r.diff(r) + sum(
        current_angular[i].diff(a) for i, a in enumerate(angles))
    return bulk + delta_bulk + at_point(divergence)


if __name__ == "__main__":
    direct = sp.expand(spacetime_scalar())
    printed = sp.expand(printed_density())
    # Both -2 Lambda A contributions agree separately. A=1 at the point.
    assert direct != 0 and not direct.has(sp.Derivative)
    assert printed != 0 and not printed.has(sp.Derivative)
    residual = sp.expand(direct - printed)
    print(f"B.10–11 general affine two-jet residual: {residual}")
    assert residual == 0
    print(f"Matched expanded monomials: {len(sp.Add.make_args(direct))}")

    # Curved, shearing control with nonzero twist at t=r=0.
    a, b, omega = sp.symbols("a b omega")
    diagonal = sp.exp(2*(a*r + b*t))
    model = {qxx: diagonal, qxy: 0, qyy: 1/diagonal, Vx: omega*r, Vy: 0, F: point_values[F]}
    model_jet = {symbol: sp.diff(model[d.expr], *d.variables).subs({t: 0, r: 0})
                 for d, symbol in derivatives.items()}
    control = sp.expand(direct.xreplace(model_jet) - (4*a*b - 2*point_values[F]*a**2 + omega**2/2))
    print(f"Shear and twist curvature control: {control}")
    assert control == 0
