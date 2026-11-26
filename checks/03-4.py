# /// script
# requires-python = ">=3.10"
# dependencies = ["sympy==1.14.0"]
# ///
"""Exact flat-metric checks of Appendix B. Run with Python 3 and SymPy."""

import sympy as sp


t, v, x, y = sp.symbols("t v x y", real=True)
angular = (x, y)
a = sp.Function("a")(t, x, y)
half = sp.Rational(1, 2)


def report(name, residual):
    simplified = sp.factor(residual)
    print(f"{name}: {simplified}")
    if simplified != 0:
        raise AssertionError(name)


def check_metric(affine):
    # Start with -dt²-2dt dR+R²dx²+dy² in flat cylindrical spacetime.
    # The affine substitution sets R=v+a. The area gauge sets R=a*v².
    area = v + a if affine else a * v**2
    lapse = area.diff(v)
    metric = sp.diag(area**2, 1)
    inverse = sp.diag(area**-2, 1)

    def gradient(field):
        return sp.Matrix([field.diff(z) for z in angular])

    def trace(tensor):
        return sp.trace(inverse * tensor)

    def tracefree(tensor):
        return tensor - half * trace(tensor) * metric

    def contract(left, right):
        return sp.trace(inverse * left * inverse * right)

    def dot(left, right):
        return (left.T * inverse * right)[0]

    def divergence(vector):
        return sum((area * vector[i]).diff(angular[i]) for i in range(2)) / area

    def christoffel(k, i, j):
        return half * sum(
            inverse[k, h] * (metric[h, i].diff(angular[j])
                             + metric[h, j].diff(angular[i])
                             - metric[i, j].diff(angular[h]))
            for h in range(2)
        )

    def angular_derivative(covector, i, j):
        return covector[j].diff(angular[i]) - sum(
            christoffel(k, i, j) * covector[k] for k in range(2)
        )

    def tensor_divergence(tensor, j):
        mixed = inverse * tensor
        return sum(
            mixed[i, j].diff(angular[i])
            + sum(christoffel(i, i, k) * mixed[k, j]
                  - christoffel(k, i, j) * mixed[i, k] for k in range(2))
            for i in range(2)
        )

    shift = -inverse * gradient(area)
    F = 1 + 2 * area.diff(t) + (shift.T * metric * shift)[0]
    f = -sp.log(lapse)
    shift_metric = sp.Matrix(2, 2, lambda i, j: sum(
        shift[k] * metric[i, j].diff(angular[k])
        + metric[i, k] * shift[k].diff(angular[j])
        + metric[k, j] * shift[k].diff(angular[i]) for k in range(2)
    ))
    K = half * metric.diff(v)
    theta, shear = trace(K), tracefree(K)
    transverse = half * (metric.diff(t) - shift_metric) - half * F * K / lapse
    vartheta, eta = trace(transverse), tracefree(transverse)
    w = -half * metric * shift.diff(v) / lapse
    varpi = w - half * gradient(f)
    mu = f.diff(t) - (shift.T * gradient(f))[0] + half * F.diff(v) / lapse
    # Intrinsic scalar curvature of area² dx² + dy².
    curvature = -2 * area.diff(y, 2) / area

    if affine:
        theta_t = area.diff(t) / area - divergence(shift)
        shear_t = half * (metric.diff(t) - shift_metric - theta_t * metric)
        L0 = area * (2*contract(shear_t, shear) - theta_t*theta + curvature + 2*dot(w, w))
        delta_L0 = area.diff(v) * F.diff(v) + F * (
            half * area.diff(v)**2 / area - area * contract(shear, shear)
        )
        Lt = 2 * area.diff(v)
        Lr = 2 * area.diff(t) - 2 * area * divergence(shift) - area * F.diff(v) - 2 * F * area.diff(v)
        La = -2 * area.diff(v) * shift
        div_L = Lt.diff(t) + Lr.diff(v) + sum(La[i].diff(angular[i]) for i in range(2))
        report("B.10–11 bulk Ricci density", L0 + delta_L0 + div_L)
        return

    report("B.3", f.diff(v) + contract(shear, shear) / theta)
    momentum = -2 * area * w
    for i, z in enumerate(angular):
        report(f"B.4a {z}", momentum[i].diff(v) / area - 2 * tensor_divergence(shear, i)
               - f.diff(v, z) + theta.diff(z) + theta * f.diff(z))
    report("B.5a", (area * vartheta).diff(v)
           + lapse * area * (half * curvature - divergence(inverse * varpi) - dot(varpi, varpi)))
    grad_varpi = sp.Matrix(2, 2, lambda i, j: half * (angular_derivative(varpi, i, j)
                                                       + angular_derivative(varpi, j, i)))
    shear_residual = tracefree(eta.diff(v)) - half * theta * eta + half * vartheta * shear - lapse * tracefree(
        grad_varpi + varpi * varpi.T
    )
    for i, j in [(0, 0), (0, 1), (1, 1)]:
        report(f"B.5b {angular[i]}{angular[j]}", shear_residual[i, j])
    report("B.5c", mu.diff(v) - contract(shear, eta) + half * theta * vartheta - lapse * (
        -half * curvature - dot(gradient(f), gradient(f)) / 4 + 3 * dot(w, w) + dot(w, gradient(f))
    ))


if __name__ == "__main__":
    check_metric(affine=False)
    check_metric(affine=True)
