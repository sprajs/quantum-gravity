"""Check the smooth interior-window estimate in audit/research-review.md.

Run from the repository root with python -B checks/clock_window.py.
The sampled lower estimates should lie below the oscillator ground energies.
"""

import cmath
import importlib.util
import math
from pathlib import Path


def sampled_window(panels, highest_frequency, epsilon, left, right):
    length = 1 - epsilon
    points = []
    for i in range(panels):
        v = epsilon + length * i / panels
        if left < v < right:
            angle = 2 * math.pi * (v - epsilon) / length
            window = math.sin(math.pi * (v - left) / (right - left)) ** 4
            points.append((v, angle, window))

    norm = sum(h * h for _, _, h in points) / panels
    divided_norm = sum((h / v) ** 2 for v, _, h in points) / panels
    transform = []
    divided_transform = []
    for n in range(highest_frequency + 1):
        terms = [h * cmath.exp(1j * n * angle) / panels for _, angle, h in points]
        transform.append(sum(terms))
        divided_transform.append(sum(term / v for term, (v, _, _) in zip(terms, points)))
    return norm, divided_norm, transform, divided_transform


def lower_estimate(cutoff, frequencies, epsilon, window_data):
    norm, divided_norm, transform, divided_transform = window_data
    length = 1 - epsilon
    kappa = 2 * math.pi / length
    gamma_squared = 1 / (2 * math.pi)
    vacuum = gamma_squared * sum(
        kappa**2 * k * norm + divided_norm / k for k in range(1, cutoff + 1)
    )

    def vacuum_fourier_norm(m):
        return gamma_squared * sum(
            abs(1j * kappa * k * transform[m + k] - divided_transform[m + k]) ** 2 / k
            for k in range(1, cutoff + 1)
        )

    # The exact remainder has infinitely many m. This is a numerical estimate.
    remainder = vacuum_fourier_norm(0) + 2 * sum(
        vacuum_fourier_norm(m) for m in range(1, frequencies + 1)
    )
    return length * (vacuum - remainder) / 4


def main():
    module_path = Path(__file__).with_name("fable-clock-sewing.py")
    spec = importlib.util.spec_from_file_location("periodic_clock", module_path)
    periodic = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(periodic)

    epsilon, left, right = 0.2, 0.28, 0.68
    cutoffs = [2, 4, 8]
    base_frequencies, check_frequencies = 119, 159
    base = sampled_window(2048, base_frequencies + max(cutoffs), epsilon, left, right)
    refined = sampled_window(4096, check_frequencies + max(cutoffs), epsilon, left, right)
    print("radial cutoff   window estimate   ground energy   refinement difference")
    for cutoff in cutoffs:
        estimate = lower_estimate(cutoff, base_frequencies, epsilon, base)
        check = lower_estimate(cutoff, check_frequencies, epsilon, refined)
        matrix = periodic.generator_matrix(cutoff, epsilon, right, 1.0, panels=3000)
        ground = periodic.zero_point(matrix)
        assert 0 < estimate < ground
        assert abs(estimate - check) < 1e-7
        print(f"{cutoff:13d}   {estimate:15.6f}   {ground:13.6f}   {abs(estimate - check):.2e}")


if __name__ == "__main__":
    main()
