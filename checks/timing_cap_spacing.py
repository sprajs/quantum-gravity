"""Integrate the finite-width bracket as two calibrated spherical caps approach."""

from fractions import Fraction as F
from math import prod

from timing_caps import bracket, sections
from weak_clock_contact import integrate, product


def integration_rule(order):
    """Integrate degree < order exactly; interior nodes avoid jump values."""
    nodes = [F(2*i+1, 2*order) for i in range(order)]
    rule = []
    for x in nodes:
        polynomial = {0: F(1)}
        others = [y for y in nodes if y != x]
        for y in others:
            polynomial = product(polynomial, {0: -y, 1: F(1)})
        weight = integrate(polynomial, F(0), F(1)) / prod(x-y for y in others)
        rule.append((x, weight))
    return rule


def averaged_bracket(ratio, width, rule):
    outer = F(1, 2)
    slope = {4: F(152, 3), 5: F(-208, 3)}
    inner_profile = sections(slope, outer-ratio*width)
    outer_profile = sections(slope, outer)
    knots = sorted({F(-1), F(0), F(1), max(F(-1), -2*ratio)})
    total = F(0)
    for left, right in zip(knots, knots[1:]):
        for node, weight in rule:
            delay_units = left+(right-left)*node
            value = bracket(inner_profile, outer_profile, width*delay_units)
            total += (right-left)*weight*(1-abs(delay_units))*value
    return total


def main():
    rule = integration_rule(14)
    assert all(sum(w*x**n for x,w in rule) == F(1,n+1) for n in range(14))
    for ratio in (F(0), F(1,8), F(1,4), F(3,4)):
        expected = 1-max(F(0), 1-2*ratio)**2
        errors = []
        for width in (F(1,10**4), F(1,10**6)):
            normalized = averaged_bracket(ratio, width, rule) / F(3,160)
            errors.append(abs(normalized-expected))
        assert errors[-1] < F(1,1000)
        assert errors[-1] <= errors[0] / 50
        print(f"Cap spacing / timing width {ratio}: normalized bracket "
              f"{float(normalized):.8f} at width 1e-6, sharp limit {expected}")


if __name__ == "__main__":
    main()
