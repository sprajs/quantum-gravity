# Fable’s review of the null-cone construction

**Scope and provenance.** Fable reviewed §§2–6 and Appendices A–E of Venkatesa Chandrasekaran’s *An algebraic quantization of gravity from the null cone* ([arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1)). Equation numbers refer to version 1. Fable reports deriving the clock, corner, sewing, and entropy objections below before reading this project’s later audit files. This public edition preserves Fable’s attributions and conclusions while recording where the editors judge a calculation’s hypotheses to leave the full gravitational question open. [Preprint and source](https://arxiv.org/abs/2611.34924v1) · [Dependency map](../audit/dependencies.md)

**Bottom line.** Fable reproduced the classical focusing identities, open sewing, the Gaussian pair amplitude, and the arithmetic of the Schwarzschild entropy logarithm. None of Fable’s objections is a physical refutation of finite-dimensional causal diamonds. Instead, they identify **defects in the construction as written** (finite-cap closure, linearized bare-clock positivity, conditional corner-charge degeneracy, and wording tensions in Appendix D) and **proof gaps** (clock nonemptiness, closed sewing, and the microscopic state count). The main unresolved question is whether the proposed clock selects a nonzero, finite-dimensional space of physical states at finite Newton’s constant $G_N$.

---

## Classical light cones, caps, and overlaps

On the regular part of a null cone, (3.25)–(3.28) express the affine length in terms of the corner area $\mathscr A$ and the integrated shear, giving the classical lower bound $(1-\epsilon)\sqrt{\mathscr A/(4\pi)}\leq\bar u_*$. Fable recovered the smooth-vertex corner potential to quadratic order, including the shift of boost angle described after (3.42a). Two classical caveats remain on the bulk setup: the phase space still requires a nonlocal check that null generators have neither crossed nor turned back, and the action relies on a branch choice after (3.3). Fable used the action audit for the sign conventions of (3.15) and checked Appendix B only through (B.3), where a corner subtraction makes the relevant variation exact. [Classical action](../audit/03-1.md) · [Domain and focusing](../audit/03-2.md)

### Finite-cap two-form defect

**Status: Defect as written (vanishes at a smooth vertex).** At a finite cap rim, set $r=\varrho_S^2$, take a single polarization $z(v)$ with angular labels fixed, and write $b$ for the rim’s dimensionless radius. Suppressing the common normalization, the exterior derivative of the printed two-form (A.14) on this family is

$$
d\omega=\frac{b^3}{2}\,\delta r\wedge\delta z'(b)\wedge\delta z(b).
$$

- Fixing the rim area density or freezing its conformal data eliminates this term.
- Holding the ratio $b=\epsilon>0$ fixed as in (3.18), while allowing the other data to vary independently, generally leaves $d\omega \neq 0$.
- The true pullback of a varied potential must be closed, and the defect disappears at a smooth vertex ($b=0$).

Because version 1’s quantum prescription uses a finite cap, it needs the missing rim and cap terms together with a derivation of the endpoint kernel in (A.36). The cap also carries constrained Cauchy data in (3.19) that the cone-and-corner Gaussian in (4.7) does not reconstruct—in particular, the incoming clock need not register outgoing radiation supplied by the cap. [Finite-cap derivation and boundary options](fable-boundaries-entropy.md) · [Independent cap check](../audit/cap-crosscheck.md)

### Overlaps and changes of cover

**Status: Proof gap (quantum implementation).** Classically, matching solutions on an open overlap and sewing along shared Cauchy data both have clear meanings. However, computing a symplectic form on an overlapping union requires choosing a single dividing cut inside the overlap; simply adding the two regional forms counts the overlap twice.

At the quantum level, gluing across the new interface requires its edge data and a shared overlap algebra. The change-of-cover unitary asserted in Appendix C does not follow automatically from Weyl ordering under a nonlinear coordinate transformation. Moreover, covers drawn around caustics can depend on the solution, and very small diamonds invoked in regions of strong curvature fall outside the macroscopic estimates. [Overlap analysis](fable-boundaries-entropy.md) · [Evolution between cuts](../audit/evolution.md)

---

## The clock at finite and increasing resolution

Let $s=\mathscr A/(4G_N\hbar)$ denote the dimensionless corner area, and let $P_{\mathscr D}$ project onto clock readings below the prescribed size limit. Given a positive self-adjoint shear integral $\widehat\Xi_y(v)$ with compatible domains, the capped comparisons and operator-monotonicity arguments in Appendix C.2 justify the regulated construction. The resolvent limit projects the reference Gaussian onto the closure of the clock’s form domain, so (5.19) requires that Gaussian to lie in that closure. At fixed finite resolution, the semiclassical estimate in the regime $NJ\ll\sqrt s$—where $N$ counts radial harmonics and $J$ is the angular cutoff—is a plausible defense. [Clock construction](../audit/04-3.md) · [Nonemptiness audit](../audit/05-1.md)

### Zero-point shear floor in bare models

**Status: Defect as written in linearized models; open in full interacting gravity.** Fable’s objection targets the positive ordering of both oscillator quadratures in the bare clock:

- For a single angular harmonic, the quadratic focusing form is proportional to $\int_\epsilon^1 v|h'|^2\,dv$ and the symplectic pairing to $\int_\epsilon^1 v^2(h'g-g'h)\,dv$.
- The $\epsilon$-dependence depends on the cutoff prescription: Fable’s normal-mode cutoff gives a factor proportional to $1/(1-\epsilon^2)$, whereas a periodic Fourier-wavenumber cutoff gives a coefficient involving $\log(1/\epsilon)/(1-\epsilon)^2$. Both are right for their respective cutoffs.
- Because the oscillator frequencies grow linearly with mode number, the state-independent ground-state floor scales as $N^2/s$ per harmonic and as $J^2N^2/s$ for an angular average over order $J^2$ modes. Squeezing cannot lower a positive oscillator below its ground energy.
- For the regular free shear current, a cutoff-independent commutator argument excludes any nonzero vector from the form domain of the literal pointwise square. In matching Gaussian models, the growing positive quadratic cost also obstructs the high-probability regular sets invoked in (C.16d). [Continuum current argument and regulated model](../audit/shear-uv.md)

**Editorial scope.** These estimates apply to the bare quadratic current under specified mode cutoffs. A lower bound at a single radial endpoint alone would not bound the integral over the whole cone, although a polarized radial model with an interior-interval floor does lose all finite readings in its cutoff limit. Concluding $P_{\mathscr D}=0$ for interacting four-dimensional gravity would require controlling the nonlinear two-polarization clock form, its fluctuating corner, its domains, and the order in which the diamond size and resolution limits are taken. [Ultraviolet model and limit](../audit/shear-uv.md)

### Vacuum subtraction and angular excitations

**Status: Proof gap.** Appendix D subtracts the coincident vacuum singularity. A locally Wick-ordered square can have negative expectation in squeezed states, and (D.28) permits a negative lower bound proportional to the squared derivative of its smearing. Restoring the area bound (5.21) after subtraction therefore requires a new lower bound on the renormalized operator.

In the quadratic subtracted model, a single quantum with a fixed radial profile has the same angularly averaged shear cost in every angular harmonic. While this degeneracy challenges compactness, equal expectation values alone do not place any given state inside a low-clock spectral subspace—the exponential clock and the opposite null cone can change the spectrum. Appendix D.3 recovers an angular penalty only after imposing additional cap and expansion conditions. [Small-shear bound](../audit/D2.md) · [Radiative count](../audit/D3.md)

---

## Where the finite-dimension argument changes its premise

**Status: Proof gap in closed sewing.** Open sewing in (4.29)–(4.31) follows directly from inserting a complete basis between two normalizable boundary vectors. The area bound, window estimate, and boost response in (5.29) motivate the collar construction, and a vacuum-like collar is physically plausible given the boost weight and frame-dressed correlators.

Closing the cut changes the mathematical requirement. For any finite-rank basis projection $P$ inside the diamond, the collar bound gives

$$
\sum_{i\in P}\|C_b i\|^2\ \geq\ m_{b,\mathscr D} e^{-s_*}\,\operatorname{rank}P,
$$

with $m_{b,\mathscr D}>0$.

- If an independently finite ordinary closed trace exists and equals $\operatorname{Tr}(PW)$ in the limit, finite rank follows immediately.
- Conversely, if the space is infinite-dimensional, the positive partial sums diverge, and different ways of ordering the basis can yield different normalized limits for inserted operators. Convergence to an independently defined uncut amplitude therefore has to be proved, not inherited from open sewing.
- For the unnormalized signed insertion $X$ in (5.38), (D.25) assumes a cofinal sequence of cycle projections on which the normalized expectation stays uniformly negative. Along that sequence, the magnitude of the unnormalized partial sum grows at least as a fixed positive multiple of the positive norm, so boundedness along those cycles is already logically equivalent to finite rank—not a weaker condition.
- Normalized expectations of restricted observables can converge even with infinite spectator multiplicity. Appendix E.3 relies on the claimed finite rank when verifying its own axiom. [Closed sewing](../audit/05-2.md) · [Compactness tests](../audit/compactness-stress.md)

### Model controls on closed sewing

Fable proposed two controls that test the inference rule (without determining the four-dimensional gravitational theory):

1. **Two-dimensional JT gravity.** In version 1’s own capped JT laboratory, the clock admits infinitely many orthogonal states even within a compact interval of corner charges. More broadly, JT gravity with matter can assign a finite disk amplitude via a semifinite trace on a type II algebra acting on an infinite-dimensional Hilbert space. That separates finiteness of a geometric trace from finite Hilbert-space dimension, though four-dimensional gravity has shear, constraints, and different boundary data. [JT audit](../audit/02-jt.md)
2. **AdS thermal double sum.** In (5.44), tensoring a divergent thermal trace with a two-state system can produce a formally vanishing signed sum whose value depends on the summation order; unconditional convergence already requires a finite thermal trace. [AdS test](../audit/area-ads.md)

### Local area density at fixed total area

**Status: Defect as written, conditional on one unchecked chart step.** A further test stays inside a single total-area sector in four dimensions.

- **Exact classical half.** In the smooth-vertex corner potential (3.42a), the boost angle enters only through $\mathscr K(y)\,\delta\Gamma(y)$, so a smeared local area charge $K_h$ for a physically marked, nonconstant angular function $h$ shifts the relative boost angle alone and leaves the incoming clock invariant. The proposed finite-rim correction contains no variation of that angle either.
- **Quantum argument.** If $K_h$ is self-adjoint, has a diffuse (continuous) spectral component in a surviving state, and its spectral projections commute with $P_{\mathscr D}$, then partitioning that component into disjoint sets yields infinitely many orthogonal clock-allowed states—forcing $\operatorname{rank} P_{\mathscr D}$ to be $0$ or $\infty$.
- **Reviewer vs. editor verdict.** Fable judged that version 1’s canonical representation in §4.2—where corner coordinates act by multiplication on $L^2(\mathbb R)$—already forces rank $0$ or $\infty$ at fixed total area, even before sewing. The zero-shear multiplication model illustrates this mechanism explicitly: run `python3 checks/corner_clock.py` from the repository root to verify infinite continuum rank at both clock cutoffs (with finite-matrix counts growing from 6 to 94 at relative cutoff $1.1$, and from 14 to 252 at $1.5$, as matrix size rises from 16 to 4096) ([zero-shear model](../checks/corner_clock.py)). The editors retain the quantum conclusion as **conditional on one unchecked step**: realizing the physically marked charge linearly in the unspecified canonical chart actually used in (4.7) and proving that its spectral projections strongly commute with the full ordered clock after gauge reduction. Note also that noncompactness of a boost group by itself determines neither the spectrum of its generator nor the dimension at fixed total area, and a defect in this construction says nothing about whether a differently built diamond is finite. [Conditional theorem and charge tests](../audit/finite-kinematics.md)

---

## Black-hole entropy and the one-loop coefficient

Whenever $\rho=e^{-\hat s}/Z$ is a trace-class density matrix, the identity $S=\langle\hat s\rangle+\log Z$ is exact, and the unitary factor cancels out of $C_b^\dagger C_b$ in (5.23b). However, evaluating the trace still requires the microscopic area multiplicities.

- **Radiative count vs. entropy scaling (Proof gap).** Reproducing the paper’s power-law clock ensemble requires, in the smoothed scaling regime, an unweighted density per unit $s$ proportional to $e^s s^{167/90}$. At fixed edge data and bounded $Q_*$, the radiative bound in (D.46c) is subexponential in $s$ and therefore **cannot supply** that growth on its own; edge and cap multiplicities remain uncomputed.
- **Tension in (D.48) (Defect as written).** Fable points out that if the disk-enhanced weights $k_a(s)$ in (D.48)—which carry an $e^s$ factor—are literally eigenvalues of the same reflected operator bounded above by $1$ in (5.30c), the two statements conflict. Reading the factor as a Euclidean disk saddle weight with its own measure avoids that contradiction, but an $e^s$ action weight and a degeneracy of $e^s$ Hilbert-space states enter different traces and cannot be distinguished by a normalized Rényi ratio alone. [Entropy audit](../audit/05-3.md) · [Radiation bound](../audit/D3.md)

### Ensemble arithmetic and the open bridge (5.67c)

On a Ricci-flat background, the local heat-kernel coefficient $(4\pi)^2 a_4=(53/45)R_{abcd}R^{abcd}$ gives $106/45$ per logarithm of area for Sen’s spin-summed Schwarzschild ensemble. Assigning $106/45$ to the collar packet $T_b$ (with its variance $2s_b$) consistently yields:

- $167/90$ for the weighted density per unit area $s$ (not to be conflated with Sen’s fixed-$J_3$ mass-density exponent, which coincidentally also equals $167/90$ in four dimensions),
- $257/90$ for the integrated clock trace $Z$ (an exponent specific to the clock ensemble, not directly comparable to Sen’s mass-density numbers),
- $q=257/302$ and $\langle s\rangle/s_*=257/347$, which follow identically from the $106/45$ packet assignment and restate it rather than adding an independent test, and
- $106/45$ again upon converting from an area density to a mass density with angular momenta summed.

The arithmetic agrees because both sides use the same local coefficient and consistent Jacobians. Whether the closed Lorentzian collar packet actually carries that $106/45$ exponent is the open physical input in (5.67c), where caps, the area mode, the clock projection, conical gauge/contact terms, and angular-momentum zero modes can all contribute. Sen’s fixed-$J_3$ and singlet ensembles supply separate tests. [Detailed ensemble review](fable-boundaries-entropy.md) · [Sen’s original calculation](https://arxiv.org/abs/1205.0971)

### Marginality condition

The bare incoming clock admits shear-free round spheres with different expansions on the opposite cone and does not select a marginal horizon. In (5.67b), the surface integrand $R[q]+2\Theta_{(\ell)}\Theta_{(n)}$ integrates to $+8\pi$ on a marginal round sphere and to $-8\pi$ on a round sphere in flat space (in the paper’s normalization). That sign flip shows that (5.67c) is conditioned on a saddle the trace never selects—it does **not** imply that the flat-sphere number is the entropy of a flat diamond. Identifying ADM mass at infinity likewise requires exterior data or an explicit operator implementing the chosen ensemble. [Marginality and mass](fable-boundaries-entropy.md)

---

## Evolution, topology, and other checks

| Steps in v1 | What Fable established and what remains open |
|---|---|
| (3.53)–(3.56), (4.1)–(4.18), App. C | The reduced Hamiltonian has the formal canonical form, and the source algebra, Gaussian rank-one identity, and pure-state extension are algebraically well-posed. Globally a pure representation generates a type I factor, without supplying interacting amplitudes or classifying the one-sided subregion algebra. A global canonical chart, regularity under area-changing sources, and unitary evolution between cuts remain open. [Representation](../audit/04-2.md) · [Dynamics](../audit/evolution.md) |
| (4.32)–(4.34) | The free oscillator displacement yields a convergent inverse-square sum for arbitrary phases, and expanding its dilogarithm before summing explains the logarithm. Coupling enters only through the chosen sources; testing gravitational self-interaction requires a dynamical observable. [Pair calculation](../audit/04-pair.md) |
| (5.70)–(5.77) | The Gram rank bound is conditional on finite rank; the Fourier integral and cross-corner correlator check out. Equation (5.71) assumes the Hilbert–Schmidt inner product needed for factorization; an independently evaluated gravitational amplitude is required to test it. [Two-boundary analysis](../audit/05-4.md) |
| (6.1)–(6.14), (D.9) | The Moyal expansion and Gaussian average of smooth classical solutions recover the stated formal identities (the vacuum equations already enter the reduced phase space). At coincidence the correlator needs renormalization. In the finite determinant model, the explicit source contact vanishes while the second-variation trace includes a tadpole, giving $-4/27$ before the $-1/2$ factor. [Semiclassical equations](../audit/06-2.md) · [Determinant](../audit/D1.md) |

## Executable checks

Run these scripts from the repository root to verify the explicit model calculations cited above:

- `python3 checks/determinant.py` — reproduces the Ricci-flat local coefficient $53/45$ (spin-2 $19/18$ minus two ghosts $-11/180$) and the separate-source determinant test (explicit mixed contact $0$, second-variation trace $-4/27$). [Determinant script](../checks/determinant.py)
- `python3 checks/pair.py` — verifies the convergent pair overlap through $10^5$ modes (within the analytic tail bound, e.g. $2.50\times 10^{-12}$ at $x=0.1$) and its small-source logarithmic expansion. [Pair script](../checks/pair.py)
- `python3 checks/fable-boundaries-entropy.py` — verifies the nonzero finite-cap exterior derivative on the fixed-ratio family, its cancellation by the endpoint correction, the Gaussian window resolution of unity, and both ensemble-exponent assignments. [Cap and entropy script](../checks/fable-boundaries-entropy.py)
- `python3 checks/corner_clock.py` — verifies the zero-shear corner shape model’s infinite continuum rank and finite-matrix growth. [Corner-clock script](../checks/corner_clock.py)

These scripts check explicit models and algebraic identities. An independent finite gravitational trace, a continuum clock, and a microscopic state count remain to be constructed.
