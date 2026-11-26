"""Check the round Einstein–scalar null-segment model in audit/matter-state-count.md."""

import cmath
import math


def simpson(function, lower, upper, intervals=256):
    """Integrate a smooth real function with an even number of subintervals."""
    step = (upper - lower) / intervals
    odd = math.fsum(function(lower + j * step) for j in range(1, intervals, 2))
    even = math.fsum(function(lower + j * step) for j in range(2, intervals, 2))
    return step / 3 * (function(lower) + function(upper) + 4 * odd + 2 * even)


CAP_RATIO = 0.5
CEILING = 1.1 * (1 - CAP_RATIO)  # clock in units of the fixed corner radius


def clock(z):
    return simpson(lambda v: math.exp(z**2 * (v**2 - CAP_RATIO**2)), CAP_RATIO, 1)


def clock_series(z):
    """Independent power series for exp(-z²ε²) ∫ exp(z²v²) dv."""
    return math.exp(-(z * CAP_RATIO) ** 2) * math.fsum(
        z ** (2 * n) * (1 - CAP_RATIO ** (2 * n + 1))
        / (math.factorial(n) * (2 * n + 1))
        for n in range(24)
    )


def main():
    assert clock(0) == 1 - CAP_RATIO
    lower, upper = 0.0, 1.0
    assert clock(lower) < CEILING < clock(upper)
    for _ in range(55):
        middle = (lower + upper) / 2
        if clock(middle) < CEILING:
            lower = middle
        else:
            upper = middle
    limit = (lower + upper) / 2
    assert abs(clock_series(limit) - CEILING) < 1e-12
    print(f"Fixed-radius window: u*/R <= {CEILING:.2f}, |z| <= {limit:.8f}")

    for spacing in (0.2, 0.1, 0.05):
        # |n| > 1/spacing gives |z| > 1, beyond the bracketed threshold.
        largest = math.ceil(1 / spacing)
        accepted = sum(
            clock_series(n * spacing) <= CEILING for n in range(-largest, largest + 1)
        )
        assert accepted == 2 * math.floor(limit / spacing) + 1
        print(f"Rotor spacing {spacing:.2f}: {accepted} accepted states")

    # For 16 translated packets all Gram entries depend only on the index difference.
    nodes = 1024
    for difference in range(16):
        phases = (
            cmath.exp(2j * math.pi * difference * ((k + 0.5) / nodes - 0.5))
            for k in range(nodes)
        )
        overlap = sum(phases) / nodes
        assert abs(overlap - (difference == 0)) < 1e-13
    print("16 real-scalar momentum-band packets: orthonormal")

    def sinc(x):
        return math.sin(x) / x if x else 1.0

    probability = 2 / math.pi * simpson(lambda x: sinc(x) ** 2, 0, math.pi / 2)
    assert abs(probability - 0.77369501) < 5e-9
    print(f"Correct scalar-value bin probability: {probability:.8f}")

    def cosine_packet_density(x):
        amplitude = sinc(x + math.pi / 2) + sinc(x - math.pi / 2)
        return amplitude**2 / (2 * math.pi)

    probability = 2 * simpson(cosine_packet_density, 0, math.pi)
    assert abs(probability - 0.97009405) < 5e-9
    print(f"Finite-variance packet, double bin width: {probability:.8f}")


if __name__ == "__main__":
    main()
