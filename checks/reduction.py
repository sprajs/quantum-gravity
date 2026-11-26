"""Check spherical constraints, linearized gravitons, tilted clocks and a gauge quotient.

Run from the repository root with python checks/reduction.py. Standard library only.
"""

from fractions import Fraction as F
from math import cosh, exp, hypot, isclose, sqrt, tanh
from random import Random


def mass(radius, radial_metric, radius_prime, p_metric, cosmological):
    return radius * (1 - (radius_prime / radial_metric) ** 2
                     + (p_metric / radius) ** 2 - cosmological * radius**2 / 3) / 2


def constraints(radius, radial_metric, radius_prime, radius_second, metric_prime,
                p_metric, p_metric_prime, p_radius, cosmological):
    normal = (-p_metric * p_radius / radius
              + radial_metric * p_metric**2 / (2 * radius**2)
              + radius * radius_second / radial_metric
              - radius * radius_prime * metric_prime / radial_metric**2
              + radius_prime**2 / (2 * radial_metric) - radial_metric / 2
              + cosmological * radial_metric * radius**2 / 2)
    radial = p_radius * radius_prime - radial_metric * p_metric_prime
    return normal, radial


def check_spherical_generators():
    rng = Random(226)
    for _ in range(128):
        r, l = (F(rng.randint(1, 13), rng.randint(1, 7)) for _ in range(2))
        dr, ddr, dl, p, dp, pr, k, n, dn, shift, dshift = (
            F(rng.randint(-11, 11), rng.randint(1, 7)) for _ in range(11))
        h, d = constraints(r, l, dr, ddr, dl, p, dp, pr, k)

        # Gradient of the mass in (R, L, R', P_L) dotted with a field variation.
        def vary_mass(delta_r, delta_l, delta_dr, delta_p):
            return ((1 - (dr / l)**2 - (p / r)**2 - k * r**2) * delta_r / 2
                    + r * dr**2 * delta_l / l**3 - r * dr * delta_dr / l**2
                    + p * delta_p / r)

        mass_prime = vary_mass(dr, dl, ddr, dp)
        assert mass_prime == -dr * h / l - p * d / (r * l)

        # Hamiltonian flow of H[N] + D[shift], with compact interior smearings.
        dot_r = -n * p / r + shift * dr
        dot_l = n * (-pr / r + l * p / r**2) + dshift * l + shift * dl
        dot_dr = (-dn * p / r - n * dp / r + n * p * dr / r**2
                  + dshift * dr + shift * ddr)
        dot_p = (-n * p**2 / (2 * r**2) - dn * r * dr / l**2
                 - n * dr**2 / (2 * l**2) + n / 2 - k * n * r**2 / 2 + shift * dp)
        assert vary_mass(dot_r, dot_l, dot_dr, dot_p) == -n * dr * d / l**3 + shift * mass_prime
    print("Spherical H and D generator identities: 128 rational jets, exact")

    # Pythagorean parametrization keeps both slicings' ADM data rational.
    m = F(1)
    zero, one = F(0), F(1)
    for t in (F(1, 5), F(1, 3), F(1, 2), F(3, 4)):
        sqrt_f = (1 - t**2) / (1 + t**2)
        infall_speed = 2 * t / (1 + t**2)
        r = 2 * m / infall_speed**2
        for l, dl, p, dp, pr in (
            (1 / sqrt_f, -m / (r**2 * sqrt_f**3), zero, zero, zero),
            (one, zero, r * infall_speed, infall_speed / 2, infall_speed / 2),
        ):
            assert constraints(r, l, one, zero, dl, p, dp, pr, zero) == (zero, zero)
            assert mass(r, l, one, p, zero) == m
            # Outward null normal n_slice + s and its partner (n_slice - s)/2.
            for boost in (F(1, 3), F(1), F(7, 2)):
                theta_out = 2 * boost * (-p / r + one / l) / r
                theta_in = (-p / r - one / l) / (r * boost)
                assert r * (1 + r**2 * theta_out * theta_in / 2) / 2 == m
    print("Static and Painleve-Gullstrand slices: 4 radii, 3 null boosts, exact mass 1")


def check_graviton_polarizations():
    """Compare a covariant spin-2 numerator to the explicit two-helicity sum."""
    def spatial_dot(v, w):
        return sum(x * y for x, y in zip(v, w))

    def spacetime_dot(v, w):
        return -v[0] * w[0] + spatial_dot(v[1:], w[1:])

    pair_count = 0
    for k in ((1, 0, 0, 1), (5, 3, 0, 4), (7, 2, 3, 6)):
        assert spacetime_dot(k, k) == 0
        nx, ny, nz = (F(x, k[0]) for x in k[1:])
        # Two orthonormal spatial polarization directions perpendicular to k.
        u = (1 - nx**2 / (1 + nz), -nx * ny / (1 + nz), -nx)
        v = (-nx * ny / (1 + nz), 1 - ny**2 / (1 + nz), -ny)
        tidal_sources = []
        for axis in range(3):
            for sign in (-1, 1):
                ray = (1,) + tuple(sign * int(j == axis) for j in range(3))
                for direction in range(3):
                    if direction == axis:
                        continue
                    screen = (0,) + tuple(int(j == direction) for j in range(3))
                    q = tuple(spacetime_dot(k, ray) * e - spacetime_dot(k, screen) * l
                              for l, e in zip(ray, screen))
                    assert spacetime_dot(k, q) == 0
                    assert spacetime_dot(q, q) == spacetime_dot(k, ray)**2
                    qu, qv = spatial_dot(q[1:], u), spatial_dot(q[1:], v)
                    tidal_sources.append((q, (qu**2 - qv**2) / 2, qu * qv))
        for a, plus_a, cross_a in tidal_sources:
            for b, plus_b, cross_b in tidal_sources:
                covariant = F(2 * spacetime_dot(a, b)**2
                              - spacetime_dot(a, a) * spacetime_dot(b, b), 8)
                # The two polarization tensors have unit squared norm.
                helicities = (plus_a * plus_b + cross_a * cross_b) / 2
                assert helicities == covariant
                pair_count += 1
    print(f"Free graviton tidal correlator: {pair_count} exact polarization-sum comparisons")


def simpson(f, low, high, steps=4000):
    assert steps % 2 == 0
    dx = (high - low) / steps
    middle = sum((4 if i % 2 else 2) * f(low + i * dx) for i in range(1, steps))
    return (f(low) + middle + f(high)) * dx / 3


def check_clocks():
    def weight(p):
        return exp(-((p - 1.1) / 0.7)**2)

    lo, hi = -7, 7
    norm = simpson(lambda p: weight(p) / (2 * hypot(1, p)), lo, hi)
    print(f"Reference mass-shell wavepacket norm squared: {norm:.9f}")
    for tilt in (-0.6, 0.6):
        p_lo, p_hi = (p + tilt * hypot(1, p) for p in (lo, hi))

        def density(momentum, include_jacobian):
            discriminant = sqrt(momentum**2 + 1 - tilt**2)
            energy = (discriminant - tilt * momentum) / (1 - tilt**2)
            p = momentum - tilt * energy
            assert isclose(energy, hypot(1, p), rel_tol=1e-12)
            return weight(p) / (2 * (discriminant if include_jacobian else energy))

        matched = simpson(lambda p: density(p, True), p_lo, p_hi)
        omitted = simpson(lambda p: density(p, False), p_lo, p_hi)
        assert isclose(norm, matched, rel_tol=1e-12)
        assert abs(omitted / norm - 1) > 0.1
        print(f"Tilt {tilt:+.1f}: matched {matched:.9f}, omitted determinant {omitted:.9f}")


def check_orbit_volume():
    # Units hbar^2/(2 mu) = kappa = 1. U sends the upstairs constant to u.
    def u(x):
        return 1 / cosh(x)

    def potential(x):
        return 1 - 2 * u(x)**2

    norm = simpson(lambda x: u(x)**2, -18, 18)
    kinetic = simpson(lambda x: (u(x) * tanh(x))**2, -18, 18) / norm
    total = kinetic + simpson(lambda x: potential(x) * u(x)**2, -18, 18) / norm
    assert isclose(norm, 2, abs_tol=1e-12)
    assert isclose(kinetic, 1 / 3, abs_tol=1e-12) and abs(total) < 1e-12
    dx = 0.001
    residual = max(abs(-(u(x + dx) - 2 * u(x) + u(x - dx)) / dx**2
                       + potential(x) * u(x)) for x in (k / 20 for k in range(-100, 101)))
    assert residual < 1e-6
    print(f"Orbit-volume ground state: free energy {kinetic:.9f}, matched {total:.9f}, "
          f"finite-difference residual {residual:.2g}")


if __name__ == "__main__":
    check_spherical_generators()
    check_graviton_polarizations()
    check_clocks()
    check_orbit_volume()
