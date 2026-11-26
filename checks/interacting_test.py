#!/usr/bin/env python3
"""Solve the two-wave vacuum characteristic problem in audit/interacting-test.md."""

from math import exp, pi, sin


def profile(x):
    return sin(pi * x) ** 4


def profile_slope(x):
    return pi * (sin(2 * pi * x) - sin(4 * pi * x) / 2)


def incoming_radius(amplitude, cells):
    """Integrate the affine null constraint by fourth-order Runge--Kutta."""
    step = 1 / cells
    radius, slope = 1.0, 0.0
    radii = [radius]
    for i in range(cells):
        x = i * step
        k_left = (amplitude * profile_slope(x) / 2) ** 2
        k_mid = (amplitude * profile_slope(x + step / 2) / 2) ** 2
        k_right = (amplitude * profile_slope(x + step) / 2) ** 2
        a1 = -k_left * radius
        s2 = slope + step * a1 / 2
        a2 = -k_mid * (radius + step * slope / 2)
        s3 = slope + step * a2 / 2
        a3 = -k_mid * (radius + step * s2 / 2)
        s4 = slope + step * a3
        a4 = -k_right * (radius + step * s3)
        radius += step * (slope + 2 * s2 + 2 * s3 + s4) / 6
        slope += step * (a1 + 2 * a2 + 2 * a3 + a4) / 6
        assert radius > 0
        radii.append(radius)
    return radii


def interaction(pump, probe, cells):
    """March the full finite-amplitude polarization equation on null rectangles."""
    area_u = [r * r for r in incoming_radius(pump, cells)]
    area_v = [r * r for r in incoming_radius(probe, cells)]
    previous = [probe * profile(j / cells) for j in range(cells + 1)]
    previous_lapse = [0.0] * (cells + 1)
    assert min(area_u) + min(area_v) > 1
    for i in range(cells):
        current = [pump * profile((i + 1) / cells)]
        current_lapse = [0.0]
        delta_u = area_u[i + 1] - area_u[i]
        for j in range(cells):
            southwest, north, east = previous[j], previous[j + 1], current[j]
            delta_v = area_v[j + 1] - area_v[j]
            area_mid = (area_u[i] + area_u[i + 1] + area_v[j] + area_v[j + 1]) / 2 - 1
            denominator = 2 * area_mid + (delta_u + delta_v) / 2
            change = -(delta_u * (north - southwest) + delta_v * (east - southwest)) / denominator
            current.append(north + east - southwest + change)
            strain_u = east - southwest + change / 2
            strain_v = north - southwest + change / 2
            lapse_change = (strain_u * strain_v - delta_u * delta_v / area_mid**2) / 2
            current_lapse.append(previous_lapse[j + 1] + current_lapse[j] - previous_lapse[j] + lapse_change)
        previous = current
        previous_lapse = current_lapse
    j = cells // 2
    area = area_u[-1] + area_v[j] - 1
    log_area_slope = (area_v[j + 1] - area_v[j - 1]) * cells / (2 * area)
    lapse_slope = (current_lapse[j + 1] - current_lapse[j - 1]) * cells / 2
    strain_slope = (current[j + 1] - current[j - 1]) * cells / 2
    strain_second = (current[j + 1] - 2 * current[j] + current[j - 1]) * cells**2
    tidal = -exp(2 * current_lapse[j]) * (strain_second + (lapse_slope + log_area_slope) * strain_slope)
    return current[j], tidal


def probe_gains(pump, probe, cells):
    plus = interaction(pump, probe, cells)
    minus = interaction(pump, -probe, cells)
    strain = (plus[0] - minus[0]) / (2 * probe)
    tidal = (plus[1] - minus[1]) / (2 * probe * 4 * pi**2)
    return strain, tidal


def cubic_coefficient(cells):
    def estimate(pump):
        return (probe_gains(pump, 0.001, cells)[0] - 1) / pump**2

    return (4 * estimate(0.02) - estimate(0.04)) / 3


def main():
    pump, probe = 0.35, 0.001
    cells = 160
    gain, tidal = probe_gains(pump, probe, cells)
    coarse_tidal = probe_gains(pump, probe, cells // 2)[1]
    tidal_extrapolated = (4 * tidal - coarse_tidal) / 3
    predicted = 1 / incoming_radius(pump, 2 * cells)[-1]
    assert abs(gain - predicted) < 3e-6
    assert abs(tidal_extrapolated - predicted) < 3e-6
    assert abs(probe_gains(0.0, probe, 40)[0] - 1) < 1e-12
    expected = 5 * pi**2 / 64
    for n in (80, cells):
        coefficient = cubic_coefficient(n)
        assert abs(coefficient - expected) < 1e-6
        print(f"{n} cells per side: cubic strain coefficient = {coefficient:.8f}")
    print(f"analytic cubic coefficient = {expected:.8f}")
    print(f"pump 0.35: two-wave probe gain = {gain:.8f}, linear-probe prediction = {predicted:.8f}")
    print(f"pump 0.35: extrapolated tidal gain = {tidal_extrapolated:.8f}")


if __name__ == "__main__":
    main()
