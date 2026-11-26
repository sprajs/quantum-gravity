"""Exact polynomial tests of the spherical clock's weak master inverse."""
from fractions import Fraction as Q
from math import comb, factorial

from joint_spherical_hessian import falling


CAP = Q(1, 3)
HALF_WIDTH = Q(1, 12)
# The optical slope Lz=sum c*t^(-p)*d^k z/dt^k.
SLOPE = ((5, 1, Q(1, 16)), (4, 2, Q(-5, 16)),
         (3, 3, Q(3, 4)), (2, 4, Q(-3, 4)))
OMEGA = Q(3, 5120)  # G_N=1; s profile, first-slot response.


def reference_weight(power):
    """Coefficients of b(t)/t^power=81*t^(5-power)*(1-t), in x=t-a."""
    terms = {}
    for degree, scale in ((5 - power, 81), (6 - power, -81)):
        for j in range(degree + 1):
            terms[j] = terms.get(j, 0) + scale * comb(degree, j) * CAP ** (degree - j)
    return terms


def left_primitive():
    """Integrate L_t[(s-t)^8/8!] against 256*b(t) from a to s."""
    coeff = {}
    for order, power, slope in SLOPE:
        q = 8 - order
        for j, term in reference_weight(power).items():
            degree = j + q + 1
            # Integral of (t-a)^j (s-t)^q/q! is j!*(s-a)^degree/degree!.
            factor = 256 * (-1) ** order * slope * Q(factorial(j), factorial(degree))
            coeff[degree] = coeff.get(degree, 0) + factor * term
    return coeff


def test_profile(extra_power):
    """x^extra_power (1-x^2/h^2)^12 on |x|<h, extended by zero."""
    return {extra_power + 2 * j: (-1) ** j * comb(12, j) / HALF_WIDTH ** (2 * j)
            for j in range(13)}


def integral_against_derivative(coeff, test, order):
    """Integrate one polynomial times a derivative of another over 0<x<h."""
    total = Q(0)
    for j, left in coeff.items():
        for k, right in test.items():
            if k >= order:
                degree = j + k - order
                moment = HALF_WIDTH ** (degree + 1) / (degree + 1)
                total += left * right * falling(k, order) * moment
    return total


def check():
    # For f_W=(18/175)*s^10 on the overlap, Lf_W=81*s^4 and Lf_W(a)=1.
    slope = sum(c * falling(10, k) for k, _, c in SLOPE) * Q(18, 175)
    assert slope == 81 and slope * CAP**4 == 1
    response = left_primitive()
    assert min(response) == 4
    jump = factorial(4) * response[4]
    assert jump == -16 * (1 - CAP)
    # Away from the rim the ninth derivative still has a nonzero bulk term.
    assert factorial(9) * response[9] == 256 * 1701
    print(f"Unit-slope jump of fourth master derivative = {jump} (G_N=1)")
    for extra_power in (0, 6):
        test = test_profile(extra_power)
        # Direct optical Hessian versus pairing the constructed field against Z^(9).
        clock = Q(3, 20) * sum(c * integral_against_derivative(reference_weight(p), test, k)
                                for k, p, c in SLOPE)
        adm = -OMEGA * integral_against_derivative(response, test, 9)
        assert adm == clock and clock != 0
        print(f"Master pairing / optical Hessian, test with x^{extra_power} = {adm / clock}")

    # A shrinking strain-normalized pulse has f_Z''''(a)=16a.
    single = OMEGA * jump * 16 * CAP
    assert single == Q(-1, 30)
    # Lf_W=x^5+O(x^6) gives b(t)/t=(1-a)x^5+O(x^6).
    # Only the kernel's (s-t)^3/3! term contributes to the order-nine jet.
    ninth_jump = -16 * (1 - CAP) * factorial(5)
    double = OMEGA * ninth_jump
    assert ninth_jump == -1280 and double == Q(-3, 4)
    print(f"Single rim pulse limit = {single}")
    print(f"Opposed unit-mass pulses, ninth derivative jump = {ninth_jump}, limit = {double}")


if __name__ == "__main__":
    check()
