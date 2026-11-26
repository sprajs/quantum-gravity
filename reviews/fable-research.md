# Fable’s research programme for the null-cone proposal

**Scope and provenance.** Fable’s research review of Venkatesa Chandrasekaran’s *An algebraic quantization of gravity from the null cone* ([arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1)) asks what concrete calculation could settle each disputed step in version 1. Fable formulated the initial research objections before a second reader assessed them. The priority ordering, predicted outcomes for proposed tests, and constructive alternatives below are **Fable’s**; the editors have kept model calculations, proof gaps, and open physical conjectures explicitly separated. [Preprint](https://arxiv.org/abs/2611.34924v1) · [Claim dependencies](../audit/dependencies.md)

---

## What the proposal still has to construct

| Stage of v1 | Result available | Missing evidence |
|---|---|---|
| Classical phase space (§3, Apps. A–B) | Bulk focusing, area boost charge, regular cone chart | A closed two-form including the finite cap and its embedding, an inverse on the declared observables, and compatibility across changes of cover. |
| Representation and evolution (§4) | Abstract source algebra, Gaussian states on a kinematic chart, pure extension, open sewing | A physical state on words containing the evolution operator, regularity and short-distance properties, regulated dynamics with a cut-independent limit, and identification of the one-sided algebra. |
| Pair amplitude (§4.4) | Convergent oscillator displacement with a nonuniform perturbative expansion | Coupling enters only through the chosen source; an interacting observable is needed to test dynamics. |
| Clock and dimension (§§5.1–5.2) | Positive capped comparisons, finite-resolution estimates, finite rank conditional on an ordinary closed trace | A common form domain for the renormalized clock, a nonzero physical projection, and either compactness or an independent trace-class estimate. The AdS claim also needs control over a closed double sum. |
| Entropy and multiple boundaries (§§5.3–5.4) | Boost weight, exact entropy identities, spin-summed one-loop arithmetic, conditional Gram bound | A state count at fixed area, selection of the marginal saddle and mass ensemble, and an evaluation of the two-boundary inner product independent of the Hilbert–Schmidt ansatz (5.71). |
| Semiclassical limit and axioms (§6, App. E) | Formal one-loop expansion about smooth solutions; reconstruction given the sewing axioms | A renormalized coincidence limit, a dynamical low-energy comparison, and verification of the axioms without appealing to the claimed finite dimension. |

---

## Four tests of the physical assumptions

### 1. Does increasing resolution leave a nonempty clock window?

With a round, frozen corner and dimensionless area $s=\mathscr A/(4G_N\hbar)$, the quadratic focusing cost contains a radial derivative and no leading angular derivative. In regular oscillator truncations with $N$ radial modes and angular cutoff $J$, its positive zero-point floor scales as $N^2J^2/s$ for an angular average. In specific polarized radial models where a floor persists across an interior radial interval at fixed $s$, all finite clock readings disappear as the cutoff grows.

Setting equal physical radial and transverse cutoffs in this linear scaling gives a model reading of a characteristic length $\sim\sqrt{b\ell_P}$, where $b$ is the corner radius. This is a **model estimate**, not a theorem about full gravity. Proving emptiness in the interacting theory would require a regulator-independent lower bound for the nonlinear two-polarization clock with a fluctuating corner. [Bare square and limit](../audit/shear-uv.md) · [Clock review](fable-clock-sewing.md)

**Effect of vacuum subtraction.** Exchanging the radial integrals puts a weight proportional to $v(1-v)\mathbf 1_{[\epsilon,1]}$ on the leading quadratic clock term. Near the endpoints, the square root of that weight lacks the smoothness needed for the standard derivative-norm lower bound on a Wick square. Negative local expectations in squeezed states and free-field quantum energy inequalities motivate testing this weight in gravity, but leave open which subtraction and lower bound the gravitational clock admits. Furthermore, in this quadratic expectation, different angular harmonics at fixed radial profile carry identical cost; turning that into infinite spectral rank requires controlling the projected states or proving a uniform spectral-subspace bound, because the cap and opposite cone in (D.40) can introduce an angular penalty if imposed as extra physical conditions. [Quantum energy inequality](https://arxiv.org/abs/math-ph/0412028) · [Null averages in four dimensions](https://arxiv.org/abs/gr-qc/0209036) · [Radiative restrictions](../audit/D3.md)

### 2. Do area-changing sources produce a continuum of allowed areas?

This test is a **reductio from the paper’s own nonemptiness claim (5.19)**—it does not simultaneously assert that the clock window is empty. Fable initially proposed using unitary source dilations $D_c$ ($D_c^{-1}\hat K D_c = e^c\hat K$ for total boost charge $K$) to generate a continuum of area sectors. Version 1 supplies boost-frequency filters in (4.12)–(4.15), not such a dilation family, and a dilation moving a sharp positive-area eigenvector cannot be strongly continuous at $c=0$.

A cleaner countability form removes the dilation hypothesis: suppose *one* physical representation contains normalized sharp-area eigenvectors across an uncountable interval of areas, each accepted with positive probability by some finite clock window (for instance via (5.19)), and suppose the clock projections commute with total area. Covering all finite clock thresholds by a countable increasing sequence forces some fixed window to admit uncountably many mutually orthogonal nonzero vectors—ruling out finite rank.

The open hypotheses are whether those sectors live in one shared representation and how area-changing sources act on the reference Gaussian. Inequivalent fixed-area representations or a direct integral with continuous spectrum (where sharp fibers have measure zero) do not supply that family, a representation question raised in footnote 20. Noncompactness of a boost group alone implies no continuum of area eigenvalues. [Cross-sector and fixed-sector tests](../audit/finite-kinematics.md)

### 3. Does a clock on one cone control all the data?

The opposite null expansion, cap Cauchy data, twist, and relative corner frames all lie outside the bare incoming shear integral. Varying the mass of a spherical vacuum exterior changes cap or exterior geometry even while a shear-free incoming congruence keeps the same clock reading at fixed corner normalization, and data emitted from a cap can reach the outgoing cone.

A classically free boundary coordinate affects quantum dimension only if it survives the gauge quotient and labels orthogonal physical states. Measuring the allowed Liouville volume at finite cutoff, then repeating with complete boundary conditions, tests this classically. At fixed total area, the sharpest quantum test is a physically marked, diffuse angular area charge whose spectral projections commute with the clock projection. [Charge theorem](../audit/finite-kinematics.md) · [Boundary review](fable-boundaries-entropy.md)

### 4. Which trace and which states?

Globally, a pure representation generates a type I factor $\mathcal B(\mathcal H)$, but identifying the algebra of a restricted subregion still requires specifying its state and local observables. Solvable JT gravity with matter and perturbative horizon constructions admit semifinite traces on infinite-dimensional algebras, showing that a finite geometric trace does not automatically imply finite Hilbert-space dimension. Four-dimensional gravity has different boundary conditions and may select a different trace.

To reproduce the claimed Schwarzschild entropy in version 1’s clock ensemble, the ordinary weighted collar trace needs a smoothed unweighted density proportional to $e^s s^{167/90}$ per unit $s$. At fixed edge data and bounded $Q_*$, (D.46c) bounds the radiative contribution by $\exp[C(sQ_*)^{3/4}]$, which **cannot supply** that exponential growth by itself. Any missing leading multiplicity must come from edge, cap, or area sectors, or from a different identification of the trace. The Euclidean disk action supplies a weight $e^s$; reading that factor as a count of orthogonal states requires an independent derivation. [JT with matter](https://arxiv.org/abs/2301.07257) · [Perturbative subregion algebras](https://arxiv.org/abs/2306.01837) · [Entropy measure](fable-boundaries-entropy.md)

---

## Order of the calculations and consequences of a negative result

Fable prioritizes **M1, M2, and M5** because each can expose a missing premise before attempting a full interacting construction. Throughout M1–M15, disproving a specific proof step leaves the underlying physical conjecture open. Fable’s original proposals are preserved here even where follow-up audit notes have already run a model check.

| Test | Calculation and evidence that would settle it | Consequence of failure |
|---|---|---|
| **M1. Area sectors** | Derive how area-changing sources act on the reference Gaussian and its clock projections, or identify superselection and the sector measure. | Orthogonal surviving vectors at infinitely many areas in one window defeat finite rank and downstream spectral bounds. Inequivalent sectors require a choice before counting. |
| **M2. Bare shear** | Obtain lower bounds uniform on an interior radial interval as both cutoffs increase at fixed physical area and clock; compare the opposite limit order. | A diverging floor for the exact clock would empty every finite window in that representation. A divergence in regulated free models challenges the existing proof. |
| **M3. Renormalized shear** | Define one composite operator, test it in squeezed states with the actual edge smearing, and establish its best finite lower bound. | Loss of (5.21) removes the positive collar lower bound used for finite dimension and the ensemble’s area cutoff. |
| **M4. Angular degeneracy** | Compute the clock Hessian, reduced symplectic volume, and actual low-clock projection while restoring angular modes; compare with Appendix D.3’s extra cap constraints. | A surviving infinite orthogonal family at fixed area excludes finite rank for this projector. A stronger projector defines a new claim. |
| **M5. Closed-sewing controls** | Apply the AdS double sum to a qubit tensored with a divergent thermal trace; compare ordinary reflected sewing with the actual disk trace in JT gravity with matter. | A false conclusion in a control invalidates the shared inference rule unless extra four-dimensional gravitational hypotheses are identified and proved. |
| **M6. State count** | Count edge and cap states at fixed area with a transverse cutoff alongside the restricted radiative count, then remove the cutoff. | Failing to find the required multiplicity leaves the microscopic entropy and fixed-area degeneracy unproved; the modular identity survives. |
| **M7. Finite cap** | Vary the complete cap-plus-null potential at a fixed rim prescription, invert the resulting two-form, and test the Jacobi identity on rim-reaching observables. | An unrepaired defect invalidates the finite-cap brackets built on (A.14); the smooth-vertex check survives. |
| **M8. Linearized flat diamond** | Construct null graviton and edge algebras, the vacuum restriction, boost generator, quadratic clock, and both cuts of the closed amplitude. | A different algebra type or trace identifies what the exact theory must change and where ordinary factorization needs justification. |
| **M9. Spherical model** | Quantize area, boost, and cap mass with the chosen domain and boundary conditions. | A continuous area spectrum in this sector tests the claimed mechanism for area discreteness. |
| **M10. Nonlinear cutoff sequence** | At fixed $s$ and $\ell/b$, track eigenvalues and clock-projection rank as radial and angular cutoffs grow, with convergence estimates. | Collapse or unbounded rank identifies which continuum limit to inspect. Numerical stabilization alone cannot prove continuum rank. |
| **M11. Evolution between cuts** | Compute the one-loop Bogoliubov map between different caps, test the Hilbert–Schmidt condition for its mixing part, and check cap refinement as $\epsilon$ varies. | Nonimplementability in the chosen representation or cut-dependent amplitudes obstructs closed sewing, the covariance axiom, and claims beyond one fixed cut. |
| **M12. Entropy controls** | Fix angular momentum, remove the local term in an odd-dimensional control, or evaluate a de Sitter ensemble with its zero modes. | Disagreement with an independently known coefficient localizes the failure beyond the shared heat-kernel input. |
| **M13. Physical state** | Construct a state on all source words that is boost-regular, has the vacuum short-distance singularity, and yields low-energy dynamics. | Failure of the one-sided type I assertion affects the ordinary state count, two-boundary factorization, and integer trace weights. |
| **M14. Compactness or trace** | Construct a compact clock or finite ordinary closed amplitude with a proved gluing rule covering cap, angular, edge, and area data—or else construct a faithful normal trace finite on the selected projection. | The two routes have different implications for Hilbert-space dimension. An independent two-boundary amplitude differing from (5.71) also defeats the factorization inference. |
| **M15. Interacting gravity** | Compute a dressed observable sensitive to the universal two-loop cubic-curvature running, with matched normalization, scheme, and external data. | Disagreement with the known low-energy scale dependence challenges the identification with quantum Einstein gravity. |

Useful controls include classical characteristic existence and boundary terms (for M7), null quantization and quantum energy inequalities (for M2–M4), and functional evolution of free fields (for M11). Three-dimensional gravity and the two-loop divergence of pure gravity test structure beyond Gaussian kinematics. Matter, black-hole evaporation, cosmology, topology weights, and identifying a holographic dual go beyond version 1’s vacuum equilibrium claims; shrinking away the artificial cap is needed for an exact causal diamond, and a nonzero cosmological constant affects the stated AdS conclusion. [Classical audit](../audit/03-5-6.md) · [Evolution of free fields](https://arxiv.org/abs/hep-th/9811222) · [Pure three-dimensional gravity](https://arxiv.org/abs/0712.0155) · [Scattering audit](../audit/scattering.md)

---

## If ordinary finite rank fails

**Fable’s constructive alternative (conjecture).** If finite Hilbert-space rank fails, Fable proposes testing a diamond algebra equipped with a faithful normal trace $\tau$ that assigns a finite trace to the clock projection inside an infinite-dimensional Hilbert space. Under a stronger conjecture, complete boundary conditions—regularity on both cones and bounded cap data—yield a type II$_1$ factor. For a normalized density proportional to $e^{-\hat s}$, the entropy relative to $\tau$ is $\langle\hat s\rangle+\log\tau(e^{-\hat s})$ up to normalization.

Establishing this alternative requires constructing the algebra, trace, state, and gluing rule from scratch; a finite projection trace alone neither classifies the factor nor derives horizon correlators, and it does not recover ordinary finite rank, discrete areas, AdS state counting, or topology-rank bounds. Conversely, positive outcomes in M1–M6 would motivate proving M14 with the ordinary Hilbert-space trace. [Subregion-algebra comparison](https://arxiv.org/abs/2306.01837)

---

## Relation to public criticism

Fable’s initial literature search predated the external responses discussed elsewhere in this repository. Since then, Jonathan Oppenheim published a specialist critique focusing on the microstate count, diffeomorphism invariance, and the return to general relativity, while Deepak Vaid challenged the historical framing of canonical quantization. The linked audits assess those independent physical arguments directly against version 1’s equations; none of M1–M15 depends on third-party referee summaries. [Vaid and the canonical-method debate](../audit/canonical-debate.md) · [Oppenheim’s article](https://superposer.substack.com/p/has-ai-come-for-quantum-gravity) · [Assessment of Oppenheim’s critique](../audit/oppenheim-obstacles.md)
