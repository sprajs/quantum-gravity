"""Einstein--Rosen cap, optical clock and mixed-surface symplectic tests."""

from math import cos, exp, isclose, sin, sqrt


def integrate(function, lower, upper, panels=80):
    """Composite Simpson rule on an even number of equal panels."""
    step = (upper - lower) / panels
    total = function(lower) + function(upper)
    for index in range(1, panels):
        total += (4 if index % 2 else 2) * function(lower + index * step)
    return total * step / 3


def bessel_j(order, x):
    """Series for J0 or J1 at the bounded wavenumbers in this test."""
    term = 1.0 if order == 0 else x / 2
    total = term
    for index in range(1, 20):
        term *= -(x / 2) ** 2 / (index * (index + order))
        total += term
    return total


RIM, WAIST = 0.25, 1.0
TIME = WAIST - RIM


def mode(t, r):
    """A regular solution, with its time and radial derivatives."""
    phase = t - TIME
    j0 = bessel_j(0, r)
    return j0 * cos(phase), -j0 * sin(phase), -bessel_j(1, r) * cos(phase)


def optical_weight(r, slope):
    exponent = slope * (r - RIM) + slope**2 * (r**2 - RIM**2) / 4
    return exp(exponent) / (2 * sqrt(RIM))


def affine_clock(slope, amplitude):
    """Get the conformal metric from the spacelike radial constraint."""
    def metric_exponent(t, r):
        def twice_gamma_prime(radius):
            _, mode_t, mode_r = mode(t, radius)
            return radius * ((slope + amplitude * mode_t)**2
                             + (amplitude * mode_r)**2) / 2

        q = slope * t + amplitude * mode(t, r)[0]
        return q + integrate(twice_gamma_prime, 0, r)

    start = metric_exponent(0, RIM)
    return integrate(lambda r: exp(metric_exponent(r - RIM, r) - start),
                     RIM, WAIST) / (2 * sqrt(RIM))


def check_surface_current():
    # X is the Bessel mode, Y=t; the coordinate orbit factor c is one.
    def cap(r):
        return -r * mode(0, r)[0]

    def sheet(r):
        t = r - RIM
        value, dt, dr = mode(t, r)
        return r * ((dt + dr) * t - value)

    def late(r):
        value, dt, _ = mode(TIME, r)
        return r * (dt * TIME - value)

    mixed = integrate(cap, 0, RIM) + integrate(sheet, RIM, WAIST)
    assert isclose(mixed, integrate(late, 0, WAIST), abs_tol=2e-9)


def check_clock(slope):
    weight = lambda r: optical_weight(r, slope)
    clock = integrate(weight, RIM, WAIST)
    assert isclose(clock, affine_clock(slope, 0), abs_tol=1e-11)
    clock_derivative = integrate(
        lambda r: weight(r) * ((r - RIM) + slope * (r*r - RIM**2) / 2),
        RIM, WAIST)
    step = 1e-4
    affine_derivative = (affine_clock(slope + step, 0) - affine_clock(slope - step, 0)) / (2 * step)
    assert isclose(clock_derivative, affine_derivative, abs_tol=2e-8)
    kernel = lambda r: (1 + slope * r) * integrate(weight, r, WAIST)

    def mode_derivative(r):
        _, dt, dr = mode(r - RIM, r)
        return kernel(r) * (dt + dr)

    bracket = integrate(mode_derivative, RIM, WAIST)
    numerical = (affine_clock(slope, step) - affine_clock(slope, -step)) / (2 * step)
    assert isclose(bracket, numerical, abs_tol=2e-8)
    # Split distribution into the rim evaluation and ordinary sheet density.
    def density(r):
        minus_kernel_prime = ((1 + slope*r) * weight(r)
                              - slope * integrate(weight, r, WAIST))
        return minus_kernel_prime * mode(r - RIM, r)[0]

    split = integrate(density, RIM, WAIST) - kernel(RIM) * mode(0, RIM)[0]
    assert isclose(split, bracket, abs_tol=2e-8)

    print(f"alpha={slope:g} U={clock:.8f} U'={clock_derivative:.8f} "
          f"rim coefficient={-kernel(RIM):.8f} Bessel response={bracket:.8f}")
    return clock_derivative


if __name__ == "__main__":
    check_surface_current()
    derivative = check_clock(0)
    assert isclose(derivative, 9/32, abs_tol=1e-13)
    unit_trace = -16 * derivative / 3
    assert isclose(unit_trace, -1.5, abs_tol=1e-13)
    check_clock(0.5)
    print(f"unit weighted rim trace dU={unit_trace:.8f}; mixed current conserved")
