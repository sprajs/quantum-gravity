# What a controlled boost could tell us about area

Suppose a preparation and its boundary reference frame can be coherently split between two paths. Apply the identity on one path and a relative boost of rapidity $\eta$ at the corner on the other, then recombine. This is an operational extension to test: the paper specifies a relative boost, but supplies no calibrated beam splitter or reference system implementing its controlled version. It is not necessary to assume a finite Hilbert space to calculate what such an instrument would measure.

## A prediction conditional on the apparatus

Let $s=A/(4G_N\hbar)$ in units with $c=1$, with boost $U(\eta)=\exp(i\eta s/(2\pi))$ as in §5.2. Starting the control in $(|0\rangle+|1\rangle)/\sqrt2$ multiplies one of its off-diagonal elements by $\chi(\eta)=\operatorname{Tr}(\rho U(\eta))$. Measuring two complementary phases of the control retrieves its real and imaginary parts. A particularly simple derived observable is $V=|\chi|^2$ (the **squared** fringe visibility). For the probability measure $\mu$ of $s$ in the prepared state,
$$
V(\eta)=\iint\cos\!\left[\frac{\eta(s-t)}{2\pi}\right]\,d\mu(s)\,d\mu(t).
$$

If the clock imposes a bounded area spectrum, this integral has the expansion
$$
1-V(\eta)=\frac{\eta^2}{4\pi^2}\operatorname{Var}_\rho(s)+O(\eta^4).
$$
The curvature near zero probes area fluctuations. A sharp area gives $V=1$ identically, even if there are infinitely many orthogonal states at that area.

## What a long scan could identify

Let the scan average $V$ uniformly from $-T$ to $T$. Integrating each cosine replaces it with $\sin x/x$ at $x=T(s-t)/(2\pi)$. This kernel is bounded by one. As $T$ grows it vanishes for each unequal pair of areas and stays one at equality. By dominated convergence,
$$
\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}V(\eta)\,d\eta
=(\mu\mathbin{\otimes}\mu)\{s=t\}
=\sum_j \mu(\{s_j\})^2 .
$$
Here $s_j$ runs over the atoms of the area distribution, each distinct value counted once. A positive average detects some sharp-area weight. For a state supported on at most $m$ values it is at least $1/m$. An infinite discrete spectrum can give a positive average too. Replicating every area eigenspace a thousandfold while holding its total probability fixed leaves *the entire curve* unchanged. An area-only interference experiment cannot count all microstates, even with perfect data.

For two equally weighted areas separated by $\Delta s$, $V(\eta)=\cos^2[\eta\Delta s/(4\pi)]$. Its first zero is at $\eta=2\pi^2/\Delta s$. With $\Delta s=4\pi^2$ that occurs at rapidity $0.5$ and the signal returns to one at rapidity $1$. A uniform continuum of the same width gives $V=\operatorname{sinc}^2[\eta\Delta s/(4\pi)]$, with first zero at rapidity $1$ instead. These are distinguishable **specified preparations**. The paper supplies neither that spacing nor a preparation with those two weights. For very small $\Delta s$ the required rapidity would push the insertions outside the semiclassical window. Finite observations with finite precision cannot distinguish an arbitrary continuous distribution from all its sufficiently fine discrete approximations.

Run `python3 checks/boost_observable.py` to compare these preparations. At rapidity $0.5$ the two sharp areas give zero squared visibility. Uniform weight spread across the interval gives $4/\pi^2\simeq0.405285$. The code also divides each sharp area’s weight among additional orthogonal states and reproduces the original visibility. [Executable check](../checks/boost_observable.py)

This control experiment and the two-sided shear measurement are different. The control reads the characteristic function of an area distribution. The shear experiment also probes matrix elements linking different areas and has a calculated vacuum response for a limited range of separations. Combining them would test both the proposed boost generator and a chosen state's gravitational dynamics. The wave-packet acceptance test probes an additional quantity, the multiplicity invisible to area-only interference. [Paper §5.2](https://arxiv.org/html/2611.34924v1#S5.SS2) · [Shear response](observable-boost.md) · [Clock acceptance](../OBSERVABLES.md)
