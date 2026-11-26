# /// script
# requires-python = ">=3.11,<3.15"
# dependencies = ["matplotlib==3.10.8"]
# ///
"""Run `uv run tools/plot_boost.py` to rebuild figures/boost-response.png.

The expected maximum absolute difference on the 61-point grid is 5.81e-5.
"""

import math
from pathlib import Path
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from checks import boost_observable as model


def main():
    packet = model.packet(144)
    rapidities = [j / 20 for j in range(61)]
    vacuum = [model.normalized_kernel(eta, packet) for eta in rapidities]
    weights = model.finite_line_weights(packet)
    finite = [
        math.fsum(weight * math.cos(k * model.GRID_STEP * eta)
                  for k, weight in enumerate(weights))
        for eta in rapidities
    ]
    differences = [abs(a - b) for a, b in zip(finite, vacuum)]
    recurrence = rapidities.index(2)

    ink, grid = "#26384A", "#DAE1E4"
    smooth, fine, coarse = "#187A70", "#334D83", "#A44716"
    plt.rcParams.update({
        "font.size": 12, "text.color": ink, "axes.labelcolor": ink,
        "xtick.color": ink, "ytick.color": ink, "axes.edgecolor": grid,
        "axes.spines.right": False, "axes.spines.top": False,
    })
    fig, (response, residual) = plt.subplots(
        2, 1, sharex=True, figsize=(8.7, 6.1), height_ratios=[2.4, 1],
    )
    fig.subplots_adjust(left=0.14, right=0.96, top=0.80, bottom=0.12, hspace=0.26)
    fig.suptitle("Shear correlation under a relative boost", x=0.14, y=0.965,
                 ha="left", fontsize=21, fontweight="bold")
    fig.text(0.14, 0.866, "Theory comparison  ·  Matched packets with 1% fractional half-width",
             fontsize=12)

    response.plot(rapidities, vacuum, color=smooth, lw=3, label="Smooth vacuum")
    response.plot(rapidities, finite, markevery=5, ls="none", marker="o", ms=6,
                  mfc="white", mec=fine, mew=1.4, label="251-area model")
    response.plot(2, 1, ls="none", marker="D", color=coarse, ms=8)
    response.annotate("Coarse lattice return\n$R(2)=1$", (2, 1), (12, -1),
                      textcoords="offset points", color=coarse, va="center")
    response.annotate(f"$R(2)={vacuum[recurrence]:.5f}$", (2, vacuum[recurrence]),
                      (12, 8), textcoords="offset points", color=smooth)
    response.set(ylabel=r"Correlation ratio $R(\eta)$", ylim=(0.12, 1.13),
                 yticks=[0.2, 0.4, 0.6, 0.8, 1])
    response.legend(loc="lower left", frameon=False)
    residual.plot(rapidities, [1e5 * d for d in differences], color=fine, lw=1.5,
                  marker=".", ms=3)
    residual.set(ylabel="Absolute difference\n" + r"(units of $10^{-5}$)",
                 xlabel=r"Relative rapidity $\eta$", ylim=(-0.2, 6.4),
                 yticks=[0, 2, 4, 6], xlim=(-0.025, 3.025))
    residual.text(0.025, 0.80, "251-area model vs. vacuum", transform=residual.transAxes,
                  fontsize=11, color=fine)
    for ax in (response, residual):
        ax.grid(axis="y", color=grid, linewidth=0.8)
        ax.set_axisbelow(True)
        ax.tick_params(length=0, pad=6)

    target = ROOT / "figures" / "boost-response.png"
    target.parent.mkdir(exist_ok=True)
    fig.savefig(target, dpi=180, facecolor="white")
    plt.close(fig)
    print(f"{target.name}: maximum sampled absolute difference {max(differences):.8g}")


if __name__ == "__main__":
    main()
