# Reading and checking *An algebraic quantization of gravity from the null cone*

Venkatesa Chandrasekaran, arXiv:2611.34924v1. This review covers the 83-page version submitted on 25 November 2026, including Appendices A–E. It combines analytic rederivations, explicit model counterexamples, selected executable checks and comparisons with original papers. It is an AI-assisted technical assessment. [Versioned preprint](https://arxiv.org/abs/2611.34924v1) · [Versioned PDF](https://arxiv.org/pdf/2611.34924v1) · [TeX source archive](https://arxiv.org/src/2611.34924v1)

[Start with Neon’s guide to the causal diamond, the gravitational clock and the state count.](EXPLAINED.md) Its worked examples explain why the finite pair amplitude and the proposed limit on information have different verification status.

The [scientific paper](output/pdf/paper.pdf) develops the clock bound, the distinction between open sewing and a closed trace, and the consequences for black-hole entropy. The [illustrated handbook](output/pdf/handbook.pdf) follows the same physics through the geometry of a causal diamond and worked numerical examples. Both editions have editable LaTeX sources. Build them with `make paper handbook` using TeX Live and latexmk. [Paper source](docs/paper.tex) · [Handbook source](docs/handbook.tex)

**Start with what can be measured or computed.** The [observable research program](OBSERVABLES.md) puts specified preparations, calculable quantities, experimental controls and discriminating tests ahead of historical debate. The [comparison of approaches](audit/approaches.md) identifies where candidate theories address the same observable and where their assumptions or ensembles differ.

**Theoretical results with matter.** A massless scalar gives an exact classical diamond, a phase-sensitive semiclassical prediction, and a conditional theorem about the number of distinguishable scalar states. A separate two-copy calculation tests the vacuum state count. The inventory records what was established in each part of v1, including the limits of the Appendix B checks. [Theoretical results and next calculations](THEORY.md) · [Verification by section and appendix](audit/verification-scope.md)

**Read the disagreements.** The [Fable challenge and Astra cross-check](audit/research-review.md), [Oppenheim critique](audit/oppenheim-obstacles.md) and [canonical-quantization debate](audit/canonical-debate.md) examine substantive objections on their merits. The [public review record](reviews/README.md) preserves Fable's arguments alongside their scope and qualifications. The [working convention](AGENTS.md) describes how to continue the study and verify future changes.

**Scope of the verdict.** Nothing in this review physically refutes finite-dimensional causal diamonds. The findings fall into three classes: exact reproductions, **defects in the construction as written** (such as the unclosed finite-cap two-form), and **proof gaps** where a step remains unproved and the physical conjecture stays open.

**What survives the checks.** The constrained first-order bulk equations reproduce Einstein gravity on the nondegenerate gravitational branch. Shear focuses the null rays by the classical amount used in the paper. The two-dimensional example genuinely has infinitely many states at bounded clock reading. The Gaussian pair correlator in four dimensions is exactly summable and its small-coupling expansion is singular. The local graviton and ghost coefficient and the ensemble conversion reproduce the known Schwarzschild one-loop number; because both derivations use the same local heat-kernel coefficient, agreement checks that conversion rather than supplying an independent microscopic state count. The stationary-phase and fixed-smearing backreaction equations recover the expected form around a regular classical solution.

**What remains conditional.** The treatment of finite caps has a defect as written: differentiating the displayed two-form (A.14) leaves a nonzero rim term, so the phase space needs moving-cap/joint terms or narrower boundary conditions sufficient for the stated brackets and Hamiltonian. Choosing a pure representation does not determine a regular interacting continuum propagator. Finite probability for the quantum clock and finite rank of its bounded spectral window require separate proofs; in two regulated quadratic models, even the lowest clock eigenvalue diverges with radial resolution and empties any fixed window, while the full nonlinear gravitational clock remains open. Open-amplitude gluing leaves an unproved closed-sewing step in the state count. Finally, the entropy trace does not by itself select the marginal horizon saddle over a flat round sphere, and the full area-packet measure is still needed for an independent microscopic derivation of the entropy logarithm. [Referee report and proposed tests](REFEREE.md)

[Equation finder with 530 links to numbered displays and subequations](EQUATIONS.md) · [Physical tests of finite rank, locality and boosts](audit/finite-kinematics.md) · [Concrete regulator and falsification program](audit/regulator-program.md)

## Read the paper with the derivations alongside it

| Pages | Question | Where to read the check |
|---|---|---|
| 2–5, §1 | Which ideas have precedents, and what would be new? | [Historical context, outside checks and novelty](audit/context.md) |
| 5–11, §2 | Can a clock bound leave infinitely many states? | [JT gravity, the Fourier construction and the reflected trace](audit/02-jt.md) |
| 11–18, §§3.1–3.2 | How do Einstein's equations and a geometric clock arise? | [First-order action and joints](audit/03-1.md) · [Null data, focusing, caps and Appendix A.1/A.3](audit/03-2.md) |
| 18–22, §§3.3–3.5 | What are the conjugate variables, what moves the cut, and how is a point identified? | [Symplectic form and Appendix A.2](audit/03-3.md) · [Hamiltonian and Appendix B](audit/03-4.md) · [Metric and relational dressing](audit/03-5-6.md) |
| 22–24, §3.6 | When do two regions describe the same geometry? | [Matching, including a vacuum plane-wave test](audit/03-5-6.md) |
| 24–31, §§4.1–4.3 | What does quantization define on a finite set of modes and on infinitely many? | [Source algebra and C.2](audit/04-1.md) · [Gaussian representation and C.1](audit/04-2.md) · [Clock operators and C.3](audit/04-3.md) |
| 31–34, §4.4 | What exactly converges, and what produces the logarithm? | [Open gluing and a multi-cut example](audit/04-gluing.md) · [Complete pair-correlator reproduction](audit/04-pair.md) · [Comparison with interacting scattering](audit/scattering.md) |
| 34–38, §5.1 | Is there even one physical state with a finite clock reading? | [Existence criterion, regulated bounds and quantum-domain test](audit/05-1.md) |
| 38–45, §5.2 | Does a bounded clock leave finitely many states? What follows for area and AdS? | [Finite-rank proof audit](audit/05-2.md) · [Two-sided sign argument](audit/dimension-crosscheck.md) · [Area changes and AdS](audit/area-ads.md) |
| 45–49, §5.3 | How does a boost give an entropy, and which state count enters the logarithm? | [Entropy derivation](audit/05-3.md) · [Fixed-area versus finite-width packet](audit/ensemble-crosscheck.md) · [Sen's actual ensemble](audit/sen.md) |
| 49–51, §5.4 | What does tracing the two boundaries say about spatial topology? | [Factorization, null states and horizon correlations](audit/05-4.md) |
| 51–54, §§6.1–6.2 | Do classical spacetime and its one-loop backreaction emerge? | [Classical saddle and branches](audit/06-1.md) · [Backreaction, subtraction and fixed resolution](audit/06-2.md) |
| 54–64, Apps. A–B | Are the finite-cap phase space and evolution well defined? | [Independent endpoint check on a common spacetime](audit/cap-crosscheck.md) · [Hamiltonian flux](audit/03-4.md) |
| 64–68, App. C | Are the representations, ordering and boundary operators sufficient? | [Algebra and ordering](audit/04-1.md) · [Representation](audit/04-2.md) · [Boundary operators](audit/04-3.md) · [Continuum evolution](audit/evolution.md) |
| 68–76, App. D | What do Gaussian fluctuations, a boosted graviton and focusing establish? | [Determinant and contact terms](audit/D1.md) · [Boost, smearing and energy bound](audit/D2.md) · [State count and angular budget](audit/D3.md) |
| 76–80, App. E | Which Euclidean and Lorentzian conclusions follow from the axioms? | [Reflection positivity, cylinder continuation, gluing and scope](audit/E.md) |

The [dependency analysis](audit/dependencies.md) follows the conclusions through failures of individual hypotheses. The [review of physical implications](audit/implications.md) explains what would change for black holes and local measurements. The [clock ultraviolet analysis](audit/shear-uv.md) and the [closed-trace stress test](audit/compactness-stress.md) give independent routes to testing the two central mathematical questions.

## Reproduction

Run `make check` to execute all 19 scripts in [checks](checks). The Appendix B calculation uses SymPy 1.14.0 via `uv`. The other 18 use the Python standard library. The table gives six starting points. Further commands and expected outputs accompany the [scalar diamond](audit/matter-diamond.md), [quantum scalar clock](audit/matter-null-energy.md), [scalar shift](audit/matter-state-count.md), [two-copy state-count test](audit/purity-test.md), [observables](OBSERVABLES.md), [clock and regulator checks](audit/research-review.md) and [independent review record](reviews/README.md).

| Command | Result from this review |
|---|---|
| `python3 checks/03-3.py` | The finite-cap exterior derivative in the stated test family vanishes at the vertex and equals $1/256$ at cap fraction $1/2$. |
| `uv run --offline --script checks/03-4.py` | Nine flat-family residuals vanish. The round off-shell density matches direct curvature for arbitrary radial and time dependence, and two curved controls agree. If the dependency is not cached, omit `--offline`. |
| `python3 checks/pair.py` | The direct sums through 100,000 modes agree with an independent evaluation inside the analytic tail bound. At $1/s=0.1$, the absolute difference is $2.50\times10^{-12}$. |
| `python3 checks/05-2.py` | In the two-area comparison model, three choices of how to exhaust the same space give boost contrasts of −0.45970, −0.18388 and −0.02242. This diagnoses the need for a closed-sewing theorem. |
| `python3 checks/determinant.py` | The Ricci-flat spin-2 and ghost contributions give $53/45$. A finite two-source test also separates a Hessian variation from an explicit source contact. |
| `python3 checks/corner_clock.py` | In the shear-free shape model with relative clock limit 1.1, increasing the matrix size from 16 to 4096 raises the accepted count from 6 to 94. The exactly solved continuum model has infinite rank. Its embedding in physical gravity is open. |

Analytic work beyond these executable tests is in the linked notes. Several derivations in the original require continuum operators, measures or limiting estimates that are incompletely specified. The review identifies those dependencies.

## How independent is this review?

In the paper's acknowledgements, the author writes: *"Several of the calculations and proofs in this paper were developed through detailed, back and forth collaboration with GPT-6 Astra over the course of many months."* Multiple Astra checks here share a model family with that collaborator. Fable reviewed the technical reasoning from a different model family. Neon edited the handbook, public guide and technical notes. Astra completed the final measurements text and publication checks. This public review has had no human specialist peer review. Agreement among model-assisted checks is weaker evidence than an exact calculation a reader can reproduce, an explicit counterexample that can be inspected, or verification by an independent specialist. Every model argument here is kept visible alongside its premises, and the literature note separates public technical checks, earlier results and specialist criticism. [Paper acknowledgements](https://arxiv.org/pdf/2611.34924v1#page=54) · [External checks](audit/context.md)

## Source provenance

The versioned PDF supplies the printed equation numbers. The source record gives the arXiv distribution terms, file hashes and commands to retrieve the reviewed files. [Source record](source/README.md)
