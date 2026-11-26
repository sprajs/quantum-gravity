"""Independent checks for the spacetime dilation probe and opposite null faces."""

import cmath
import math


def simpson(function, lower, upper, panels):
    step = (upper - lower) / panels
    odd = sum(function(lower + index * step) for index in range(1, panels, 2))
    even = sum(function(lower + index * step) for index in range(2, panels, 2))
    return step * (function(lower) + function(upper) + 4 * odd + 2 * even) / 3


def conformal_einstein(t, amplitude, chi, dchi, ddchi):
    """Return G_00 and mixed spatial G^i_i of a diagonal Bianchi I metric."""
    powers = (-2 / 7, 3 / 7, 6 / 7)
    lapse = cmath.exp(amplitude * chi)
    expansion = [power / t + amplitude * dchi for power in powers]
    expansion_rate = [-power / t**2 + amplitude * ddchi for power in powers]
    result = []
    temporal = 0
    for j, k in ((1, 2), (2, 0), (0, 1)):
        temporal += expansion[j] * expansion[k]
        spatial = (expansion_rate[j] + expansion_rate[k] + expansion[j] ** 2
                   + expansion[k] ** 2 + expansion[j] * expansion[k]
                   - amplitude * dchi * (expansion[j] + expansion[k]))
        result.append(-spatial / lapse**2)
    return [temporal, *result]


def check_einstein_source():
    powers = (-2 / 7, 3 / 7, 6 / 7)
    step = 1e-25
    errors = []
    for t in (0.7, 1, 1.8):
        # A local jet of the cutoff suffices to test the source at an event.
        chi, dchi, ddchi = math.sin(t), math.cos(t), -math.sin(t)
        actual = conformal_einstein(t, 1j * step, chi, dchi, ddchi)
        expected = [2 * dchi / t]
        expected.extend(-2 * (ddchi + (1 - p) * dchi / t) for p in powers)
        errors.extend(abs(value.imag / step - target)
                      for value, target in zip(actual, expected))
    assert max(errors) < 1e-12


def check_torus_probe():
    def bump(t):
        return math.exp(-1 / (t * (1 - t))) if 0 < t < 1 else 0

    def weighted_derivative(t):
        if t in (0, 1):
            return 0
        return t * bump(t) * (1 - 2 * t) / (t * (1 - t))**2

    normalization = simpson(bump, 0, 1, 1200)
    value = simpson(weighted_derivative, 0, 1, 1200) / normalization
    assert abs(value + 1) < 1e-12
    return value


def check_cross_face_kernel():
    # Replace the light-cone delta by a Gaussian in its invariant argument.
    # The three root positions have a fixed separation from the angular poles.
    width = 0.004
    for r, s in ((0.7, 0.8), (0.65, 0.55), (0.3, 0.45)):
        def averaged_kernel(cosine):
            distance_squared = r**2 + s**2 - 2 * r * s * cosine
            interval = (2 - r - s)**2 - distance_squared
            delta = math.exp(-(interval / width)**2) / (math.sqrt(math.pi) * width)
            return delta / (4 * math.pi)

        value = simpson(averaged_kernel, -1, 1, 6000)
        expected = 1 / (8 * math.pi * r * s) if r + s > 1 else 0
        assert abs(value - expected) < 1e-12


if __name__ == "__main__":
    check_einstein_source()
    torus_probe = check_torus_probe()
    check_cross_face_kernel()
    print("Conformal Einstein source on Kasner: 12 components agree within 1e-12")
    print(f"Flat torus probe in units of V_0/(4 pi G): {torus_probe:.6f}")
    print("Opposite-face scalar kernel: 3 angular integrals agree within 1e-12")
