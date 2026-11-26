#!/usr/bin/env python3
"""Check the shear-free corner clock in audit/regulator-program.md.

q is multiplication on L²(R,dq). The reported finite count is for the
function of the Hermite-truncated q matrix. Its off-diagonals are sqrt(k/2).
The continuum clock subspace is L²([-q_star,q_star]) for ratios above one.
"""

import argparse
import math


def squared_clock_excess(q):
    """Return (T(q)/u0)^2 - 1, including its value at the round corner."""
    t = abs(q) / 2
    if t < 1.0e-3:
        return t * t * (1 / 3 - t * t / 45 + 2 * t**4 / 945)
    return t / math.tanh(t) - 1


def corner_interval(ratio):
    """Bracket the nonnegative root of (q/2)coth(q/2) = ratio²."""
    target = (ratio - 1) * (ratio + 1)
    lower, upper = 0.0, max(2.0, 2 * (target + 1))
    while math.nextafter(lower, upper) < upper:
        midpoint = lower + (upper - lower) / 2
        if squared_clock_excess(midpoint) < target:
            lower = midpoint
        else:
            upper = midpoint
    return lower, upper


def inertia(n, x):
    """Count eigenvalues at or below x using the shifted tridiagonal LDL pivots."""
    pivot = -x
    count = 0
    for k in range(1, n + 1):
        # A zero pivot at an intermediate minor uses the right-hand limit in x.
        if abs(pivot) < 1.0e-200:
            pivot = -1.0e-200
        count += pivot < 0
        if k != n:
            pivot = -x - k / (2 * pivot)
    return count


def finite_count(n, q):
    # The Hermite nodes are symmetric about zero. Subtract both outside tails.
    return 2 * inertia(n, q) - n


def positive_integer(value):
    size = int(value)
    if size < 1:
        raise argparse.ArgumentTypeError("provide a positive matrix dimension")
    return size


def threshold(value):
    ratio = float(value)
    if ratio < 0 or not math.isfinite(2 * ratio * ratio):
        raise argparse.ArgumentTypeError("provide a nonnegative finite ratio with representable square")
    return ratio


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ratios", type=threshold, nargs="+", default=[1.10, 1.50])
    parser.add_argument("--dimensions", type=positive_integer, nargs="+",
                        default=[16, 64, 256, 1024, 4096])
    options = parser.parse_args()
    print("ell/u0  q_star      vacuum_probability  continuum_rank  " +
          "  ".join(f"n={n}" for n in options.dimensions))
    for ratio in options.ratios:
        if ratio <= 1:
            # At equality, the singleton q=0 has zero Lebesgue measure, while
            # every odd Hermite matrix has exactly one eigenvalue at zero.
            counts = [str(n % 2 if ratio == 1 else 0) for n in options.dimensions]
            q_value = "0" if ratio == 1 else "empty"
            print(f"{ratio:14.12g}  {q_value:>10}  {0:18}  {0:14}  " + "  ".join(counts))
            continue
        lower, upper = corner_interval(ratio)
        q = lower + (upper - lower) / 2
        counts = []
        for n in options.dimensions:
            low_count, high_count = finite_count(n, lower), finite_count(n, upper)
            counts.append(str(low_count) if low_count == high_count
                          else f"[{low_count},{high_count}]")
        print(f"{ratio:14.12g}  {q:10.7f}  {math.erf(q):18.12g}  {'infinite':>14}  " +
              "  ".join(counts))


if __name__ == "__main__":
    main()
