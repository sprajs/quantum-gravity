"""Reproduce the finite-cut boost example for the audit of section 5.2."""

import cmath
import math


def boost_response(copies, lower_multiplicity, rapidity, areas, weights):
    """Evaluate the expectation of a simultaneous flip on the doubled cut."""
    amplitudes = {}
    for area_label, count in enumerate((lower_multiplicity * copies, copies)):
        phase = cmath.exp(1j * rapidity * areas[area_label] / (2 * math.pi))
        for copy in range(count):
            amplitudes[area_label, copy] = math.sqrt(weights[area_label]) * phase
    overlap = sum(
        amplitude.conjugate() * amplitudes.get((1 - area_label, copy), 0j)
        for (area_label, copy), amplitude in amplitudes.items()
    )
    norm_squared = sum(abs(amplitude) ** 2 for amplitude in amplitudes.values())
    return (overlap / norm_squared).real, norm_squared


def main():
    areas = (1, 1 + 2 * math.pi)
    center = 2 + math.pi
    weights = [math.exp(-area - (area - center) ** 2 / 2) for area in areas]
    assert math.isclose(*weights)
    copies = 7
    for multiplicity in (1, 4, 40):
        original, norm_squared = boost_response(copies, multiplicity, 0, areas, weights)
        boosted, _ = boost_response(copies, multiplicity, 1, areas, weights)
        difference = boosted - original
        predicted = 2 * (math.cos(1) - 1) / (multiplicity + 1)
        assert math.isclose(difference, predicted, abs_tol=1e-12)
        assert math.isclose(norm_squared, weights[0] * (multiplicity + 1) * copies)
        print(f"k={multiplicity:2d}  rank={(multiplicity+1)*copies:3d}  "
              f"contrast={difference:.10f}  norm_squared={norm_squared:.10f}")


if __name__ == "__main__":
    main()
