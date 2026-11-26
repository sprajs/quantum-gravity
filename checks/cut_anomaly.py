"""Compare affine and optical-radius current vacua on a vacuum sandwich wave."""

import cmath
import math
from fractions import Fraction


def bump(z):
    """An unnormalized, symmetric smooth density supported on the unit interval."""
    if not 0 < z < 1:
        return 0.0
    return math.exp(4 - 1 / (z * (1 - z)))


def simpson(values, step):
    return step / 3 * (
        values[0] + values[-1] + 4 * sum(values[1:-1:2]) + 2 * sum(values[2:-1:2])
    )


def sandwich(loss, intervals=2048):
    """Integrate the density and its first moment to obtain D and its slope."""
    step = 1 / intervals
    nodes = [1 + j * step for j in range(intervals + 1)]
    density = [bump(x - 1) for x in nodes]
    norm = simpson(density, step)
    density = [value / norm for value in density]
    mass = moment = 0.0
    rows = [(nodes[0], 1.0, 1.0, 0.0)]
    for j, (left, right) in enumerate(zip(nodes, nodes[1:])):
        middle = (left + right) / 2
        mid_density = bump(middle - 1) / norm
        mass += step / 6 * (density[j] + 4 * mid_density + density[j + 1])
        moment += step / 6 * (
            left * density[j] + 4 * middle * mid_density + right * density[j + 1]
        )
        radius = right - loss * (right * mass - moment)
        rows.append((right, radius, 1 - loss * mass, -loss * density[j + 1]))
    return rows


def bogoliubov(rows, k, omega):
    step = rows[1][0] - rows[0][0]
    phases = [cmath.exp(-1j * (k * x + omega * radius)) for x, radius, _, _ in rows]
    curvatures = [
        phase * curvature / (k + omega * slope) ** 2
        for phase, (_, _, slope, curvature) in zip(phases, rows)
    ]
    compact = 1j * math.sqrt(k * omega) * simpson(curvatures, step) / math.tau

    # Abel integrals on the two affine tails provide an independent mode overlap.
    left_tail = 1j * phases[0] / (k + omega * rows[0][2])
    right_tail = -1j * phases[-1] / (k + omega * rows[-1][2])
    direct = (left_tail + simpson(phases, step) + right_tail) * math.sqrt(k / omega) / math.tau
    return compact, direct


def check_vacuum_wave(rows):
    """Reconstruct the Jacobi axes and difference them to test vacuum trace."""
    step = rows[1][0] - rows[0][0]
    shear = [math.sqrt(-curvature / radius) for _, radius, _, curvature in rows]
    tilt = 0.0
    plus = [rows[0][1]]
    minus = [rows[0][1]]
    for j, (_, radius, _, _) in enumerate(rows[1:]):
        tilt += (shear[j] + shear[j + 1]) * step / 2
        plus.append(radius * math.exp(tilt))
        minus.append(radius * math.exp(-tilt))
    trace = [
        sum((axis[j + 1] - 2 * axis[j] + axis[j - 1]) / (axis[j] * step**2)
            for axis in (plus, minus))
        for j in range(1, len(rows) - 1)
    ]
    assert max(map(abs, trace)) < 2e-5
    return max(map(abs, trace))


def main():
    loss = Fraction(1, 4)
    slope = 1 - loss
    left, right = Fraction(1, 4), Fraction(9, 4)
    gap = right - left
    optical_gap = right - loss * (right - Fraction(3, 2)) - left
    ratio = slope * gap**2 / optical_gap**2
    difference = (1 - ratio) / gap**2
    assert ratio == Fraction(768, 841) and difference == Fraction(73, 3364)
    print(f"Current covariance ratio: {ratio}; difference / C: {difference}")

    # Smooth positive bumps B sampled with their integration weights. Their
    # derivatives are signed current probes realizable by compact shear probes.
    width, points = 0.1, 256
    weights = [bump(j / points) for j in range(points + 1)]
    normalization = math.fsum(weights)
    weights = [weight / normalization for weight in weights]
    derivative_weights = []
    for j, weight in enumerate(weights):
        z = j / points
        log_derivative = (1 - 2 * z) / (z * (1 - z))**2 if 0 < z < 1 else 0
        derivative_weights.append(weight * log_derivative / width)
    values = []
    direct_values = []
    for i, left_weight in enumerate(weights):
        x = float(left) + width * (i / points - 0.5)
        for j, right_weight in enumerate(weights):
            y = float(right) + width * (j / points - 0.5)
            physical_gap = y - x
            radius_gap = y - float(loss) * (y - 1.5) - x
            local_ratio = float(slope) * physical_gap**2 / radius_gap**2
            values.append(left_weight * right_weight * 6 * (local_ratio**2 - 1) / physical_gap**4)
            direct_values.append(
                derivative_weights[i] * derivative_weights[j] * (1 - local_ratio) / physical_gap**2
            )
    mixed = math.fsum(values)
    assert abs(math.fsum(direct_values) - mixed) < 1e-10
    assert abs(mixed + 0.06234985) < 5e-9
    print(f"Compact shear probes, covariance difference / C: {mixed:.8f}")

    rows = sandwich(float(loss))
    assert abs(rows[-1][1] - 1.875) < 1e-13 and abs(rows[-1][2] - 0.75) < 1e-13
    residual = check_vacuum_wave(rows)
    print(f"Maximum absolute Jacobi trace residual: {residual:.2g}")
    beta, direct = bogoliubov(rows, 0.5, 0.5)
    assert abs(beta - direct) < 1e-12
    assert abs(beta - complex(-0.02249044, -0.00159372)) < 7e-9
    print(f"Full-line beta(1/2,1/2): {beta.real:.8f}{beta.imag:+.8f}i")
    for fraction in (0.25, 0.5, 0.75):
        soft_scale = 1e-6
        soft, _ = bogoliubov(rows, fraction * soft_scale, (1 - fraction) * soft_scale)
        predicted = (
            -1j * math.sqrt(fraction * (1 - fraction)) * float(loss)
            / (math.tau * (fraction + (1 - fraction) * float(slope)))
        )
        assert abs(soft_scale * soft - predicted) < 5e-8
    print("Soft limits agree on three frequency ratios.")


if __name__ == "__main__":
    main()
