"""Check the fluctuating corner bounds in audit/fluctuating-corner-state.md."""

import math

from clock_construction import variance_bound


def shape_bounds(delta, variance):
    low = math.exp(-delta)
    high = math.exp(delta) * math.cosh(delta)

    def moment(q):
        return 1 / math.sqrt(1 - 2 * variance * q)

    chord = ((high - 1) * moment(low) + (1 - low) * moment(high)) / (high - low)
    return low, high, math.cosh(delta / 2), chord


def check_shape(values, weights, delta, variance):
    """Evaluate the actual corner sandwich and compare with the analytic bounds."""
    assert math.isclose(sum(weights), 1)
    assert abs(sum(value * mass for value, mass in zip(values, weights))) < 1e-12
    low, high, corner_bound, chord = shape_bounds(delta, variance)
    total = sum(mass * math.exp(value) for value, mass in zip(values, weights))
    density = [math.exp(value) / total for value in values]
    rho = [math.sqrt(value) for value in density]  # round radius is one
    a = 4 * math.pi * sum(mass * radius for mass, radius in zip(weights, rho))
    corner = 4 * math.pi / a
    assert 1 - 1e-14 <= corner <= corner_bound + 1e-14
    q = [1 / value for value in density]
    assert all(low - 1e-14 <= value <= high + 1e-14 for value in q)
    assert math.isclose(sum(mass * w * s for mass, w, s in zip(weights, density, q)), 1)
    wick = [1 / math.sqrt(1 - 2 * variance * value) for value in q]
    sandwich = 4 * math.pi * sum(mass * (radius / math.sqrt(a))**2 * cost
                                 for mass, radius, cost in zip(weights, rho, wick))
    assert sandwich <= corner * chord + 1e-14
    return corner, sandwich


def check_cutoff_floor():
    """Place almost all area on a shrinking patch and vary cap and prefix scales."""
    late_fraction = 0.5
    for prefix, cap in ((4, 2), (128, 10), (12, 64), (1024, 48)):
        capped_cost = 1 + late_fraction * math.expm1(cap)
        bound = 1 / math.sqrt(1 / capped_cost + 1 / (late_fraction * math.e * prefix))
        for fraction in (1 / prefix, 0.125, 0.5):
            low = math.exp(-2 * cap)
            high = (1 - (1 - fraction) * low) / fraction
            populations = [(fraction, high), (1 - fraction, low)]
            normalizer = sum(p * math.sqrt(w) for p, w in populations)
            total = sum(p * w * (1 + late_fraction * math.expm1(min(prefix / w, cap)))
                        for p, w in populations)
            assert total / normalizer >= bound


def main():
    delta = 0.5
    variance = variance_bound(0.25, 10000, 0.5, 0.5)
    _, high, corner_bound, chord = shape_bounds(delta, variance)
    check_shape([0.5, -0.5], [0.5, 0.5], delta, variance)
    check_shape([0.5, -0.125], [0.2, 0.8], delta, variance)
    check_shape([0], [1], delta, variance)

    # f=delta*cos(theta). The mean shape factors are known by integration.
    panels = 4096
    dipole = [delta * ((2 * i + 1) / panels - 1) for i in range(panels)]
    corner, _ = check_shape(dipole, [1 / panels] * panels, delta, variance)
    exact = math.sqrt(math.sinh(delta) / delta) / (math.sinh(delta / 2) / (delta / 2))
    assert math.isclose(corner, exact, rel_tol=1e-8)
    assert math.isclose(exact**2, delta / (2 * math.tanh(delta / 2)))
    check_cutoff_floor()

    for j in range(2, 501):
        term = (2 * j + 1) / (1 + j * (j + 1))**2
        assert term <= 1 / j**2 - 1 / (j + 1)**2
    rms_bound = (1 / 3 + 1 / 4) / math.sqrt(4 * math.pi)
    event = 1 - (rms_bound / delta)**2
    window = 1.2
    conditional = (window - corner_bound * chord) / (window - corner_bound)
    assert 0 < event < 1 and 0 < conditional < 1
    assert conditional * event >= 0.47806146

    print(f"largest conditional prefix variance  {variance * high:.8f}")
    print(f"corner normalization upper bound     {corner_bound:.8f}")
    print(f"conditional mean / u0 upper bound    {corner_bound * chord:.8f}")
    print(f"conditional acceptance lower bound   {conditional:.8f}")
    print(f"shape event probability lower bound  {event:.8f}")
    print(f"full vacuum acceptance lower bound   {conditional * event:.8f}")


if __name__ == "__main__":
    main()
