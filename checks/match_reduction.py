"""Test the marked rim potential, its Maurer–Cartan sign, and the round projection."""

from fractions import Fraction as F
from math import isclose


def composed_frame(x, step):
    # The plus frame moves in angle and rapidity. The comparison also moves.
    moved = x + step * (1 - x*x)
    angle = moved + (F(1, 5) + step * moved) * (1 - moved*moved)
    rapidity = step * x + moved*moved + step * (1 + moved)
    return angle, rapidity


def check_composition(x):
    step = F(1, 10**7)
    forward, backward = composed_frame(x, step), composed_frame(x, -step)
    angle, boost = [(a - b) / (2*step) for a, b in zip(forward, backward)]
    target, _ = composed_frame(x, 0)
    jac = 1 - 2*x / 5
    angular_minus, boost_minus = 2 + target, 1 - target/3
    # Vanishing of the two common moment maps, including the boost gradient.
    boost_plus = -jac * boost_minus
    angular_plus = -jac**2 * angular_minus - jac * boost_minus * 2*x
    two_sides = (angular_plus * (1 - x*x) + boost_plus * x
                 + jac * (angular_minus * angle + boost_minus * boost))
    relative = jac * (angular_minus * x * (1 - x*x) + boost_minus * (1 + x))
    assert abs(two_sides - relative) < F(1, 10**12)


def inverse_angle(y, s, t):
    # Invert Y(x) = x + (s + tx)(1-x²), which is increasing at these steps.
    low, high = -1., 1.
    for _ in range(60):
        x = (low + high) / 2
        if x + (s + t*x) * (1 - x*x) < y:
            low = x
        else:
            high = x
    return (low + high) / 2


def check_bracket(y):
    f = lambda x: 1 - x*x
    g = lambda x: x * (1 - x*x)
    step = 1e-5
    ds_vt = (g(inverse_angle(y, step, 0)) - g(inverse_angle(y, -step, 0))) / (2*step)
    dt_vs = (f(inverse_angle(y, 0, step)) - f(inverse_angle(y, 0, -step))) / (2*step)
    bracket = f(y) * (1 - 3*y*y) - g(y) * (-2*y)
    assert isclose(ds_vt - dt_vs, -bracket, abs_tol=5e-9)


def quadrupole_projection(x):
    # Unit-sphere orthonormal diagonal components. x=cos(theta), w=grad Q.
    sine_squared = 1 - x*x
    gradient_x = 3*x*sine_squared
    gradient_x_prime = 3 - 9*x*x
    strain_theta = 2*(gradient_x_prime + 3*x*x)
    strain_phi = -6*x*x
    b_theta = F(3, 4)*sine_squared
    return 3*x*gradient_x, b_theta*(strain_theta - strain_phi)/2


if __name__ == '__main__':
    for value in (F(-3, 4), F(-1, 4), F(0), F(1, 3), F(2, 3)):
        check_composition(value)
        check_bracket(float(value))
    print('Composed angular and boost frame potentials agree')
    print('Eulerian displacement satisfies Dv(1,2) = -[v1,v2]')

    # Boole's rule integrates both degree-four angular polynomials exactly.
    samples = [quadrupole_projection(F(i, 2)) for i in range(-2, 3)]
    weights = (7, 32, 12, 32, 7)
    pairings = [sum(w*z for w, z in zip(weights, column))/90 for column in zip(*samples)]
    assert pairings == [F(6, 5), F(6, 5)]
    charge = -F(1, 3)**2 * pairings[1]/4
    assert charge == F(-1, 30)
    print(f'Angular charge from the marked metric discrepancy: {charge}')
