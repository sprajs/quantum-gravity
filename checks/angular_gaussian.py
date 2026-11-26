#!/usr/bin/env python3
"""Resolve a twisted highest-weight spherical harmonic into round eigenmodes."""

import math


def spectral_weights(ell, twist, panels, extra_degrees):
    """Squared overlaps at fixed m=ell, for degrees ell through ell+extra_degrees."""
    # Integral of (1-z²)^ell over [-1,1], with z=cos(theta).
    integral = 2 * math.prod(2 * j / (2 * j + 1) for j in range(1, ell + 1))
    # z Y_j^m = a_(j+1) Y_(j+1)^m + a_j Y_(j-1)^m.
    coupling = [
        math.sqrt((j * j - ell * ell) / (4 * j * j - 1))
        for j in range(ell, ell + extra_degrees + 2)
    ]
    overlaps = [0.0] * (extra_degrees + 1)
    for i in range(panels + 1):
        z = i / panels
        simpson = 1 if i in (0, panels) else (4 if i % 2 else 2)
        # Parity supplies the other hemisphere. Odd overlaps are imaginary.
        angle = ell * twist * z
        weights = (math.cos(angle) * simpson, math.sin(angle) * simpson)
        previous = 0.0
        product = (1 - z * z) ** ell / integral
        for n in range(extra_degrees + 1):
            overlaps[n] += weights[n % 2] * product
            following = (z * product - coupling[n] * previous) / coupling[n + 1]
            previous, product = product, following
    return [(2 * overlap / (3 * panels)) ** 2 for overlap in overlaps]


def mode_variance(ell, twist, alpha, panels, extra_degrees):
    weights = spectral_weights(ell, twist, panels, extra_degrees)
    eigenvalue = 1 + ell * (ell + 1)
    scaled = [(1 + j * (j + 1)) / eigenvalue for j in range(ell, ell + len(weights))]
    # Independent differential-operator prediction for the first two moments.
    z2 = 1 / (2 * ell + 3)
    z4 = 3 / ((2 * ell + 3) * (2 * ell + 5))
    slope = (ell * twist) ** 2 / eigenvalue
    drift = 2 * ell * twist * (ell + 1) / eigenvalue
    mean = 1 + slope * (1 - z2)
    variance = slope**2 * (z4 - z2**2) + drift**2 * z2
    assert abs(sum(weights) - 1) < 1e-10
    assert abs(sum(w * x for w, x in zip(weights, scaled)) - mean) < 1e-10
    spectral_variance = sum(w * (x - mean) ** 2 for w, x in zip(weights, scaled))
    assert abs(spectral_variance - variance) < 1e-10
    return sum(w * x ** (-alpha) for w, x in zip(weights, scaled))


def main():
    alpha = 3
    twist = 1.0
    limit = (1 + twist**2) ** (-alpha)
    assert abs(mode_variance(8, 0, alpha, 400, 32) - 1) < 1e-10
    print("ell   normalized twisted variance")
    for ell, expected in ((8, 0.23249645), (32, 0.14709651), (128, 0.13022480)):
        coarse = mode_variance(ell, twist, alpha, 400, ell + 32)
        fine = mode_variance(ell, twist, alpha, 800, ell + 48)
        assert abs(coarse - fine) < 1e-10
        assert abs(fine - expected) < 5e-9
        print(f"{ell:3d}   {fine:.8f}")
    print(f"continuum limit   {limit:.8f}")


if __name__ == "__main__":
    main()
