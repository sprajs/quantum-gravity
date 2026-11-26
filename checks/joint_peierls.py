"""Sharp clock response on an Einstein–Rosen cap and outgoing cylinder."""

from cmath import exp
from math import pi, sin, sqrt

CAP, WAIST = 0.25, 1.0
SPAN = WAIST - CAP
CURVATURE_SCALE = 1 / (WAIST * SPAN)


def midpoint_integral(fn, start, stop, count):
    step = (stop - start) / count
    return step * sum(fn(start + (i + 0.5) * step) for i in range(count))


def shape(time, radius):
    return -1 + CURVATURE_SCALE * (radius**2 - CAP**2 + 2 * time**2)


def conformal_exponent(amplitude, time, radius):
    psi = amplitude * shape(time, radius)
    gamma = (amplitude * CURVATURE_SCALE)**2 * (radius**4 + 8 * time**2 * radius**2)
    return 2 * (gamma - psi)


def affine_clock(amplitude):
    cap_factor = conformal_exponent(amplitude, 0, CAP)

    def integrand(radius):
        return exp(conformal_exponent(amplitude, radius - CAP, radius) - cap_factor)

    return midpoint_integral(integrand, CAP, WAIST, 4096) / (2 * sqrt(CAP))


def forcing(radius):
    return -1 / sqrt(CAP * radius)


def retarded_kernel(elapsed, radius, source_radius):
    """Angular integral of the planar retarded kernel, before the far front."""
    if elapsed <= abs(radius - source_radius):
        return 0.0
    parameter = (elapsed**2 - (radius - source_radius)**2) / (4 * radius * source_radius)
    assert 0 < parameter < 1
    return midpoint_integral(lambda x: (1 - parameter * sin(x)**2)**-0.5, 0, pi/2, 16) / pi


def causal_kernel(time, radius, source_radius):
    elapsed = time - (source_radius - CAP)
    return (retarded_kernel(elapsed, radius, source_radius)
            - retarded_kernel(-elapsed, radius, source_radius))


def response(time, radius):
    # All responses are multiplied by the reduced action coefficient C.
    alpha = SPAN / CAP
    # Split the quadrature at the ingoing characteristic reaching the test point.
    crossing = min(WAIST, max(CAP, (time + radius + CAP) / 2))
    integrand = lambda s: forcing(s) * causal_kernel(time, radius, s)
    return (alpha * causal_kernel(time, radius, CAP)
            + midpoint_integral(integrand, CAP, crossing, 256)
            + midpoint_integral(integrand, crossing, WAIST, 256))


def initial_momentum(radius, time_step):
    return (response(time_step, radius) - response(-time_step, radius)) / (2 * time_step)


if __name__ == "__main__":
    step = 1e-16
    variation = affine_clock(step * 1j).imag / step
    assert abs(variation + 1.5) < 1e-7
    print(f"Affine clock variation on curved perturbation: {variation:.6f}")

    assert response(0, 0.2) == 0
    radius = 0.64
    inner = response(radius - CAP + 1e-7, radius)
    outer = response(radius - CAP - 1e-7, radius)
    assert abs(inner - 0.9) < 2e-6 and abs(outer - 0.4) < 2e-6
    print(f"One-sided values of C times the response: {inner:.5f}, {outer:.5f}")
    assert abs(response(1.01e-5, CAP + 1e-5) - 1.5) < 3e-5
    print("Open cap response: 0; sheet-side rim limit: 1.50000")

    width = 1e-4
    step = width / 8
    corners = (CAP - width, CAP - step, CAP + step, CAP + width)
    impulse = sum(midpoint_integral(lambda r: initial_momentum(r, step), left, right, 4)
                  for left, right in zip(corners, corners[1:]))
    assert abs(impulse - 2) < 2e-4
    print(f"Initial momentum in shrinking rim collar: {impulse:.5f}")

    step = 1e-4
    far_front = 2 * WAIST - CAP
    fronts = (CAP - step, CAP + step, far_front - step, far_front + step)

    def pair_with_preparation(radius):
        return sqrt(radius) * shape(0, radius) * initial_momentum(radius, step)

    pairing = sum(midpoint_integral(pair_with_preparation, left, right, order)
                  for left, right, order in zip(fronts, fronts[1:], (8, 256, 8)))
    assert abs(pairing - variation) < 5e-6
    print(f"Complete initial-surface pairing: {pairing:.5f}")
