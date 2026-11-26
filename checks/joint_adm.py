"""Compare the capped clock and full-cone pairing for a spherical collar."""

from math import exp, expm1, log


def simpson(function, lo, hi, panels=128):
    step = (hi - lo) / panels
    total = function(lo) + function(hi)
    for index in range(1, panels):
        total += (4 if index % 2 else 2) * function(lo + index * step)
    return total * step / 3


def bump(s):
    return exp(1 - 1 / (1 - s * s)) if abs(s) < 1 else 0.0


cap = 0.5


def trace_density(mu):
    amplitude = 1 - mu * mu
    power = amplitude**2 + 1
    kernel_at_cap = cap * expm1(-power * log(cap)) / power
    return -kernel_at_cap * amplitude**2 / cap


# For an even axisymmetric integrand the spherical mean is its integral
# over mu = cos(theta) from 0 to 1.
trace = simpson(trace_density, 0, 1, 256)
print(f"Spherical clock trace limit {trace:.9f}")
previous = None
for width in (1 / 32, 1 / 64, 1 / 128, 1 / 256):
    def clock_bulk(mu):
        amplitude = 1 - mu * mu

        def density(s):
            v = cap + width * s
            return (v / cap)**(amplitude**2) * amplitude**2 * bump(s) / v

        return width * simpson(density, 0, 1)

    def direct_clock(mu):
        amplitude = 1 - mu * mu
        power = 1 + amplitude**2

        def density(s):
            if s == 1:
                return 0.0
            v = cap + width * s
            kernel = -expm1(power * log(v)) / (cap**(power - 1) * power)
            derivative = -2 * s * bump(s) / (1 - s * s)**2
            return kernel * amplitude**2 / v * (derivative - width * bump(s) / v)

        return simpson(density, 0, 1, 512)

    variation = trace + simpson(clock_bulk, 0, 1, 256)
    assert abs(variation - simpson(direct_clock, 0, 1, 256)) < 1e-9
    # c = 1, X = v^2 (1-mu^2), Y = (1-mu^2) bump((v-cap)/width).
    pairing = 4 * width * simpson(lambda mu: (1 - mu * mu)**2, 0, 1)
    pairing *= simpson(lambda s: (cap + width * s) * bump(s), -1, 1)
    if previous is not None:
        assert abs(pairing / previous - 0.5) < 1e-12
    previous = pairing
    print(f"width {width:.8f}  clock {variation:.9f}  full-cone pairing {pairing:.9f}")
