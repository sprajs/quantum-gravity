#!/usr/bin/env python3
"""Gaussian matrix elements of the two-cell capped clock in corner-commutant.md."""

import math


def radial_average(z):
    """Integrate exp(min(v²z²/8, 1)) over v from zero to one."""
    coefficient = z * z / 8
    stop = 1.0 if coefficient <= 1 else 1 / math.sqrt(coefficient)
    argument = min(coefficient, 1.0)
    # Before the cap, rescale v to [0,1] and integrate the exponential series.
    average = 1.0
    term = 1.0
    for n in range(1, 20):
        term *= argument / n
        average += term / (2 * n + 1)
    return stop * average + (1 - stop) * math.e


def clock_ratio(displacement, panels):
    """Simpson quadrature of the translated Z spectral measure, with hbar=1."""
    limit = 9.0
    step = 2 * limit / panels
    terms = []
    for j in range(panels + 1):
        standard = -limit + j * step
        weight = 1 if j in (0, panels) else (4 if j % 2 else 2)
        z = 1.5 * (standard + displacement)
        terms.append(weight * math.exp(-standard**2) * radial_average(z))
    return step * math.fsum(terms) / (3 * math.sqrt(math.pi))


def main():
    displacements = (0, 4, 20)
    ratios = []
    print("shape phase t    clock / zero-focus clock")
    for displacement in displacements:
        coarse = clock_ratio(displacement, 4096)
        ratio = clock_ratio(displacement, 8192)
        assert abs(coarse - ratio) < 1e-8
        ratios.append(ratio)
        print(f"{displacement:13d}    {ratio:.8f}")
    assert 1 < ratios[0] < ratios[1] < ratios[2] < math.e
    print(f"large-t limit    {math.e:.8f}")


if __name__ == "__main__":
    main()
