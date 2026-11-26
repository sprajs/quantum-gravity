"""Exact full-sky contractions of the spherical Weyl source in affine units."""

from fractions import Fraction as F


RADIUS = F(2)
CAP = RADIUS / 3
SCREEN_MEAN = F(3, 5)


def integrate(fn, lo, hi):
    # Closed seven-node Newton-Cotes is exact through degree seven.
    weights = (41, 216, 27, 272, 27, 216, 41)
    return (hi - lo) * sum(w * fn(lo + i * (hi - lo) / 6)
                           for i, w in enumerate(weights)) / 840


def kernel(t, inside):
    # H'_W = t B. Return K, K', and the ordinary one-sided K''.
    if inside:
        scale = -(RADIUS - CAP) ** 2 / 4
        return scale * t**2, 2 * scale * t, 2 * scale
    gap = RADIUS - t
    return (-t**2 * gap**2 / 4,
            (-t * gap**2 + t**2 * gap) / 2,
            -gap**2 / 2 + 2 * t * gap - t**2 / 2)


def cone_integral(fn):
    return SCREEN_MEAN * (
        integrate(lambda t: fn(t, *kernel(t, True)), F(0), CAP)
        + integrate(lambda t: fn(t, *kernel(t, False)), CAP, RADIUS)
    )


def metric_pair(jets, jump):
    # Jets contract D_A D_B h_kk, D_A h_Bk, h_AB against B, respectively.
    def bulk(t, k, dk, ddk):
        hh, kh, ab = jets(t)
        return -(k * hh + 2 * dk * kh + ddk * ab) / 2

    rim = -SCREEN_MEAN * jump * jets(CAP)[2] / 2
    return cone_integral(bulk) + rim, rim


def main():
    # Mean of |B|^2 from the actual full-sphere projection, z=cos(theta).
    assert integrate(lambda z: 9 * (1 - z*z)**2 / 8, F(0), F(1)) == SCREEN_MEAN
    assert kernel(F(0), True)[:2] == kernel(RADIUS, False)[:2] == (0, 0)
    assert kernel(CAP, True)[0] == kernel(CAP, False)[0]
    jump = kernel(CAP, False)[1] - kernel(CAP, True)[1]
    assert jump == CAP**2 * (RADIUS - CAP) / 2

    # Static harmonic reference W used on both slots: C_AkBk=-3 B_AB/2.
    vacuum, vacuum_rim = metric_pair(lambda t: (3, 0, 0), jump)
    assert vacuum_rim == 0
    assert vacuum == SCREEN_MEAN * integrate(
        lambda s: s**3 * (RADIUS-s) / 4, CAP, RADIUS) == F(464, 2025)
    assert vacuum == cone_integral(lambda t, k, dk, ddk: -3*k/2)

    # h_ij=t^3 S_ij, h_0mu=0. Its screen tidal tensor C_AkBk=-3t B_AB.
    # Jacobi gives H'_h=(3/2)t^2 B. The probe is smooth and off shell.
    direct = SCREEN_MEAN * integrate(
        lambda s: s * (RADIUS-s) * s * (3*s**2/2) / 4, CAP, RADIUS)
    curvature = cone_integral(lambda t, k, dk, ddk: -3*t*k)
    metric, rim = metric_pair(lambda t: (0, 0, t**3), jump)
    assert direct == curvature == metric and rim < 0

    # Pure gauge h_munu = 2 partial_(mu xi_nu). Use a lower-index covector
    # xi_0=t^3 S_ij x^i x^j, xi_i=t^2 S_ij x^j. All three metric terms enter.
    gauge, gauge_rim = metric_pair(
        lambda t: (12*t**2, 2*t + 2*t**3, 2*t**2), jump)
    assert gauge == 0 and gauge_rim != 0
    print(f"Vacuum self-pairing: {vacuum}")
    print(f"Jacobi, Weyl and metric pairings: {direct}, {curvature}, {metric}")
    print(f"Metric rim term: {rim}")
    print(f"Pure gauge pairing: {gauge} (rim alone: {gauge_rim})")


if __name__ == "__main__":
    main()
