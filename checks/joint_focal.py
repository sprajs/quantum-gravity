"""A compensated plane wave and the angularly averaged clock on a true diamond."""

from math import cos, cosh, exp, log, pi, sin, sinh, sqrt, tan, tanh

L, D, EPS = 1.0, 1.0, 0.5


def radius(u):
    return sqrt(sinh(u) * sin(u))


def shape_rate(u):
    return 1 / tanh(u) - 1 / tan(u)


def radius_rate(u):
    return radius(u) * (1 / tanh(u) + 1 / tan(u)) / 2


def inverse_radius(value):
    lo, hi = 0.0, L
    for _ in range(52):
        mid = (lo + hi) / 2
        if radius(mid) < value:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


C = inverse_radius(EPS * radius(L))


def pulse(u, width):
    x = (u - C) / width
    if abs(x) >= 1:
        return 0.0
    d = 1 - x**2
    return -2 * x * exp(1 - 1/d) / (width * d**2)


def angular_denominator():
    """Do the azimuthal integral analytically, then the remaining integral in U."""
    def integrand(x):
        if x == 0 or x == 1:
            return 0.0
        s = L*x**4
        m1 = sinh(s)*sinh(L)/sinh(L-s)
        m2 = sin(s)*sin(L)/sin(L-s)
        ratio = (sqrt(m1+D) + sqrt(m2+D)) / (sqrt(m1) + sqrt(m2))
        return 4*L*x**3 * radius_rate(s) * log(ratio)

    panels = 1024
    odd = sum(integrand(i/panels) for i in range(1, panels, 2))
    even = sum(integrand(i/panels) for i in range(2, panels, 2))
    return 4*pi*sqrt(2)*(4*odd + 2*even)/(3*panels)


def run(width):
    # Integrate against fixed tip angles, using the *background* waist coordinate
    # s and azimuth for quadrature. s itself varies for each fixed direction.
    splits = [0, C - width, C + width, inverse_radius(radius(C - width)/EPS), L]
    nodes = (-0.861136311594053, -0.339981043584856,
             0.339981043584856, 0.861136311594053)
    weights = (0.347854845137454, 0.652145154862546,
               0.652145154862546, 0.347854845137454)
    quadrature = []
    for lo, hi in zip(splits, splits[1:]):
        step = (hi - lo) / 20
        for j in range(20):
            for node, weight in zip(nodes, weights):
                s = lo + (j + (1 + node)/2) * step
                quadrature.append((s, inverse_radius(EPS * radius(s)), weight * step/2))

    # First variations of R and the two optical integrals. Set w = delta R/R.
    # The auxiliary g integrates (R² H')' f so no derivative of the pulse is needed.
    def rhs(u, state):
        g, w, _, _ = state
        a, b = cosh(u), cos(u)
        f = pulse(u, width)
        return (2*a*b*f, -(tanh(u) + tan(u))*f/2 + g/(2*a*b),
                (-2*w - f)/a**2, (-2*w + f)/b**2)

    def add(state, rates, factor):
        return tuple(v + factor*r for v, r in zip(state, rates))

    grid = {s for s, b, _ in quadrature} | {b for s, b, _ in quadrature}
    grid.update(C - width + j*width/64 for j in range(129))
    grid.update((0.0, L))
    history = {}
    state, last = (0., 0., 0., 0.), 0.
    for u in sorted(grid):
        du = u - last
        k1 = rhs(last, state)
        k2 = rhs(last + du/2, add(state, k1, du/2))
        k3 = rhs(last + du/2, add(state, k2, du/2))
        k4 = rhs(u, add(state, k3, du))
        state = tuple(v + du*(x + 2*y + 2*z + w)/6
                      for v, x, y, z, w in zip(state, k1, k2, k3, k4))
        history[u] = state
        last = u

    def optics(u):
        g, w, di, dj = history[u]
        i, j = tanh(u), tan(u)
        a, b = cosh(u), cos(u)
        f = pulse(u, width)
        frac = w + (di/i + dj/j)/2
        dfrac = (-(tanh(u) + tan(u))*f/2 + g/(2*a*b)
                 + ((-2*w - f - di/i)/(a*a*i) + (-2*w + f - dj/j)/(b*b*j))/2)
        return radius(u)*frac, radius_rate(u)*frac + radius(u)*dfrac

    total_i, total_j = tanh(L), tan(L)
    di_end, dj_end = history[L][2:]
    numerator = denominator = dn = dd = 0.
    nang = 24
    for s, b, ws in quadrature:
        i, j = tanh(s), tan(s)
        ni, nj = total_i/(total_i-i), total_j/(total_j-j)
        di, dj = history[s][2:]
        df_s, _ = optics(s)
        df_b, dfp_b = optics(b)
        for m in range(nang):
            phi = (m + 0.5)*2*pi/nang
            x, y = cos(phi)**2, sin(phi)**2
            g = x*i*ni + y*j*nj
            gp = x*(ni/cosh(s))**2 + y*(nj/cos(s))**2
            dg = (x*(ni**2*di - (ni-1)**2*di_end)
                  + y*(nj**2*dj - (nj-1)**2*dj_end))
            ds = -dg/gp
            dfs = df_s + radius_rate(s)*ds
            db = (EPS*dfs - df_b)/radius_rate(b)
            dfpb = dfp_b - radius(b)*shape_rate(b)**2*db/4
            weight = ws*(2*pi/nang)*D*gp/g**2
            aff = sqrt(2)/(1 + D/g)
            length = s-b
            n = radius(s)*radius_rate(b)*length
            numerator += weight*n
            denominator += weight*aff*radius(s)
            dn += weight*(dfs*radius_rate(b)*length + radius(s)
                          * (dfpb*length + radius_rate(b)*(ds-db)))
            dd += weight*aff*dfs

    # The determinant of the quadratic-form matrix at the maximum of U|C.
    determinant_root = (EPS * radius_rate(L)/radius_rate(C)
                        * sinh(L)*sin(L)/(2*D))
    exact_angle = angular_denominator()
    assert abs(denominator - exact_angle) < 1e-7
    prediction = (-pi*radius(L)*(L-C)*radius(C)*shape_rate(C)
                  / (2*determinant_root*exact_angle))
    return (dn - numerator*dd/denominator)/denominator, prediction


if __name__ == "__main__":
    errors = []
    for width in (0.025, 0.0125, 0.00625, 0.003125):
        derivative, limit = run(width)
        errors.append(abs(derivative - limit))
        print(f"width {width:.6f}: clock variation {derivative:.6f}, limit {limit:.6f}")
    assert all(b < 0.55*a for a, b in zip(errors, errors[1:]))
    assert errors[-1] < 0.003
