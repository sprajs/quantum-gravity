"""Open clock-filtered source bounds. Run python3 checks/sewing_repair.py."""

import math


def rectangular_cut_errors(levels, seed, keep_levels, keep_copies):
    """Worst omitted norm for full contractions and for independent copy blocks."""
    omitted_per_copy = []
    for copy in range(len(seed)):
        omitted_weights = [
            2.0 ** -level
            for level in range(levels)
            if level >= keep_levels or copy >= keep_copies
        ]
        omitted_per_copy.append(max(omitted_weights, default=0.0))

    # Block contractions can direct their own seed component into its best level.
    restricted = math.sqrt(sum(
        abs(coefficient * weight) ** 2
        for coefficient, weight in zip(seed, omitted_per_copy, strict=True)
    ))
    # A full contraction can direct the entire normalized seed into any one level.
    return restricted, max(omitted_per_copy)


def main():
    levels = 12
    threshold = 2.0 ** -4
    print(f"clock cutoff 4, required error < {threshold:.6f}")

    for keep_levels in (4, 5):
        restricted, full = rectangular_cut_errors(levels, [1.0], keep_levels, 1)
        assert restricted == full == 2.0 ** -keep_levels
        assert (full < threshold) == (keep_levels >= 5)
        print(f"one copy, retain {keep_levels} levels: error {full:.6f}")

    keep_levels = keep_copies = 5
    omitted_copy_probability = 4.0 ** -keep_copies
    continuum = math.sqrt(
        (1 - omitted_copy_probability) * 4.0 ** -keep_levels + omitted_copy_probability
    )

    for copies in (6, 10, 24):
        norm = math.sqrt(1 - 4.0 ** -copies)
        seed = [math.sqrt(3.0) * 2.0 ** -k / norm for k in range(1, copies + 1)]
        assert math.isclose(sum(coefficient**2 for coefficient in seed), 1.0)
        restricted, full = rectangular_cut_errors(levels, seed, keep_levels, keep_copies)
        tail = (omitted_copy_probability - 4.0 ** -copies) / norm**2
        assert math.isclose(restricted**2, (1 - tail) * 4.0 ** -keep_levels + tail)
        assert restricted <= continuum < threshold < full
        assert full == 1.0
    assert math.isclose(restricted, continuum, abs_tol=1e-12)
    print(f"5 by 5 cut, restricted-source error {continuum:.8f}, full-source error {full:.1f}")


if __name__ == "__main__":
    main()
