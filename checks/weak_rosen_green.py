"""Symmetric-tensor Green transport on a vacuum Rosen strip; standard library."""

from cmath import exp
from math import cos, cosh, pi, sin, sinh, sqrt, tan, tanh


def geometry(u, profile):
    """Scale factor, first and second u derivatives on each transverse axis."""
    if profile == "wave":
        return ((cosh(u), sinh(u), cosh(u)), (cos(u), -sin(u), -cos(u)))
    if profile == "affine":
        return ((1 + 0.4 * u, 0.4, 0), (1 - 0.2 * u, -0.2, 0))
    return ((1, 0, 0), (1, 0, 0))


def volume(s, profile):
    first, second = geometry(s, profile)
    return first[0] * second[0]


def connection(h, axis, scale, slope):
    # -Gamma on each lower index. Indices 0,1 denote the two null directions.
    result = [0j] * 16
    for target, source, value in ((0, axis, -slope / scale), (axis, 1, -scale * slope)):
        for other in range(4):
            result[4 * target + other] += value * h[4 * source + other]
            result[4 * other + target] += value * h[4 * other + source]
    return result


def raise_indices(h, factors):
    rows = (1, 0, 2, 3)
    values = (-1, -1, factors[0][0]**-2, factors[1][0]**-2)
    return [values[i] * values[j] * h[4 * rows[i] + rows[j]]
            for i in range(4) for j in range(4)]


def transport_rhs(u, h, direction, p, k, profile):
    factors = geometry(u, profile)
    expansion = (0, 0, *(slope / scale for scale, slope, _ in factors))
    result = [direction * (expansion[i] + expansion[j] - sum(expansion) / 2)
              * h[4 * i + j] for i in range(4) for j in range(4)]
    raised = raise_indices(h, factors)
    for axis, (scale, slope, second) in enumerate(factors, 2):
        frequency = k[axis - 2]
        first = connection(h, axis, scale, slope)
        twice = connection(first, axis, scale, slope)
        for n in range(16):
            result[n] += (twice[n] + 2j * frequency * first[n] - frequency**2 * h[n]) / (
                2 * p * scale**2)
        # R_abcd = -a a'' (du wedge dx^i)_ab (du wedge dx^i)_cd.
        two_form = ((0, axis, 1), (axis, 0, -1))
        for a, c, sign_ac in two_form:
            for b, d, sign_bd in two_form:
                result[4 * a + b] -= scale * second * sign_ac * sign_bd * raised[4 * c + d] / p
    return result


def propagate(s, u, p, k, source, profile, steps=96):
    direction = 1 if u > s else -1
    step = abs(u - s) / steps
    h = [-v / (2 * p * volume(s, profile)) for v in source]

    def shifted(values, rate, length):
        return [value + length * slope for value, slope in zip(values, rate)]

    for m in range(steps):
        at = s + direction * m * step
        midpoint = at + direction * step / 2
        one = transport_rhs(at, h, direction, p, k, profile)
        two = transport_rhs(midpoint, shifted(h, one, step / 2), direction, p, k, profile)
        three = transport_rhs(midpoint, shifted(h, two, step / 2), direction, p, k, profile)
        four = transport_rhs(at + direction * step, shifted(h, three, step), direction, p, k, profile)
        h = [value + step * (a + 2*b + 2*c + d) / 6
             for value, a, b, c, d in zip(h, one, two, three, four)]
    return h


def wave_polynomial(s, u, p, k, source):
    """Degree-four exponential in the parallel null coframe, in closed form."""
    direction = 1 if u > s else -1
    U = abs(u - s)
    start, stop = geometry(s, "wave"), geometry(u, "wave")
    source_scale = [1, 1, start[0][0], start[1][0]]
    target_scale = [1, 1, stop[0][0], stop[1][0]]
    moments = [direction * (tanh(u) - tanh(s)), direction * (tan(u) - tan(s))]
    generator = []
    for before, after in zip(start, stop):
        a, da, dda = before
        end, end_da, _ = after
        mixing = direction * (1/a - 1/end)
        squared = U * dda/a - direction * (end_da/end - da/a)
        generator.append((mixing, squared, -dda/a))

    term = [source[4*i+j] / (source_scale[i] * source_scale[j])
            for i in range(4) for j in range(4)]
    total = term.copy()
    for order in range(1, 5):
        next_term = [0j] * 16
        for axis, (mixing, squared, curvature) in enumerate(generator, 2):
            # For unit scale and slope the lower-index connection equals -J_i.
            minus_j = connection(term, axis, 1, 1)
            j_squared = connection(minus_j, axis, 1, 1)
            for n in range(16):
                next_term[n] += (2j * k[axis-2] * mixing * minus_j[n]
                                 + squared * j_squared[n])
            # Curvature action in the parallel null frame.
            strength = 2 * U * curvature
            next_term[0] += strength * term[4*axis+axis]
            next_term[4*axis+axis] += strength * term[5]
            next_term[axis] += strength * term[4*axis+1]
            next_term[4*axis] += strength * term[4+axis]
        term = [x / (2 * p * order) for x in next_term]
        total = [x+y for x, y in zip(total, term)]
    scalar = -exp(-sum(w*w*moment for w, moment in zip(k, moments)) / (2*p)) / (
        2 * p * sqrt(volume(s, "wave") * volume(u, "wave")))
    return [scalar * total[4*i+j] * target_scale[i] * target_scale[j]
            for i in range(4) for j in range(4)]


def check_spacetime_image(s, u, k):
    """Fourier integrate the wavefront and both tails for an incoming vv source."""
    p = 1.7
    U = abs(u - s)
    direction = 1 if u > s else -1
    before, after = geometry(s, "wave"), geometry(u, "wave")
    moments = (direction * (tanh(u) - tanh(s)), direction * (tan(u) - tan(s)))
    slopes, transverse = [], []
    uv = 0
    for start, stop, moment in zip(before, after, moments):
        a, da, dda = start
        end, end_da, _ = stop
        mixing = direction * (1 / a - 1 / end)
        beta = U * dda / a - direction * (end_da / end - da / a) - mixing**2 / moment
        slopes.append(mixing / moment)
        uv += beta / 2
        transverse.append(beta - U * dda / a)
    square_uu = sum(value**2 for value in transverse) + 2 * uv**2
    uu, u1 = 0j, 0j
    for i in range(-24, 25):
        for j in range(-24, 25):
            y = (i / 3 * sqrt(moments[0]/p), j / 3 * sqrt(moments[1]/p))
            weight = exp(-(i*i + j*j)/18 - 1j * (k[0]*y[0] + k[1]*y[1])) / (18*pi)
            t1, t2 = (slope * value for slope, value in zip(slopes, y))
            norm = t1*t1 + t2*t2
            uu += weight * (norm**2/4 + (uv*norm + transverse[0]*t1**2
                                          + transverse[1]*t2**2)/p + square_uu/(2*p**2))
            u1 += weight * (norm*t1/2 + (uv + transverse[0])*t1/p)
    scale = -1 / (2 * p * sqrt(volume(u, "wave") * volume(s, "wave")))
    source = [0] * 16
    source[5] = 1
    solved = propagate(s, u, p, k, source, "wave")
    assert abs(uu*scale - solved[0]) < 1e-9
    assert abs(u1*scale*after[0][0] - solved[2]) < 1e-9


def flat_images():
    periods = (1.9, 2.4)
    y = (0.6, -0.2)
    U, p = 0.74, 2.2 + 0.4j
    modes, images = 0j, 0j
    for i in range(-10, 11):
        for j in range(-10, 11):
            k = (2 * pi * i / periods[0], 2 * pi * j / periods[1])
            modes += exp(1j * (k[0] * y[0] + k[1] * y[1]) - U * (k[0]**2 + k[1]**2) / (2*p))
            r2 = (y[0] + i * periods[0])**2 + (y[1] + j * periods[1])**2
            images += exp(-p * r2 / (2 * U))
    modes /= -2 * p * periods[0] * periods[1]
    images /= -4 * pi * U
    assert abs(modes - images) < 1e-13


def component(s, u, p, k, profile):
    direction = 1 if u > s else -1
    start, stop = geometry(s, profile), geometry(u, profile)
    if profile == "wave":
        moments = (direction * (tanh(u) - tanh(s)), direction * (tan(u) - tan(s)))
    else:
        moments = [abs(u-s) / (before[0] * after[0]) for before, after in zip(start, stop)]
    a, da, _ = start[0]
    end_a, end_da, _ = stop[0]
    shear_change = direction * (end_da / end_a - da / a)
    mixing = direction * (1 / a - 1 / end_a)
    average = sqrt(volume(s, profile) * volume(u, profile))
    scalar = -exp(-sum(w**2 * moment for w, moment in zip(k, moments)) / (2 * p)) / (2 * p * average)
    response = scalar * (-shear_change / p - (k[0] * mixing / p)**2) / a**2
    interior = (shear_change + mixing**2 / moments[0]) / (
        4 * pi * a**2 * average * sqrt(moments[0] * moments[1]))
    return response, interior


if __name__ == "__main__":
    flat_images()
    p, k = 1.15 + 0.47j, (1.3, -0.9)
    s, u = 0.14, 0.76
    point_source = [0] * 16
    point_source[4*2 + 2] = 1
    left = [(1 + i * j + i + j) / 8 for i in range(4) for j in range(4)]
    right = [(i + j - i * j + 1) / 4 for i in range(4) for j in range(4)]
    flat = propagate(s, u, p, k, left, "flat")
    scalar = -exp(-(u-s) * sum(w**2 for w in k) / (2*p)) / (2*p)
    assert max(abs(x - scalar * y) for x, y in zip(flat, left)) < 1e-9
    print("Flat scalar image sum and flat tensor identity agree with their Fourier kernels.")

    for profile in ("wave", "affine"):
        for start, stop in ((s, u), (u, s)):
            for frequency in ((0, 0), k):
                numerical = propagate(start, stop, p, frequency, point_source, profile)
                analytic, tail = component(start, stop, p, frequency, profile)
                assert abs(numerical[0] - analytic) < 1e-9
                if profile == "wave":
                    assert tail > 0
                else:
                    assert abs(tail) < 1e-14

    for start, stop in ((s, u), (u, s)):
        for i in range(4):
            for j in range(i, 4):
                seed = [0] * 16
                seed[4*i+j] = seed[4*j+i] = 1
                solved = propagate(start, stop, p, k, seed, "wave")
                finite = wave_polynomial(start, stop, p, k, seed)
                assert max(abs(x-y) for x, y in zip(solved, finite)) < 1e-9
        check_spacetime_image(start, stop, k)
    print("Degree-four kernel reproduces all ten tensor columns in both directions.")
    print("The position-space wavefront and both tails reproduce two Fourier components.")

    forward = propagate(s, u, p, k, left, "wave")
    backward = propagate(u, s, p, tuple(-w for w in k), right, "wave")
    left_raised = raise_indices(left, geometry(s, "wave"))
    right_raised = raise_indices(right, geometry(u, "wave"))
    residual = sum(x*y for x, y in zip(right_raised, forward)) - sum(x*y for x, y in zip(left_raised, backward))
    assert abs(residual) < 1e-9
    print("Retarded and advanced uu <- 11 mixtures agree at k=0 and at nonzero k.")
    print("Bilinear reciprocity holds for a source and a probe with all tensor components.")
    print(f"Interior uu <- 11 coefficient: curved={component(s,u,p,k,'wave')[1]:.8f}, flat affine=0.")
