"""Check the Schwarzschild clock's local calibration, optical tide and master wave."""

from decimal import Decimal as D, getcontext
from fractions import Fraction as F

getcontext().prec = 55


def check_master():
    """Test the exponential RT seed in the homogeneous quadrupole Zerilli equation."""
    for mass, r in [(F(1), F(9, 4)), (F(1), F(4)), (F(3), F(29))]:
        lapse = 1 - 2 * mass / r
        denom = 2 * r + 3 * mass
        potential = (2 * lapse * (12 * r**3 + 12 * mass * r**2
                                  + 18 * mass**2 * r + 9 * mass**3)
                     / (r**3 * denom**2))
        amplitude = -2 * mass * r / denom
        first = -6 * mass**2 / denom**2
        second = 24 * mass**2 / denom**3
        # Remove the common exp[-2(t-r*)/m] before differentiating.
        residual = (lapse**2 * second
                    + lapse * (2 * mass / r**2 + 4 / mass) * first
                    - potential * amplitude)
        assert residual == 0

        # Outgoing RW amplitudes with the harmonic and temporal factor divided out.
        h_uu = -4 * (r / mass - 1)
        angular = -2
        angular_u = 4 / mass
        master = r / 3 * (angular + 2 / (4 + 6 * mass / r) * (h_uu + r * angular_u))
        assert master == amplitude


def calibrated_radius(amplitude):
    """Solve rho=4 at the wave pole (m=1,u=u0), using the RT metric jet."""
    angular_curvature = (2 * amplitude).exp() * (1 - 6 * amplitude)
    r = D(4)
    for _ in range(7):
        radial_term = angular_curvature + 4 * r * amplitude
        residual = r**2 - 16 * radial_term
        r -= residual / (2 * r - 64 * amplitude)
    return r


def jacobi_column(length, tide):
    """Exact constant-tide Jacobi column and its derivative by convergent series."""
    argument = length**2 * tide
    value = slope = term = D(1)
    for order in range(1, 13):
        term *= argument / ((2 * order) * (2 * order + 1))
        value += term
        slope += (2 * order + 1) * term
    return length * value, slope


def area(length, tide):
    growing, dg = jacobi_column(length, tide)
    oscillating, ds = jacobi_column(length, -tide)
    distance = (growing * oscillating).sqrt()
    slope = (dg * oscillating + ds * growing) / (2 * distance)
    return distance, slope


def frozen_clock(size, radius):
    """Match the measured sky size and solve for the cap of each frozen-tide ray."""
    q = 1 / radius**3
    # Three polar Gauss nodes; the two off-equator nodes have identical tides.
    rays = [(D(4) / 9, 3 * q), (D(5) / 9, 3 * q * (1 - D(3) / 5))]
    waist = size
    for _ in range(5):
        distances = [(w, area(waist, tide)[0]) for w, tide in rays]
        first = sum(w * distance for w, distance in distances)
        second = sum(w * distance**2 for w, distance in distances)
        waist += size - second / first
    weighted_clock = weight_sum = D(0)
    for weight, tide in rays:
        distance = area(waist, tide)[0]
        cap = waist / 2
        for _ in range(5):
            cap_distance, slope = area(cap, tide)
            cap -= (cap_distance - distance / 2) / slope
        slope = area(cap, tide)[1]
        weighted_clock += weight * distance * slope * (waist - cap)
        weight_sum += weight * distance
    return weighted_clock / weight_sum


if __name__ == "__main__":
    check_master()
    step = D("1e-10")
    plus, minus = calibrated_radius(step), calibrated_radius(-step)
    curvature_change = (48 / plus**6 - 48 / minus**6) / (2 * step)
    assert abs(curvature_change + D(27) / 64) < D("1e-16")
    print("Zerilli seed solves the quadrupole master equation at 3 exterior radii.")
    print(f"Curvature derivative at fixed radius reading = {curvature_change:.8f}")
    target = F(-39, 204800)
    coefficient = D(target.numerator) / D(target.denominator)
    previous_error = None
    for size in (D("0.4"), D("0.2"), D("0.1")):
        observed = (frozen_clock(size, plus) - frozen_clock(size, minus)) / (2 * step * size**5)
        error = abs(observed - coefficient)
        if previous_error is not None:
            assert error < previous_error / 12
        previous_error = error
        print(f"Frozen-tide radius {size}: normalized derivative {observed:.12f}")
    assert previous_error < D("1e-11")
    print(f"Compact quadrupole bracket coefficient = {target}")
