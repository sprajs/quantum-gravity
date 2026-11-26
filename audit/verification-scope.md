# What has been checked in the 83-page preprint?

All six main sections and all five appendices of Venkatesa Chandrasekaran’s *An algebraic quantization of gravity from the null cone* have technical or contextual review notes. All 530 numbered displays and subequations have index entries pointing to their labelled locations in the versioned HTML. The record supports complete navigation and selected independent derivations. It supplies no count of 530 independently reproduced equations. In particular, an equation may define a quantity, express an assumption, or assert a limit whose existence is the point under review. [arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Equation finder](../EQUATIONS.md) · [Public review provenance](../reviews/README.md)

## Evidence by part of the paper

Page numbers refer to the v1 PDF. Pages 1–2 contain the abstract and contents, page 54 includes the acknowledgements, and the 84-item bibliography starts on page 80 and ends on page 83. The original cites earlier results throughout. The review checks selected primary references, including Sen’s ensemble. A source-by-source rederivation of the cited literature remains outside this record. [PDF](https://arxiv.org/pdf/2611.34924v1) · [Source hashes](../source/README.md) · [Comparison with Sen](sen.md)

| Part, pages | Indexed labels | What the derivations and tests establish | What remains conditional or unverified |
|---|---:|---|---|
| §1, 2–5 | 0 | Identifies precedents and states the claims tested below. | Historical comparisons provide context. [Context and prior work](context.md) |
| §2, 5–11 | 32 | The JT model admits infinitely many orthogonal wavefunctions with the same bounded clock distribution. | The argument uses the stated cap freedom and clock representation in two dimensions. [JT derivation](02-jt.md) |
| §3, 11–24 | 105 | The invertible gravitational branch reproduces the bulk Einstein equations. Raychaudhuri focusing yields the classical area ceiling. A plane wave tests the limitations of matching corner data alone. | Finite-cap closure and a differentiable generator for a moving external radiating cut require additional boundary data or terms. [First-order action](03-1.md) · [Focusing](03-2.md) · [Overlap test](03-5-6.md) |
| §4, 24–34 | 45 | Equations (4.32)–(4.34) have a step-by-step reproduction of the single-harmonic Gaussian pair sum and its nonuniform weak-coupling expansion. Open sewing across one cut follows for bounded evolution and normalizable endpoints. | A pure extension gives an abstract representation under the algebraic hypotheses. The interacting continuum generator, its domain, and convergence under refinement require further construction. [Pair derivation](04-pair.md) · [Open sewing](04-gluing.md) · [Evolution](evolution.md) |
| §5, 34–51 | 98 | Clock estimates, a finite-rank sign test and the Schwarzschild coefficient conversion are checked under their respective hypotheses. Two-area and corner models test proposed inferences. | Nonzero continuum clock acceptance, finite rank, independent closed sewing, horizon saddle selection, the area-packet measure and gluing across general topologies remain open. [Existence](05-1.md) · [Rank](dimension-crosscheck.md) · [Entropy](05-3.md) · [Topology](05-4.md) |
| §6, 51–54 | 19 | Regular-saddle stationary phase and fixed-smearing backreaction reproduce the stated classical and quadratic relations. An exact vacuum plane wave tests (6.13). | Uniform propagation through regulator removal and a renormalized local one-loop equation remain unverified. [Saddle](06-1.md) · [Backreaction](06-2.md) |
| A.1–A.3, 54–59 | 56 | Tetrad, null constraints, corner boost and interior inverse receive analytic checks. The displayed finite-cap form (A.14) has a nonzero exterior derivative on admitted variations. With a common metric and frame, the mixed flat spherical clock response has a distributional generator on vacuum tests smooth up to the closed diamond. [Curvature source and packet checks](spherical-generator.md) · [Joined cap and sheet](weak-boundary.md) | The defect in (A.14) requires a boundary repair or restricted variations. The [matched-rim tests](rim-matching.md) exclude a differentiable family of smooth generators under the stated hypotheses. The full independently marked cap still lacks a demonstrated inverse. [Rim calculation](cap-crosscheck.md) · [Green functions and endpoints](03-2.md) |
| B.1–B.3, 59–64 | 51 | Nine flat-family checks, curved controls and a general off-shell proof of the affine bulk density. Two independent derivations include angular shift, shear and all three divergence terms. [General identity](bulk-identity.md) | A differentiable Hamiltonian for the full moving boundary with all cap data remains open. [Radiative flux](radiative-flux.md) · [Hamiltonian analysis](03-4.md) |
| C.1–C.3, 64–68 | 34 | Gaussian representation, finite-mode source identities, ordering and contact terms have model or operator-theoretic checks. | Extending the physical inner product and ordered nonlinear operators to the chosen gravitational continuum requires domain and regularity control. [Representation](04-2.md) · [Ordering](04-1.md) · [Clock operators](04-3.md) |
| D.1–D.3, 68–76 | 65 | Finite-dimensional Hessian algebra, the local graviton/ghost coefficient, linearized boost correlations and a count for a prescribed radiative energy budget have derivations. A polynomial model separates Hessian motion from the explicit source contact in (D.9). | The full null-region determinant, a uniform bound in the uncut gravitational state, and enforcement of the radiative budget by the physical clock projector remain open. [Determinant](D1.md) · [Boosts](D2.md) · [Focusing and counting](D3.md) |
| E.1–E.3, 76–80 | 25 | Reconstruction and finite-energy-window results follow under the stated axioms with canonical reflected pairings. | A geometric Euclidean amplitude agreeing on other topologies, and gravitational closed sewing independently of §5, require further evidence. [Axioms, continuation and realization](E.md) |

### Exactly what Appendix B tests

Run `uv run --script checks/03-4.py` from the repository root. Eight reported residuals in the area coordinate concern (B.3), the two components of (B.4a), (B.5a), three components of (B.5b) and (B.5c). The ninth evaluates the combined Ricci density of (B.10)–(B.11) in an affine coordinate. Each result is zero for flat cylindrical spacetime in the indicated coordinates with an arbitrary smooth function of time and the two angular labels. For round cuts, zero shift and affine radial gauge, a separate four-dimensional Christoffel calculation verifies the full bulk density for independent smooth functions $F(t,r)$ and $b(t,r)>0$ without imposing the field equations. Its two controls recover the constant-curvature scalar and a genuinely non-Einstein radial Ricci component. A subsequent general affine calculation includes arbitrary shift and shear, matches all 39 expanded monomials of the Ricci density, and derives the result independently by a geometric decomposition. [General proof and command](bulk-identity.md) In (B.7) only the angular divergence integrates to zero on a closed cut. The radial derivative survives and gives an endpoint contribution on integrating along the cone. [Symbolic calculation](../checks/03-4.py) · [Constraint (B.7)](https://arxiv.org/html/2611.34924v1#A2.E7) · [Bulk density (B.10)](https://arxiv.org/html/2611.34924v1#A2.E10)

The pullback, embedding-charge and moving-endpoint identities in (B.16)–(B.24) explain terms in the generator. On a single Schwarzschild cut the Komar charge alone gives half the mass variation. The full covariant variation recovers the other half from the potential. With unrestricted radiating external data one must still derive compensation of the boundary flux in the proposed full reduced theory. [Covariant charge variation (3.50b)](https://arxiv.org/html/2611.34924v1#S3.E50.2) · [Extended potential (B.21)](https://arxiv.org/html/2611.34924v1#A2.E21) · [Analytic tests](03-4.md)

## Reproduce the inventory

Verify the v1 files using the four SHA-256 values in the source record. Run the block below from the repository root with Python 3 and network access. It checks that each index anchor is followed by its own printed equation tag and compares the full set of tags with the index. Expected output is `33 subsections, 530 matching equation labels and anchors`. Run `make check` to repeat the repository calculations. At baseline commit `2b20bb1` all 15 scripts ran to completion. [Source record](../source/README.md) · [Test commands and expected results](../README.md#reproduction)

```sh
python3 - <<'PY'
from pathlib import Path
import re
from urllib.request import urlopen

url = "https://arxiv.org/html/2611.34924v1"
html = urlopen(url).read().decode("utf-8")
index = Path("EQUATIONS.md").read_text()
entries = re.findall(r"\[([2-6A-E]\.\d+[a-z]?)\]\(" + re.escape(url) + r"#([^)]+)\)", index)
tag = re.compile(r'<span class="ltx_tag ltx_tag_equation[^"]*">\(([^<]+)\)</span>')
assert len(entries) == len(set(entries)) == 530
assert sorted(tag.findall(html)) == sorted(label for label, _ in entries)
for label, anchor in entries:
    marker = 'id="' + anchor + '"'
    position = html.index(marker)
    assert tag.search(html, position)[1] == label, (label, anchor)
assert len(re.findall(r"^## Section ", index, re.M)) == 33
print("33 subsections, 530 matching equation labels and anchors")
PY
```

## What would settle the main theoretical questions?

1. **Finite-cap dynamics.** Specify the allowed variations, derive the full potential including moving caps and joints, and recover the boundary evolution. Closure and integrable charge variation on those data are necessary conditions. A surviving rim three-form or nonintegrable radiative flux defeats that formulation. [Finite-cap test](cap-crosscheck.md) · [Hamiltonian flux](03-4.md)
2. **Existence at a fixed physical reading.** Construct the limiting positive clock in a specified physical representation with a controlled cutoff limit. Positive spectral weight at the prescribed threshold for a physical preparation establishes existence there. A divergent lower bound for the full physical clock would empty that window. Current divergent floors concern two quadratic models. [Clock criterion](regulator-program.md) · [Regulated bounds](research-review.md)
3. **Finite rank and closed sewing.** On a nonzero window, prove a finite ordinary closed trace for the bounded-below positive reflected weight using a separately justified cut identity, or prove compactness directly. Constructing arbitrarily many independent accepted physical states at the same threshold would disprove finite rank in that representation. [Trace criterion](dependencies.md) · [Cutoff stress test](compactness-stress.md)
4. **Entropy and dynamics.** Compute the full normalized replica measure in the specified clock and mass/spin ensembles. Its logarithm must reproduce the target coefficient including packet width, zero modes and Jacobians. Separately, an interacting packet calculation can test the known low-energy graviton amplitude. A controlled discrepancy in the same ensemble or external kinematics would challenge the corresponding prediction. [Ensemble test](ensemble-crosscheck.md) · [Scattering test](scattering.md)

These unresolved steps identify proof gaps and a defect in the finite-cap construction as written. The evidence inventoried here supplies no physical refutation of finite-dimensional causal diamonds.
