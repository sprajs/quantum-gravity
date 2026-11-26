# /// script
# requires-python = ">=3.11,<3.15"
# dependencies = ["matplotlib==3.10.8"]
# ///
"""Plot the before-focusing transfer predicted for a weak aligned probe."""
from math import pi
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from checks.interacting_test import incoming_radius, probe_gains


def main():
    strengths = [i / 200 for i in range(101)]
    gains = [1 / incoming_radius(e, 640)[-1] for e in strengths]
    weak = [1 + 5*pi**2*e**2/64 for e in strengths]
    points = [0.15, 0.25, 0.35, 0.45]
    measured = [probe_gains(e, 0.001, 80)[0] for e in points]
    fig, ax = plt.subplots(figsize=(7.4, 3.7), layout="constrained")
    ax.plot(strengths, gains, color="#1B6559", label="Reciprocal focusing radius", lw=2.5)
    ax.plot(strengths, weak, color="#914713", ls="--", label="Leading interaction term", lw=1.8)
    ax.scatter(points, measured, s=35, facecolors="white", edgecolors="#253447",
               label="Independent two-wave evolution", zorder=3)
    ax.set(xlabel="Incoming pump log-strain amplitude", ylabel="Weak-probe strain gain",
           title="A weak gravitational wave crossing a stronger pulse")
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    ax.grid(axis="y", lw=0.7, color="#d7dfe1")
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    target = ROOT / "figures" / "wave-transfer.png"
    fig.savefig(target, dpi=180, facecolor="white")
    plt.close(fig)
    print(target.name)


if __name__ == "__main__":
    main()
