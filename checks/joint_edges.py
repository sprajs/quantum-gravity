"""Check cylindrical cap matching and a spherical plane-wave clock endpoint."""

from decimal import Decimal as D, localcontext
from fractions import Fraction as F

from observable_optics import axis


def spherical_rim():
    # The leading term is already quadratic in the perturbed optical data.
    # Its two factors can be evaluated at the unperturbed half-radius cut.
    amplitude = D("1e-5")
    cap = D("0.5")
    coefficient = D(0)
    # Boole's closed rule is exact on the leading angular polynomial nu**4.
    for index, weight in enumerate([7, 32, 12, 32, 7]):
        nu = D(index) / 4
        curvature = amplitude * nu**2
        jx, dx = axis(curvature, cap)
        jy, dy = axis(-curvature, cap)
        shear_per_amplitude = (dx / jx - dy / jy) / amplitude
        polarization_per_amplitude = (jx / jy).ln() / amplitude
        coefficient -= (D(weight) / 90 * cap * (1 - cap) / 2
                        * shear_per_amplitude * polarization_per_amplitude)
    expected = F(-1, 1440)
    assert abs(coefficient - D(expected.numerator) / D(expected.denominator)) < D("1e-13")
    print(f"Spherical half-radius rim coefficient in units of L A dA: {expected}")


def main():
    # In flat cylindrical coordinates, R = b**2 + u and q = diag(R**2, 1).
    b = F(1, 2)
    radius = b**2
    metric = (radius**2, F(1))
    delta_u = 1 - radius
    dz = 1 / b  # unit weighted trace Y_C = b Dz_C in the paper's chart
    delta_metric = (metric[0] * dz, -metric[1] * dz)
    base_shape = (radius, F(0))

    # Tilt the cap normal in the (t,R) plane. Its angular derivative
    # contributes to K_As and cancels the tilt's derivative in log(a).
    exp_rapidity = F(3, 2)
    cosh = (exp_rapidity + 1 / exp_rapidity) / 2
    sinh = (exp_rapidity - 1 / exp_rapidity) / 2
    angular_rapidity_derivative = F(4, 7)
    angular_scale_log_derivative = F(2, 9)
    cap_curvature = tuple(sinh * shape for shape in base_shape)
    rim_curvature = tuple(cosh * shape for shape in base_shape)

    def endpoint(scale):
        a = scale * (cosh - sinh)
        optical = tuple(a * (k_cap + k_rim)
                        for k_cap, k_rim in zip(cap_curvature, rim_curvature))
        assert optical == tuple(scale * shape for shape in base_shape)

        # Directly project the normal-plane derivatives using diag(-1,1).
        # The derivative of the cylindrical radial unit vector is tangential.
        normal_t = (cosh - sinh) / (2 * a)
        normal_r = (sinh - cosh) / (2 * a)
        scale_derivative = scale * angular_scale_log_derivative
        twist = (normal_t - normal_r) * scale_derivative
        mixed_cap_curvature = (cosh**2 - sinh**2) * angular_rapidity_derivative
        angular_log_a = angular_scale_log_derivative - angular_rapidity_derivative
        assert angular_log_a + mixed_cap_curvature == twist

        expansion = sum(chi / q for chi, q in zip(optical, metric))
        # Use 16 pi G / sqrt(h) as the unit for the ADM momentum.
        cap_ss = F(5, 11)  # controlled by the extension of the cap away from C
        cap_trace = cap_ss + sum(k / q for k, q in zip(cap_curvature, metric))
        adm_ss = cap_ss - cap_trace
        rim_trace = sum(k / q for k, q in zip(rim_curvature, metric))
        assert a * (rim_trace - adm_ss) == expansion
        shear = tuple(chi - expansion * q / 2 for chi, q in zip(optical, metric))
        assert sum(dq / q for dq, q in zip(delta_metric, metric)) == 0
        contraction = sum(sig * dq / q**2
                          for sig, dq, q in zip(shear, delta_metric, metric))
        return contraction, -b * (delta_u / scale) * contraction / 2

    contraction, coefficient = endpoint(F(1))
    assert (contraction, coefficient) == (8, F(-3, 2))
    assert endpoint(F(7, 3))[1] == coefficient
    print(f"Optical shear contraction for unit cap trace: {contraction}")
    print(f"Clock endpoint from the cap geometry: {coefficient}")
    print("Affine rescaling leaves the coefficient invariant: yes")
    with localcontext() as context:
        context.prec = 50
        spherical_rim()


if __name__ == "__main__":
    main()
