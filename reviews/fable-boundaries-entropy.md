# Fable’s review of the entropy measure and boundary conditions

Fable examined three structural questions in Venkatesa Chandrasekaran’s *An algebraic quantization of gravity from the null cone* ([arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1), version 1):

1. **Entropy ensemble bookkeeping (Proof gap at (5.67c)).** The paper’s one-loop numbers are mutually consistent once the packet exponent is assigned, but deriving that exponent for the Lorentzian collar trace remains open.
2. **Finite-cap symplectic closure (Defect as written).** The printed two-form (A.14) fails a closure test on the fixed-ratio cap chosen in (3.18), though an explicit endpoint term restores closure on the tested family.
3. **Gluing across overlapping regions (Proof gap at the quantum level).** Classical overlap conditions can be read as matching solutions; their quantum implementation remains open.

All equations and numbers below refer to version 1. [Preprint](https://arxiv.org/abs/2611.34924v1)

---

## Which density carries the logarithm?

Write $s=\mathscr A/(4G_N\hbar)$ for the dimensionless corner area and let $P_{\mathscr D}$ select states within the clock bound. The closed collar trace in (5.66) is $T_b=\operatorname{Tr}[f_b(\hat s)e^{-\hat s}P_{\mathscr D}]$, with Gaussian area window $f_b(s)=\exp[-(s-s_b)^2/(4s_b)]$. For every $s\geq 0$, this window resolves unity identically:

$$
\int_0^\infty f_b(s)\frac{ds_b}{\sqrt{4\pi s_b}}=1.
$$

For a Schwarzschild exterior, $s_b=4\pi G_N M_b^2/\hbar$, so $ds_b/\sqrt{4\pi s_b}=2\,dM_b/M_P$ with Planck mass $M_P=\sqrt{\hbar/G_N}$. At large mass, the packet therefore spans a **constant mass width** $\Delta M=M_P/\sqrt{8\pi}\approx 0.1995\,M_P$, whereas its width in area grows as $\sqrt{2s_b}$. An area density and a mass density count different intervals of the same spectrum. [Window audit](../audit/ensemble-crosscheck.md)

### Comparing the two exponent assignments

Suppose the spin-summed packet scales as $T_b\propto s_b^c$ and the underlying coarse-grained density varies slowly over the packet width $\propto\sqrt{s_b}$. Then:

- the weighted density per unit area $s$ scales as $s^{c-1/2}$,
- the integrated clock trace up to $s_*$ scales as $Z\propto s_*^{c+1/2}$, and
- the unweighted state count per unit mass scales as $e^s s^c$.

Sen’s mixed ensemble counts states per unit mass and sums over angular momenta; his coefficient $212/45$ per $\log(\text{length})$ equals $c=106/45$ per $\log(\text{area})$.

| Quantity | Reading 1: $106/45$ assigned to packet $T_b$ | Reading 2: $106/45$ assigned to density per unit $s$ |
|---|---|---|
| Packet $T_b$ (and fixed-mass count) | $106/45$ (matches Sen’s mixed ensemble) | $257/90$ |
| Weighted density per unit $s$ | $167/90$ | $106/45$ |
| Integrated clock trace $Z$ | $257/90$ | $151/45$ |
| Clock ratio $q$ and mean ratio $\langle s\rangle/s_*$ | $q=257/302$, $\langle s\rangle/s_*=257/347$ | $q=302/347$, $\langle s\rangle/s_*=151/196$ |

**Important clarifications on these numbers:**

- **What Sen’s definitions settle—and what stays open.** Sen’s ensemble definitions fix which column *can* agree with his mixed ensemble (Reading 1). Whether the Lorentzian collar packet $T_b$ actually carries the $106/45$ exponent is the separate, open bridge in (5.67c).
- **No independent confirmation from $q$ or $x^2$.** For any power-law weighted density $s^a$ with small delay, $\langle s\rangle/s_*=(a+1)/(a+2)$ and $a+1=x^2/(1-x^2)$ hold identically. Thus $x^2=257/347$ and $q=257/302$ restate the $106/45$ assignment rather than supplying independent evidence.
- **Avoid conflating ensembles.** The integrated-trace exponent $257/90$ belongs specifically to the clock ensemble and is not directly comparable with Sen’s mass-density exponents. Likewise, $167/90$ appears here as the spin-summed weighted density per unit *area* $s$; in four dimensions it coincidentally equals Sen’s fixed-$J_3$ exponent per unit *mass*, which is a different ensemble. [Sen, equations (1.1)–(1.5)](https://arxiv.org/abs/1205.0971) · [Comparison of ensembles](../audit/sen.md)

### Why the packet width is plausible—and what (5.67c) assumes

At fixed inverse temperature $\beta$, the Schwarzschild Euclidean action $I_E=\beta M(s)-s$ has second derivative $I_E''=-1/(2s)$ at its saddle, whose magnitude picks out the exact variance $2s_b$ and mass-interval scaling. By itself, however, resolving unity permits any width $2\kappa s_b$ with matching normalization; more generally, a variance $\propto s_b^\alpha$ over a density $s^a\,ds$ shifts the packet exponent to $a+\alpha/2$ for a narrow window. The local heat-kernel coefficient alone does not determine that measure.

Equation (5.67c) assumes that the exponent of the ordinary closed $n=1$ Lorentzian packet equals the conical coefficient extracted via a replica variation. On complete Euclidean Schwarzschild, the Euler density aligns both routes. In the capped Lorentzian diamond, the caps, clock projection, area zero mode, other corner modes, and gauge fixing all enter the trace; a classical cyclic variational principle does not compute that one-loop normalization. Summing over spins matches the Kerr shift $\delta s\simeq -4\pi^2 j^2/s$ at fixed mass, whereas restricting to $J_3=0$ or to singlets reduces the coefficient by $1/2$ or $3/2$ per $\log s$, respectively. A direct packet determinant—or a normalized replica calculation retaining the area mode and reproducing those spin-sector shifts—would directly test (5.67c). [Determinant audit](../audit/D1.md) · [Sen’s comparison](https://arxiv.org/abs/1205.0971)

### Marginality and exterior mass

The incoming clock does not impose marginality at the corner. The surface integrand $R[q]+2\Theta_{(\ell)}\Theta_{(n)}$ in (5.67b) integrates to $+8\pi$ on a round marginal sphere and to $-8\pi$ on a round sphere in flat space. That evaluates one surface term and demonstrates sensitivity to a saddle condition that the trace never selects (the flat-sphere number is not a flat-diamond entropy). Connecting the trace to a black hole requires either a proof that the marginal saddle dominates or an explicit projector onto it, plus exterior data to define an ADM mass. In the stated clock ensemble, the relative width of $s$ is $\operatorname{std}(s)/\langle s\rangle\approx 0.27$, and $(1-\epsilon)r_h/\ell=\sqrt{257/347}$ follows directly from the mean. [Entropy and saddle selection](../audit/05-3.md)

---

## Does the finite-cap form close?

Reisenberger’s null-cone derivation fixes the area density of each truncating cut in a fixed chart for admissible variations and restricts bracket tests at the cut edge. Version 1 instead fixes the radial ratio $v=\epsilon$ in (3.18), so the rim area density $\epsilon^2\varrho_S^2$ varies whenever the corner density $\varrho_S^2$ varies. Equation (A.17) also mentions a fixed affine location; these prescriptions produce different endpoint variations. [Reisenberger, §4](https://arxiv.org/abs/1211.3880) · [Finite-cap audit](../audit/03-3.md)

On a single branch and single polarization with angular labels fixed, put $r=\varrho_S^2$ and write $b$ for the rim radius. At fixed $b$, Fable finds a nonzero exterior derivative $d\omega=(b^3/2)\,\delta r\wedge\delta z'(b)\wedge\delta z(b)$ for the printed two-form (A.14) in test normalization. Including the endpoint variation of the potential supplies the missing terms (up to the common integral and normalization):

$$
\frac b2\,\delta(b^2r)\wedge \mathsf g(\partial_v z,\delta^o z)\big|_b
-\delta(b^2)\wedge\delta r,
$$

where $\delta^o z$ is Appendix A’s variation at fixed area coordinate.

- At **fixed ratio** ($b=\epsilon$), the first term cancels the defect and the second vanishes.
- At **fixed rim area density** ($b^2 r=\text{const}$), both terms vanish.
- Under the **joint variation** of (A.18), the corrected form is closed and modifies the conjugate momentum to $r$.

An exact rational check confirms closure after adding this endpoint term on the tested family, even for a moving rim, though corner and cap-interior terms still require independent variation to derive the full cap phase space. [Independent cap expansion](../audit/cap-crosscheck.md) · [Test code](../checks/fable-boundaries-entropy.py)

### Three concrete ways to repair the cap

1. **Fix the rim area density.** Preserves Reisenberger’s endpoint condition, but changes the lower limit and scaling of the clock.
2. **Fix the ratio and freeze conformal rim data.** Restores closure, but removes variations from the phase space in (3.19).
3. **Keep the phase space of (3.19).** Requires deriving the complete cap-plus-null symplectic form and inverting it anew.

In the one-polarization endpoint model, a sign kernel generates an interior observable shifted by endpoint values; free endpoint variations prevent it from generating the unshifted interior field. That missing condition affects the determination of $\mathsf k_\partial$ in (A.36) for observables reaching the rim. Because the computed correction contains no relative boost variation, the total area’s boost action survives on this family. Full endpoint brackets, the Jacobi identity, and strong commutation of *local* quantum area charges remain to be checked after reduction. [Corner charge test](../audit/finite-kinematics.md)

---

## What can be matched across regions?

| Geometric operation | Classical data and remaining requirement |
|---|---|
| Successive slabs joined at a cap, (3.29) | Match identical induced Cauchy data; equality defines a fiber product of solution spaces. |
| Neighboring regions meeting at a corner, (3.60)–(3.66) | Match the induced metric, both null extrinsic curvatures, and the normal connection up to a relative boost. With edge variables, symplectic forms add before reducing at zero total charge. Smoothness can require higher-derivative compatibility. |
| Two descriptions of an open overlap, (3.30)–(3.31) | Match solutions throughout the overlap. Torsion-free tetrads related by a frame transformation induce the transformed connection, and compatible transitions obey the cocycle condition. The conserved symplectic current allows a dividing cut inside the overlap; simply summing both regional forms double-counts it. |

The transport equations after (3.62) can begin from identical corner values on both sides while freely specified shear differs farther along each ray—as a vacuum plane wave demonstrates, first-derivative matching at a cut permits curvature jumps excluded by smooth solutions on the union.

At the quantum level, gluing across overlaps requires a common overlap algebra, a compatible handling of solution-dependent covers near caustics, and a unitary or algebraic map whose amplitudes agree across covers. Appendix C.1 treats source shifts in a fixed chart; two overlapping linearized diamonds would supply a concrete first test of the stronger claim. [Classical plane-wave test](../audit/03-5-6.md) · [Evolution and changes of cover](../audit/evolution.md)

## Executable check

Run `python3 checks/fable-boundaries-entropy.py` from the repository root:

- **Part A (finite cap):** verifies that the printed two-form has nonzero exterior derivative on the fixed-ratio family ($\max|dW|=6.859\times 10^{-3}$ in the test family) and exact closure ($\max|d(W+C)|=0$) after adding the endpoint correction, including for a generic field-dependent cut $b(\varrho_S,z)$, while vanishing identically at fixed rim area density, frozen rim modes, or a smooth vertex ($b=0$).
- **Part B (entropy bookkeeping):** verifies the Gaussian window integral equals $1$ at $s=0, 0.3, 4, 60$, confirms the exponent shift $a+\alpha/2$ for $\alpha=0, 1, 1.5$ (slopes $1.85556, 2.35556, 2.60525$), and checks both exponent readings, the relative width $\operatorname{std}(s)/\langle s\rangle = 0.2686$, and the constant mass width $0.19947\,M_P$. [Script](../checks/fable-boundaries-entropy.py)
