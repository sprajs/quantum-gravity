"""The full Einstein surface charge at the moving spherical focal cut (G = 1)."""

from math import cos, cosh, exp, pi, sin, sinh, tan, tanh

from joint_focal import C, D, EPS, L, inverse_radius, pulse, radius, radius_rate


def pulse_rate(u, width):
    x = (u - C) / width
    if abs(x) >= 1:
        return 0.0
    d = 1 - x*x
    return exp(1 - 1/d) * (-2/d**2 - 8*x*x/d**3 + 4*x*x/d**4) / width**2


def area_above(u):
    """Angular-plane area K(u) inside the ellipse b(k) > u and its negative derivative."""
    s = inverse_radius(radius(u)/EPS)
    v = L - s
    v_rate = radius_rate(v) if v > 1e-12 else 1.0
    factor = 2*pi*D / (radius(L)*radius(s))
    ds = radius_rate(u)/(EPS*radius_rate(s))
    return factor*radius(v), factor*ds*(v_rate + radius(v)*radius_rate(s)/radius(s))


def integrate(width, steps=1024):
    # w = delta R/R; gamma integrates (R^2 H')' times the pulse.
    def rhs(u, state):
        gamma, w, _, _ = state
        wave = pulse(u, width)
        a1, a2 = cosh(u), cos(u)
        return (2*a1*a2*wave, -(tanh(u)+tan(u))*wave/2 + gamma/(2*a1*a2),
                (-2*w-wave)/a1**2, (-2*w+wave)/a2**2)

    def advance(state, rates, step):
        return tuple(x + step*y for x, y in zip(state, rates))

    dt = width/steps
    state = (0., 0., 0., 0.)
    integrals = [0., 0., 0.]
    cap_angular = 0.
    for j in range(steps+1):
        u = C - width*(1 - j/steps)
        slopes = rhs(u, state)
        _, w, di1, di2 = state
        _, dw, di1_rate, di2_rate = slopes
        # r_i = delta q_ii/q_ii for q_ii = (A_i I_i)^2 in optical coordinates.
        wave, wave_rate = pulse(u, width), pulse_rate(u, width)
        i1, i2 = tanh(u), tan(u)
        r1 = 2*(w+di1/i1) + wave
        r2 = 2*(w+di2/i2) - wave
        smooth1 = 2*(dw+di1_rate/i1-di1/(cosh(u)*i1)**2)
        smooth2 = 2*(dw+di2_rate/i2-di2/(cos(u)*i2)**2)
        p1, p2 = 1/tanh(u), 1/tan(u)
        theta = p1*r1 + p2*r2 + smooth1 + smooth2
        trace = 4*w + 2*(di1/i1 + di2/i2)
        area, density = area_above(u)
        # Independent pullback of delta Q_xi - i_xi theta for xi^U=f, xi^i=d_i k_i.
        # Each output is the integrated multiplier of f, d1 or d2, respectively.
        terms = (density*theta, area*(theta-smooth1-wave_rate-p1*trace),
                 area*(theta-smooth2+wave_rate-p2*trace))
        simpson_weight = 1 if j in (0, steps) else 4 if j % 2 else 2
        measure = simpson_weight*dt*radius(u)**2/(3*16*pi)
        # Independent bulk Einstein current with X_11/q_1 = 1, X_22/q_2 = -1.
        # eps_wU12 is negative and this cap has U <= b(k).
        cap_angular -= measure*area*(trace*(p1-p2)+smooth1-smooth2+2*wave_rate)/2
        for i, term in enumerate(terms):
            integrals[i] += measure*term
        if j < steps:
            mid = u + dt/2
            half1 = rhs(mid, advance(state, slopes, dt/2))
            half2 = rhs(mid, advance(state, half1, dt/2))
            end = rhs(u+dt, advance(state, half2, dt))
            state = tuple(x + dt*(a+2*b+2*c+d)/6
                          for x, a, b, c, d in zip(state, slopes, half1, half2, end))
    assert abs(cap_angular - (integrals[1]-integrals[2])/2) < 1e-12
    return integrals


if __name__ == "__main__":
    p1, p2 = 1/tanh(C), 1/tan(C)
    e_factor = EPS*radius_rate(L)/(2*D*radius_rate(C))
    e1, e2 = e_factor*sinh(L)**2, e_factor*sin(L)**2
    n1, n2 = -2*e1/sinh(C)**2, -2*e2/sin(C)**2
    m = pi/(e1*e2)**0.5
    scale = m*radius(C)**2/(16*pi)
    assert abs(area_above(C)[1] - m) < 1e-12
    print(f"Null shear differences at the axis: {p1-p2:.6f}, {n1-n2:.6f}")
    print(f"Limits for unit angular strain and unit outgoing shift: {-scale:.6f}, "
          f"{-scale*(p1-p2):.6f}")
    print(f"Parallel translation, angular and normal parts: {scale*(n1-n2):.6f}, "
          f"{-scale*(n1-n2):.6f}")
    errors = []
    for width in (1/40, 1/80, 1/160, 1/320):
        outgoing, axis1, axis2 = integrate(width)
        angular = (axis1-axis2)/2
        matched = outgoing - p1*axis1 - p2*axis2
        print(f"width {width:.6f}  angular {angular:.6f}  outgoing {outgoing:.6f}  "
              f"matched {matched:.6f}")
        errors.append((abs(angular+scale), abs(outgoing+scale*(p1-p2)), abs(matched)))
    assert all(all(y < 0.60*x for x, y in zip(older, newer))
               for older, newer in zip(errors, errors[1:]))
    assert max(errors[-1]) < 0.002
    print("Cap volume and angular surface charge agree within 1e-12.")
