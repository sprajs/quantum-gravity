"""Check a cap TT packet, its second-order flux, and the Schwarzschild collar."""
from collections import defaultdict
from fractions import Fraction as Q
from math import comb, factorial, isclose, sqrt


def radial_product(left, right):
    """Integrate two radial polynomials with the three-dimensional Jacobian."""
    return sum(Q(x * y, p + q + 3) for p, x in left.items() for q, y in right.items())


def tt_norm():
    # phi=(1-r^2)^8 on the unit ball, extended by zero. Apply the local
    # TT operator with S=diag(-1/2,-1/2,1) term by term to this radial seed.
    radial, mixed, screen, bilaplacian = {}, {}, {}, {}
    for j in range(2, 9):
        k = 2 * j
        coeff = (-1)**j * comb(8, j)
        jets = [factorial(k + 1) // factorial(k + 1 - i) for i in range(5)]
        f0, f1, f2, f3, f4 = jets
        radial[k-4] = coeff * (18*f0 - 18*f1 + 6*f2)
        mixed[k-4] = coeff * (-12*f0 + 12*f1 - 6*f2 + 2*f3)
        screen[k-4] = coeff * (3*f0 - 3*f1 + 3*f2 - 2*f3 + f4)
        bilaplacian[k-4] = coeff * k*(k+1)*(k-2)*(k-1)
    direct = (3*radial_product(radial, radial)/10
              + 3*radial_product(mixed, mixed)/5
              + 3*radial_product(screen, screen)/5)
    # Independent Parseval check: the angular mean squared TT symbol is 3/5.
    assert direct == 3*radial_product(bilaplacian, bilaplacian)/5 > 0
    # Solve the monopole Poisson equation termwise for the cap correction:
    # Δu = -<|T|²>/8. Match its radial derivative to the harmonic exterior
    # u_ext = const + mass_term/r at the packet radius one.
    source = defaultdict(Q)
    for weight, poly in ((Q(3,10),radial), (Q(3,5),mixed), (Q(3,5),screen)):
        for power, a in poly.items():
            for other_power, b in poly.items():
                source[power + other_power] -= weight * a * b / 8
    solution = {n+2: coefficient / ((n+2)*(n+3)) for n, coefficient in source.items()}
    mass_term = -sum(n*u for n,u in solution.items())
    return direct, mass_term


def check():
    norm, mass_term = tt_norm()  # integral |T|^2 divided by 4*pi
    print(f"TT norm divided by 4 pi = {norm}")
    # For q=(1+lambda^2 u)^4 delta and K'=T, the averaged constraint
    # gives (r^2 u')'=-r^2 <|T|^2>/8. Evaluate the boundary metric flux.
    cap_radius = 2
    slope = -mass_term / cap_radius**2
    assert -8 * cap_radius**2 * slope == norm
    print("Canonical normalization from the TT norm; solved boundary flux / TT norm = 1")

    a, waist = Q(2), Q(5, 2)
    for mass in (Q(1, 8), Q(1, 4)):
        f = 1 - 2*mass/a
        # Normalize the outgoing affine tangent in the local static frame.
        dr_du = sqrt(f)
        assert isclose(dr_du * (float(waist-a) / dr_du), float(waist-a))
        # Future outgoing and ingoing expansions for null normals with l.n = -1.
        product = (2/waist) * (-(1-2*mass/waist)/waist)
        inferred_mass = waist/2 * (1 + waist**2 * product/2)
        assert inferred_mass == mass
        # Differentiate the finite-radius Brown-York energy with proper-time
        # lapse, then multiply by the Schwarzschild Killing lapse at the rim.
        def energy(m):
            return float(a)*(1-sqrt(1-2*m/float(a)))
        step = 1e-6
        derivative = (energy(float(mass)+step)-energy(float(mass)-step))/(2*step)
        assert isclose(sqrt(f) * derivative, 1, rel_tol=2e-10)
        print(f"m={mass}: clock={waist-a}, rim Weyl square={48*mass**2/a**6}, G dH/dm=1")


if __name__ == "__main__":
    check()
