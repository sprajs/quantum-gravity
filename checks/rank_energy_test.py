"""Check the sharp weighted clock estimate and the polarized comparison spectrum."""

from math import atan, cos, exp, log, pi, sin, sqrt


def clock_minimum(energy):
    if energy <= 1:
        return 1 + energy**2
    return 2 * exp(energy - 1)


def sharp_scalar_examples():
    # Integrate in r = sqrt((1-v)/d).  The logarithmic endpoint is integrable.
    # r = u^2 gives an ordinary midpoint rule with error O(log(N)/N^2).
    steps = 8192
    for parameter in (0.25, 0.8, 1.0, 2.0):
        energy = 0.0
        clock = 0.0
        for index in range(steps):
            u = (index + 0.5) / steps
            r = u**2
            focusing = max(0.0, log(parameter / r))
            energy += 2 * u * focusing / steps
            clock += 4 * r * u * exp(focusing) / steps
        assert abs(clock - clock_minimum(energy)) < 5e-7
        print(f"Scalar t={parameter:.2f}: E={energy:.6f}, T/(dM)={clock:.6f}")
    for eta in (0.1, 0.01, 0.0001, 1e-8):
        energy = 1 - sqrt(eta) * atan(1 / sqrt(eta))
        clock = 2 * sqrt(1 + eta) / (sqrt(1 + eta) + sqrt(eta))
        assert 2 * energy < clock
    print(f"Smooth endpoint regularization: E/[T/(dM)]={energy / clock:.6f}")


def matrix_exp_expectation(matrix, vector):
    """Spectral formula for a real symmetric two by two matrix."""
    a, b, c = matrix
    x, y = vector
    mean = (a + c) / 2
    gap = sqrt(((a - c) / 2) ** 2 + b**2)
    norm = x**2 + y**2
    if not gap:
        return exp(mean) * norm
    signed = ((a - mean) * x**2 + 2 * b * x * y + (c - mean) * y**2) / gap
    return (exp(mean + gap) * (norm + signed) + exp(mean - gap) * (norm - signed)) / 2


def two_cell_test():
    # In each cell Xi=s*A+s^2*B, s=(v-epsilon)/d.  Both A and B are positive.
    # The two diagonal area densities have squared sum 5*I.
    cells = [
        ((1.0, 0.0, 0.0), (0.5, 0.5, 0.5), (2.0, sqrt(2.5))),
        ((1.0, -1.0, 1.0), (0.25, 0.0, 0.0), (1.0, sqrt(2.5))),
    ]
    min_margin = float("inf")
    min_joint_margin = float("inf")
    round_density = sqrt(2.5)
    steps = 512
    for direction in range(17):
        theta = direction * pi / 17
        mass = energy = clock = 0.0
        weak_clock = density_variance = 0.0
        for first, second, density in cells:
            x = density[0] * cos(theta) / sqrt(3)
            y = density[1] * sin(theta) / sqrt(2 * sqrt(2.5))
            mass += x**2 + y**2
            density_variance += (
                ((density[0] / round_density - 1) * cos(theta)) ** 2
                + ((density[1] / round_density - 1) * sin(theta)) ** 2
            ) / 2
            for matrix, factor in ((first, 2 / 3), (second, 8 / 15)):
                a, b, c = matrix
                energy += factor * (a * x**2 + 2 * b * x * y + c * y**2)
            for index in range(steps):
                s = (index + 0.5) / steps
                matrix = tuple(s * a + s**2 * b for a, b in zip(first, second))
                clock += matrix_exp_expectation(matrix, (x, y)) / steps
                weak_matrix = tuple(value / 10 for value in matrix)
                weak_clock += matrix_exp_expectation(weak_matrix, (x, y)) / steps
        margin = clock / mass - clock_minimum(energy / mass)
        assert margin > 0.05
        min_margin = min(min_margin, margin)
        delta = weak_clock / round_density - 1
        assert 0 < delta < 1
        joint_margin = delta - (energy / (10 * mass)) ** 2 - (1 + delta) * density_variance / 2
        assert joint_margin > 0
        min_joint_margin = min(min_joint_margin, joint_margin)
    print(f"Near-minimum joint budget: minimum sampled margin={min_joint_margin:.6f}")
    print(f"Noncommuting two-cell example: minimum sampled margin={min_margin:.6f}")


def radial_pairs():
    epsilon = 0.25
    d = 1 - epsilon
    length = 2 * d
    steps = 256
    labels = [(n, phase) for n in range(1, 9) for phase in (0, 1)]
    modes = []
    for n, phase in labels:
        k = 2 * pi * n / length
        values = []
        for index in range(steps):
            t = (index + 0.5) * length / steps
            scale = sqrt(2 / length)
            if phase == 0:
                values.append((scale * (1 - cos(k * t)) / k, scale * sin(k * t)))
            else:
                values.append((scale * sin(k * t) / k, scale * cos(k * t)))
        modes.append(values)
    for i, first in enumerate(modes):
        for j, second in enumerate(modes):
            energy = pairing = 0.0
            for (x, dx), (y, dy) in zip(first, second):
                energy += dx * dy * length / steps
                pairing += (dx * y - dy * x) * length / steps
            n, phase = labels[i]
            expected = 0.0
            if n == labels[j][0] and phase != labels[j][1]:
                expected = (1 - 2 * phase) * length / (pi * n)
            assert abs(energy - float(i == j)) < 1e-12
            assert abs(pairing - expected) < 1e-12
    print("Eight radial oscillator pairs: energy and all symplectic entries agree.")


if __name__ == "__main__":
    sharp_scalar_examples()
    two_cell_test()
    radial_pairs()
