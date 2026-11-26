# /// script
# requires-python = ">=3.11,<3.15"
# dependencies = ["matplotlib==3.10.8"]
# ///
"""Reproduce figures/clock-floor.png with uv run --script tools/plot_clock_floor.py."""

import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "checks"))
from existence_limit import prefix_floor


def clock_lower_bound(cutoff):
    # All radiation modes through K=J=cutoff pass with unit amplitude.
    response_sum = cutoff * (cutoff + 1) * ((cutoff + 1)**2 - 4)
    focusing = prefix_floor(0.25, 0.625, 10000, response_sum)
    late_fraction = 0.5
    max_cost = 1 + late_fraction * math.expm1(4)
    coupled_bound = (1 / max_cost + 1 / (late_fraction * math.e * focusing))**-0.5
    return max(1.0, coupled_bound)


def main():
    modes = list(range(2, 17))
    bounds = [clock_lower_bound(n) for n in modes]
    assert clock_lower_bound(7) < 1.2 < clock_lower_bound(8)
    fig, ax = plt.subplots(figsize=(7.4, 3.1), layout="constrained")
    ax.plot(modes, bounds, "o-", color="#17635e", linewidth=1.8, markersize=4)
    ax.axhline(1.2, color="#9a501c", linestyle="--")
    ax.text(12.5, 1.28, "Clock ceiling 1.2", color="#844619")
    ax.annotate(f"First certified exclusion\nK = J = 8, floor {bounds[6]:.3f}",
                xy=(8, bounds[6]), xytext=(3.4, 2.4),
                arrowprops={"arrowstyle": "->", "color": "#234454"},
                color="#234454", fontsize=10)
    ax.set(xlabel="Largest radial and angular mode retained (K = J)",
           ylabel="Certified floor / round reading",
           xticks=[2, 4, 6, 8, 10, 12, 14, 16], xlim=(1.5, 16.5))
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.18)
    fig.savefig(ROOT / "figures" / "clock-floor.png", dpi=200)
    print(f"clock-floor.png  K=J=8 bound {bounds[6]:.8f}")


if __name__ == "__main__":
    main()
