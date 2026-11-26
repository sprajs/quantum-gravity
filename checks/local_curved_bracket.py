"""Check the optical boost derivative and the local graviton polarization factor."""

from fractions import Fraction
from math import cos, exp, fsum, pi, sin, sqrt

from weak_curved import GAUSS, optics, radius, ray, root


def sky():
    # Composite Gauss integration in cos(theta), periodic azimuth quadrature.
    for panel in range(2):
        for node, weight in GAUSS:
            mu = panel - 0.5 + node / 2
            for azimuth in range(12):
                phi = (azimuth + 0.5) * 2 * pi / 12
                yield mu, phi, weight / 48


def unit_radius_preparation(kappa, caps):
    # Use a fixed duration temporarily. A final change of length unit sets M=1.
    radius_integral = area_integral = 0.0
    numerators = [0.0 for cap in caps]
    for mu, phi, weight in sky():
        ku, _, waist, _, distance, _ = ray(mu, phi, kappa, 0.0)
        frequency = kappa * ku
        radius_integral += weight * distance
        area_integral += weight * distance ** 2
        for i, cap in enumerate(caps):
            cut = root(lambda s: radius(s, frequency) - cap * distance, waist)
            affine = optics(cut, frequency)[1] * (waist - cut)
            numerators[i] += weight * distance * (affine - (1-cap) * distance)
    matched_radius = area_integral / radius_integral
    return (kappa * matched_radius) ** 4, [value / area_integral for value in numerators]


def optical_slopes(kappa, caps):
    low_w, low_clocks = unit_radius_preparation(0.99 * kappa, caps)
    high_w, high_clocks = unit_radius_preparation(1.01 * kappa, caps)
    return [-(high-low)/(high_w-low_w) for low, high in zip(low_clocks, high_clocks)]


def polarization_factor():
    # E = diag(1,-1,0)/2, B_12=B_21=1/2. Their squared norms sum to one.
    def electric(a, b):
        return (a[0]*b[0] - a[1]*b[1])/2

    def magnetic(a, b):
        return (a[0]*b[1] + a[1]*b[0])/2

    def polarizations(form, theta, phi):
        return ((form(theta, theta)-form(phi, phi))/sqrt(2),
                sqrt(2)*form(theta, phi))

    samples = []
    for mu, azimuth, weight in sky():
        theta = (mu*cos(azimuth), mu*sin(azimuth), -sqrt(1-mu**2))
        phi = (-sin(azimuth), cos(azimuth), 0.0)
        ep, ec = polarizations(electric, theta, phi)
        bp, bc = polarizations(magnetic, theta, phi)
        samples.append(weight * ((ep+bc)**2 + (ec-bp)**2))
    return fsum(samples)


def delay_derivative():
    # Two centered Gaussian timing windows for an independent Fourier sign check.
    # The second mixes means -1 and 2 with weights 2/3 and 1/3; both variances
    # within the mixture and the variance of the first window equal one.
    mixture = ((-1.0, 2/3), (2.0, 1/3))
    derivative = 0.0
    for mean, weight in mixture:
        x = mean / sqrt(2)
        hermite = x**5 - 10*x**3 + 15*x
        derivative += weight * exp(-mean**2/4) * hermite / (sqrt(4*pi)*sqrt(2)**5)

    for width in (1.0, 0.25):
        panels = 1000
        step = 10 / (panels * width)
        samples = []
        for i in range(panels + 1):
            k = i * step
            sine_transform = exp(-(width*k)**2) * fsum(
                weight * sin(k*width*mean) for mean, weight in mixture)
            simpson = 1 if i in (0, panels) else (4 if i % 2 else 2)
            samples.append(simpson * k**5 * sine_transform)
        measured = width**6 * fsum(samples) * step / (3*pi)
        assert abs(measured - derivative) < 1e-12
    return derivative


def main():
    caps = Fraction(1, 3), Fraction(1, 2)
    slopes = [-Fraction(4, 45) * (Fraction(1, 20) - a**4/4 + a**5/5)
              for a in caps]
    print("Weak-wave launch coefficients at caps 1/3 and 1/2:", *slopes)
    for kappa in (0.35, 0.20):
        numerical = optical_slopes(kappa, [float(a) for a in caps])
        errors = [abs(actual/expected-1) for actual, expected in zip(numerical, slopes)]
        assert max(errors) < 0.0006
        print(f"Direct matched-radius derivatives, kappa={kappa:.2f}:"
              f" {numerical[0]:.9f}, {numerical[1]:.9f}")
    projected = polarization_factor()
    assert abs(projected - 2/5) < 2e-14
    coefficient = Fraction(32, 5) * slopes[0] * slopes[1]
    assert coefficient == Fraction(6032, 61509375)
    print(f"Angular TT norm / superenergy: {projected:.8f}")
    print(f"Gaussian delay test, scaled fifth derivative: {delay_derivative():.8f}")
    print(f"Weak h^(-6) coefficient / (G W R^10 eta^(5)(0)): {coefficient}")


if __name__ == "__main__":
    main()
