# /// script
# requires-python = ">=3.11,<3.15"
# dependencies = ["matplotlib==3.10.8"]
# ///
"""Plot proper-time windows and the sharp limit of two quadrupole clock readings.

Run `uv run --script tools/plot_timing.py` at the repository root.
Expected output: clock-timing.png
"""

from fractions import Fraction
from math import erfc, exp, pi, sqrt
from pathlib import Path
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "checks"))
from timing_two_clocks import bracket, response


def later_probability(offset):
    """P(t5 > t4) for two Gaussian weights of equal width, offset in single-window rms."""
    return erfc(-offset / 2) / 2


def main():
    # The optical responses and their two one-sided brackets use G_N = 1.
    first, second = response({4: Fraction(1)}), response({5: Fraction(1)})
    later = bracket(first, second, Fraction(0), left_trace=True)
    earlier = bracket(first, second, Fraction(0), left_trace=False)
    lower, upper = 1e4 * float(earlier), 1e4 * float(later)
    midpoint = (lower + upper) / 2

    ink, teal, rust = "#243e49", "#076861", "#9c481c"
    grid = "#ccd7d8"
    plt.rcParams.update({"font.size": 9, "text.color": ink, "axes.labelcolor": ink,
                         "axes.edgecolor": ink, "xtick.color": ink, "ytick.color": ink,
                         "axes.titleweight": "bold", "axes.titlesize": 10})
    fig, (windows, limits) = plt.subplots(1, 2, figsize=(7.35, 2.85),
                                         layout="constrained")
    fig.get_layout_engine().set(w_pad=0.06, h_pad=0.06, wspace=0.07)

    time = [i / 60 for i in range(-210, 331)]
    for center, color, style, label in [
        (0, teal, "-", r"$s^4$ reading"),
        (2, rust, "--", r"$s^5$ reading"),
    ]:
        density = [exp(-(t-center)**2 / 2) / sqrt(2*pi) for t in time]
        windows.fill_between(time, density, color=color, alpha=0.12)
        windows.plot(time, density, ls=style, lw=2, color=color, label=label)
        windows.vlines(center, 0, 1/sqrt(2*pi), colors=color, ls=":", lw=1)
    windows.annotate("", xy=(2, 0.45), xytext=(0, 0.45),
                     arrowprops={"arrowstyle": "<->", "color": ink, "shrinkA": 0, "shrinkB": 0})
    windows.text(1, 0.47, r"$\Delta=2\sigma$", ha="center", va="bottom")
    windows.set(title="Two windows on one clock", xlim=(-3.5, 5.5), ylim=(0, 0.59),
                xticks=[-2, 0, 2, 4], yticks=[0, 0.2, 0.4],
                xlabel=r"Central proper time, $(t-\mu_4)/\sigma$",
                ylabel=r"Window density, $\sigma\,w(t)$")
    windows.legend(loc="upper left", ncol=2, frameon=False, fontsize=8,
                   columnspacing=1.2, handlelength=1.7, borderaxespad=0.1)

    offsets = [i / 40 for i in range(-240, 241)]
    values = [lower + (upper-lower) * later_probability(x) for x in offsets]
    for level in (lower, upper):
        limits.axhline(level, color=ink, linewidth=0.8, linestyle=(0, (4, 3)))
    limits.axvline(0, color=grid, linewidth=0.8)
    limits.plot(offsets, values, color=teal, lw=2.3)
    limits.plot(0, midpoint, "o", color=ink, markersize=4)
    limits.annotate("Same center", xy=(0, midpoint), xytext=(-6, 8),
                    textcoords="offset points", ha="right", fontsize=8)
    limits.plot(2, lower + (upper-lower) * later_probability(2), "o",
                markerfacecolor="white", markeredgecolor=teal, markersize=5)
    limits.text(-5.8, lower + 0.13, r"$s^5$ earlier", color=ink, fontsize=8)
    limits.text(5.8, upper + 0.09, r"$s^5$ later", color=ink, fontsize=8, ha="right")
    limits.set(title="Bracket as both windows narrow", xlim=(-6, 6), ylim=(0, 3.33),
               xticks=[-6, -4, -2, 0, 2, 4, 6], yticks=[0, lower, midpoint, upper],
               yticklabels=["0", f"{lower:.3f}", f"{midpoint:.3f}", f"{upper:.3f}"],
               xlabel=r"Center offset, $\Delta/\sigma$",
               ylabel=r"Limiting bracket ($10^{-4}\,G_N$)")
    for axis in (windows, limits):
        axis.set_axisbelow(True)
        axis.spines[["right", "top"]].set_visible(False)
        axis.tick_params(labelsize=8)
    windows.grid(axis="y", color=grid, linewidth=0.55)

    target = ROOT / "figures" / "clock-timing.png"
    fig.savefig(target, dpi=300, facecolor="white")
    plt.close(fig)
    print(target.name)


if __name__ == "__main__":
    main()
