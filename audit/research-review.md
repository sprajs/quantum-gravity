# Can the proposed gravitational clock count the states of a diamond?

In Venkatesa Chandrasekaran’s proposal ([arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1)), a macroscopic causal diamond is defined by the subspace of physical preparations that pass a geometric clock measurement—an average affine length along a lightlike boundary. Three mathematical outcomes carry sharply different physical meanings: an empty space (rank $0$), a nonzero finite-dimensional space (finite rank), or an infinite-dimensional space (infinite rank).

This cross-check evaluates the core questions raised in Fable’s independent review against version 1’s equations and explicit models. Throughout, **model calculations** (which test an inference rule or supply a control) are kept distinct from **results about interacting four-dimensional quantum gravity**. None of the calculations below is a physical refutation of finite-dimensional diamonds; rather, they isolate specific proof gaps and defects in the construction as written, leaving the interacting four-dimensional outcome open. [Original preprint, v1](https://arxiv.org/abs/2611.34924v1) · [Definition of the projector, (5.1)–(5.3)](https://arxiv.org/html/2611.34924v1#S5.E1)

| Question from Fable’s review | Classification | What survives cross-examination |
|---|---|---|
| Does vacuum shear empty the bare diamond? | Obstruction in two linearized models. Its extension to the gravitational clock remains open. | Two linearized, polarized radial models with frozen corner geometry exclude every state below a fixed clock threshold as the radial cutoff increases. Extending this to the full two-polarization field and fluctuating corner remains open. |
| Does subtracting vacuum shear leave infinitely many angular excitations? | Proof gap | The averaged quadratic clock charges a fixed radial excitation equally in every normalized angular harmonic. Proving infinite rank still requires an estimate for the spectral projector after subtraction, constraints, and nonlinear focusing. |
| Can a Lorentzian boost produce a continuum of allowed areas? | Conditional reductio from (5.19) | A continuous family of sharp, clock-accepted areas inside *one* representation would defeat finite rank. Version 1 extends a single fixed-area state; its boost filters do not construct that family. |
| Does the Appendix D count contradict the entropy law? | Proof gap (cannot supply) | Appendix D.3 bounds radiative occupations at prescribed cap and corner data. The entropy calculation traces all selected states across areas; the full physical counting measure remains uncomputed. |
| Does a finite closed amplitude select a type II algebra? | Control / reviewer prior | JT gravity with matter shows one way a finite geometric trace can arise in an infinite-dimensional Hilbert space. Identifying the subregion algebra, state, and trace in four-dimensional gravity is an independent task. |

[Fable’s whole-paper review](../reviews/fable.md) · [Fable’s research priorities](../reviews/fable-research.md) · [Clock domain](05-1.md) · [Radiative state count](D3.md) · [Closed-cut test](dimension-crosscheck.md)

---

## A lower bound on an interval of the bare clock

Freeze the angular area density at the round value $b$. The clock then averages $b\int_\epsilon^1 e^{\Xi_y(v)}\,dv$ over the sphere. Two subtleties prevent naive shortcuts:

- A lower bound at the single upper endpoint $\Xi_y(1)$ does not bound the integral proportionally to $e^{\Xi_y(1)}$ (a large peak confined to an arbitrarily thin layer near $v=1$ contributes negligibly).
- A diverging vacuum *mean* still leaves open whether some squeezed subspace has finite clock readings.

A **state-independent lower bound holding across a fixed interior radial interval** resolves both issues at once. An earlier radial basis with interior nodes yields such a bound by orthogonality; the calculation below checks that the same mechanism holds under the periodic Fourier regulator used in Fable’s clock review. [Clock and form, (4.22)–(4.27)](https://arxiv.org/html/2611.34924v1#S4.E22) · [Interior-node calculation](shear-uv.md) · [Periodic generator used for comparison](../checks/fable-clock-sewing.py)

Let $L=1-\epsilon$, $\kappa=2\pi/L$, and $\theta=\kappa(v-\epsilon)$. For one polarization write $z=x/v$, and with canonical oscillators $[a_k,a_j^\dagger]=\delta_{kj}$ set

$$
x_N(v)=\gamma\sum_{k=1}^N\frac{a_ke^{-ik\theta}+a_k^\dagger e^{ik\theta}}{\sqrt{k}},
\qquad D_N=x_N'-x_N/v,\qquad
\Xi_N(v)=\frac14\int_\epsilon^v D_N(r)^2\,\frac{dr}{r}.
$$

Hold $\gamma>0$ fixed as $N$ grows. Choose a nonzero real smooth window $h$ supported strictly inside $(\epsilon,v_0)$ with $v_0<1$ and $h(v)^2\le 1/v$. Write $\|h\|^2=L^{-1}\int h^2\,dv$ and $H_h=L^{-1}\int h^2 D_N^2\,dv$ (all operator manipulations hold as quadratic forms on the finite oscillator core). Setting $F_m=L^{-1}\int h D_N e^{im\theta}\,dv$, Parseval’s identity and $F_{-m}=F_m^\dagger$ yield

$$
H_h=F_0^2+2\sum_{m>0}F_m^\dagger F_m+\sum_{m>0}[F_m,F_m^\dagger].
$$

Because every commutator is a scalar, writing $C_{h,N}=\|F_0\Omega\|^2+2\sum_{m>0}\|F_m\Omega\|^2$ for the oscillator vacuum $\Omega$ and using positivity of the first two sums gives $H_h\ge\langle H_h\rangle_\Omega-C_{h,N}$. The two terms scale differently with the cutoff $N$:

$$
\langle H_h\rangle_\Omega
=\gamma^2\sum_{k=1}^N\left(\kappa^2 k\|h\|^2+\frac{\|h/v\|^2}{k}\right),
$$

while for $m\ge 0$ only the creation part of $F_m$ survives on $\Omega$. With $\widehat h_n=L^{-1}\int h(v)e^{in\theta}\,dv$,

$$
\|F_m\Omega\|^2
=\gamma^2\sum_{k=1}^N\frac1k
 \left|i\kappa k\widehat h_{m+k}-\widehat{(h/v)}_{m+k}\right|^2 .
$$

Because $h$ vanishes near the endpoints, both Fourier sequences decay faster than any power of $n$. Summing first over $n=m+k$ bounds $C_{h,N}$ by a cutoff-independent multiple of $\sum_{n\ge 1}\big[n^2|\widehat h_n|^2+(1+\log n)|\widehat{(h/v)}_n|^2\big]$. Hence there exist constants $c_h>0$ and $c'_h<\infty$, independent of $N$, such that

$$
\Xi_N(v)\ \ge\ (L/4) H_h\ \ge\ [c_h N(N+1)-c'_h]I,
\qquad v_0\le v\le 1.
$$

Spectral calculus converts this operator lower bound into an exponential floor on every generator. For an angular profile $Y(y)$ multiplying the focusing by $|Y(y)|^2$, restricting to any patch of positive solid angle where $|Y|$ is bounded below and integrating over $[v_0,1]$ makes the clock floor diverge with $N$, driving the spectral projection below any fixed $\ell$ to zero. Under §5.1’s focusing ceiling $R$, replacing the scalar floor by its minimum with $R$ leaves the obstruction intact as both $N$ and $R$ diverge—using only scalar bounds on individual exponentials, with no ordering relation assumed between exponentials of distinct quadratic operators. [Bounded focusing and the resolvent](https://arxiv.org/html/2611.34924v1#A3.SS2.p3.1)

**Numerical check.** Taking $\epsilon=0.2$, $v_0=0.68$, $\gamma^2=1/(2\pi)$, and a single half-wave $\sin^4$ window on $(0.28,0.68)$ (sufficiently smooth for the required Fourier decay) at $N=2, 4, 8$:

- the window bound $L(\langle H_h\rangle_\Omega-C_{h,N})/4$ gives $0.556, 2.392, 9.383$;
- direct symplectic diagonalization of $\Xi_N(v_0)$ gives $9.284, 29.914, 107.311$.

Run `python3 -B checks/clock_window.py` from the repository root to reproduce both columns (using 2,048 radial samples, 119 positive Fourier frequencies, and 3,000 Simpson panels) and confirm $0.00\times 10^0$ refinement difference at 4,096 samples and 159 frequencies. The infinite-cutoff divergence follows from the analytic bound above. [Window calculation](../checks/clock_window.py) · [Generator and symplectic diagonalization](../checks/fable-clock-sewing.py)

**Limits of the model.** In the full theory, operators are $\mathcal Q(z^\alpha)$ in a nonlinear canonical chart, the finite-cap symplectic form mixes radiation with the corner, the second polarization carries the metric weight $e^{2\widehat z^1}$, and the clock sandwiches the exponential between quantum area densities. Establishing a lower bound on a truncated subsystem requires verifying that it persists on the full state space, because cross-terms with omitted degrees of freedom can shift an infimum. A rotationally invariant family of independent linear channels adds an angular factor $\sim J^2$ via the harmonic addition theorem, but inferring a universal UV length or an exact $N^2J^2/s$ floor at finite $G_N$ requires the full field commutators and boundary conditions. [Canonical fields and area weighting](https://arxiv.org/html/2611.34924v1#S4.SS3.p1.1) · [Finite-cap form](cap-crosscheck.md)

---

## What the renormalized and angular tests could settle

**Vacuum subtraction.** Exchanging the two radial integrals in the round, one-polarization quadratic clock yields the weight $v(1-v)/4$ on $(z')^2$ in $\bar u_*/b$. Extended by zero outside $[\epsilon,1]$, its square root has a logarithmically divergent squared-derivative integral near $v=1$ and a jump at $v=\epsilon>0$ (smoothing the jump over width $\delta$ costs order $1/\delta$). Consequently, the lower bound $-c_f\|g'\|^2/2$ in (D.28) gives no uniform lower bound by this route. Moreover, (D.28) applies to the Wick square of a *transversely smeared* free current in affine coordinate $u$ with a smooth window—squaring an angularly smeared shear and averaging its local square are distinct operations. Known sharp inequalities for chiral stress tensors and single-null-line counterexamples for a four-dimensional free scalar act as controls for specified smearings; because the gravitational clock exponentiates a partial integral, a negative quadratic correction or the failure of one lower-bound route leaves its full spectrum undetermined. [Paper, (D.28)](https://arxiv.org/html/2611.34924v1#A4.E28) · [Fewster and Hollands](https://arxiv.org/abs/math-ph/0412028) · [Fewster and Roman](https://arxiv.org/abs/gr-qc/0209036)

**Angular degeneracy as a rank test.** At a fixed radial profile, every normalized angular harmonic carries the same quadratic incoming-clock cost; classically, smooth data oscillating rapidly around an angular annulus can even keep the averaged clock fixed while transverse focusing grows. In (D.40), the angular penalty comes from the induced normal connection together with cap and corner expansion data.

To turn angular degeneracy into a decisive quantum rank test, construct physical orthonormal incoming waves $\{e_j\}$ and set $p_j=\|P_\ell e_j\|^2$ for one limiting projector. By Bessel’s inequality, $\sum_j p_j\le\operatorname{rank}P_\ell$ for any finite family, so a divergent sum at fixed $\ell$ proves infinite rank even when projected states overlap. Uniform estimates on the *full positive clock* $T$ would suffice: if $\langle e_j,Te_j\rangle\le C<\ell$, the spectral theorem gives $p_j\ge 1-C/\ell$. Equal Hessian eigenvalues alone give no such estimate once the exponential, cap compatibility, and opposite cone enter. [Physical projector](https://arxiv.org/html/2611.34924v1#S5.SS1.p2.1) · [Angular example and boundary cost](D3.md) · [Rank test](finite-kinematics.md)

---

## Does choosing the base area already decide the spectrum?

Starting from a normalized eigenstate at one positive total area $A$ on the incoming area-preserving algebra, version 1 extends its expectation values to one pure state $\omega$ on the full source algebra, forming the GNS Hilbert space $\mathcal H_\omega$. The paper exhibits the boost phase appropriate to an area-changing transition *if* one connects two areas, gives Fourier filters selecting spectral intervals, and claims in (5.41) a matrix element connecting at least two allowed areas—without constructing an operator for every desired area shift. [Choice of representation and interval filters](https://arxiv.org/html/2611.34924v1#S4.SS2.p5.1) · [Equation (5.41)](https://arxiv.org/html/2611.34924v1#S5.E41)

**Why a continuous area dilation cannot act strongly continuously on sharp states.** If a unitary $D_c$ satisfies $D_c^{-1}\widehat A D_c=e^c\widehat A$ and $\widehat A\Omega=A\Omega$ with $A>0$, then $D_c\Omega$ is an orthogonal eigenvector of eigenvalue $e^c A$, giving $\|D_c\Omega-\Omega\|=\sqrt{2}$ for every $c\ne 0$. Such a family cannot be strongly continuous at $c=0$. The standard continuous boost $e^{i\eta\widehat A/(8\pi G_N\hbar)}$ preserves area, so a source implementing area dilations is an extra assumption; a noncompact boost parameter alone allows either discrete or continuous spectra. (A multiplication representation with continuous area accommodates regular dilations on wave packets, but sharp positive areas are then generalized rather than normalizable eigenstates.) [Relations (4.2) and (4.12)–(4.15)](https://arxiv.org/html/2611.34924v1#S4.E2)

**The countability reductio (no dilation required).** Note that this argument is a *reductio* from the paper’s own nonemptiness claim (5.19)—it tests internal consistency rather than asserting simultaneously with the UV floor that the clock window is empty. Suppose *one* representation contains normalized sharp-area states across an uncountable interval of areas, suppose the clock commutes strongly with area, and suppose every such vector has positive acceptance probability at some finite clock threshold. Taking integer thresholds $n$, the sets of accepted areas form a countable cover of the interval, so some fixed $n$ accepts uncountably many mutually orthogonal nonzero projected vectors—contradicting finite rank (indeed, finite rank at every integer threshold permits at most countably many distinct sharp areas across all finite thresholds). The same conclusion follows immediately from version 1’s stronger full-weight limit (5.19). [Equations (5.19)–(5.20) and footnote 20](https://arxiv.org/html/2611.34924v1#S5.E19)

The decisive open question is whether the construction identifies observables, states, and clock projections *across* base areas inside one representation. Re-applying the existence estimate inside a separate representation for each base area never compares vectors across areas; a direct integral gives individual sharp fibers measure zero, while a direct sum makes distinct fibers orthogonal by fiat—neither is the pure state extension specified in §4.2. Conversely, a source mixing two discrete levels already changes area without generating a continuum. Computing allowed area-changing sources and their matrix elements in one physical representation would distinguish these scenarios. [Choice of one pure extension](https://arxiv.org/html/2611.34924v1#S4.SS2.p8.1) · [Fixed-area and full algebras](04-2.md)

**Fixed-total-area test (local area density).** A sharper test stays within a single total-area sector. Let $h$ be a nonconstant angular function tied to a physical boundary frame and set $K_h=(8\pi G_N)^{-1}\int h\,dA$:

- **Exact classical half.** For the smooth-vertex corner potential (3.42a), the boost angle enters only through $\mathscr K(y)\,\delta\Gamma(y)$, so $K_h$ generates a shift of the relative boost angle alone and leaves the incoming clock **exactly invariant**.
- **Quantum spectral lemma.** If $K_h$ is self-adjoint, has no eigenvectors (or merely has a nonzero diffuse spectral component in one accepted state), and its spectral projections commute strongly with $P_\ell$, then partitioning that diffuse component into disjoint sets produces infinitely many orthogonal accepted states at the *same* total area—forcing $\operatorname{rank}P_\ell$ to be $0$ or $\infty$.
- **Unchecked chart and domain steps.** In a multiplicative shape chart $f_S=xh+f_0$, the derivative of $K_h$ with respect to $x$ is a positive multiple of the angular variance of $h$, so a regular continuous coordinate $x$ gives a diffuse area moment. What remains to be established is that the physically marked charge survives the gauge quotient, is linear in the unspecified canonical chart actually used in (4.7), and has spectral projections preserving the completed clock form and its domain. A classical bracket or formal core commutator does not imply strong commutation for unbounded operators; equation (4.26) asserts preservation of *total* area, not strong commutation with every local area density. [Smeared corner test](finite-kinematics.md) · [Local boost geometry and quantum area density](https://arxiv.org/html/2611.34924v1#S4.SS3.p4.1) · [Reviewer vs. editor readings](../reviews/fable-clock-sewing.md)

---

## Which density enters the Schwarzschild logarithm?

Set $s=A/(4G_N\hbar)$ and let $dN_\ell$ count exact states (with multiplicities) inside one clock window, with boost-weighted measure $d\nu_\ell=e^{-s}dN_\ell$. The packet trace in (5.66) is its Gaussian transform $T(b)=\int e^{-(s-b)^2/(4b)}\,d\nu_\ell$ (writing $b=s_b$), which has width $\sqrt{2b}$ in $s$.

If a coarse-grained density varies smoothly on that width and scales as $d\nu_\ell\sim C s^p\,ds$, then $T(b)\sim C\sqrt{4\pi}\,b^{p+1/2}$. Assigning the local coefficient $106/45$ to the packet exponent gives:

- $p=167/90$ for the weighted density per unit *area* $s$ (distinct from Sen’s fixed-$J_3$ exponent per unit *mass*, which coincidentally also equals $167/90$ in four dimensions),
- $Z\propto s_*^{257/90}$ for the integrated clock trace (an exponent specific to the clock ensemble, not directly comparable with Sen’s mass-density coefficients),
- $\langle s\rangle/s_*\to 257/347$ and via (5.61) $q=257/302$—relations that follow identically from any power-law density $s^p$ with small delay and thus restate the $106/45$ assignment rather than adding an independent test, and
- $dN/dM\propto e^s s^{106/45}$ at fixed mass with angular momenta summed, upon restoring $e^s$ locally and using $ds/dM\propto\sqrt{s}$.

Both routes rely on the same scaling input; discreteness, irregular level spacings, cutoff dependence, and bounded prefactors can each block a pointwise inference of $dN/ds$ from a logarithmic asymptotic. [Equations (5.60)–(5.69)](https://arxiv.org/html/2611.34924v1#S5.E60a) · [Packet and density calculation](ensemble-crosscheck.md) · [Sen’s ensembles](https://arxiv.org/abs/1205.0971)

**Clock ratios and joint distributions.** The clock ratio $q$ constrains the *cumulative weighted clock distribution*. For nested projectors put $F(L)=\int_0^L Z(t)\,dt$; equation (5.56) gives $F(L)/(LZ(L))=1-\langle u\rangle_L/L$. If $\langle u\rangle_L/L\to q\in(0,1)$, then $LF'(L)/F(L)\to 1/(1-q)$ away from jumps, giving $Z(L)=L^{q/(1-q)+o(1)}$ (which still allows factors such as $\log L$). Converting to a law *per unit area* requires the joint clock-area distribution—for example, even a polynomially suppressed density $dN/ds=e^s/\sqrt{s}$ on $1<s<s_*$ yields a weighted mean asymptotic to $s_*/3$, not an order-one area. The Schwarzschild delay assumption (5.53) and scaling (5.54) are therefore substantive inputs. [Clock moment and integrated trace](https://arxiv.org/html/2611.34924v1#S5.SS3.p6.2) · [Entropy cross-check](05-3.md)

**Microscopic multiplicities vs. Euclidean weights.** Equation (D.46c) bounds radiative states at *fixed edge and cap data* and prescribed budget for (D.40) by $\log d_{\rm rad}(s)\lesssim_\epsilon 1+(sQ_*)^{3/4}$. At bounded $Q_*$ this is sublinear in $s$ and therefore **cannot supply** the $e^s$ multiplicity on its own, while leaving boundary and area-sector multiplicities uncounted. (Claiming an order-one thermal mean would additionally require a uniform bound on the *total* weighted tail and a nonvanishing normalization as the clock window grows.) The factor $e^s$ from the normal disk in (D.48) is a Euclidean action weight; reading it as a state count requires proving equality between that integral and the Hilbert-space trace across all allowed sectors. Similarly, the local conical heat-kernel coefficient supplies only one ingredient of a capped finite-width trace alongside collective-coordinate measures, zero modes, boundary conditions, marginality selection, and ADM mass. [Bound and disk integral](https://arxiv.org/html/2611.34924v1#A4.SS3.p6.1) · [Entropy review](../reviews/fable-boundaries-entropy.md) · [Comparison with Sen](sen.md)

---

## A finite trace and a finite number of states

Globally, version 1’s pure state on the full algebra yields the type I factor $\mathcal B(\mathcal H_\omega)$, whereas a fixed-area incoming algebra or a one-sided subregion algebra in another representation can have different observable content. Open sewing resolves the identity between two normalizable boundary states by Cauchy–Schwarz. Closing the final cut in (5.38) instead asks for an unnormalized signed amplitude along an exhaustion. Given the assumed uniform lower bound $W=C_b^\dagger C_b\ge cI$ on $\mathcal H_{\mathscr D}$, the ordinary trace obeys $\operatorname{Tr}(PWP)\ge c\,\operatorname{rank}P$ for every finite cut—and along the uniformly negative cycle family of (D.25), bounded partial sums of the signed insertion are already logically equivalent to finite rank. Model exhaustions confirm that open sewing alone leaves the closed answer undetermined. [Open and closed cuts](04-gluing.md) · [The specific sign argument](dimension-crosscheck.md)

**JT gravity and type II controls.** In JT gravity with bulk matter and asymptotic boundaries, Penington and Witten obtain a type II$_\infty$ boundary algebra whose semifinite trace can be finite on projections of infinite Hilbert-space rank (giving a type II$_1$ corner upon compression). Version 1’s §2 instead studies a capped JT model with an unrestricted clock-conjugate direction. Comparing either to four-dimensional gravity requires identifying preparations, trace, boost response, and cut matching; Jensen, Sorce, and Speranza’s perturbative compact-region construction likewise relies on an observer and modular-flow assumptions. Failure of the finite-rank proof by itself selects neither an algebra type nor an entropy correction. [Penington and Witten](https://arxiv.org/abs/2301.07257) · [Kolchmeyer](https://arxiv.org/abs/2303.04701) · [Jensen, Sorce and Speranza](https://arxiv.org/abs/2306.01837) · [The paper’s JT control](02-jt.md)

The proposed JT reductio also has a missing premise: at fixed corner dilaton, version 1’s capped JT preparations yield an $L^2$ clock family with a divergent ordinary reflected trace, whereas allowing a compact dilaton interval leaves unspecified how to build and normalize the uncut preparation required in §5.2. A free-scalar derivative can mimic the kinematic boost ratio (5.29), but four dimensions involves a shared graviton polarization and the uncut collar hypothesis (5.36b). Thus JT disproves inferring finite rank from open sewing and bounded weights alone, while leaving (5.38)’s status in four-dimensional gravity dependent on the actual gravitational cutting rule. [Capped JT trace](02-jt.md) · [Common polarization and collar hypothesis](https://arxiv.org/html/2611.34924v1#S5.SS2.p11.3) · [One-loop collar check](D2.md)

### Narrower tests of related claims

- **Caps and matching.** On the variable-area, fixed-ratio cap, the printed two-form (A.14) has a nonzero exterior derivative in an explicit polarization family. An endpoint cap term repairs the tested pullback, while fixing different edge data makes the discrepancy vanish. Classical matching on an open overlap patches solutions, whereas matching a few corner fields is strictly weaker; quantum propagators between covers remain to be built. Cap Cauchy data in (3.19) motivates searching for clock-insensitive states without automatically supplying an unconstrained cap Hilbert factor. [Boundary conditions](../reviews/fable-boundaries-entropy.md) · [Matching examples](03-5-6.md)
- **Marginality, determinants, and backreaction.** The bare clock constrains one cone without imposing marginality; evaluating the surface integrand of (5.67b) on a round flat sphere ($-8\pi$ vs. $+8\pi$ on a marginal sphere) tests that saddle condition without predicting a flat-diamond entropy. In (D.9), differentiating a source-dependent Hessian includes the classical saddle’s response (a tadpole missed by calling the result an explicit contact term), and the semiclassical variational identity at finite smearing leaves coincident-point renormalization open. [Schwarzschild condition](https://arxiv.org/html/2611.34924v1#S5.SS3.p2.1) · [Hessian counterexample](D1.md) · [One-loop field equation](06-2.md)
- **AdS, topology, and reconstruction.** For a nontrivial band probability $p$, the absolute centered double sum in (5.44) equals $2p(1-p)Z_\beta$, so row-wise cancellations cannot establish joint convergence. For a connected two-boundary filling, (5.71) assumes its inner product equals the Hilbert–Schmidt pairing with product preparations; proving that independently would exclude components orthogonal to the product subspace. Appendix E’s reconstruction checks its own closed-amplitude axiom using §5.2’s claimed finite rank, leaving the AdS spectrum and alternative realizations open. [AdS double sum](area-ads.md) · [Two-boundary residual](05-4.md) · [Axioms](E.md)

---

## Independent public criticism and the next four calculations

On 26 November 2026 Jonathan Oppenheim published a critique questioning the microscopic state count, diffeomorphism and cut invariance, and the existence of the quantum Hamiltonian needed for the semiclassical limit. Those objections map directly onto concrete equation-level tests here—especially closed sewing in (5.38), cut independence in Appendix E, and continuum evolution—while local finite-cut bounds and the Schwarzschild ensemble arithmetic can be checked separately. [Oppenheim’s article](https://superposer.substack.com/p/has-ai-come-for-quantum-gravity) · [Assessment of Oppenheim’s checks](oppenheim-obstacles.md) · [Closed-cut assertion](https://arxiv.org/html/2611.34924v1#S5.SS2.p13.2) · [Appendix E axioms](https://arxiv.org/html/2611.34924v1#A5.SS1)

Two earlier AI-assisted repositories also checked selected pieces without specialist peer review: SHIN09-git reproduced the Gaussian pair overlap and exhibited the closed-cut gap in a two-area model, while Lluis Eriksson’s Lean work formalized finite tails, conditional inequalities, and coefficient arithmetic. Neither settles the four-dimensional gravitational projector. [SHIN09-git, pinned report](https://github.com/SHIN09-git/null-cone-quantum-gravity-verification/tree/44df2c1e4915c0e654dd5907d91b775e83f31326) · [Eriksson’s publication and disclosures](https://airr.science/papers/ARR-2026-4VGGGBES9N9QKRJ9/versions/v1/) · [Pinned Lean statements](https://github.com/lluiseriksson/null-cone-quantum-gravity-certificates/blob/57ad447de34724c676eafdc6fa325cd8eb211520/lean/NullConeQGCert.lean)

Four concrete calculations would move the main questions from open to settled:

1. **Construct one physical clock.** Start from a closed finite-cap symplectic form with explicit boundary conditions, radial and angular smearings, refinement embeddings, and a composite shear prescription. Compute both a smooth interior lower bound and the finite-reading spectral weight of the reference Gaussian at fixed physical $G_N,\hbar,A,\epsilon,\ell$ to establish either a uniformly surviving state or a uniform obstruction. [Finite-cap check](cap-crosscheck.md) · [Regulator program](regulator-program.md)
2. **Test sector compatibility and angular acceptance before counting.** Specify the represented sources and spectral measures at each base area, test whether states transfer across areas preserving the same clock projection, and compare one-wave acceptance with and without fixed transverse expansions using the countability and Bessel rank tests above. Hold external boundary preparations fixed when changing an intermediate cut. [Cap and angular data](D3.md) · [Evolution between cuts](evolution.md)
3. **Compute one closed observable with its measure specified.** Evaluate the boost-sensitive insertion of (5.38) at fixed sources—or prove a uniform positive lower bound on the exact two-copy ratio (D.47)—computing the uncut value and the cut limit independently, including sectors outside the regular saddle. For a type II comparison, identify the observable algebra and trace used by the same preparation. [Compactness and replica tests](compactness-stress.md) · [Trace comparison](D3.md)
4. **Make the entropy and dynamical tests independent.** Compute a direct determinant for the specified area window across controlled widths and angular-momentum sectors to test (5.67c). Separately, compare an interacting low-energy observable at fixed kinematics with the known two-loop four-graviton scale dependence after matching infrared terms—unlike the free Gaussian pair overlap, where a coupling-dependent source delay can generate a logarithm without graviton self-interaction. [Ensemble test](ensemble-crosscheck.md) · [Graviton amplitude comparison](scattering.md) · [Bern, Chi, Dixon and Edison](https://arxiv.org/abs/1701.02422)
