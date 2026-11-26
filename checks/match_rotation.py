"""Integrate the angular endpoint momentum on exact exterior Kerr spheres."""


def kerr_coefficients(mass, spin, radius, cosine):
    sine_squared = 1 - cosine**2
    sigma = radius**2 + spin**2 * cosine**2
    delta = radius**2 - 2 * mass * radius + spin**2
    area_factor = (radius**2 + spin**2)**2 - spin**2 * delta * sine_squared
    q_phi_phi = area_factor * sine_squared / sigma
    shift_phi = -2 * mass * spin * radius / area_factor
    return sigma, delta, area_factor, q_phi_phi, shift_phi


def charge(mass, spin, radius, panels=512):
    # x=cos(theta) supplies the sin(theta) in the area element. Set G=1.
    def density(cosine):
        sigma, delta, area_factor, q_phi_phi, _ = kerr_coefficients(
            mass, spin, radius, cosine
        )
        radial_normal = (delta / sigma)**0.5
        lapse = (sigma * delta / area_factor)**0.5
        complex_radius = radius + 1e-20j
        shift = kerr_coefficients(mass, spin, complex_radius, cosine)[4]
        shift_derivative = shift.imag / complex_radius.imag
        twist_phi = -q_phi_phi * radial_normal * shift_derivative / (2 * lapse)
        return area_factor**0.5 * twist_phi / 4

    step = 2 / panels
    total = density(-1) + density(1)
    for index in range(1, panels):
        weight = 4 if index % 2 else 2
        total += weight * density(-1 + index * step)
    return total * step / 3


mass = 1.25
for spin in (0.0, 0.03125, 0.75, 1.125):
    for radius in (2.75, 6.0, 17.0):
        for cosine in (-1, -0.625, 0, 0.375, 1):
            positive = kerr_coefficients(mass, spin, radius, cosine)
            negative = kerr_coefficients(mass, -spin, radius, cosine)
            assert positive[:4] == negative[:4]
            assert positive[4] == -negative[4]
        forward = charge(mass, spin, radius)
        reverse = charge(mass, -spin, radius)
        assert abs(forward + mass * spin) < 1e-10
        assert abs(forward + reverse) < 1e-12
print("Kerr rim metrics agree for opposite spins and axial charges equal -J within 1e-10")
