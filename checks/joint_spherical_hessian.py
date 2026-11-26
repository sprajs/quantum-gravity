"""Spherical cap-clock Hessian for two linearized vacuum waves. Standard library."""
from math import comb, factorial, isclose

# Affine units L=1. S=diag(-1/2,-1/2,1) has mean |Pi_TT(n) S|^2=3/5.
CAP = 1 / 3
SCREEN_MEAN = 3 / 5


def falling(n, k):
    return factorial(n) // factorial(n - k) if 0 <= k <= n else 0


def profile(x, order):
    """Derivative of x^4 (1-x)^12 (1+x)^12 / 24 inside the unit interval."""
    if abs(x) >= 1:
        return 0.0
    result = 0.0
    for i in range(min(4, order) + 1):
        for j in range(order - i + 1):
            k = order - i - j
            factor = comb(order, i) * comb(order - i, j) * (-1) ** j
            result += (factor * falling(4, i) * falling(12, j) * falling(12, k)
                       * x ** (4 - i) * (1 - x) ** (12 - j) * (1 + x) ** (12 - k))
    return result / 24


def optical_mode(s, jets):
    """Cut strain and its affine derivative, from the regular-vertex Jacobi solution."""
    _, _, f2, f3, f4, f5, _ = jets
    strain = f4 / s - 2 * f3 / s**2 + f2 / s**3
    slope = 2 * f5 / s - 5 * f4 / s**2 + 6 * f3 / s**3 - 3 * f2 / s**4
    return strain, slope


def tidal(s, jets):
    """Screen-projected linearized Riemann tensor in the J''=tidal*J convention."""
    _, _, f2, f3, f4, f5, f6 = jets
    return 2*f6/s - 4*f5/s**2 + 6*f4/s**3 - 6*f3/s**4 + 3*f2/s**5


def shell(s, width):
    x = 2 * (s - CAP) / width
    return [CAP * width ** (4 - j) * profile(x, j) for j in range(7)]


def reference(s):
    # A smooth compact cutoff can be taken equal to one on the entire test support.
    x = 2 * (s - CAP)
    return [CAP * falling(5, j) * x ** (5 - j) / 240 if j <= 5 else 0 for j in range(7)]


def simpson(fn, lo, hi, pieces=400):
    step = (hi - lo) / pieces
    odd = sum(fn(lo + k * step) for k in range(1, pieces, 2))
    even = sum(fn(lo + k * step) for k in range(2, pieces, 2))
    return step * (fn(lo) + fn(hi) + 4 * odd + 2 * even) / 3


def check():
    # Unit vector n has cos(theta)=z; the specified axisymmetric screen tensor
    # has norm squared 9(1-z^2)^2/8.
    assert isclose(simpson(lambda z: 9*(1-z*z)**2/8, 0, 1), SCREEN_MEAN, abs_tol=1e-10)
    assert optical_mode(CAP, reference(CAP)) == (0, 1)
    errors = []
    limit = -CAP * (1 - CAP) * SCREEN_MEAN / 4
    assert isclose(limit, -1/30)
    for width in (1/8, 1/16, 1/32, 1/64, 1/128):
        def integrand(s):
            slope = optical_mode(s, shell(s, width))[1]
            return SCREEN_MEAN / 4 * s * (1-s) * slope * optical_mode(s, reference(s))[1]

        ans = simpson(integrand, CAP, CAP + width/2, pieces=1200)
        rim = optical_mode(CAP, shell(CAP, width))[0]
        assert isclose(rim, 1)
        # Solve the regular Jacobi equation directly by quadrature up to the rim.
        from_curvature = 2/CAP * simpson(
            lambda s: (CAP - s) * s * tidal(s, shell(s, width)),
            CAP - width/2, CAP, pieces=1000)
        assert isclose(from_curvature, rim, abs_tol=3e-7)
        errors.append(abs(ans - limit))
        print(f"width={width:.7f}  spherical Hessian={ans:.10f}  rim strain={rim:.6f}")
    assert errors[0] > errors[1] > errors[2]
    assert max(errors[-2:]) < 1e-8
    print(f"sharp analytic limit={limit:.10f}  (-1/30)")


if __name__ == "__main__":
    check()
