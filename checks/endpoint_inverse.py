"""Fixed-area Green kernel on a graph of rotations, with 2c = L = 1."""

from cmath import exp
from math import exp as real_exp, expm1, isclose


def main():
    source_mean = 0.3 - 0.2j
    for angle in (0.2, 1.1, 2.9):
        rotation = exp(1j * angle)
        constant = 1 / (rotation - 1)
        start = constant * source_mean
        assert abs(rotation * start - (start + source_mean)) < 1e-14
        assert abs(1 + constant + constant.conjugate()) < 1e-14
        # Integrate the step kernel on each side of v for f(w)=1-2w.
        for v in (0, 0.1, 0.4, 0.8, 1):
            below = v * (1 - v)
            above = (1 - v) * (1 - (1 + v))
            result = (1 + constant) * below + constant * above
            assert abs(result - v * (1 - v)) < 1e-14
    for t in (0.1, 0.01, 0.001):
        angle = t * expm1(t)
        start = t / (exp(1j * angle) - 1)
        print(f"t={t:g}, |t X(0)|={abs(t * start):.7f}")
        assert isclose(abs(t * start), 1, abs_tol=t)

    # For z=2 log(v)+a(3/v-4), the prefix focusing integral is elementary.
    def clock(a):
        n = 10000
        dv = 0.5 / n
        total = 0
        for i in range(n):
            v = 0.5 + (i + 0.5) * dv
            correction = 3*a*(1/v-2) + 9*a*a*(4-1/v**2)/8
            total += 2*v*real_exp(correction)
        return total * dv

    step = 1e-5
    derivative = (clock(step) - clock(-step)) / (2 * step)
    assert isclose(clock(0), 0.75, abs_tol=1e-12)
    assert isclose(derivative, -1.5, abs_tol=1e-8)
    print(f"geodesic clock={clock(0):.8f}, endpoint derivative={derivative:.8f}")


if __name__ == "__main__":
    main()
