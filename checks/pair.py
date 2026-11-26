#!/usr/bin/env python3
"""Reproduce the connected radial-mode correlator in Eqs. (4.32)–(4.34).

Run with python3 checks/pair.py. Only the Python standard library is required.
"""

import cmath
import math


def mode_sum(x, cutoff):
    """Direct cutoff sum with x = 4 G_N hbar / area."""
    angle = math.remainder(2 * x, math.tau)
    real = math.fsum(math.cos(k * angle) / k**2 for k in range(1, cutoff + 1))
    imag = -math.fsum(math.sin(k * angle) / k**2 for k in range(1, cutoff + 1))
    return x**2 / 2 * complex(real, imag)


def log_sinc(t):
    """Smooth integrand left after subtracting log(t) from log(2 sin(t/2))."""
    u = t / 2
    if abs(u) < 0.01:
        return math.log1p(u**2 * (-1 / 6 + u**2 * (1 / 120 - u**2 / 5040)))
    return math.log(math.sin(u) / u)


def closed_form(x):
    """Evaluate Li_2 on the unit circle by integrating its logarithmic derivative."""
    theta = math.remainder(2 * x, math.tau)
    t = abs(theta)
    real = math.pi**2 / 6 - math.pi * t / 2 + t**2 / 4
    imag = 0.0
    if t:
        panels = 1024
        h = t / panels
        interior = math.fsum(
            (4 if j % 2 else 2) * log_sinc(h * j) for j in range(1, panels)
        )
        correction = h / 3 * (log_sinc(0) + interior + log_sinc(t))
        imag = t * (math.log(t) - 1) + correction
        if theta < 0:
            imag = -imag
    return x**2 / 2 * complex(real, imag)


def check_single_mode():
    # Acting twice with q = delta_q (a + a†) reaches levels 0 and 2.
    def apply_q(vector, delta_q):
        result = [0.0] * (len(vector) + 1)
        for n, value in enumerate(vector):
            if n:
                result[n - 1] += delta_q * math.sqrt(n) * value
            result[n + 1] += delta_q * math.sqrt(n + 1) * value
        return result

    k, x = 7, 0.23
    delta_q = math.sqrt(x / (2 * k))
    pair = apply_q(apply_q([1.0], delta_q), delta_q)
    overlap = sum(abs(v)**2 * cmath.exp(-1j * n * k * x) for n, v in enumerate(pair))
    connected = overlap - abs(pair[0])**2
    expected = x**2 / (2 * k**2) * cmath.exp(-2j * k * x)
    assert abs(connected - expected) < 5e-16 * abs(expected)


def check_sums():
    print("Closed form compared with a direct sum through N = 100000")
    print("          x           real           imag       abs err    tail bound")
    cutoff = 100_000
    for x in [0.0001, 0.01, 0.1, 1.0, math.pi / 2, math.pi, math.pi + 0.1, 5.25]:
        exact = closed_form(x)
        error = abs(mode_sum(x, cutoff) - exact)
        angle = math.remainder(2 * x, math.tau)
        bound = x**2 / (2 * cutoff)
        if angle:
            oscillatory = x**2 / (2 * abs(math.sin(angle / 2)) * (cutoff + 1)**2)
            bound = min(bound, oscillatory)
        print(f"{x:11.7f} {exact.real:14.7g} {exact.imag:14.7g} {error:13.5g} {bound:13.5g}")
        assert error <= bound + 1e-13 * x**2

    # Independent special values with both phase signs represented above.
    for x, dilog in [(math.pi, math.pi**2 / 6), (math.pi / 2, -math.pi**2 / 12)]:
        assert abs(closed_form(x) - x**2 / 2 * dilog) < 1e-13


def check_uv_limits():
    print("\nFixed-cutoff cubic coefficient checked against -i H_N")
    print("   N          H_N        Im[A_N(x)]/x^3 + H_N")
    x = 1e-7
    for n in [10, 100, 1000, 10_000]:
        harmonic = math.fsum(1 / k for k in range(1, n + 1))
        difference = mode_sum(x, n).imag / x**3 + harmonic
        print(f"{n:5d} {harmonic:13.9f} {difference:25.7g}")
        # |sin(u) - u| <= |u|^3/6 bounds the error after dividing by x^3.
        assert abs(difference) <= x**2 * n * (n + 1) / 3 + 5e-14

    print("\nInfinite-sum expansion: Im[A]/x^3 - log(2x) + 1, divided by x^2")
    print("         x         scaled remainder   (limit -1/18)")
    for x in [0.25, 0.1, 0.03, 0.01]:
        exact = closed_form(x)
        remainder = (exact.imag / x**3 - math.log(2 * x) + 1) / x**2
        print(f"{x:10.5f} {remainder:24.10f}")
        assert abs(remainder + 1 / 18) < 0.002 * x**2 + 2e-11
        real = math.pi**2 * x**2 / 12 - math.pi * x**3 / 2 + x**4 / 2
        assert abs(exact.real - real) < 5e-15 * x**2


if __name__ == "__main__":
    check_single_mode()
    check_sums()
    check_uv_limits()
    print("\nAll pair-correlator checks passed.")
