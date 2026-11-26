"""Test the spherical clock adjoint, emitter calibration and compact wave controls."""

from math import cos, cosh, exp, log, pi, sin, sinh, sqrt, tan, tanh

import joint_focal

GAUSS = ((-0.861136311594053, 0.347854845137454),
         (-0.339981043584856, 0.652145154862546),
         (0.339981043584856, 0.652145154862546),
         (0.861136311594053, 0.347854845137454))


def integral(fn, lo, hi, panels=3):
    width = (hi-lo)/panels
    return sum(weight*width/2 * fn(lo+(i+(1+node)/2)*width)
               for i in range(panels) for node, weight in GAUSS)


def root(fn, hi):
    lo = 0.
    for _ in range(50):
        mid = (lo+hi)/2
        if fn(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def integrals(u, k):
    return tanh(k*u)/k, tan(k*u)/k


def axes(s, frequency):
    return (sinh(frequency*s)/frequency, sin(frequency*s)/frequency)


def slopes(s, frequency):
    return cosh(frequency*s), cos(frequency*s)


def radius(s, frequency):
    j1, j2 = axes(s, frequency)
    return sqrt(j1*j2)


def optics(s, frequency):
    j = axes(s, frequency)
    jp = slopes(s, frequency)
    d = sqrt(j[0]*j[1])
    rates = [p/i for p, i in zip(jp, j)]
    expansion = sum(rates)/2
    n = [d/(2*i) for i in j]
    np = [v*(expansion-rate) for v, rate in zip(n, rates)]
    return d, d*expansion, -d*(rates[0]-rates[1])**2/4, n, np


def ray(mu, phi, kappa, boost):
    end_u, end_v = exp(boost), exp(-boost)
    a = exp(boost)*(1+mu)/sqrt(2)
    beta = tuple(sqrt(1-mu**2)*f(phi)/a for f in (cos, sin))
    total = integrals(end_u, kappa)

    def waist(u):
        local = integrals(u, kappa)
        return sum(b*b*i*t/(t-i) for b, i, t in zip(beta, local, total))-2*end_v

    s = root(waist, end_u)/a
    frequency = kappa*a
    d = radius(s, frequency)
    c = root(lambda v: radius(v, frequency)-d/2, s)
    return a, beta, s, c, d, optics(c, frequency)[1]*(s-c)


DIRECTIONS = [(mu, (i+0.3)*2*pi/8)
              for mu in (-0.8, -0.4, 0., 0.4, 0.8) for i in range(8)]


def clock(kappa, boost):
    rays = [ray(mu, phi, kappa, boost) for mu, phi in DIRECTIONS]
    return sum(d*u for _, _, _, _, d, u in rays)/sum(r[4] for r in rays)


def waist_derivative(a, beta, s):
    # The return connector is affine on [0,1], runs from q to x(S), and
    # has covariant transverse momenta p_i and constant negative U-velocity.
    u = a*s
    du = u-1
    local, total = integrals(u, 1), integrals(1, 1)
    inverse_scale = (1/cosh(u)**2, 1/cos(u)**2)
    p = [du*b*i/(i-t) for b, i, t in zip(beta, local, total)]
    pu = -sum(v*v*r for v, r in zip(p, inverse_scale))/(2*du)
    pv = -du
    ray_kv = a*sum(b*b*r for b, r in zip(beta, inverse_scale))/2
    transversality = pu*a+pv*ray_kv+a*sum(
        v*b*r for v, b, r in zip(p, beta, inverse_scale))
    di = [u*r-i for i, r in zip(local, inverse_scale)]
    endpoint = pv*sum(b*b*di_i for b, di_i in zip(beta, di))/2
    endpoint += sum(v*b*di_i for v, b, di_i in zip(p, beta, di))

    def metric_insertion(lam):
        z = 1+lam*du
        return z*(p[0]**2*sinh(z)/cosh(z)**3-p[1]**2*sin(z)/cos(z)**3)

    return -(endpoint+integral(metric_insertion, 0., 1., 12))/transversality


def adjoint_derivative():
    rays = [ray(mu, phi, 1., 0.) for mu, phi in DIRECTIONS]
    mean_radius = sum(r[4] for r in rays)/len(rays)
    mean_clock = clock(1., 0.)
    result = 0.
    for a, beta, s, c, d, u in rays:
        _, p, dpp, nc, ncp = optics(c, a)
        _, dslope, _, ns, _ = optics(s, a)
        w = d/mean_radius
        g = (s-c)*dpp/p-1
        a1, b, h = w*(s-c), -w*g, 0.5*w*g+(u-mean_clock)/mean_radius
        terminal = w*p+h*dslope

        def optical_kernel(t):
            j = axes(t, a)
            endpoint_b = axes(s-t, a)
            coeff = [h*bb*nn for bb, nn in zip(endpoint_b, ns)]
            if t < c:
                cap_b, cap_bp = axes(c-t, a), slopes(c-t, a)
                for i in range(2):
                    coeff[i] += cap_b[i]*(b*nc[i]+a1*ncp[i])+a1*cap_bp[i]*nc[i]
            return 2*a*a*(coeff[0]*j[0]-coeff[1]*j[1])

        result += integral(optical_kernel, 0, c)+integral(optical_kernel, c, s)
        result += terminal*waist_derivative(a, beta, s)
    return result/len(rays)


def bump_jets(x):
    if abs(x) >= 1:
        return 0., 0., 0.
    d = 1-x*x
    b = exp(1-1/d)
    l1 = -2*x/d**2
    return b, b*l1, b*(l1*l1-2/d**2-8*x*x/d**3)


def compact_completion():
    ends = (1.1, 1.33)
    width = 0.04
    pulse_width = 0.025
    nu = 1.45

    def moments(center, half_width, slot):
        def coefficient(u, second):
            profile = bump_jets((u-center)/half_width)[slot]/half_width
            mp = 2*cosh(u)*cos(u)
            if second:
                mp = mp*integral(lambda t: 1/(cosh(t)*cos(t)), u, nu, 12)-tanh(u)-tan(u)
            return mp*profile
        return tuple(integral(lambda u: coefficient(u, second),
                              center-half_width, center+half_width, 50)
                     for second in (False, True))

    v, w = [moments(c, width, 0) for c in ends]
    original = moments(joint_focal.C, pulse_width, 1)
    det = v[0]*w[1]-w[0]*v[1]
    a = (-w[1]*original[0]+w[0]*original[1])/det
    b = (v[1]*original[0]-v[0]*original[1])/det
    # Independent forward integration of the original forced ODE with g'.
    def force(u):
        pulse = bump_jets((u-joint_focal.C)/pulse_width)[2]/pulse_width**2
        for c, scale in zip(ends, (a, b)):
            pulse += scale*bump_jets((u-c)/width)[1]/width**2
        return -(sinh(u)*cos(u)+cosh(u)*sin(u))*pulse/2

    velocity = displacement = 0.
    steps = 20000
    step = nu/steps
    for i in range(steps):
        lo, mid, hi = i*step, (i+0.5)*step, (i+1)*step
        f0, fm, f1 = force(lo), force(mid), force(hi)
        d0 = velocity/(cosh(lo)*cos(lo))
        dm1 = (velocity+step*f0/2)/(cosh(mid)*cos(mid))
        dm2 = (velocity+step*fm/2)/(cosh(mid)*cos(mid))
        d1 = (velocity+step*fm)/(cosh(hi)*cos(hi))
        displacement += step*(d0+2*dm1+2*dm2+d1)/6
        velocity += step*(f0+4*fm+f1)/6
    assert abs(det) > 0.02
    return max(abs(displacement), abs(velocity))


if __name__ == "__main__":
    step = 0.0002
    centered = (clock(1+step, 0.)-clock(1-step, 0.))/(2*step)
    adjoint = adjoint_derivative()
    # A longitudinal boost compensates the curvature-coordinate scaling:
    # W=κ⁴ exp(4χ) is fixed by χ=-log κ.
    calibrated = (clock(1+step, -log(1+step))-clock(1-step, -log(1-step)))/(2*step)
    compact_error = compact_completion()
    assert abs(centered-adjoint) < 2e-8 and abs(adjoint) > 1e-4
    assert abs(calibrated) < 1e-10 and compact_error < 1e-8
    print(f"Fixed emitter, adjoint derivative {adjoint:.8f}")
    print(f"Fixed emitter, direct derivative  {centered:.8f}")
    print(f"Calibrated curvature-scale derivative below 1e-10: {abs(calibrated) < 1e-10}")
    print(f"Post-tip control residual below 1e-8: {compact_error < 1e-8}")
