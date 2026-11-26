"""Compare the Cartesian TT ADM integral with the spherical master line integral."""

from fractions import Fraction
from math import comb, factorial, isclose

from joint_spherical_hessian import falling, simpson


WIDTH = 1 / 8
CENTERS = (1 / 2, 3 / 2, 5 / 2)
AMPS = ((1, 0.65, 0.5), (-1 / 3, 1.2, 1.1))


def bell(x, order):
    """Differentiate (1-x)^12 (1+x)^12 without endpoint cancellation."""
    if abs(x) >= 1:
        return 0.0
    return sum(comb(order, j) * (-1)**j * falling(12, j) * falling(12, order-j)
               * (1-x)**(12-j) * (1+x)**(12-order+j) for j in range(order+1))


def master(which, u, order):
    """The two profiles are a bell and x times a bell on each occupied interval."""
    result = 0.0
    for center, amp in zip(CENTERS, AMPS[which]):
        x = (u - center) / WIDTH
        if abs(x) < 1:
            val = bell(x, order)
            if which == 1:
                val = x * val + (order * bell(x, order-1) if order else 0)
            result += amp * WIDTH**(5-order) * val
    return result


def tt_components(which, r, time_order):
    """Return h_nn/Q, h_nA/(S n)_A and h_AB^TF/B_AB at t=1."""
    radial_jets = [
        (master(which, 1+r, j+time_order)
         - (-1)**j * master(which, 1-r, j+time_order)) / r**(5-j)
        for j in range(5)
    ]
    f0, f1, f2, f3, f4 = radial_jets
    return (18*f0-18*f1+6*f2,
            -12*f0+12*f1-6*f2+2*f3,
            3*f0-3*f1+3*f2-2*f3+f4)


def contraction(left, right):
    """Round average with S=diag(-1/2,-1/2,1), including the screen trace."""
    a, b, c = left
    d, e, f = right
    return 3*a*d/10 + 3*b*e/5 + 3*c*f/5


def bulk(r, energy):
    h = tt_components(0, r, 0)
    ht = tt_components(0, r, 1)
    if energy:
        # With compact support, integrate the spatial gradient term by parts.
        return r*r*(contraction(ht, ht) - contraction(h, tt_components(0, r, 2))) / 16
    z = tt_components(1, r, 0)
    zt = tt_components(1, r, 1)
    return r*r*(contraction(ht, z) - contraction(h, zt)) / 8


def line(u, energy):
    if energy:
        return 3 * master(0, u, 5)**2 / 40
    return (3 / 40 * (master(0, u, 5) * master(1, u, 4)
                      - master(1, u, 5) * master(0, u, 4)))


def integrate_lobes(integrand, centers):
    return sum(simpson(integrand, c-WIDTH, c+WIDTH, pieces=120) for c in centers)


def check():
    for energy, name in [(False, "symplectic product"), (True, "wave energy")]:
        values = []
        for radii, centers in [((0.5,), CENTERS[:2]), ((0.5, 1.5), CENTERS)]:
            direct = integrate_lobes(lambda r: bulk(r, energy), radii)
            reduced = integrate_lobes(lambda u: line(u, energy), centers)
            assert isclose(direct, reduced, rel_tol=2e-11), (name, direct, reduced)
            values.append(direct)
        assert not isclose(*values, rel_tol=0.01)
        print(f"ADM/master {name} ratio = 1 (ball and full slice)")

    # Unit powers u^k are valid near the whole cone after a smooth cutoff.
    # The uncorrected optical coefficients multiply s^(k-5).
    def optical_coefficient(k):
        return (falling(k, 4) * 2**(k-4) - 2*falling(k, 3) * 2**(k-3)
                + falling(k, 2) * 2**(k-2))

    assert [optical_coefficient(k) for k in range(7)] == [0, 0, 2, 0, -24, -80, 0]
    assert optical_coefficient(7) == 1344
    for k in range(7):
        bare_slope = (k-5) * optical_coefficient(k)
        vertex_slope = {2: 3*factorial(2), 4: -factorial(4)}.get(k, 0)
        assert bare_slope + vertex_slope == 0
    print("Vertex-normalized slope vanishes for degrees 0 through 6.")
    print("Degree 7 optical strain = 1344 s^2.")

    # Jets in s of f=(s-a)^2+(s-a)^5/(5a^3) near the cap, zero near the waist.
    a = Fraction(1, 3)
    f2, f5 = 2, 24/a**3
    strain = f2 / (4*a**3)
    rim_slope = f5 / (16*a) - 3*f2 / (4*a**4)
    integrated_slope = -(1/a - 1)*strain + f2/(16*a**4)
    vertex = -Fraction(3, 20) * integrated_slope
    assert rim_slope == 0 and vertex == Fraction(81, 32)
    print(f"Rim slope = {rim_slope}, vertex fourth-derivative coefficient = {vertex}.")


if __name__ == "__main__":
    check()
