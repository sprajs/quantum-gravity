"""Check the curved-target Dirac kernel and its finite-mode clock bound."""

from math import cos, pi, sin, sqrt


EPSILON, LEFT, RIGHT = 0.2, 0.3, 0.7
TURN = 3.0  # theta' = exp(z1) z2' on the background


def evaluate(frequency, points=2048, modes=48):
    length = RIGHT - LEFT
    step = length / points
    scale = 1 / sqrt(length * 35 / 128)  # integral of sin^8 on this interval
    samples = []
    sum_g = [0.0, 0.0]
    for i in range(points):
        s = LEFT + (i + 0.5) * step
        phase = pi * (s - LEFT) / length
        w = scale * sin(phase) ** 4
        dw = scale * 4 * pi / length * sin(phase) ** 3 * cos(phase)
        co, si = cos(frequency * s), sin(frequency * s)
        f, g = w * co, w * si
        hf = (dw + w / s) * co - frequency * w * si
        hg = (dw + w / s) * si + frequency * w * co
        u = (cos(TURN * s), sin(TURN * s))
        b = (-TURN * u[1] - u[0] / s, TURN * u[0] - u[1] / s)
        for j in range(2):
            sum_g[j] += step * g * b[j]
        samples.append((s, f, g, hf, hg, u, b))

    # The two triangles s > t and s < t, with zero weight on the diagonal.
    prefix_g = [0.0, 0.0]
    remainder = 0.0
    for _, f, g, _, _, _, b in samples:
        for j in range(2):
            d = step * g * b[j]
            remainder += step * f * b[j] * (2 * prefix_g[j] + d - sum_g[j])
            prefix_g[j] += d

    # Independently integrate the projected coordinate bracket by parts.
    bracket = 0.0
    for n in range(modes):
        odd = 2 * n + 1
        omega = odd * pi / (1 - EPSILON)
        fs, fc, gs, gc = ([0.0, 0.0] for _ in range(4))
        for s, _, _, hf, hg, u, _ in samples:
            si = step * sin(omega * (s - EPSILON))
            co = step * cos(omega * (s - EPSILON))
            for j in range(2):
                fs[j] += hf * u[j] * si
                fc[j] += hf * u[j] * co
                gs[j] += hg * u[j] * si
                gc[j] += hg * u[j] * co
        bracket += 4 / (pi * odd) * sum(fc[j] * gs[j] - fs[j] * gc[j] for j in range(2))

    continuum = frequency - remainder
    remainder_bound = (TURN**2 * length + 1 / LEFT - 1 / RIGHT) / 2
    assert abs(remainder) <= remainder_bound
    assert abs(bracket - continuum) < 2e-5
    return bracket, continuum, (frequency - remainder_bound) / 4


def shifted_current_floor(modes):
    """Integrate the exact finite-kernel uncertainty bound at distance L/(4N)."""
    length = 1 - EPSILON
    d = length / (4 * modes)
    kernel = first = minus_second = 0.0
    for n in range(modes):
        odd = 2 * n + 1
        phase = odd * pi / (4 * modes)
        kernel += 4 * sin(phase) / (pi * odd)
        first += 4 * cos(phase) / length
        minus_second += 4 * pi * odd * sin(phase) / length**2
    co, si = cos(TURN * d), sin(TURN * d)
    step = (RIGHT - LEFT - d) / 1024
    lower = 0.0
    for j in range(1024):
        t = LEFT + (j + 0.5) * step
        s = t + d
        mixed = 2 * TURN * si + co * (1 / s - 1 / t)
        b_dot = co * (TURN**2 + 1 / (s * t)) + TURN * si * (1 / t - 1 / s)
        lower += step * abs(minus_second * co + first * mixed + kernel * b_dot) / 8
    return lower / modes**2


if __name__ == "__main__":
    print("K    finite bracket   contact minus remainder   limit floor for Xi")
    for k in (32, 64, 128):
        finite, exact, floor = evaluate(k)
        print(f"{k:3d}  {finite:14.7f}  {exact:23.7f}  {floor:18.7f}")
    asymptotic = 4 * (RIGHT - LEFT) / (pi * (1 - EPSILON)**2)
    print(f"Shifted-current floor divided by N^2; predicted limit {asymptotic:.7f}")
    for n in (16, 64, 256, 1024):
        estimate = shifted_current_floor(n)
        print(f"{n:4d}  {estimate:.7f}")
    assert abs(shifted_current_floor(1024) - asymptotic) < 0.001
