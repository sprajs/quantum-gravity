"""Kirchhoff shell and canonical clock pairing on the flat waist slice."""

from math import isclose, pi

from entropy_determinant import gaussian_rule, integrate
from joint_spherical_hessian import SCREEN_MEAN, optical_mode, profile, simpson


RULE = gaussian_rule(18)


def ring_tide(mu):
    """Azimuthal mean of Q_zz on n_x=mu for h=(t-z)^2 diag(1,-1,0)."""
    transverse_sq = 1 - mu**2
    return (mu**2 - transverse_sq / 2 + mu**2 * transverse_sq / 2
            - transverse_sq**2 / 8)


def excess_sine_kernel(cap, width):
    """Subtract the smooth continuation across the interior Kirchhoff shell."""
    radius = abs(2 * cap - 1) + width
    lower, upper = (1 - radius) / 2, (1 + radius) / 2

    def difference(s):
        # J_high - J_low for the polynomial tidal wave. J_low uses max(s,a)=a.
        mu = (1 - (1 - radius**2) / (2 * s)) / radius
        return s * (cap - s) * (2 - cap - s) * ring_tide(mu) / 6

    if cap > 0.5:
        excess = integrate(difference, cap, upper, RULE)
    else:
        excess = -integrate(difference, lower, cap, RULE)
    return -excess / (8 * pi * radius)


def packet_jets(argument, cap, width):
    return [cap * width**(4-j) * profile(argument, j) for j in range(7)]


def spatial_screen(jets, radius, sign):
    """Screen coefficient of the spatial TT metric on the waist annulus."""
    f0, f1, f2, f3, f4 = jets[:5]
    return sign * (f4 / radius - 2 * sign * f3 / radius**2
                   + 3 * f2 / radius**3 - 3 * sign * f1 / radius**4
                   + 3 * f0 / radius**5)


def check(cap):
    sign = 1 if cap > 0.5 else -1
    radius = abs(2 * cap - 1)
    kernel_coefficient = (1 - cap) * (2 * cap / 3) / (128 * pi * radius)
    ratios = [excess_sine_kernel(cap, width) / (width**2 * kernel_coefficient)
              for width in (1e-3, 1e-4, 1e-5)]
    assert abs(ratios[-1] - 1) < 2e-4
    assert abs(ratios[0] - 1) > abs(ratios[1] - 1) > abs(ratios[2] - 1)

    # Test H'_W(a)=B against a regular compact TT wave of unit optical rim strain.
    width = 1 / 512
    prefactor = 4 * pi * SCREEN_MEAN * (1 - cap) / (32 * pi * radius)
    displacement = (-sign * prefactor * radius**2
                    * spatial_screen(packet_jets(0, cap, width), radius, sign))

    def velocity_integrand(x):
        r = radius + width * x
        jets = packet_jets(sign * x, cap, width)
        return width * r**2 * spatial_screen(jets[1:], r, sign)

    velocity = prefactor * simpson(velocity_integrand, 0, 1, pieces=1000)
    half_limit = -SCREEN_MEAN * cap * (1 - cap) / 8
    assert isclose(displacement, half_limit, abs_tol=1e-12)
    assert isclose(velocity, half_limit, abs_tol=2e-7)

    # An independent direct Jacobi integral, with H'_W(a)=B. The same first
    # branch is used throughout this narrow packet regardless of the waist sign.
    def optical_integrand(x):
        s = cap + width * x / 2
        # A fifth degree master yields unit slope at the rim. Its lower
        # derivatives give the regular continuation of W through the packet.
        y = width * x
        jets = [cap * factor * y**(5-j) / 240
                for j, factor in enumerate((1, 5, 20, 60, 120, 120))] + [0]
        reference_slope = optical_mode(s, jets)[1]
        trial_slope = optical_mode(s, packet_jets(x, cap, width))[1]
        return width / 2 * s * (1-s) * reference_slope * trial_slope

    optical = SCREEN_MEAN / 4 * simpson(optical_integrand, 0, 1, pieces=1000)
    assert isclose(optical, displacement + velocity, abs_tol=2e-7)
    print(f"cap={cap:.6f}  Kirchhoff coefficient ratio={ratios[-1]:.6f}  "
          f"position={displacement:.8f}  velocity={velocity:.8f}  optical={optical:.8f}")


def check_focus():
    # h=(t-z)^2 diag(1,-1,0), x along z. The ring mean of Q_xx-Q_yy is
    # (1-mu)^4/2. Differentiate the smooth scaled Kirchhoff profile in time.
    radius = 1e-5
    step = 0.04

    def profile_at_time(offset):
        time = 1 + offset * radius

        def integrand(s):
            mu = (time - (time**2-radius**2)/(2*s)) / radius
            return s * (0.5-s) * (1.5-s) * (1-mu)**4 / 12

        return -integrate(integrand, 0.5, (time+radius)/2, RULE) / (8*pi*radius**2)

    values = {index: profile_at_time(index*step) for index in range(-3, 4)}
    second = (-values[2] + 16*values[1] - 30*values[0]
              + 16*values[-1] - values[-2]) / (12*step**2)
    third = (-values[3] + 8*values[2] - 13*values[1]
             + 13*values[-1] - 8*values[-2] + values[-3]) / (8*step**3)
    sine_ratio = 2 * second / (1/(384*pi))
    cosine_ratio = -2 * third / (-1/(96*pi))
    assert abs(sine_ratio-1) < 1e-4 and abs(cosine_ratio-1) < 1e-4
    print(f"focus: sine coefficient ratio={sine_ratio:.6f}  cosine coefficient ratio={cosine_ratio:.6f}")


if __name__ == "__main__":
    for cap_fraction in (1/3, 2/3):
        check(cap_fraction)
    check_focus()
