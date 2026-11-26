#!/usr/bin/env python3
"""Check the finite-spectrum witnesses in audit/observable-boost.md.

Everything is dimensionless. The affine packets are positive, smooth bumps
centered at unit distance from the corner with fractional half-width 0.01.
Only the Python standard library is required.
"""

import cmath
import math


WIDTH = 0.01
GRID_STEP = 0.02
FREQUENCY_CUTOFF = 5


def packet(panels):
    """Midpoint quadrature weights for the normalized C-infinity bump."""
    points = [-1 + 2 * (j + 0.5) / panels for j in range(panels)]
    weights = [math.exp(-1 / (1 - x * x)) for x in points]
    total = math.fsum(weights)
    return [(1 + WIDTH * x, weight / total) for x, weight in zip(points, weights)]


def cross_kernel(eta, samples):
    scale = math.exp(eta)
    return 4 * scale * math.fsum(
        left_weight * right_weight / (left + scale * right) ** 2
        for left, left_weight in samples
        for right, right_weight in samples
    )


def normalized_kernel(eta, samples):
    return cross_kernel(eta, samples) / cross_kernel(0, samples)


def smallest_toeplitz_eigenvalue(a, b, c):
    """First row (1,a,b,c). Reflection splits the matrix into two 2x2 blocks."""
    values = []
    for parity in (1, -1):
        top = 1 + parity * c
        bottom = 1 + parity * a
        off_diagonal = a + parity * b
        values.append((top + bottom - math.hypot(top - bottom, 2 * off_diagonal)) / 2)
    return min(values)


def finite_line_weights(samples):
    """Deposit the positive continuum measure on adjacent frequency nodes.

    Composite Simpson quadrature on each spectral cell integrates its two
    linear interpolation weights. The omitted tail is assigned to node zero.
    """
    count = round(FREQUENCY_CUTOFF / GRID_STEP)
    weights = [0.0] * (count + 1)
    mellin_samples = [(math.log(a), w / a) for a, w in samples]

    def density(nu):
        real = math.fsum(w * math.cos(nu * x) for x, w in mellin_samples)
        imag = math.fsum(w * math.sin(nu * x) for x, w in mellin_samples)
        point_density = 4 * nu / math.sinh(math.pi * nu) if nu else 4 / math.pi
        return point_density * (real * real + imag * imag)

    normalization = cross_kernel(0, samples)
    for cell in range(count):
        for j, simpson in enumerate((1, 4, 2, 4, 1)):
            fraction = j / 4
            nu = (cell + fraction) * GRID_STEP
            mass = simpson * GRID_STEP / 12 * density(nu) / normalization
            weights[cell] += (1 - fraction) * mass
            weights[cell + 1] += fraction * mass
    remainder = 1 - math.fsum(weights)
    assert 0 < remainder < tail_bound()
    weights[0] += remainder
    return weights


def tail_bound():
    cutoff = FREQUENCY_CUTOFF
    tail = 8 * math.exp(-math.pi * cutoff) * (cutoff / math.pi + 1 / math.pi**2)
    return tail / ((1 - math.exp(-2 * math.pi * cutoff)) * (1 - WIDTH) ** 2)


def check_controlled_boost():
    """Compare the squared control visibility for three prepared area distributions."""
    spacing = 4 * math.pi**2
    bins = 1024
    discrete = [(0, 0.5), (spacing, 0.5)]
    degenerate = [(0, 0.25), (0, 0.25), (spacing, 0.125), (spacing, 0.375)]
    uniform = [(spacing * (j + 0.5) / bins, 1 / bins) for j in range(bins)]

    def squared_visibility(rapidity, distribution):
        phase_scale = rapidity / (2 * math.pi)
        amplitude = sum(p * cmath.exp(1j * phase_scale * s) for s, p in distribution)
        return abs(amplitude) ** 2

    for eta in (0.0, 0.25, 0.5, 1.0):
        angle = eta * spacing / (4 * math.pi)
        two_points = squared_visibility(eta, discrete)
        assert abs(two_points - math.cos(angle) ** 2) < 1e-14
        assert abs(squared_visibility(eta, degenerate) - two_points) < 1e-14
        continuum = (math.sin(angle) / angle) ** 2 if angle else 1.0
        assert abs(squared_visibility(eta, uniform) - continuum) < 5e-7
    print("controlled boost at eta=0.5: two areas = 0, uniform interval = "
          f"{squared_visibility(0.5, uniform):.6f}, splitting degeneracies leaves visibility fixed")


def main():
    check_controlled_boost()
    samples = packet(144)
    coarse = packet(96)
    values = [normalized_kernel(eta, samples) for eta in (1, 2, 3)]
    assert max(abs(v - normalized_kernel(eta, coarse))
               for eta, v in enumerate(values, start=1)) < 1e-12
    assert abs(normalized_kernel(-3, samples) - values[2]) < 1e-14
    tolerance = smallest_toeplitz_eigenvalue(*values) / 3
    assert 0.0136 < tolerance < 0.0137
    assert 0.579 < 1 - values[1] < 0.581
    print("packet ratios for eta = 1, 2, 3:", *(f"{v:.9f}" for v in values))
    print(f"lattice at eta=2: ratio=1, discrepancy={1 - values[1]:.9f}")
    print(f"two-area minimum uniform discrepancy: {tolerance:.9f}")

    weights = finite_line_weights(samples)
    assert min(weights) > 0 and abs(math.fsum(weights) - 1) < 1e-14
    bound = 9 * GRID_STEP**2 / 8 + 2 * tail_bound()
    errors = []
    for j in range(61):
        eta = j / 20
        candidate = math.fsum(w * math.cos(k * GRID_STEP * eta)
                              for k, w in enumerate(weights))
        errors.append(abs(candidate - normalized_kernel(eta, samples)))
    assert max(errors) < bound
    print(f"{len(weights)}-area model: sampled max error={max(errors):.9g}, "
          f"uniform analytic bound={bound:.9g}, period={2 * math.pi / GRID_STEP:.6f}")
    variance_integral_bound = math.pi**2 / 16 - 1 / 4
    correlation_bound = WIDTH**2 / (4 * (1 - WIDTH)**2 * variance_integral_bound)
    pair_count_bound = 2 / ((1 - values[1]) * correlation_bound)**2
    assert pair_count_bound > 1.2e9
    print(f"independent Gaussian pairs per setting for SNR one: >= {pair_count_bound:.4g}")


if __name__ == "__main__":
    main()
