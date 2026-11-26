# /// script
# requires-python = ">=3.11,<3.15"
# dependencies = ["matplotlib==3.10.8"]
# ///
"""Plot the source and spherical-clock response in the common-frame vacuum example."""
from pathlib import Path
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from checks.joint_focal import C, pulse, run


def main():
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.3), layout="constrained")
    teal, ochre = "#08675e", "#9e541c"
    x = [j/250 for j in range(-250, 251)]
    shape = [pulse(C+t, 1) for t in x]
    left.axhline(0, color="#51616b", lw=0.9)
    left.fill_between(x, shape, where=[t <= 0 for t in x], color=teal, alpha=.22)
    left.fill_between(x, shape, where=[t >= 0 for t in x], color=ochre, alpha=.14)
    left.plot(x, shape, color="#273f4a", lw=1.6)
    left.axvline(0, color="#51616b", lw=.85, ls=":")
    left.text(-.57, .6, "+1", ha="center", color=teal, weight="bold")
    left.text(.56, -.8, "−1", ha="center", color=ochre, weight="bold")
    left.set(title="Opposite halves of the incident pulse", xlabel="Position in the pulse, (U − c) / h",
             ylabel="Normalized profile", xlim=(-1.04, 1.04), xticks=[-1, -.5, 0, .5, 1])

    widths = [.025, .0125, .00625, .003125]
    samples = [run(h) for h in widths]
    limit = samples[0][1]
    right.axhline(limit, color=ochre, ls="--", lw=1.6, label=f"Sharp limit  {limit:.6f}")
    right.scatter(widths, [pair[0] for pair in samples], s=46, color=teal,
                  edgecolor="white", linewidth=.75, zorder=3, label="Direct sky integration")
    right.set(xlim=(.027, -.0015), ylim=(-.0613, -.0556), xticks=[.025, .02, .015, .01, .005, 0],
              xlabel="Pulse half-width h (decreasing)", ylabel="Mean clock variation",
              title="Clock on the half-radius cap")
    right.legend(loc="upper right", frameon=False, fontsize=8)
    for axis in (left, right):
        axis.grid(axis="y", linewidth=.55, color="#d3dfe0")
        axis.set_axisbelow(True)
        axis.spines[["right", "top"]].set_visible(False)
        axis.title.set_fontsize(10)
        axis.tick_params(labelsize=8)
    target = ROOT / "figures" / "joint-clock.png"
    fig.savefig(target, dpi=185, facecolor="white")
    plt.close(fig)
    print(target.name)


if __name__ == "__main__":
    main()
