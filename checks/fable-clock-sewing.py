"""Checks for audit/fable-clock-sewing.md. Standard library only.

1. One-pair thresholds for the clock form domain under three orderings.
2. Zero-point floor and Gaussian domain test for a mode-truncated null generator.
"""

import math


# ---------------------------------------------------------------- linear algebra

def matmul(a, b):
    cols = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in cols] for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def identity(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def jacobi(a, sweeps=60):
    """Eigenvalues and eigenvectors (columns) of a real symmetric matrix."""
    n = len(a)
    a = [list(row) for row in a]
    v = identity(n)
    for _ in range(sweeps):
        off = sum(a[i][j] ** 2 for i in range(n) for j in range(i + 1, n))
        if off < 1e-26:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(a[p][q]) < 1e-300:
                    continue
                theta = (a[q][q] - a[p][p]) / (2 * a[p][q])
                t = math.copysign(1.0, theta) / (abs(theta) + math.hypot(theta, 1.0))
                c = 1 / math.hypot(t, 1.0)
                s = t * c
                for k in range(n):
                    akp, akq = a[k][p], a[k][q]
                    a[k][p], a[k][q] = c * akp - s * akq, s * akp + c * akq
                for k in range(n):
                    apk, aqk = a[p][k], a[q][k]
                    a[p][k], a[q][k] = c * apk - s * aqk, s * apk + c * aqk
                for k in range(n):
                    vkp, vkq = v[k][p], v[k][q]
                    v[k][p], v[k][q] = c * vkp - s * vkq, s * vkp + c * vkq
    return [a[i][i] for i in range(n)], v


def symplectic_j(pairs):
    j = [[0.0] * (2 * pairs) for _ in range(2 * pairs)]
    for m in range(pairs):
        j[2 * m][2 * m + 1], j[2 * m + 1][2 * m] = 1.0, -1.0
    return j


def spectral_data(g):
    """Return (R, nu^2 list, eigenvectors) with R = g^{1/2} and K = R J R.

    K is real antisymmetric and K^T K has the squared symplectic eigenvalues
    of g, each twice, for commutators [q, p] = i.
    """
    n = len(g)
    j = symplectic_j(n // 2)
    values, vectors = jacobi(g)
    root = matmul(matmul(vectors, [[math.sqrt(max(values[i], 0.0)) if i == k else 0.0
                                    for k in range(n)] for i in range(n)]),
                  transpose(vectors))
    k = matmul(matmul(root, j), root)
    squares, modes = jacobi(matmul(transpose(k), k))
    return root, [max(x, 0.0) for x in squares], modes


def zero_point(g):
    """inf spec of (1/2) xi^T g xi: half the sum of the symplectic eigenvalues."""
    _, squares, _ = spectral_data(g)
    return 0.25 * sum(math.sqrt(x) for x in squares)


def symbol_matrix(g):
    """M with Weyl symbol of exp[(1/2) xi^T g xi] proportional to exp(xi^T M xi).

    M = J^{-1} tan(J g / 2). Since tan(x/2) = x k(x) with k even, and
    f(AB) = A k(BA) B for A = J R, B = R, this equals R phi(K^T K) R with
    phi(nu^2) = tanh(nu/2)/nu, which is real, symmetric and stable.
    """
    n = len(g)
    root, squares, modes = spectral_data(g)
    phi = []
    for x in squares:
        nu = math.sqrt(x)
        phi.append(0.5 if nu < 1e-8 else math.tanh(nu / 2) / nu)
    middle = matmul(matmul(modes, [[phi[i] if i == k else 0.0 for k in range(n)]
                                   for i in range(n)]), transpose(modes))
    return matmul(matmul(root, middle), root)


def vacuum_margin(g):
    """Largest eigenvalue of M. <0|exp(Xi)|0> is finite iff it is below one."""
    values, _ = jacobi(symbol_matrix(g))
    return max(values)


# ------------------------------------------------------- one-pair thresholds

def one_pair():
    lo, hi = 1.0, 1.5
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if mid * math.tanh(mid) < 1 else (lo, mid)
    print(f"nested threshold: root of t*tanh(t)=1 is t = {lo:.9f}")

    # Symbol check on a pair: exp[c(Q^2+P^2)] in the vacuum equals exp(c*hbar).
    for coupling in (0.3, 1.0, 2.5):
        g = [[2 * coupling, 0.0], [0.0, 2 * coupling]]
        m = symbol_matrix(g)
        assert abs(m[0][0] - math.tanh(coupling)) < 1e-9 and abs(m[0][1]) < 1e-9
        assert abs(zero_point(g) - coupling) < 1e-9
        # <0|e^{Xi}|0> = [det cos(Jg/2)]^{-1/2} [det(1 - M)]^{-1/2} = e^{coupling}
        value = 1 / (math.cosh(coupling) * (1 - math.tanh(coupling)))
        assert abs(value - math.exp(coupling)) < 1e-9
    # Squeezed pair: Xi = (a q^2 + b p^2)/2 has nu = sqrt(ab).
    m = symbol_matrix([[3.0, 0.0], [0.0, 0.5]])
    nu = math.sqrt(1.5)
    assert abs(m[0][0] - 3.0 * math.tanh(nu / 2) / nu) < 1e-9
    assert abs(m[1][1] - 0.5 * math.tanh(nu / 2) / nu) < 1e-9
    # exp(c Q^2): nilpotent J g, so M = g/2 exactly.
    m = symbol_matrix([[1.4, 0.0], [0.0, 0.0]])
    assert abs(m[0][0] - 0.7) < 1e-12 and abs(m[1][1]) < 1e-12

    # Gaussians exp(-beta x^2/(2 hbar)) in each form domain, t = c*hbar.
    print(" t=c*hbar   unnested {cX^2,cP^2}   nested {cX^2,c(X^2+P^2)}   "
          "v-ordered e^{cP^2/2}e^{cX^2/2}")
    for t in (0.5, 0.9, 1.0, 1.1, 1.19, 1.21, 2.0, 5.0):
        unnested = (t, 1 / t)
        nested = (max(t, math.tanh(t)), 1 / math.tanh(t))
        ordered = (t, t + 1 / t)
        cells = []
        for low, high in (unnested, nested, ordered):
            cells.append(f"({low:.4f},{high:.4f})" if low < high else "empty")
        print(f"  {t:5.2f}    {cells[0]:>18}   {cells[1]:>24}   {cells[2]:>22}")

    # Independent check of the nested window: number-basis tail of a squeezed
    # vacuum, |c_{2n}|^2 ~ r^{2n} with r = |1-beta|/(1+beta); the weight e^{2tn}
    # per level sums iff e^{2t} r < 1, i.e. tanh(t) < beta < coth(t).
    t = 1.1
    for beta in (1.20, 1.26):
        ratio = abs(1 - beta) / (1 + beta)
        inside = math.exp(2 * t) * ratio < 1
        assert inside == (math.tanh(t) < beta < 1 / math.tanh(t))


# ------------------------------------------- mode-truncated null generator

def generator_matrix(pairs, epsilon, upper, hbar_eff, panels=6000):
    """g with Xi(upper) = (1/4) int_eps^upper (x' - x/t)^2 dt/t = (1/2) xi^T g xi.

    x = t z on one generator, [x(t), x'(t')] = i hbar_eff delta(t - t'),
    x = sum_m sqrt(hbar_eff/(pi m)) [q_m cos(m th) + p_m sin(m th)],
    th = 2 pi (t - eps)/(1 - eps), [q_m, p_m] = i.
    """
    size = 2 * pairs
    g = [[0.0] * size for _ in range(size)]
    k = 2 * math.pi / (1 - epsilon)
    step = (upper - epsilon) / panels
    for index in range(panels + 1):
        t = epsilon + index * step
        weight = (1 if index in (0, panels) else 4 if index % 2 else 2) * step / 3
        theta = k * (t - epsilon)
        w = []
        for m in range(1, pairs + 1):
            amp = math.sqrt(hbar_eff / (math.pi * m))
            cos, sin = math.cos(m * theta), math.sin(m * theta)
            w.append(amp * (-m * k * sin - cos / t))
            w.append(amp * (m * k * cos - sin / t))
        scale = 0.5 * weight / t
        for a in range(size):
            wa = scale * w[a]
            row = g[a]
            for b in range(size):
                row[b] += wa * w[b]
    return g


def generator():
    epsilon = 0.2
    print(f"\nnull generator, epsilon = {epsilon}; hbar_eff = 2*pi*N_ang/s")
    leading = math.pi * math.log(1 / epsilon) / (4 * (1 - epsilon) ** 2)
    print(f"local estimate E0(1)/(hbar_eff n^2) = {leading:.4f}")
    print("  n   E0(1)/(hbar_eff n^2)   <Xi(1)>_vac/(hbar_eff n^2)   "
          "critical hbar_eff   hbar_eff*n")
    cuts = [epsilon + (1 - epsilon) * i / 8 for i in range(1, 9)]
    for pairs in (2, 4, 8):
        family = [generator_matrix(pairs, epsilon, v, 1.0, panels=3000) for v in cuts]
        g = family[-1]
        e0 = zero_point(g)
        vac = 0.25 * sum(g[i][i] for i in range(2 * pairs))
        lo, hi = 0.0, 4.0
        for _ in range(26):
            mid = 0.5 * (lo + hi)
            worst = max(vacuum_margin([[mid * x for x in row] for row in member])
                        for member in family)
            lo, hi = (mid, hi) if worst < 1 else (lo, mid)
        print(f" {pairs:2d}        {e0 / pairs ** 2:.4f}                 "
              f"{vac / pairs ** 2:.4f}                {lo:.4f}        {lo * pairs:.4f}")

    # Floor on the clock: u >= b * int_eps^1 exp(E0(v)) dv, against (1-eps) b.
    pairs = 8
    grid = [epsilon + (1 - epsilon) * i / 16 for i in range(17)]
    unit = [0.0] + [zero_point(generator_matrix(pairs, epsilon, v, 1.0, panels=3000))
                    for v in grid[1:]]
    assert all(b >= a - 1e-9 for a, b in zip(unit, unit[1:]))
    print(f"\nfloor ratio  int exp(E0(v)) dv / (1-eps)  at n = {pairs}")
    for hbar_eff in (0.01, 0.03, 0.1, 0.3):
        values = [math.exp(hbar_eff * e) for e in unit]
        h = (1 - epsilon) / 16
        simpson = h / 3 * sum((1 if i in (0, 16) else 4 if i % 2 else 2) * value
                              for i, value in enumerate(values))
        print(f"  hbar_eff = {hbar_eff:5.2f}   E0(1) = {hbar_eff * unit[-1]:7.3f}   "
              f"ratio = {simpson / (1 - epsilon):.4g}")


if __name__ == "__main__":
    one_pair()
    generator()
