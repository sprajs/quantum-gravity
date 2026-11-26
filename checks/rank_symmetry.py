#!/usr/bin/env python3
"""Angular clock transformations and the finite-spin example in rank-symmetry.md."""

import math


def integrate(function, lower, upper, panels=1024):
    """Composite Simpson rule for a smooth real integrand."""
    assert panels % 2 == 0
    step = (upper - lower) / panels
    weighted = [function(lower), function(upper)]
    for i in range(1, panels):
        weighted.append((4 if i % 2 else 2) * function(lower + step * i))
    return step * math.fsum(weighted) / 3


def sphere_average(function):
    """Uniform solid-angle average of an azimuth-independent function of z."""
    return integrate(function, -1, 1) / 2


def spin_one_density(vector, direction, alpha):
    """Apply the Cartesian spin-one density at unit area radius."""
    x, y, z = direction
    vx, vy, vz = vector
    cross = (y * vz - z * vy, z * vx - x * vz, x * vy - y * vx)
    normalization = math.sqrt(1 + alpha**2 / 3)
    return tuple((v + 1j * alpha * c / math.sqrt(2)) / normalization
                 for v, c in zip(vector, cross))


def main():
    t = 1
    def root_jacobian(z):
        return 1 / (math.cosh(t) + z * math.sinh(t))

    mass = sphere_average(lambda z: root_jacobian(z)**2)
    clock_ratio = mass / sphere_average(root_jacobian)
    assert abs(mass - 1) < 1e-9
    assert abs(clock_ratio - math.sinh(t) / t) < 1e-9
    print(f"conformal displacement t=1, round clock ratio  {clock_ratio:.8f}")

    # Im <z(x+iy), (x+iy) o s_1>, with normalized solid angle.
    quadrupole = sphere_average(lambda z: z * (1-z*z) * math.sin(z))
    assert abs(quadrupole - (4 * math.sin(1) - 6 * math.cos(1))) < 1e-10
    assert quadrupole > 0
    print(f"twisted dipole, imaginary quadrupole overlap   {quadrupole:.8f}")

    axes = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    directions = axes + [tuple(-a for a in axis) for axis in axes]
    alpha = 0.5
    root_d = math.sqrt(1 + alpha**2 / 3)
    for basis_vector in axes:
        # The six directions integrate degree-two polynomials in n exactly.
        first = [spin_one_density(basis_vector, n, alpha) for n in directions]
        second = [spin_one_density(v, n, alpha) for v, n in zip(first, directions)]
        for component in range(3):
            mean = sum(v[component] for v in first) / 6
            square = sum(v[component] for v in second) / 6
            assert abs(mean - basis_vector[component] / root_d) < 1e-14
            assert abs(square - basis_vector[component]) < 1e-14

    epsilon = 0.25
    def clock(j):
        casimir = j * (j + 1)
        return root_d * integrate(
            lambda v: math.exp((v*v - epsilon**2) * casimir / 8), epsilon, 1
        )

    t1, t2 = clock(1), clock(2)
    threshold = 1
    assert t1 < threshold < t2
    print(f"spin clocks t1, t2                            {t1:.8f}, {t2:.8f}")
    print(f"rank at ceiling 1, shape deficit              3, {1 - 1/root_d:.8f}")


if __name__ == "__main__":
    main()
