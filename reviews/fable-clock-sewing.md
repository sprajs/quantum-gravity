# Fable’s review of the clock tail and the closed cut

Two key steps in Venkatesa Chandrasekaran’s *An algebraic quantization of gravity from the null cone* ([arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1)) ask different existence questions:

1. **Clock nonemptiness, (5.16):** Do physical states of finite clock reading approximate the reference Gaussian?
2. **Closed sewing, (5.38):** Does an uncut gravitational amplitude equal the limit of partial sums over states on a closed intermediate cut?

Fable tested the strongest defenses of each step. Neither follows from open sewing or from the classical clock distribution alone. All equation references use version 1. [Preprint](https://arxiv.org/abs/2611.34924v1) · [Clock estimate](https://arxiv.org/html/2611.34924v1#S5.E16) · [Closed-cut argument](https://arxiv.org/html/2611.34924v1#S5.E38)

---

## What the clock tail measures

Let $Q=\sup_c Q_c$ be the monotone limit of the capped clock forms, $M=\overline{D(Q)}$ the closure of its form domain, and $P_M$ the orthogonal projection onto $M$. Let $T$ be the positive self-adjoint operator representing $Q$ on $M$. For a normalized reference Gaussian $\Omega$, (C.13)–(C.14) give

$$
1-\langle\Omega,\Psi_L\rangle
=\|(1-P_M)\Omega\|^2+
\left\langle P_M\Omega,\frac{T}{L+T}P_M\Omega\right\rangle .
$$

As the resolvent scale $L\to\infty$, the second term vanishes and operator monotonicity controls the capped contribution at $c_L=\tfrac12\log(L/b)$ (with corner radius $b$). The remaining quantum tail therefore converges to $\|(1-P_M)\Omega\|^2$.

A vanishing classical Wigner tail implies (5.16) only if one also proves that $\Omega$ lies in $M$ (or has nonzero projection onto $M$, as needed in (5.20)). Expanding around a classical configuration does not bound the Weyl symbol of a difference of noncommuting resolvents by a classical indicator function. Fable agrees with the manuscript’s own footnote describing this step as heuristic. [Appendix C.2](https://arxiv.org/html/2611.34924v1#A3.SS2) · [Form-domain audit](../audit/05-1.md)

### The strongest finite-resolution defense—and its limits

Freeze the corner of a round diamond, retain one polarization, and truncate to $n$ radial Fourier pairs and $N_{\rm ang}$ angular harmonics. In this model’s conventions, $\hbar_e=2\pi N_{\rm ang}/s$ with $s=\mathscr A/(4G_N\hbar)$. For a quadratic shear cost $\Xi=\xi^TG\xi/2$ in canonical quadratures, the Gaussian expectation of $e^{\Xi}$ is finite whenever $\Sigma^{-1}>2M_G$, where $\Sigma$ is the covariance matrix and $M_G=J^{-1}\tan(JG/2)$ for the symplectic matrix $J$.

At $\epsilon=0.2$, the numerical cut grid yields vacuum stability thresholds $\hbar_e n \approx 0.28, 0.33, 0.34$ at $n=2, 4, 8$. Whenever this criterion holds uniformly across the radial interval, $Q[\Omega]<\infty$ and Markov’s inequality bounds the probability above clock limit $\ell$ by $Q[\Omega]/\ell$; indeed, a single finite-form vector suffices for nonemptiness at large enough $\ell$. [Quadratic model](../checks/fable-clock-sewing.py)

Four effects restrict extending this finite-resolution defense to the full continuum theory:

- **Curved target metric.** The second polarization enters with weight $e^{2z^1}(\partial z^2)^2$. Even on a single radial cell, its exponential can have infinite expectation in a product Gaussian because the conditional quadratic coefficient is unbounded. (Infinite expectation in $\Omega$ still leaves open whether *other* finite-form vectors approximate $\Omega$.)
- **Fluctuating corner.** A varying corner density makes the local coupling $\propto 1/\varrho_S(y)^2$ arbitrarily large in tails.
- **Resolution dependence.** The Gaussian threshold shrinks as the number of modes increases.
- **Zero-point floor.** A positive oscillator ground energy raises the minimum possible clock reading itself. At $n=8$, the model’s integrated lower bound in units of the classical minimum is about $2.6$, $24$, and $1.8\times 10^5$ for $\hbar_e=0.01, 0.03, 0.10$. A separate polarized radial model proves complete loss of finite readings in its cutoff limit.

Neither calculation determines the interacting continuum projector for four-dimensional gravity. [Independent lower-bound model](../audit/shear-uv.md)

---

## Can nested cuts have incompatible exponential domains?

Because integrated shear increases outward along a light ray, physical clock cuts are **nested**. Unnested models with independent position and momentum weights already test whether vanishing classical tails imply a nonempty quantum domain, while nested models test whether nesting rescues the domain. Writing $[X,P]=i\hbar$ for positive exponential clock terms gives the following comparison:

| Positive clock terms | Common finite-form domain |
|---|---|
| $e^{cX^2}$ and $e^{cP^2}$ (unnested) | Zero space for $c\hbar\ge 1$ by the Gaussian uncertainty theorem. |
| $e^{cX^2}$ and $e^{c(X^2+P^2)}$ (nested) | Zero space above the root of $c\hbar\tanh(c\hbar)=1$ ($c\hbar\approx 1.19968$); dense below it. |
| $e^{V(X)}$ and $e^{V(P)}$, $V(t)=t^2+t^4$ (unnested) | Zero space for every $c>0$ by Fourier uncertainty. |
| Three nested costs with the target metric of (4.21c) | Zero common domain for every $c>0$ in the differential-operator model below. |

In the second row, any vector in the range of $e^{-c(X^2+P^2)/2}$ inherits Gaussian Fourier decay from the oscillator heat kernel; combining that with $e^{cX^2/2}\psi\in L^2$ fixes the threshold $c\hbar\tanh(c\hbar)=1$. Below threshold, Gaussians $e^{-\beta x^2/(2\hbar)}$ and their translates lie in the domain for $\max(c\hbar,\tanh(c\hbar))<\beta<\coth(c\hbar)$. Classical tails vanish on both sides of the threshold. [Quadratic domain test](../audit/04-3.md) · [Superquadratic test](../audit/05-1.md)

### Three-cut curved-target model

On $L^2(\mathbb R^2)$, consider positive form realizations of three nested operators incorporating the target-metric weight $e^{2Q_1}$:

$$
A_1=cQ_2^2,\qquad A_2=A_1+c e^{2Q_1}P_2^2,\qquad A_3=A_2+cP_1^2 .
$$

The first two operators commute with $Q_1$. On each fiber $q_1$, a dilation reduces them to the nested one-pair model with effective coupling $c e^{q_1}$, so any vector in the joint domain must vanish on the entire half-plane where $c e^{q_1}$ exceeds the threshold. Membership in $D(e^{A_3/2})$ simultaneously supplies the factorial bounds on powers of $A_3$ needed for analytic-vector elliptic regularity, making the wavefunction locally real analytic. A real-analytic function that vanishes on an open half-plane vanishes identically.

**Scope of this model.** This is a continuum differential operator on **two configuration coordinates** with three modeled cuts. It preserves nesting and the target metric factor while omitting the rest of the null-cone algebra and cap. It is a counterexample to inferring a nonempty quantum domain from small classical tails, **not** a no-go theorem for the gravitational clock.

### Constructive alternative orderings

Two modifications show how changing the quantization prescription alters the domain question:

- **Path-ordered exponentials.** On a finite radial partition, replace $e^{\Xi(v_k)}$ by $R_k^\dagger R_k$, where $R_k=e^{\Delta_k/2}\cdots e^{\Delta_1/2}$ for positive increments $\Delta_j$. Each factor’s bounded inverse is injective with dense range, so reversing the product of inverses yields a dense domain at *every* coupling. The $R_k$ are closed, their domains nest, and $\|R_j\psi\|\le\|R_k\psi\|$ for $j<k$. This provides a densely defined positive clock on a finite partition with a frozen or suitably fiberwise corner and compatible generators. Refining the partition, restoring angular and corner correlations, and controlling zero-point energy remain separate tasks.
- **Anti-Wick effects.** Integrating coherent-state projectors over the classical allowed region produces a positive operator that converges strongly to the identity under finite-dimensional coherent-state hypotheses, with trace equal to the classical phase-space volume in quantum units. However, an effect is not a sharp spectral projection and does not deliver the exact area bound (5.21).

Both alternatives change the operator being quantized.

---

## Does the signed closed amplitude prove finite rank?

Set $W=C_b^\dagger C_b$, and assume the claimed uniform lower bound $W\ge dI$ on the clock-selected space, where $d=m_{b,\mathscr D}e^{-s_*}>0$. For any finite-rank basis projection $P$, define the cut vector $V_P=\sum_{i\in P}C_b e_i\otimes\bar e_i$, so that $\|V_P\|^2=\operatorname{Tr}(PW)$. Three readings of (5.38) carry different proof obligations: [Dimension audit](../audit/05-2.md) · [Independent examination of the sign argument](../audit/dimension-crosscheck.md)

1. **Unnormalized signed insertion (equivalent to finite rank).** Suppose a cofinal family of cycle projections obeys $\langle V_P,XV_P\rangle/\|V_P\|^2\le-\kappa<0$ for the bounded insertion $X$, as used from (D.25). Then
   $$
   \kappa d\,\operatorname{rank}P\ \le\ |\langle V_P,XV_P\rangle|\ \le\ \|X\|\operatorname{Tr}(PW).
   $$
   Boundedness of the partial sums along that cofinal family is therefore **already equivalent to finite rank**—the sign argument is no weaker than proving a finite trace. The uncut boost signal provides a plausible physical observable, but it cannot by itself force the cut partial sums to remain bounded.
2. **Normalized correlators.** Tensoring with an infinite-dimensional spectator space $\ell^2$ leaves normalized expectations of finite-system probes unchanged along product cutoffs even while the unnormalized closed norm diverges. Open sewing constrains matrix elements between two fixed normalizable external states; proving that normalized cut limits converge uniquely to the uncut value for version 1’s insertion requires a separate estimate.
3. **Independent finite uncut trace.** If the gravitational path integral independently supplies a finite uncut amplitude $Z[1]$ and identifies it with the ordinary Hilbert-space trace $\operatorname{Tr}(W)$, then $\operatorname{rank}P_{\mathscr D}\le Z[1]/d$ follows immediately. However, Appendix E.3 appeals to finite rank when verifying closure, and the normalized one-loop ratio in (5.28a) cancels $Z[1]$. As a control, version 1’s JT model exhibits open sewing alongside a divergent ordinary reflected trace, while JT gravity with matter admits a finite trace of type II. These models test the inference rule without determining the four-dimensional algebra. [Open and closed cuts](../audit/04-gluing.md) · [JT example](../audit/02-jt.md)

---

## Can any nonzero projection have finite rank?

A general spectral lemma underlies the corner-charge test: if a self-adjoint operator $K$ has no eigenvectors and its spectral projections commute with a projection $P$, then every nonzero $P$ has infinite rank (a finite-dimensional reducing subspace would carry a Hermitian matrix with an eigenvector).

Two candidates in version 1 trigger this test:

- A physically marked angular area charge, which classically generates a relative boost leaving the incoming focusing data unchanged in the smooth-vertex chart.
- Any variable omitted from a truncated clock that remains in the physical Hilbert space as a spectator. (A variable removed by gauge reduction creates no spectator multiplicity.)

In both cases, turning the lemma into a theorem about the quantum theory requires proving that the variable survives gauge reduction and that its spectral projections **strongly commute** with the clock projection—formal commutation on an algebraic core does not guarantee strong spectral commutation for unbounded operators. [Physical corner-charge hypotheses](../audit/finite-kinematics.md)

**What would settle both questions.** Settling nonemptiness requires exhibiting one finite-form vector for the actual two-polarization clock under the chosen boundary conditions. Settling finiteness requires either proving compactness of its physical sublevel spaces or proving that the closed cut inner product equals an independently finite ordinary trace while keeping all corner-distinguished states (some of which Appendix D.3 restricts). A bare shear square needs an ultraviolet construction; a renormalized square needs its own lower bound. [Radiative count and hypotheses](../audit/D3.md)

## Executable checks

Run these scripts from the repository root to verify the explicit models above:

- `python3 checks/fable-clock-sewing.py` — confirms the nested one-pair threshold $t\tanh t=1$ ($t\approx 1.19968$), the dense domain of the $v$-ordered exponential at every coupling, the sampled vacuum-domain thresholds $\hbar_e n \approx 0.28, 0.33, 0.34$ at $n=2,4,8$, and the $n=8$ zero-point floor ratios ($2.593$, $23.83$, $1.836\times 10^5$ at $\hbar_e=0.01, 0.03, 0.10$). (The three-cut elliptic argument is analytic.) [Clock checks](../checks/fable-clock-sewing.py)
- `python3 checks/05-2.py` — reproduces the spectator-multiplicity and exhaustion tests, showing how three exhaustions of the same space yield boost contrasts of $-0.45970$, $-0.18388$, and $-0.02242$. [Closed-sum checks](../checks/05-2.py)
