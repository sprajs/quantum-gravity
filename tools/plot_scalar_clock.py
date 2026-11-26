# /// script
# requires-python = ">=3.11,<3.15"
# dependencies = ["matplotlib==3.10.8"]
# ///
"""Reproduce the mean geometric clock excess for the two scalar preparations."""

from math import pi
from pathlib import Path
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from checks.matter_null_energy import FUTURE, PAST, clock_coefficient


def main():
    fig, ax = plt.subplots(figsize=(7.6, 3.7), layout="constrained")
    phases = [i / 200 for i in range(401)]
    ax.axhline(0, color="#626C76", lw=0.9)
    for name, integrals, color, style in [
        ("From the past tip", PAST, "#24665F", "-"),
        ("From the future tip", FUTURE, "#8D420B", "--"),
    ]:
        ax.plot(phases, [clock_coefficient(x*pi, *integrals) for x in phases],
                color=color, ls=style, lw=2.5, label=name)
        for x in (0, 1, 2):
            ax.plot(x, clock_coefficient(x*pi, *integrals), "o", color=color, ms=4)
    ax.set(xlim=(-0.03, 2.03), ylim=(-0.016, 0.020), xticks=[0, .5, 1, 1.5, 2],
           xticklabels=["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"],
           xlabel="Relative phase between vacuum and two particles",
           ylabel=r"Clock excess  $R\,E^{(1)}/\ell_P^2$")
    ax.grid(axis="y", color="#D7E0E1", lw=0.7)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Scalar interference in the two faces of a causal diamond",
                 loc="left", fontsize=13, weight="bold", pad=12)
    ax.legend(loc="lower left", frameon=False, fontsize=9)
    target = ROOT / "figures" / "scalar-clock-phase.png"
    fig.savefig(target, dpi=180, facecolor="white")
    plt.close(fig)
    print(target.name)


if __name__ == "__main__":
    main()
