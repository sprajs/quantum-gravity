"""Reproduce the positive smoothed-clock example in audit/clock-construction.md."""

import cmath
import math


def variance_bound(epsilon, entropy, radial_ratio, angular_ratio):
    """Geometric sums include every radial mode and both tensor polarizations."""
    radial_sum = 1 / (1 - radial_ratio**2) ** 2
    q = angular_ratio**2
    angular_sum = 2 * (5 / (1 - q) + 2 * q / (1 - q) ** 2)
    kappa = 2 * math.pi / (1 - epsilon)
    return angular_sum * radial_sum * kappa**2 * math.log(1 / epsilon) / (4 * entropy)


def simpson(values, step):
    return step / 3 * (values[0] + values[-1] + 4 * sum(values[1:-1:2])
                       + 2 * sum(values[2:-1:2]))


def check_pinned_mode(epsilon, upper, mode):
    """Test the integrated variance identity at an interior and a full cut."""
    angular_frequency = 2 * math.pi * mode / (1 - epsilon)
    panels = 4096
    step = (upper - epsilon) / panels
    measured = []
    correction = []
    for index in range(panels + 1):
        radius = epsilon + index * step
        phase = cmath.exp(1j * angular_frequency * (radius - epsilon))
        amplitude = phase - 1
        derivative = 1j * angular_frequency * phase
        measured.append(abs(derivative - amplitude / radius) ** 2 / radius)
        correction.append(abs(amplitude) ** 2 / radius**3)
    upper_bound = angular_frequency**2 * math.log(upper / epsilon)
    endpoint = abs(cmath.exp(1j * angular_frequency * (upper - epsilon)) - 1) ** 2 / upper**2
    direct = simpson(measured, step)
    assert direct < upper_bound
    assert math.isclose(direct, upper_bound - endpoint - simpson(correction, step),
                        rel_tol=1e-10)


def moment_sums(c, d):
    """Use the exact Fock recurrence for X=c(a+a*)^2+d[i(a*-a)]^2."""
    variance = c + d
    mean_values = []
    for occupation in (0, 1):
        vector = {occupation: 1.0}
        denominator = 1
        exponential_mean = 1.0
        for order in range(1, 29):
            next_vector = {}
            for level, amplitude in vector.items():
                transitions = [(level, variance * (2 * level + 1)),
                               (level + 2, (c - d) * math.sqrt((level + 1) * (level + 2)))]
                if level >= 2:
                    transitions.append((level - 2, (c - d) * math.sqrt(level * (level - 1))))
                for destination, coefficient in transitions:
                    next_vector[destination] = (next_vector.get(destination, 0.0)
                                                + amplitude * coefficient)
            vector = next_vector
            denominator *= order
            exponential_mean += vector[occupation] / denominator
        mean_values.append(exponential_mean)
    return mean_values


def main():
    epsilon = 0.25
    for upper in (0.61, 1.0):
        for mode in (1, 3, 7):
            check_pinned_mode(epsilon, upper, mode)
    # A single quadrature saturates both Wick bounds.
    for c, d in ((0.08, 0.0), (0.06, 0.02)):
        variance = c + d
        vacuum, excited = moment_sums(c, d)
        vacuum_bound = (1 - 2 * variance) ** -0.5
        excess_bound = 2 * variance * (1 - 2 * variance) ** -1.5
        if d == 0:
            assert math.isclose(vacuum, vacuum_bound, abs_tol=1e-13)
            assert math.isclose(excited - vacuum, excess_bound, abs_tol=1e-13)
        else:
            assert vacuum < vacuum_bound and abs(excited - vacuum) < excess_bound

    variance = variance_bound(epsilon, 10000, 0.5, 0.5)
    mean_bound = (1 - 2 * variance) ** -0.5
    window = 1.2
    acceptance = (window - mean_bound) / (window - 1)
    offset = 2 * variance * (1 - 2 * variance) ** -1.5 / (window - 1)
    assert 0 < variance < 0.5 and 0 < acceptance < 1
    print(f"integrated variance upper bound    {variance:.8f}")
    print(f"vacuum mean / u0 upper bound       {mean_bound:.8f}")
    print(f"vacuum acceptance lower bound      {acceptance:.8f}")
    print(f"rank lower bound at M=100          {math.ceil(100 * acceptance - offset)}")


if __name__ == "__main__":
    main()
