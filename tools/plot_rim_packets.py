# /// script
# requires-python = ">=3.11,<3.15"
# dependencies = ["matplotlib==3.10.8"]
# ///
"""Plot the two master pulses and the measured flat-diamond clock Hessian."""
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "checks"))
from match_packets import bump, hessian


def main():
    teal, rust, ink = "#066861", "#a65327", "#253e49"
    fig, (profiles, response) = plt.subplots(1, 2, figsize=(9.4, 3.35),
                                             layout="constrained")
    x = [i / 125 for i in range(-420, 421)]
    outer = [bump(v - 2) for v in x]
    inner = [-bump(v + 2) for v in x]
    profiles.axhline(0, color=ink, lw=0.8)
    profiles.axvline(0, color=ink, lw=0.9, ls=":")
    for values, color in [(inner, rust), (outer, teal)]:
        profiles.fill_between(x, values, color=color, alpha=0.22)
        profiles.plot(x, values, color=color, lw=1.6)
    profiles.text(-2, 0.38, "Inside cap", ha="center", color=rust, fontsize=9)
    profiles.text(2, -0.55, "On sheet", ha="center", color=teal, fontsize=9)
    profiles.text(0.06, 1.55, "Rim", ha="left", color=ink, fontsize=9)
    profiles.set(title="Where the two wave profiles sit",
                 xlabel=r"Distance from the rim in pulse widths, $(v-a)/\eta$",
                 ylabel=r"Scaled radial master $\eta F(2v)$", xlim=(-3.4, 3.4))

    widths = [2 ** -j for j in range(7, 18, 2)]
    values = [hessian(width) for width in widths]
    response.set_xscale("log", base=2)
    response.invert_xaxis()
    response.axhline(-0.75, ls="--", color=rust, lw=1.4, label="Exact limit  −3/4")
    response.plot(widths, values, color=teal, lw=1.1, marker="o", markersize=5,
                  label="Direct integration")
    response.set(title="Response of the sharp clock",
                 xlabel=r"Pulse width $\eta$ (decreasing)", ylabel="Mixed second variation",
                 xticks=widths[::2], xticklabels=[r"$2^{-7}$", r"$2^{-11}$", r"$2^{-15}$"],
                 ylim=(-0.785, -0.45))
    response.legend(loc="upper right", frameon=False, fontsize=8)
    for axis in (profiles, response):
        axis.spines[["right", "top"]].set_visible(False)
        axis.tick_params(labelsize=8)
        axis.title.set_fontsize(11)
        axis.grid(axis="y", lw=0.55, color="#d3dfe0")
        axis.set_axisbelow(True)
    destination = ROOT / "figures" / "rim-packets.png"
    fig.savefig(destination, dpi=180, facecolor="white")
    plt.close(fig)
    print(destination.name)


if __name__ == "__main__":
    main()
