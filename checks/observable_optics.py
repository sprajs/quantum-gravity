#!/usr/bin/env python3
"""Check the exact plane-wave screen and finite-cap results in observable-optics.md."""

from decimal import Decimal as D, localcontext
from math import cos, cosh, pi, sin, sinh, sqrt


def axis(parameter, distance):
    """Solve J'' = parameter * J with J(0)=0, J'(0)=1, in units of L."""
    argument = parameter * distance**2
    term = D(1)
    axis_ratio = D(1)
    slope = D(1)
    for order in range(1, 50):
        term *= argument / ((2 * order) * (2 * order + 1))
        axis_ratio += term
        slope += (2 * order + 1) * term
    return distance * axis_ratio, slope


def screen(parameter, distance):
    jx, dx = axis(parameter, distance)
    jy, dy = axis(-parameter, distance)
    radius = (jx * jy).sqrt()
    return radius, (dx * jy + dy * jx) / (2 * radius), (jx - jy) / (jx + jy)


def verify_cap(parameter, epsilon):
    """Locate the cap by its measured area and compare its clock with flat space."""
    radius, _, _ = screen(parameter, D(1))
    lower, upper = D(0), D(1)
    for _ in range(140):
        middle = (lower + upper) / 2
        if screen(parameter, middle)[0] < epsilon * radius:
            lower = middle
        else:
            upper = middle
    cap = (lower + upper) / 2
    _, slope, _ = screen(parameter, cap)
    excess = slope * (1 - cap) - (1 - epsilon) * radius
    coefficient = (1 - 5 * epsilon**4 + 4 * epsilon**5) / 180
    assert abs(excess / parameter**2 - coefficient) < D("1e-13")
    return excess / parameter**2


def increasing_root(function, upper):
    lower = 0.0
    for _ in range(52):
        middle = (lower + upper) / 2
        if function(middle) < 0:
            lower = middle
        else:
            upper = middle
    return (lower + upper) / 2


def diamond_excess(parameter, epsilon):
    """Intersect the two exact cones in units L=1 and average over launch angles."""
    k = sqrt(parameter)

    def radii(u):
        return sinh(k * u) / k, sin(k * u) / k

    def area_radius(u):
        sx, sy = radii(u)
        return sqrt(sx * sy)

    end_x, end_y = radii(1)
    mean_radius = mean_square_radius = weighted_clock = 0.0
    # Three Gaussian nodes integrate all powers up to beta^5 on [0,1].
    offset = sqrt(3 / 5) / 2
    for beta, weight in [(0.5 - offset, 5/18), (0.5, 4/9), (0.5 + offset, 5/18)]:
        for angle in range(8):
            phi = angle * pi / 4
            nx2 = 4 * beta * (1 - beta) * cos(phi)**2
            ny2 = 4 * beta * (1 - beta) * sin(phi)**2

            def cone_difference(u):
                sx, sy = radii(u)
                rx, ry = radii(1 - u)
                return nx2 * sx * end_x / rx + ny2 * sy * end_y / ry - 4 * beta**2

            waist = increasing_root(cone_difference, 1.0)
            radial = area_radius(waist)
            cap = increasing_root(lambda u: area_radius(u) - epsilon * radial, waist)
            sx, sy = radii(cap)
            slope = (cosh(k * cap) * sy + cos(k * cap) * sx) / (2 * area_radius(cap))
            clock = slope * (waist - cap) / beta
            distance = radial / beta
            mean_radius += weight / 8 * distance
            mean_square_radius += weight / 8 * distance**2
            weighted_clock += weight / 8 * distance * clock

    average_clock = weighted_clock / mean_radius
    focus = average_clock - (1 - epsilon) * mean_square_radius / mean_radius
    total = average_clock - (1 - epsilon) * sqrt(mean_square_radius)
    return focus / parameter**2, total / parameter**2


def main():
    with localcontext() as context:
        context.prec = 84   # The laboratory area-distance deficit is of order 1e-52.
        weak = D("1e-5")
        radius, _, ellipticity = screen(weak, D(1))
        deficit = 1 - radius
        assert abs(ellipticity / weak - D(1) / 6) < D("1e-12")
        assert abs(deficit / weak**2 - D(1) / 180) < D("1e-13")
        assert abs(deficit / ellipticity**2 - D("0.2")) < D("1e-11")
        print(f"weak-profile deficit/ellipticity^2 = {deficit / ellipticity**2:.12f}")
        for epsilon in map(D, ["0.1", "0.5", "0.9"]):
            coefficient = verify_cap(weak, epsilon)
            print(f"cap fraction {epsilon}: normalized clock excess = {coefficient:.12f}")

        radius, _, ellipticity = screen(D(1), D(1))
        print(f"unit profile: D/L = {radius:.9f}, ellipticity = {ellipticity:.9f}")
        light_speed, frequency, strain, length = map(D, ["299792458", "100", "1e-21", "4000"])
        tidal = 2 * strain * (2 * D(str(pi)) * frequency / light_speed)**2
        radius, _, ellipticity = screen(tidal * length**2, D(1))
        print(f"laboratory: q = {tidal:.5E} m^-2, ellipticity = {ellipticity:.5E}")
        print(f"            1-D/L = {1-radius:.5E}, L-D = {(1-radius)*length:.5E} m")

    epsilon = 0.5
    focus, total = diamond_excess(0.0125, epsilon)
    focus_expected = (1 - 5 * epsilon**4 + 4 * epsilon**5) / 900
    total_expected = focus_expected + (1 - epsilon) / 1080
    assert abs(focus - focus_expected) < 1e-8
    assert abs(total - total_expected) < 1e-8
    print(f"full diamond at cap fraction 0.5: focus = {focus:.8f}, total = {total:.8f}")


if __name__ == "__main__":
    main()
