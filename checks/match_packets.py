"""Quadrupole packets on opposite sides of a spherical cap. Standard library."""

from fractions import Fraction
from math import comb, factorial, fsum, isclose

from joint_spherical_hessian import falling, optical_mode, simpson


CAP = Fraction(1, 3)
POWER = 12
NORMALIZATION = factorial(2 * POWER + 1) / (2 ** (2 * POWER + 1) * factorial(POWER) ** 2)


def bump(x, order=0):
    """A unit-mass bell in x, differentiated before evaluating it."""
    if abs(x) >= 1:
        return 0.0
    terms = []
    for j in range(order + 1):
        k = order - j
        terms.append(comb(order, j) * (-1) ** j * falling(POWER, j) * falling(POWER, k)
                     * (1 - x) ** (POWER - j) * (1 + x) ** (POWER - k))
    return NORMALIZATION * fsum(terms)


def packet(s, width, side):
    """F(2s) has signed unit mass in s; the jets differentiate in u=2s."""
    x = (s - float(CAP)) / width - 2 * side
    return [side * bump(x, j) / (width * (2 * width) ** j) for j in range(7)]


def reference(s, n=0):
    # This polynomial is multiplied by a smooth cutoff equal to one near the cap.
    # The leading slope is (s-a)^(n+5).
    degree = n + 10
    scale = float(CAP) / ((n + 6) * 2 ** (n + 6) * falling(degree, 4))
    u_offset = 2 * (s - float(CAP))
    return [scale * falling(degree, j) * u_offset ** (degree - j) for j in range(7)]


def hessian(width, n=0):
    def clock_integrand(x):
        s = float(CAP) + width * (2 + x)
        trial_slope = optical_mode(s, packet(s, width, 1))[1]
        reference_slope = optical_mode(s, reference(s, n))[1]
        return (3 / 20) * width * s * (1 - s) * trial_slope * reference_slope

    return simpson(clock_integrand, -1, 1, pieces=1000)


def check():
    assert isclose(simpson(bump, -1, 1), 1.0, abs_tol=1e-12)
    # After integrating by parts, only the leading fourth derivative of
    # -[s(1-s)G'_W]'/s survives at s=a.
    limit = -Fraction(3, 20) * (1 - CAP) * factorial(5) / 16
    assert limit == Fraction(-3, 4)
    errors = []
    for width in (1 / 128, 1 / 512, 1 / 2048, 1 / 8192, 1 / 32768, 1 / 131072):
        for side in (-1, 1):
            assert all(jet == 0 for jet in packet(float(CAP), width, side))

        clock = hessian(width)
        # On the uncut line the signed master packets pair to 4*width
        # against the smooth function s, independently of bell shape.
        def linear_probe(x):
            outer = (float(CAP) + width * (2 + x)) * bump(x)
            inner = (float(CAP) + width * (-2 + x)) * bump(x)
            return outer - inner

        signed_moment = simpson(linear_probe, -1, 1)
        assert isclose(signed_moment, 4 * width, abs_tol=1e-13)
        errors.append(abs(clock - float(limit)))
        print(f"width={width:.8f}  clock Hessian={clock:.8f}  "
              f"signed first moment={signed_moment:.8f}")

    assert all(x > y for x, y in zip(errors, errors[1:]))
    assert errors[-1] < 0.001
    for n in (1, 2):
        # The leading right-hand density c_n (s-a)^n is sampled by the
        # signed packet as c_n width^n times this displaced bell moment.
        c_n = -Fraction(3, 20) * (1 - CAP) * factorial(n + 5) / (16 * factorial(n))
        displaced_moment = simpson(lambda x: (2 + x) ** n * bump(x), -1, 1)
        estimate = hessian(width, n) / (width ** n * displaced_moment)
        assert isclose(estimate, float(c_n), rel_tol=0.002)
        print(f"order {n} right-hand coefficient={estimate:.5f}  exact limit={c_n}")
    print(f"Limiting clock Hessian: {limit}")


if __name__ == "__main__":
    check()
