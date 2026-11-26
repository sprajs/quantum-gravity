"""Check the localized current estimate and transfer through a fluctuating corner."""

import math


def check_frequency_sum(length, fraction, wave_number, cutoff=2048):
    """Compare a signed sum over measured frequencies to its telescoped value."""
    def window_power(index):
        if index == 0:
            return length * fraction**2
        return length * (math.sin(math.pi * fraction * index) / (math.pi * index))**2

    signed = sum(window_power(m - wave_number) - window_power(m + wave_number)
                 for m in range(1, cutoff + 1))
    central = sum(window_power(n) for n in range(1 - wave_number, wave_number + 1))
    tail = sum(window_power(n) for n in range(cutoff - wave_number + 1,
                                               cutoff + wave_number + 1))
    assert abs(signed + tail - central) < 2e-14
    assert central >= window_power(0)
    assert tail <= 2 * wave_number * length / (math.pi * (cutoff - wave_number + 1))**2


def check_one_oscillator(epsilon, v0, entropy, k):
    """Obtain the bottom of the prefix directly from its two-quadrature matrix."""
    length = 1 - epsilon
    omega = 2 * math.pi * k / length
    panels = 8192
    step = (v0 - epsilon) / panels
    qq = qp = pp = 0.0
    for i in range(panels + 1):
        r = epsilon + i * step
        phase = omega * (r - epsilon)
        sn, cs = math.sin(phase), math.cos(phase)
        q = -omega * sn / r - (cs - 1) / r**2
        p = omega * cs / r - sn / r**2
        weight = step * r * (1 if i in (0, panels) else 4 if i % 2 else 2) / 3
        qq += weight * q**2
        qp += weight * q * p
        pp += weight * p**2
    bottom = math.sqrt(qq * pp - qp**2) / (2 * entropy * k)
    certified = prefix_floor(epsilon, v0, entropy, k)
    assert bottom >= certified
    return bottom, certified


def prefix_floor(epsilon, v0, entropy, response_sum):
    length = 1 - epsilon
    kappa = 2 * math.pi / length
    return epsilon * kappa**2 * (v0 - epsilon)**2 * response_sum / (
        4 * v0**2 * length * entropy)


def det(matrix):
    a, b, c = matrix
    return a * c - b * b


def positive_sqrt(matrix):
    """Square root of a real symmetric positive 2 by 2 matrix."""
    a, b, c = matrix
    assert a > 0 and det(matrix) > 0
    t = math.sqrt(det(matrix))
    d = math.sqrt(a + c + 2 * t)
    return ((a + t) / d, b / d, (c + t) / d)


def corner_matrix_floor():
    # E_i = rho_i squared / 3. They sum to identity and do not commute.
    effects = [(0.50, 0.12, 0.20), (0.10, 0.06, 0.35), (0.40, -0.18, 0.45)]
    densities = [positive_sqrt(tuple(3 * v for v in e)) for e in effects]
    average = tuple(sum(r[i] for r in densities) / 3 for i in range(3))
    strengths = (16, 16, 1)
    # Local integrated factors d_i I + |v_i><v_i| need not commute with rho_i.
    directions = [(0.2, -0.1), (0.4, 0.3), (-0.2, 0.5)]
    numerator = [0.0] * 3
    for e, (a, b, c), d, (x, y) in zip(effects, densities, strengths, directions):
        u, v = a*x + b*y, b*x + c*y
        for i, square in enumerate((u*u, u*v, v*v)):
            numerator[i] += d * e[i] + square / 3
    lower = (sum(1/d for d in strengths) / 3)**-0.5
    difference = tuple(n - lower*a for n, a in zip(numerator, average))
    assert difference[0] > 0 and det(difference) > 0
    a, b, c = numerator
    aa, ab, ac = average
    linear = a*ac + c*aa - 2*b*ab
    minimum = 2 * det(numerator) / (
        linear + math.sqrt(linear**2 - 4 * det(numerator) * det(average)))
    return lower, minimum


def sharp_two_cell_floor(fraction, cost):
    """Optimize the dual scalar using its strictly decreasing stationarity condition."""
    low, high = 0.0, 1.0
    for _ in range(56):
        shift = (low + high) / 2
        reciprocal = (1 - fraction) / (1 - shift) + fraction / (cost - shift)
        derivative = (1 - fraction) / (1 - shift)**2 + fraction / (cost - shift)**2
        if reciprocal > shift * derivative:
            low = shift
        else:
            high = shift
    shift = (low + high) / 2
    reciprocal = (1 - fraction) / (1 - shift) + fraction / (cost - shift)
    floor = 2 * math.sqrt(shift / reciprocal)

    # Minimize independently over all positive, normalized scalar two-cell profiles.
    def quotient(angle):
        g_out = math.cos(angle) / math.sqrt(1 - fraction)
        g_in = math.sin(angle) / math.sqrt(fraction)
        return ((1 - fraction) * g_out**2 + fraction * cost * g_in**2) / (
            (1 - fraction) * g_out + fraction * g_in)

    low, high = 0.0, math.pi / 2
    for _ in range(80):
        left = (2*low + high) / 3
        right = (low + 2*high) / 3
        if quotient(left) < quotient(right):
            high = right
        else:
            low = left
    assert abs(quotient((low + high) / 2) - floor) < 2e-13
    return floor


def main():
    epsilon, v0, entropy = 0.25, 0.625, 10000
    for fraction in (0.25, 0.37, 0.5):
        for k in (1, 2, 7, 16):
            check_frequency_sum(1-epsilon, fraction, k)
    print("localized Fourier commutator: 12 identities verified")
    for k in (1, 4):
        bottom, certified = check_one_oscillator(epsilon, v0, entropy, k)
        print(f"k={k}  one-mode spectral bottom {bottom:.8f}  lower bound {certified:.8f}")
    for cutoff in (4, 6, 8, 16):
        radial = sum(range(1, cutoff + 1))
        angular = 2 * sum(2*j + 1 for j in range(2, cutoff + 1))
        floor = prefix_floor(epsilon, v0, entropy, radial * angular)
        if cutoff == 6:
            clock_ratio = 1 + (1-v0)/(1-epsilon) * math.expm1(min(floor, 1))
            assert clock_ratio > 1.2
            print(f"K=J={cutoff:2d}  clock lower bound at cap 1: {clock_ratio:.6f}")
        else:
            print(f"K=J={cutoff:2d}  bare prefix floor {floor:.6f}")
    lower, minimum = corner_matrix_floor()
    print(f"noncommuting corner: lower bound {lower:.6f}  exact matrix minimum {minimum:.6f}")
    p = 0.75
    optimum = sharp_two_cell_floor(p, 16)
    print(f"three-quarter patch at cost 16: sharp floor {optimum:.9f}")
    for d in (16, 256, 4096):
        bound = (1-p+p/d)**-0.5
        example = (1-p+p/d**2)**-0.5
        assert bound <= sharp_two_cell_floor(p, d) <= example <= (1-p)**-0.5
    print(f"three-quarter patch: bound {bound:.6f}  scalar example {example:.9f}  limit 2")


if __name__ == "__main__":
    main()
