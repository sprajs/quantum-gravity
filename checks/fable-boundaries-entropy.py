"""Checks for audit/fable-boundaries-entropy.md.  Python 3, standard library only.

Part A  (A.14): exact rational test of which cap-edge conditions make the
        displayed two-form closed, and of the missing cap-edge term.
Part B  (5.66)-(5.69): the window identity, the dependence of the window
        trace on the window width, and the two readings of 106/45.
"""

from fractions import Fraction as Fr
from itertools import combinations
import math

# --------------------------------------------------------------------------
# Second-order jets in N field-space coordinates, exact rational arithmetic.
# --------------------------------------------------------------------------
N = 5                      # coordinates: lambda, r, c1, c2, c3   (rho_S^2 = r^2)


class Jet:
    """Value, gradient and (optionally) Hessian of a function on field space."""

    def __init__(self, v, g=None, h=None):
        self.v = Fr(v)
        self.g = list(g) if g is not None else [Fr(0)] * N
        self.h = [list(row) for row in h] if h is not None else None

    @staticmethod
    def lift(x):
        return x if isinstance(x, Jet) else Jet(x, None, [[Fr(0)] * N for _ in range(N)])

    def __add__(self, o):
        o = Jet.lift(o)
        h = None
        if self.h is not None and o.h is not None:
            h = [[self.h[i][j] + o.h[i][j] for j in range(N)] for i in range(N)]
        return Jet(self.v + o.v, [a + b for a, b in zip(self.g, o.g)], h)

    __radd__ = __add__

    def __neg__(self):
        h = None if self.h is None else [[-x for x in row] for row in self.h]
        return Jet(-self.v, [-a for a in self.g], h)

    def __sub__(self, o):
        return self + (-Jet.lift(o))

    def __rsub__(self, o):
        return Jet.lift(o) + (-self)

    def __mul__(self, o):
        o = Jet.lift(o)
        g = [self.v * b + o.v * a for a, b in zip(self.g, o.g)]
        h = None
        if self.h is not None and o.h is not None:
            h = [[self.v * o.h[i][j] + o.v * self.h[i][j]
                  + self.g[i] * o.g[j] + self.g[j] * o.g[i]
                  for j in range(N)] for i in range(N)]
        return Jet(self.v * o.v, g, h)

    __rmul__ = __mul__

    def inv(self):
        v = 1 / self.v
        g = [-a * v * v for a in self.g]
        h = None
        if self.h is not None:
            h = [[-self.h[i][j] * v * v + 2 * self.g[i] * self.g[j] * v ** 3
                  for j in range(N)] for i in range(N)]
        return Jet(v, g, h)

    def __truediv__(self, o):
        return self * Jet.lift(o).inv()

    def __rtruediv__(self, o):
        return Jet.lift(o) * self.inv()

    def __pow__(self, n):
        out = Jet.lift(1)
        for _ in range(n):
            out = out * self
        return out


def coord(i, value):
    g = [Fr(0)] * N
    g[i] = Fr(1)
    return Jet(value, g, [[Fr(0)] * N for _ in range(N)])


def comp(f, i):
    """Component i of the one-form df, as a first-order jet."""
    return Jet(f.g[i], f.h[i], None)


# Polynomials in v with Jet coefficients: list index = power of v.
def padd(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)]


def pscale(p, s):
    return [c * s for c in p]


def pmul(p, q):
    out = [Jet.lift(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = out[i + j] + a * b
    return out


def pdiff(p):
    return [c * k for k, c in enumerate(p)][1:] or [Jet.lift(0)]


def peval(p, x):
    out = Jet.lift(0)
    for c in reversed(p):
        out = out * x + c
    return out


def pint(p, lo, hi):
    out = Jet.lift(0)
    for k, c in enumerate(p):
        out = out + c * (hi ** (k + 1) - lo ** (k + 1)) / (k + 1)
    return out


V = [Jet.lift(0), Jet.lift(1)]          # the polynomial v


def wedge(a, b):
    return [[a[i] * b[j] - a[j] * b[i] for j in range(N)] for i in range(N)]


def fadd(*forms):
    return [[sum((f[i][j] for f in forms), Jet.lift(0)) for j in range(N)] for i in range(N)]


def fscale(f, s):
    return [[f[i][j] * s for j in range(N)] for i in range(N)]


def ext_d(w):
    """Largest |component| of the exterior derivative of a two-form."""
    worst = Fr(0)
    for i, j, k in combinations(range(N), 3):
        val = w[j][k].g[i] + w[k][i].g[j] + w[i][j].g[k]
        worst = max(worst, abs(val))
    return worst


def cap_edge_test(name, modes, b_of, point):
    """One null sheet, flat one-dimensional target chart, per unit 1/(16 pi G).

    Potential in the v = rho/rho_S parametrization on shell (A.30a):
        Theta = lam dR + R int_1^b v^2 z' (dz)_v dv
                - [ int_1^b (v^3/2) z'^2 dv + (b^2 - 1) ] dR ,     R = rho_S^2 .
    Displayed (A.14):
        W = dlam ^ dR - (1/2) dR ^ z'(1) X(1) + R int_1^b v^2 X' ^ X dv ,
        X = (dz)_v - (v z'/2R) dR      (variation at fixed area).
    Claimed completion:  d Theta = W + C ,
        C = (b/2) d(b^2 R) ^ z'(b) X(b) - d(b^2) ^ dR .
    """
    lam, r = coord(0, point[0]), coord(1, point[1])
    cs = [coord(2 + k, point[2 + k]) for k in range(3)]
    R = r * r
    b = b_of(r, cs)
    phis = [[Jet.lift(c) for c in m] for m in modes]
    z = [Jet.lift(0)]
    for c, phi in zip(cs, phis):
        z = padd(z, pscale(phi, c))
    zd = pdiff(z)

    dR = [comp(R, i) for i in range(N)]
    dlam = [comp(lam, i) for i in range(N)]
    dz = [[Jet.lift(0)], [Jet.lift(0)]] + phis          # (dz)_v, polynomial-valued

    # exact two-form from the potential
    F2 = pint(pscale(pmul(pmul(V, pmul(V, V)), pmul(zd, zd)), Fr(1, 2)), Jet.lift(1), b)
    theta = []
    for i in range(N):
        rad = R * pint(pmul(pmul(V, V), pmul(zd, dz[i])), Jet.lift(1), b)
        theta.append((lam - F2 - (b * b - 1)) * dR[i] + rad)
    omega = [[Jet(theta[j].g[i] - theta[i].g[j]) for j in range(N)] for i in range(N)]

    # displayed (A.14)
    vzd = pmul(V, zd)
    X = [padd(dz[i], pscale(vzd, -dR[i] / (2 * R))) for i in range(N)]
    Xd = [pdiff(x) for x in X]
    one = Jet.lift(1)
    corner = wedge(dR, [peval(zd, one) * peval(X[i], one) for i in range(N)])
    bulk = [[R * pint(pmul(pmul(V, V), padd(pmul(Xd[i], X[j]), pscale(pmul(Xd[j], X[i]), -1))),
                      one, b) for j in range(N)] for i in range(N)]
    W = fadd(wedge(dlam, dR), fscale(corner, Fr(-1, 2)), bulk)

    # claimed cap-edge completion
    dA = [comp(b * b * R, i) for i in range(N)]
    db2 = [comp(b * b, i) for i in range(N)]
    edge = wedge(dA, [peval(zd, b) * peval(X[i], b) for i in range(N)])
    C = fadd(fscale(edge, b / 2), fscale(wedge(db2, dR), -1))

    resid = max(abs(omega[i][j].v - W[i][j].v - C[i][j].v) for i in range(N) for j in range(N))
    cmax = max(abs(C[i][j].v) for i in range(N) for j in range(N))
    print(f"  {name:<46} |dTheta-W-C|={resid}  max|C|={float(cmax):.3e}"
          f"  max|dW|={float(ext_d(W)):.3e}  max|d(W+C)|={float(ext_d(fadd(W, C))):.3e}")
    return resid, cmax, ext_d(W), ext_d(fadd(W, C))


def part_a():
    print("Part A.  (A.14) on one sheet with a cap edge at v = b")
    eps = Fr(1, 3)
    mono = [[0, 1], [0, 0, 1], [0, 0, 0, 1]]                       # v, v^2, v^3
    dirichlet = [[-eps, 1], [0, -eps, 1], [0, 0, -eps, 1]]         # (v-eps) v^k
    pt = [Fr(2, 7), Fr(5, 3), Fr(3, 5), Fr(-4, 9), Fr(7, 11)]
    a = Fr(4, 7)
    out = {}
    out["F"] = cap_edge_test("fixed cap-edge area density, b = a/rho_S", mono,
                             lambda r, cs: a / r, pt)
    out["R"] = cap_edge_test("fixed ratio (3.18), b = eps", mono,
                             lambda r, cs: Jet.lift(eps), pt)
    out["D"] = cap_edge_test("fixed ratio, modes vanish at the cap edge", dirichlet,
                             lambda r, cs: Jet.lift(eps), pt)
    out["V"] = cap_edge_test("smooth vertex, b = 0", mono,
                             lambda r, cs: Jet.lift(0), pt)
    out["G"] = cap_edge_test("field-dependent cut, generic b(rho_S, z)", mono,
                             lambda r, cs: eps * (1 + cs[0] / 3) / (1 + r / 7), pt)
    assert all(v[0] == 0 for v in out.values())          # d Theta = W + C always
    assert all(v[3] == 0 for v in out.values())          # W + C is closed
    assert out["F"][1] == 0 and out["F"][2] == 0         # A.14 complete and closed
    assert out["D"][1] == 0 and out["D"][2] == 0
    assert out["V"][1] == 0 and out["V"][2] == 0
    assert out["R"][1] != 0 and out["R"][2] != 0         # A.14 neither complete nor closed
    print("  all assertions hold\n")


# --------------------------------------------------------------------------
def simpson(f, lo, hi, n):
    h = (hi - lo) / n
    s = f(lo) + f(hi)
    for k in range(1, n):
        s += (4 if k % 2 else 2) * f(lo + k * h)
    return s * h / 3


def part_b():
    print("Part B.  Window identity and bookkeeping of the logarithm")
    # (5.66a): int_0^inf f_b(s) ds_b / sqrt(4 pi s_b) = 1, with s_b = t^2.
    for s in (0.0, 0.3, 4.0, 60.0):
        def g(t, s=s):
            if t == 0:                       # limit of the integrand at s_b -> 0
                return 1 / math.sqrt(math.pi) if s == 0 else 0.0
            return math.exp(-(s - t * t) ** 2 / (4 * t * t)) / math.sqrt(math.pi)
        val = simpson(g, 0.0, math.sqrt(s) + 40.0, 200000)
        print(f"  s={s:5.1f}:  window integral = {val:.12f}")
        assert abs(val - 1) < 1e-9

    # Window trace for a weighted density  dmu = s^a ds  and width sigma^2 = 2 b^alpha.
    a = 167 / 90
    print("  exponent of T_b for dmu = s^(167/90) ds and sigma_s^2 = 2 s_b^alpha:")
    for alpha in (0.0, 1.0, 1.5):
        def logT(b):
            sig = math.sqrt(2 * b ** alpha)
            lo, hi = max(b - 12 * sig, 0.0), b + 12 * sig
            return math.log(simpson(lambda s: (s / b) ** a * math.exp(-(s - b) ** 2 / (2 * sig * sig)),
                                    lo, hi, 20000)) + a * math.log(b)
        slope = (logT(1e8) - logT(1e6)) / math.log(100.0)
        print(f"    alpha={alpha:3.1f}: slope = {slope:.5f}   a + alpha/2 = {a + alpha / 2:.5f}")
        assert abs(slope - (a + alpha / 2)) < 2e-3

    def chain(a_density):
        """a_density: exponent of the weighted density per unit area, e^{-s} dN/ds."""
        c_window = a_density + Fr(1, 2)          # exponent of T_b at sigma^2 = 2 s_b
        z_exp = a_density + 1                    # Z ~ s_*^{a+1}
        p = 2 * z_exp
        q = p / (1 + p)
        x2 = q / (2 - q)
        mean_ratio = (a_density + 1) / (a_density + 2)
        per_mass = a_density + Fr(1, 2)          # log(dN/dM) - s, coefficient of log s
        return c_window, z_exp, q, x2, mean_ratio, per_mass

    c = Fr(106, 45)
    print("  reading 1: 106/45 is the exponent of T_b (window of width sqrt(2 s_b))")
    r1 = chain(c - Fr(1, 2))
    print("    T_b, Z, q, x^2, <s>/s_*, fixed mass:", *r1)
    print("  reading 2: 106/45 is the exponent of the density per unit area")
    r2 = chain(c)
    print("    T_b, Z, q, x^2, <s>/s_*, fixed mass:", *r2)
    assert r1 == (Fr(106, 45), Fr(257, 90), Fr(257, 302), Fr(257, 347), Fr(257, 347), Fr(106, 45))
    assert r2 == (Fr(257, 90), Fr(151, 45), Fr(302, 347), Fr(151, 196), Fr(151, 196), Fr(257, 90))
    # relative spread of area in the clock ensemble of reading 1
    A = float(r1[1])
    print(f"    reading 1: std(s)/<s> = {math.sqrt(1 / (A * (A + 2))):.4f},"
          f"  Pr(s_*/4 < s < s_*/2) = {0.5 ** A - 0.25 ** A:.4f}")
    # mass width of the window: delta M = sqrt(2 s) hbar / (8 pi G M) = M_P / sqrt(8 pi)
    print(f"    window width in mass: {1 / math.sqrt(8 * math.pi):.5f} M_P, independent of s_b")
    print("  all assertions hold")


if __name__ == "__main__":
    part_a()
    part_b()
