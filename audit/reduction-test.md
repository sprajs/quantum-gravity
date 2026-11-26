# Diffeomorphisms, reduced quantization, and the choice of clock

Venkatesa Chandrasekaran proves a classical invariance for his dressed gravitational shear: moving the metric and its physical reference frame together cancels the diffeomorphism variation in (3.40) and (3.59). At the quantum level, §5.2 and Appendix E.1 require amplitudes to remain unchanged when an intermediate cut moves. Jonathan Oppenheim points to the unproved bridge between those two statements and asks whether solving constraints before quantizing agrees with Dirac quantization or depends on the chosen reduction.

To separate what is established from what remains open, this note works through four explicit calculations—kept strictly distinct from theorems about interacting four-dimensional null-cone gravity:

1. **Classical 4D spherical check:** the local mass matches identically across spacelike ADM slices and null-cone data.
2. **Linearized 4D graviton check:** covariant (de Donder) and canonical transverse-traceless quantizations yield the exact same tidal two-point function.
3. **Soluble best-case clock control:** a linear, field-independent clock tilt for a free relativistic particle gives unitary equivalence once the measure is tracked—highlighting why *nonlinear, shear-dependent* clock changes in gravity are much harder.
4. **Soluble gauge-quotient mismatch and repair:** a smooth cylinder quotient where naive reduced quantization and Dirac quantization have *different spectra* unless an orbit-volume ordering potential is included.

[Chandrasekaran, v1](https://arxiv.org/abs/2611.34924v1) · [Dressed shear](https://arxiv.org/html/2611.34924v1#S3.E59) · [Appendix E.1](https://arxiv.org/html/2611.34924v1#A5.I1.i1) · [Oppenheim’s commentary](https://superposer.substack.com/p/has-ai-come-for-quantum-gravity)

---

## 1. A four-dimensional classical observable across two slicings

Consider a vacuum spherically symmetric region with areal radius $R>0$, radial metric $L^2\,dr^2$ on a spacelike slice, cosmological constant $\Lambda$, and $G=c=1$. In Kuchař’s canonical variables $(L,P_L)$ and $(R,P_R)$ (with primes denoting $d/dr$), the normal and radial constraint densities are

$$
\begin{aligned}
H={}&-P_LP_R/R+LP_L^2/(2R^2)+RR''/L-RR'L'/L^2
        +R'^2/(2L)-L/2+\Lambda LR^2/2,\\
D={}&P_R R'-LP_L'.
\end{aligned}
$$

The local mass is $M=\tfrac R2[1-(R'/L)^2+(P_L/R)^2-\Lambda R^2/3]$. Direct differentiation yields the first identity below, and Hamilton’s equations for compactly supported interior lapse $N$ and shift $\xi$ yield the second: [Kuchař, spherical ADM variables and mass, §§II and IV–VI](https://arxiv.org/pdf/gr-qc/9403003)

$$
M'=-\frac{R'}{L}H-\frac{P_L}{RL}D,\qquad
\{M,H[N]+D[\xi]\}=-\frac{N R'}{L^3}D+\xi M'.
$$

Both identities hold *before* imposing the constraints (in the lapse bracket, the $-N'RR'/L^2$ term from varying $L$ in $H[N]$ cancels the $N'$ term in $\dot R'$). On any vacuum solution, $M$ is constant along the slice and invariant under interior normal and tangential deformations.

**Agreement with null-cone data.** For sphere-orthogonal null normals satisfying $\ell\cdot n=-1$, the expansions are $\Theta_\ell=2\ell(R)/R$ and $\Theta_n=2n(R)/R$. Using $(\nabla R)^2=-2\ell(R)n(R)$ gives

$$
M=\frac R2\left[1+\tfrac12 R^2\Theta_\ell\Theta_n-\Lambda R^2/3\right],
$$

which is invariant under null boost rescalings $\ell\mapsto a\ell$, $n\mapsto n/a$. In a Schwarzschild exterior ($\Lambda=0$, $R=r$), both a static slice ($L=(1-2m/R)^{-1/2}$, $P_L=0$) and a spatially flat Painlevé–Gullstrand slice ($L=1$, $P_L=\sqrt{2mR}$) give $M=m$ in either description. On an expanding round ray the shear vanishes and version 1’s capped clock reads $(1-\epsilon)R_S$ at fixed corner radius $R_S$; the transverse expansion $\Theta_n$ supplies mass information invisible to that single-cone clock. (These identities apply to a common exterior region—a regular vacuum center forces $M=0$—and supply no state count for capped diamonds.) [Focusing and capped clock](https://arxiv.org/html/2611.34924v1#S3.SS2.p6.2) · [Transverse data](https://arxiv.org/html/2611.34924v1#S3.SS5.p1.1)

**Published quantum controls in spherical symmetry.** For two-ended asymptotically flat Schwarzschild spacetime, Kuchař’s embedding chart turns the Dirac constraints into $P_T=P_{\mathcal R}=0$, reducing the physical wavefunctional to $\psi(m)$; Cavaglià, de Alfaro, and Filippov likewise obtain agreement between reduced and Dirac Hilbert spaces in a suitable gauge. Those proofs depend on spherical symmetry and specific global boundary data, whereas the null-cone theory includes radiative polarizations and fluctuating corner geometry. [Kuchař](https://arxiv.org/abs/gr-qc/9403003v1) · [Cavaglià, de Alfaro and Filippov](https://arxiv.org/abs/gr-qc/9508062v1)

---

## 2. A free-graviton measurement in covariant and reduced quantization

In Minkowski vacuum, consider a beam of neighboring null rays with null tangent $\ell$ and orthogonal unit screen vector $e$ probing a plane-wave metric perturbation $h_{\mu\nu}e^{ik\cdot x}$ with future-directed null wavevector $k$. The linearized tidal curvature read by the beam has Fourier coefficient

$$
R^{(1)}_{\ell e\ell e}=\tfrac12 Q^\mu Q^\nu h_{\mu\nu},\qquad
Q=(k\cdot\ell)e-(k\cdot e)\ell .
$$

Because $k\cdot Q=0$, pure gauge modes $k_\mu\xi_\nu+k_\nu\xi_\mu$ drop out, and frame displacements vanish on flat background curvature. Given initial shear data, this curvature sources the linearized optical shear. [Paper, optical equations](https://arxiv.org/html/2611.34924v1#S3.SS2.p5.1)

Contracting the four-dimensional de Donder graviton numerator with two probe vectors $Q_1, Q_2$ yields the on-shell Wightman numerator

$$
W_{12}(k)=\tfrac18\big[2(Q_1\cdot Q_2)^2-Q_1^2Q_2^2\big].
$$

In signature $(-,+,+,+)$, $k\cdot Q_i=0$ implies $Q_i^0=\widehat{\mathbf k}\cdot\mathbf Q_i$, so the canonical transverse-traceless polarization sum gives the *exact same* expression mode by mode (for one probe, $W_{11}=(k\cdot\ell)^4/8$), and therefore after smooth spacetime smearing with the measure $d^3k/[(2\pi)^3 2|\mathbf k|]$. Reproducing this exact kernel—including its normalization and initial shear data—from version 1’s characteristic boundary representation would provide a direct check of its free radiative sector. [De Donder numerator, Eq. (4.1)](https://doi.org/10.1103/PhysRevD.104.065014) · [Paper, incoming state and radiative sources](https://arxiv.org/html/2611.34924v1#S4.SS2.p1.1)

---

## 3. A linear clock change in a soluble free-particle model (best-case control)

*Model, not gravity.* For a free massive particle in $1+1$ dimensions ($\hbar=c=1$) with constraint $C=p_t^2-p^2-m^2=0$ on the branch $p_t=-E=-\sqrt{p^2+m^2}$, integrating $\delta(C)\,dp_t\,dp$ gives the physical measure $dp/(2E)$. Compare coordinate time $t$ with a linearly tilted global clock $T=t+\alpha x$ ($|\alpha|<1$, $X=x$). The canonical one-form becomes $-E\,dT+P\,dX$ with $P=p+\alpha E$, and solving the constraint gives

$$
B=\sqrt{P^2+(1-\alpha^2)m^2}=E+\alpha p,\qquad
H_T(P)=\frac{B-\alpha P}{1-\alpha^2},\qquad
\frac{dp}{2E}=\frac{dP}{2B}.
$$

Because $dP/dp=1+\alpha p/E>0$, the momentum map is bijective and its pullback is unitary between the weighted spaces, with matching phase $px-Et=PX-H_T(P)T$ at every event. Both mass-shell integration and the transversality factor $|\{T,C\}|=2B$ produce the required measure factor. [Relational dynamics on a single frequency sector, Höhn, Smith and Lock](https://arxiv.org/abs/2007.00580)

For $m=1$ and $|a(p)|^2=\exp[-((p-1.1)/0.7)^2]$, the squared norm equals $0.426044354$ for $\alpha=0, -0.6, +0.6$ once the measure $2B$ is updated, whereas keeping the old denominator $2E$ while integrating over $dP$ yields the wrong norms $0.261708321$ and $0.590380387$.

**Why this is a best-case control.** A free particle with a linear, field-independent clock tilt is the most favorable possible setting. Two cautionary distinctions apply to version 1:

1. Particle clocks label time slices, whereas version 1’s $\bar u_*$ is a measured geometric size used to define a spectral projection; changing how *the same* clock is presented requires unitarily equivalent projections, while changing the physical reading can select different states. [Paper, §5.1](https://arxiv.org/html/2611.34924v1#S5.SS1.p2.1)
2. In the null-cone theory, distinct classical reductions of the same phase space—such as area gauge, affine parameter, and the dressing time $V$ in (A.31)—are related by **nonlinear, shear-dependent reparametrizations** acting across infinitely many null generators. Even for free chiral fields on one generator, non-Möbius reparametrizations generate nonzero Bogoliubov mixing, which sums over infinitely many generators and can obstruct unitary equivalence in the transverse continuum.

---

## 4. A smooth gauge quotient where reduced and Dirac spectra differ

*Model, not gravity.* Even with finitely many degrees of freedom and a completely smooth, free gauge action, naive reduced quantization and Dirac quantization can disagree unless ordering and measure factors match. Take a particle on $\mathbb R\times S^1$ with metric $dx^2+a(x)^2\,d\theta^2$, kinetic Hamiltonian $(p_x^2+p_\theta^2/a^2)/(2\mu)$, and rotation constraint $p_\theta=0$. Every orbit is a circle with trivial stabilizer and global section $\theta=0$. [Ordóñez and Pons](https://doi.org/10.1063/1.531111)

- **Flat reduced quantization:** the classical quotient is $T^*\mathbb R$ with free Hamiltonian $p_x^2/(2\mu)$, quantized on $L^2(dx)$ as $-c_0\partial_x^2$ ($c_0=\hbar^2/(2\mu)$), whose spectrum is purely continuous on $[0,\infty)$ with no normalizable ground state.
- **Dirac quantization of the Laplace–Beltrami operator:** quantizing first as $-c_0\Delta_g$ and imposing $-i\hbar\partial_\theta\psi=0$ yields $-c_0 a^{-1}\partial_x(a\partial_x)$ on $L^2(a\,dx)$. Mapping unitarily to $L^2(dx)$ via $\psi\mapsto u\psi$ ($u=\sqrt{a}$) adds an orbit-volume potential: $c_0(-\partial_x^2+u''/u)$, even though the Faddeev–Popov phase-space determinant is $1$.

Choosing the smooth, complete metric $u(x)=\operatorname{sech}(\kappa x)$ ($\kappa>0$) gives, with $A=\partial_x+\kappa\tanh(\kappa x)$,

$$
H_D/c_0=A^\dagger A=-\partial_x^2+\kappa^2(1-2\operatorname{sech}^2(\kappa x)),\qquad
AA^\dagger=-\partial_x^2+\kappa^2 .
$$

Because $Au=0$ and $\int u^2\,dx=2/\kappa<\infty$, the Dirac Hamiltonian has a **normalizable zero-energy bound state** separated by a gap $c_0\kappa^2$ from its continuum, whereas the flat reduced Hamiltonian has continuous spectrum starting at zero and no ground state. Adding the ordering potential $c_0 u''/u$ to the reduced Hamiltonian restores exact equivalence. Thus disagreement comes from ordering and measure choices, and Dirac quantization itself is not immune to ordering ambiguity.

---

## 5. What tests decide the question for the null-cone theory?

Version 1’s formal path-integral measure in (D.7)–(D.8) includes the second-class bracket determinant, the first-class gauge-fixing determinant, and an eliminated Gaussian block—so it formally assumes the measure matching that an operator test must verify. Two concrete calculations replace a vague “check against Dirac quantization”:

1. **Construct the quantum null constraint and compute its central term.** Version 1 solves (A.30b) classically. A strict Dirac comparison requires operators for changes of parameter along each null generator, including the area and boundary contributions. A nonzero net central charge on a generator precludes a nonzero state annihilated by every mode there. Ciambelli, Freidel and Leigh obtain a nonzero charge per ray in a related quantization. A vanishing charge is necessary for the strict prescription. One would still need a domain, ordering, physical inner product and nonzero states before comparing an area spectrum. [Ciambelli, Freidel and Leigh](https://arxiv.org/abs/2407.11132)
2. **Test reduction and gauge independence directly on a radiative observable.** Starting from smooth, expanding null data, a fixed physical cap frame, and a nonzero radiative wave packet, compute a normalized, smeared shear two-point function on two interior cuts spanning the same boundaries—comparing covariant gauge against reduced null variables, and comparing distinct null reductions (such as area gauge vs. affine parameter) at one loop while keeping edge variables, zero modes, and matching renormalization conditions. A regulator-independent mismatch disproves equivalence for those specifications; comparing *closed* amplitudes further requires independent control of the unnormalized trace. [Equations (D.7)–(D.9)](https://arxiv.org/html/2611.34924v1#A4.E7) · [Intermediate cuts](https://arxiv.org/html/2611.34924v1#S5.SS2.p11.1) · [One-loop determinant audit](D1.md)

## Executable check

Run `python3 checks/reduction.py` from the repository root. Expected checks:

- exact verification of both spherical ADM identities across 128 rational field jets and exact mass $M=1$ across static and Painlevé–Gullstrand slices at four exterior radii under three null boosts;
- exact agreement across 432 free-graviton tidal two-point polarization sums;
- reproduction of the matched tilted-clock norm $0.426044354$ (vs. $0.261708321$ and $0.590380387$ when the measure determinant is omitted);
- finite-difference verification of the cylinder orbit-volume ground state at $c_0=\kappa=1$ with maximum residual $4.2\times 10^{-7}$ ($<10^{-6}$). (The spectral gap follows from the analytic factorization above.) [Reproduction code](../checks/reduction.py)
