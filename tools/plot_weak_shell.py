# /// script
# requires-python = ">=3.11,<3.15"
# dependencies = ["matplotlib==3.10.8"]
# ///
"""Draw the two spherical fronts and the principal terms on the flat waist.

From the repository root, run `uv run --script tools/plot_weak_shell.py`.
Expected output: weak-shell.png (written under figures/).
"""
from math import erfc, exp, pi, sqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
CAP = 1 / 3
WAIST = 1
TEAL = "#08675e"
RUST = "#a65327"
INK = "#263f49"
MUTED = "#5a6970"


def spacetime(ax):
    turn = 2 * CAP
    shell = WAIST - turn
    # t-r=2a reaches the future boundary when t+r=2R.
    exit_radius = WAIST - CAP
    ax.fill([0, WAIST, 0], [0, WAIST, 2 * WAIST], color="#f1f5f5")
    ax.plot([0, WAIST, 0], [0, WAIST, 2 * WAIST], color=MUTED, lw=1.4)
    ax.axvline(0, color=MUTED, lw=1)
    ax.hlines(WAIST, 0, WAIST, color=MUTED, lw=1, ls=(0, (3, 3)))
    ax.plot([CAP, 0], [CAP, turn], color=RUST, lw=2.8)
    ax.plot([0, exit_radius], [turn, WAIST + CAP], color=TEAL, lw=2.8)
    for r, t, color in [(CAP, CAP, RUST), (shell, WAIST, TEAL)]:
        ax.plot(r, t, "o", ms=6, color=color, mec="white", mew=.8, zorder=4)

    ax.annotate(r"$t+r=2a$", xy=(.16, turn - .16), xytext=(.66, .52),
                color=RUST, arrowprops=dict(arrowstyle="-", color=RUST, lw=.8))
    ax.annotate(r"$t-r=2a$", xy=(.53, turn + .53), xytext=(.70, 1.54),
                color=TEAL, arrowprops=dict(arrowstyle="-", color=TEAL, lw=.8))
    ax.annotate(r"Cap rim ($a=1/3$)", xy=(CAP, CAP), xytext=(.52, .23),
                color=INK, fontsize=9,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=.7))
    ax.annotate(r"$r_* = 1/3$", xy=(shell, WAIST), xytext=(.42, .84),
                color=INK, fontsize=9,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=.7))
    ax.text(.63, 1.035, "Waist", color=MUTED, fontsize=9)
    ax.set(title="Radial section of the flat diamond", xlabel=r"Radius $r$",
           ylabel=r"Time $t$", xlim=(-.04, 1.18), ylim=(-.025, 2.06),
           xticks=[0, .5, 1], yticks=[0, turn, 1, 2],
           xticklabels=["0", "½", "1"], yticklabels=["0", r"$2a$", "1", "2"])
    ax.spines["left"].set_position(("data", 0))
    ax.spines["left"].set_bounds(0, 2)
    ax.spines["bottom"].set_bounds(0, 1)
    ax.set_aspect("equal")


def profiles(strain, momentum):
    shell = WAIST - 2 * CAP
    radii = [i / 1500 for i in range(1001)]
    for width, color, style, label in [
        (1 / 16, RUST, "--", r"$\sigma=1/16$"),
        (1 / 48, TEAL, "-", r"$\sigma=1/48$"),
    ]:
        z = [(r - shell) / width for r in radii]
        # Subtract an interior smooth continuation.  Outgoing speed dr*/dt=1
        # gives d_t[-H(r-r*)] = +delta(r-r*), so p=-d_r q in these units.
        q = [-erfc(-v / sqrt(2)) / 2 for v in z]
        p = [exp(-v*v / 2) / (sqrt(2*pi) * width) for v in z]
        strain.plot(radii, q, color=color, ls=style, lw=2, label=label)
        momentum.plot(radii, p, color=color, ls=style, lw=2)

    for axis in (strain, momentum):
        axis.axvline(shell, color=MUTED, ls=":", lw=.85, zorder=0)
        axis.grid(axis="y", color="#d8e1e2", lw=.65)
        axis.set_axisbelow(True)
    strain.tick_params(axis="x", bottom=False, labelbottom=False)
    strain.legend(loc="upper right", frameon=True, facecolor="white",
                  framealpha=1, edgecolor="none", fontsize=8.5,
                  title="Gaussian width", title_fontsize=8.5)
    strain.set(ylabel=r"Strain $q$", ylim=(-1.10, .15), yticks=[-1, 0],
               title=r"Singular strain   $h^{\rm TT}_{AB,\,sing}=2G_N B_{AB}\,q$")
    momentum.set(ylabel=r"Momentum $p$", xlabel=r"Radius $r$ on the waist ($t=1$)",
                 ylim=(-1, 21), yticks=[0, 10, 20], xlim=(0, 2/3),
                 xticks=[0, 1/6, shell, 1/2, 2/3],
                 xticklabels=["0", r"$1/6$", r"$1/3$", r"$1/2$", r"$2/3$"],
                 title=r"Shell momentum   $\pi^{\rm TT}_{AB,\,sing}=B_{AB}\,p/(16\pi)$")


def main():
    fig = plt.figure(figsize=(7.5, 3.65), layout="constrained")
    grid = fig.add_gridspec(2, 2, width_ratios=[1, 1.5])
    diamond = fig.add_subplot(grid[:, 0])
    strain = fig.add_subplot(grid[0, 1])
    momentum = fig.add_subplot(grid[1, 1], sharex=strain)
    spacetime(diamond)
    profiles(strain, momentum)
    for axis in fig.axes:
        axis.spines[["top", "right"]].set_visible(False)
        axis.tick_params(labelsize=9, width=.75, length=3)
        axis.title.set_fontsize(10.5)
    target = ROOT / "figures" / "weak-shell.png"
    fig.savefig(target, dpi=240, facecolor="white")
    plt.close(fig)
    print(target.name)


if __name__ == "__main__":
    main()
