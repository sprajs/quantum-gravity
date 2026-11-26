"""Schwarzschild null geodesics, marginal-cut spectrum and reduced packet volumes."""

from math import acos, ceil, cos, erf, exp, fsum, log, pi, sin, sqrt


def gaussian_rule(order):
    """Gauss-Legendre nodes and weights for integration on [-1, 1]."""
    pairs = []
    for j in range(1, order + 1):
        x = cos(pi * (j - 0.25) / (order + 0.5))
        for _ in range(16):
            previous, current = 1.0, x
            for k in range(2, order + 1):
                previous, current = current, ((2*k-1)*x*current - (k-1)*previous)/k
            derivative = order * (previous - x*current) / (1-x*x)
            correction = current / derivative
            x -= correction
            if abs(correction) < 2e-15:
                break
        pairs.append((x, 2 / ((1-x*x)*derivative**2)))
    return pairs


RADIAL = gaussian_rule(18)
ANGULAR = gaussian_rule(24)


def integrate(function, a, b, rule):
    mid, half = (a+b)/2, (b-a)/2
    return half * fsum(weight * function(mid+half*x) for x, weight in rule)


def clock_reading(theta0, alpha, epsilon):
    """Trace the exact inward normal geodesic in units with r_h=1, E=1."""
    angular_momentum = -3*alpha*cos(theta0)*sin(theta0)
    angular_derivative = -3*alpha*cos(2*theta0)

    def speed(r):
        return sqrt(1 - (1-1/r)*(angular_momentum/r)**2)

    def screen(r):
        # Angular position and separation of adjacent generators at fixed r.
        theta = theta0 + angular_momentum*integrate(
            lambda u: 1/(u*u*speed(u)), r, 1, RADIAL)
        separation = 1 + angular_derivative*integrate(
            lambda u: 1/(u*u*speed(u)**3), r, 1, RADIAL)
        w = speed(r)
        assert 0 < theta < pi and separation > 0
        rho = r*sqrt(w*separation*sin(theta)/sin(theta0))
        dlog_w = angular_momentum**2 * (2*r-3)/(2*r**4*w*w)
        theta_r = -angular_momentum/(r*r*w)
        separation_r = -angular_derivative/(r*r*w**3)
        rho_r = rho*(1/r + (dlog_w + theta_r*cos(theta)/sin(theta)
                             + separation_r/separation)/2)
        return rho, w*rho_r

    lower, upper = 0.8*epsilon, 1.0
    assert screen(lower)[0] < epsilon
    for _ in range(45):
        trial = (lower+upper)/2
        if screen(trial)[0] < epsilon:
            lower = trial
        else:
            upper = trial
    cap = (lower+upper)/2
    slope = screen(cap)[1]
    assert slope > 0
    return slope * integrate(lambda u: 1/speed(u), cap, 1, RADIAL)


def mean_clock(alpha, epsilon):
    return 0.5 * fsum(weight*clock_reading(acos(x), alpha, epsilon)
                      for x, weight in ANGULAR)


def heat_constant(t, first_mode):
    last_mode = ceil(sqrt(60/t))
    return fsum((2*l+1)*exp(-t*(1+l*(l+1)))
                for l in range(first_mode, last_mode+1)) - 1/t


def packet_powers():
    # m=sqrt(s) is proportional to M. Centered mass bins resolve the peak.
    rule = gaussian_rule(80)
    centers = (1e4, 4e4)
    time_integrals, boost_integrals = [], []
    for b in centers:
        def weight(offset):
            return exp(-(offset*(2+offset/sqrt(b)))**2/4)

        time_integrals.append(integrate(weight, -10, 10, rule))
        boost_integrals.append(integrate(lambda x: 2*(sqrt(b)+x)*weight(x), -10, 10, rule))
        exact = sqrt(pi*b)*(1+erf(sqrt(b)/2))
        assert abs(boost_integrals[-1]/exact-1) < 2e-12
    return tuple(log(seq[1]/seq[0])/log(centers[1]/centers[0])
                 for seq in (time_integrals, boost_integrals))


if __name__ == "__main__":
    for first, expected in [(0, -2/3), (1, -5/3)]:
        extrapolated = 2*heat_constant(0.001, first) - heat_constant(0.002, first)
        assert abs(extrapolated-expected) < 2e-6
        print(f"shape heat constant, first l={first}: {extrapolated:.6f}")
    time_power, boost_power = packet_powers()
    assert abs(time_power) < 5e-5 and abs(boost_power-0.5) < 1e-10
    print(f"packet powers, fixed time and boost widths: {time_power:.5f}, {boost_power:.5f}")
    for eps in (0.5, 0.65):
        alpha = 0.002
        assert abs(mean_clock(0, eps)-(1-eps)) < 1e-12
        excess = (mean_clock(alpha, eps)+mean_clock(-alpha, eps))/2 - (1-eps)
        estimated = excess/alpha**2
        expected = 0.6*((1-eps)/eps)**2
        assert abs(estimated/expected-1) < 3e-4
        print(f"quadrupole delay / alpha^2 at epsilon={eps}: "
              f"{estimated:.6f}, analytic {expected:.6f}")
