"""Finite-cut two-copy return. Run python3 checks/purity_test.py from the root."""

import cmath
import math


def diagonal_purity(weights):
    return sum(weight**2 for weight in weights) / sum(weights) ** 2


def rank_constant(lower, upper):
    return (lower + upper) ** 2 / (4 * lower * upper)


def open_return(inputs, weights, arm_filter):
    """Compare the finite open Gram formula with a swap on the output density."""
    outputs = [
        [math.sqrt(weight) * amp * factor
         for amp, weight, factor in zip(vector, weights, arm_filter, strict=True)]
        for vector in inputs
    ]
    gram = [
        [sum(a.conjugate() * b for a, b in zip(u, v, strict=True)) for v in outputs]
        for u in outputs
    ]
    normalization = sum(row[i].real for i, row in enumerate(gram))
    ratio = sum(abs(entry) ** 2 for row in gram for entry in row) / normalization**2

    dimension = len(weights)
    density = [
        [sum(v[i] * v[j].conjugate() for v in outputs) / normalization
         for j in range(dimension)]
        for i in range(dimension)
    ]
    swap = sum(density[i][j] * density[j][i]
               for i in range(dimension) for j in range(dimension))
    assert cmath.isclose(swap, ratio, abs_tol=1e-13)
    return ratio, normalization / len(inputs)


def continuous_area_control():
    # x = exp(s) ranges over [1,3]. The center is s_b = 1/4 and sigma_s = 1.
    center = 0.25
    s_max = math.log(3)

    def one_copy_integral(left, right):
        return math.sqrt(math.pi / 2) * (
            math.erf((right - center) / math.sqrt(2))
            - math.erf((left - center) / math.sqrt(2))
        )

    one = one_copy_integral(0, s_max)
    # Completing the square in exp[-s-(s-center)^2] gives the cyclic integral.
    two = math.exp(0.25 - center) * math.sqrt(math.pi) / 2 * (
        math.erf(s_max - center + 0.5) - math.erf(0.5 - center)
    )
    regular = two / one**2
    lipschitz = 1 + s_max - center
    lower = math.exp(-s_max - (s_max - center) ** 2 / 2)
    upper = math.exp(-center**2 / 2)
    rank_four_ceiling = rank_constant(lower, upper) / 4
    assert rank_four_ceiling < 0.5 <= regular
    print(f"disk-weighted regular return = {regular:.6f}, "
          f"rank-four ceiling = {rank_four_ceiling:.6f}")
    for n in (8, 32, 128):
        width = 2 / n
        endpoints = [math.log(1 + j * width) for j in range(n + 1)]
        means = [one_copy_integral(left, right) / width
                 for left, right in zip(endpoints[:-1], endpoints[1:], strict=True)]
        measured = diagonal_purity(means)
        error = width * regular - measured
        bound = 2 * lipschitz**2 * width**3 / (12 * one**2)
        assert 0 < error < bound
        print(f"N={n:3}   full return = {measured:.8f}   "
              f"h R_reg - R = {error:.3e}   bound = {bound:.3e}")


def main():
    print("k   N   full swap    area-only swap")
    for k in (1, 4):
        for n in (8, 32):
            labels = [0] * (k * n) + [1] * n
            full = diagonal_purity([1] * len(labels))
            area_only = diagonal_purity([labels.count(0), labels.count(1)])
            assert math.isclose(full, 1 / ((k + 1) * n))
            assert math.isclose(area_only, (k**2 + 1) / (k + 1) ** 2)
            print(f"{k}  {n:2}   {full:.6f}     {area_only:.6f}")

    continuous_area_control()

    lower, upper = 0.25, 1.0
    endpoint_weights = [lower] * 4 + [upper]
    sharp = len(endpoint_weights) * diagonal_purity(endpoint_weights)
    assert math.isclose(sharp, rank_constant(lower, upper))
    print(f"sharp rR = {sharp:.6f}")

    # Two Fourier columns in the three-dimensional area basis mix all weights.
    omega = cmath.exp(2j * math.pi / 3)
    inputs = [[omega ** (j * k) / math.sqrt(3) for j in range(3)] for k in (0, 1)]
    weights = [lower, 0.5, upper]
    ratio, _ = open_return(inputs, weights, [1] * len(weights))
    assert math.isclose(ratio, 4 / 7)
    error = 0.01
    assert math.ceil(1 / (ratio + error)) == len(inputs)
    assert math.floor(sharp / (ratio - error)) == len(inputs)

    exact_filter = [math.sqrt(lower / weight) for weight in weights]
    calibrated, success = open_return(inputs, weights, exact_filter)
    assert math.isclose(calibrated, 1 / len(inputs))
    assert math.isclose(success, lower / upper)
    print(f"mixed cut R = {ratio:.6f}, calibrated R = {calibrated:.6f}, "
          f"success = {success:.6f}")

    delta = 0.05
    errors = [-delta, 0, delta]
    imperfect = [f * (1 + e) for f, e in zip(exact_filter, errors, strict=True)]
    measured, _ = open_return(inputs, weights, imperfect)
    ceiling = 1 + 4 * delta**2 / (1 - delta**2) ** 2
    assert 1 < len(inputs) * measured < ceiling
    # These endpoint multiplicities attain the sharp 5 percent calibration bound.
    perturbed = [(1 - delta)**2] * 441 + [(1 + delta)**2] * 361
    assert math.isclose(len(perturbed) * diagonal_purity(perturbed), ceiling)
    print(f"5% filter error gives rR = {len(inputs) * measured:.6f}, "
          f"ceiling = {ceiling:.6f}")

    for r in (2, 8, 32):
        tail = 2.0**-r
        decaying = diagonal_purity([2.0**-j for j in range(1, r + 1)])
        assert math.isclose(decaying, (1 + tail) / (3 * (1 - tail)))


if __name__ == "__main__":
    main()
