# Gluing across a cut and closing a trace

**Physical question.** When a causal diamond is sliced along an intermediate cut and summed over intermediate states, does the open transition amplitude stay invariant—and does that open-amplitude gluing theorem also justify closing the external ends into a finite trace for the finite-dimension and AdS heat-trace arguments of §5.2?

**Outcome.** Open-amplitude gluing with normalizable external states holds cleanly in (4.29)–(4.31): one intermediate basis sum converges absolutely, and for any fixed finite number of cuts, completing each cut basis in any order recovers the exact matrix element. Both facts hold universally for any unitary evolution. What open gluing does *not* provide are three stronger inputs needed elsewhere in the paper: realizing the algebraic unitary as a continuum gravitational Hamiltonian propagator (alongside a construction of spatial gluing $\mathsf J_t$), controlling simultaneous limits or source derivatives, and closing the external ends into a finite trace. Closing a trace requires a Hilbert–Schmidt condition—or an independent closed-sewing theorem—that open-vector sewing cannot supply; this distinction bears directly on the finite-diamond proof in (5.38)–(5.39) and the AdS heat trace in (5.44)–(5.46).

Primary locations are §4.4, pp. 31–34, Appendix C.1, and Appendix E, pp. 76–80. The radial-mode pair calculation (4.32)–(4.34) is audited separately. [Radial calculation](04-pair.md) · [Paper](https://arxiv.org/pdf/2611.34924v1) · [TeX archive](https://arxiv.org/src/2611.34924v1)

## Which unitarity is available?

Section 4.1 enforces causal factorization on unitary source generators and identifies cap evolution, for an admissible deformation, with the generator labeled by the reduced Hamiltonian in (4.4). In any representation of this algebra, unitarity (4.18) is immediate:

$$
\|\pi(U)b\Omega\|^2=\omega(b^*U^*Ub)=\omega(b^*b).
$$

The adjoint provides the inverse, and causal factorization gives composition in time. That proves unitarity of the abstract algebraic element. Obtaining a propagator independently from the gravitational Hamiltonian requires quantizing it, controlling its domains and regularization, and constructing its time evolution in this representation. Appendix C.2 builds time-ordered evolutions for bounded, strongly continuous generators with integrable operator norm, while the discussion of (4.28) expands polynomial interactions order by order; neither establishes those hypotheses for the full nonlinear, unregulated gravitational Hamiltonian. [§§4.1–4.3](https://arxiv.org/html/2611.34924v1#S4.SS1) · [Appendix C.2](https://arxiv.org/html/2611.34924v1#A3.SS2)

Even an exact one-parameter group of algebraic unitaries needs a continuity condition to admit a self-adjoint generator. For instance, translations on the Hilbert space spanned by orthonormal vectors $\{e_x\}_{x\in\mathbb R}$ (with counting measure) are unitary and obey the group law, yet have vacuum matrix element $\langle e_0,U(t)e_0\rangle=\mathbf 1_{\{0\}}(t)$, which is discontinuous at $t=0$. Appendix E.1 accordingly imposes strong continuity separately as axiom 4.

Spatial gluing $\mathsf J_t$ also requires its own construction. Section 4.4 describes $\mathsf J_t$ by matching fields across the shared corner and enforcing simultaneous frame symmetry; matching the two fixed corner areas is necessary so that their uniform boost charges cancel. When matching data are continuous, the choice of physical inner product matters: the multiplication constraint $(a_+-a_-)\psi=0$ on $L^2(\mathbb R^2,da_+da_-)$ has no nonzero square-integrable solution because the diagonal has measure zero, whereas quantizing the diagonal directly with its own measure produces a different Hilbert space. (For normalizable area eigenvectors, by contrast, matching the uniform boost is direct.) The time-composition bounds below rely on neither a norm formula nor a completeness theorem for $\mathsf J_t$. [Beginning of §4.4](https://arxiv.org/html/2611.34924v1#S4.SS4)

## An open amplitude with one or more cuts

For a single intermediate cut, set $x=U_1\psi$ and $y=U_2^*\phi$ and expand both vectors in any orthonormal basis of the cut space. Parseval's identity and Cauchy–Schwarz give

$$
\sum_i |\overline{y_i}x_i|
\le \Big(\sum_i|y_i|^2\Big)^{1/2}\Big(\sum_i|x_i|^2\Big)^{1/2}
=\|\phi\|\|\psi\|.
$$

The series converges absolutely to $\langle y,x\rangle$, even in a nonseparable Hilbert space (since each vector has at most countably many nonzero coordinates in any orthonormal basis). Implementing a change of boundary frame by the unitaries in (C.1) cancels adjacent factors $V^{-1}V$, verifying invariance under those implemented identifications.

For $m-1$ cuts, define $x_j=U_j\cdots U_1\psi$. The difference between the full evolved vector and the vector truncated by projections $P_1,\ldots,P_{m-1}$ telescopes into $m-1$ terms: term $j$ propagates $(1-P_j)x_j$ through all subsequent projections and unitaries, each of norm at most $1$. Pairing with $\phi$ gives

$$
|A-A_{P_1,\ldots,P_{m-1}}|
\le \|\phi\|\sum_{j=1}^{m-1}\|(1-P_j)x_j\|.
$$

At fixed $m$, enlarging each finite basis subset to exhaust its cut sends every term to zero. Hence scalar sums over Cartesian products of finite cut subsets converge to $A$, and taking the limits sequentially in any order returns $A$. With exact propagators, inserting an exact resolution of the identity at any additional finite cut leaves $A$ unchanged immediately. [Equations (4.29)–(4.31)](https://arxiv.org/pdf/2611.34924v1#page=32)

### Two cuts with an infinite absolute sum

Absolute convergence across a single cut does not extend automatically to *joint* absolute convergence over multiple cuts. Let $\mathcal H=\bigoplus_{n\ge1}\mathbb C^{4^n}$, where block $n$ has dimension $d=4^n$, and take the middle propagator in block $n$ to be the normalized Walsh–Hadamard matrix

$$
H_{ij}=d^{-1/2}(-1)^{i\cdot j},\qquad 0\le i,j<d,
$$

with $i\cdot j$ the binary dot product modulo $2$, while the outer two propagators are the identity. Choose both external states equal to the normalized vector whose entries in block $n$ all equal $2^{-n/2}/\sqrt d$ (squared norm $\sum_{n\ge1}2^{-n}=1$). Because $H$ maps the normalized flat vector in each block onto its first coordinate vector,

$$
\sum_{i,j\text{ in block }n}\overline{x_i}H_{ij}x_j=2^{-n}/\sqrt d=4^{-n},
\qquad
\sum_{i,j\text{ in block }n}|\overline{x_i}H_{ij}x_j|=2^{-n}\sqrt d=1.
$$

The signed matrix element converges to $\sum_{n\ge1}4^{-n}=1/3$, whereas the sum of absolute values over all pairs $(i,j)$ diverges. Direct enumeration of the first four blocks confirms signed contributions $1/4,1/16,1/64,1/256$ and absolute contributions $1,1,1,1$. Even for normalized external states and an exact real orthogonal evolution, unrestricted joint absolute convergence fails; only the narrower statement about each individual resolution of the identity holds in general.

### What refinement and source variation require

Equation (4.31) holds at a *fixed* number of cuts $m$. When the number of cuts grows together with the mode cutoff, the bound still controls the limit if the sum of omitted norms vanishes, but cut-by-cut convergence alone is insufficient. Take identity evolution on $\mathbb C^2$ with external state $e_0$ at both ends, and at cutoff $N$ set $P_{j,N}=1$ for $j\le N$ and $P_{j,N}=|e_1\rangle\langle e_1|$ for $j>N$. Every fixed cut projection $P_{j,N}$ increases to the identity, yet with $2N$ cuts the truncated amplitude is $0$ at every $N$ while the exact amplitude is $1$. Constructing the formal phase-space integral (4.5) via time slicing therefore requires specifying short-time approximating kernels and proving convergence to the intended evolution; similarly, evaluating a distributional kernel at sharp field configurations requires more than a Hilbert-norm bound for external wave packets.

Nor does absolute convergence at fixed source values imply the differentiability needed for (4.28). Take $D e_n=n e_n$ on $\ell^2(\mathbb N)$ ($n\ge 1$) and the normalized vector $x_n=c/n$. The amplitude $\langle x,e^{itD}x\rangle$ is well defined for all real $t$, yet by Fatou's lemma the positive sum $\sum_n |x_n|^2(1-\cos(nt))/t^2$ has infinite limit as $t\to 0$ because each term converges to $c^2/2$. The second symmetric derivative fails to exist. Source derivatives thus require independent domain or moment bounds (the pair correlator (4.33) is a special case whose connected sum can be evaluated directly).

## Closing the external ends

The sharpest distinction in §4.4 lies between an open matrix element, which fixes two external vectors, and a closed trace, which sums over a complete orthonormal basis. For identity evolution on $\ell^2$, equations (4.29)–(4.30) hold for every vector pair while $\operatorname{Tr}1=\infty$. Representing an operator $C$ as a normalizable state on the doubled cut via reflected gluing requires precisely the Hilbert–Schmidt condition

$$
\|C\|_{\rm HS}^2=\sum_i\|Ce_i\|^2=\operatorname{Tr}(C^*C)<\infty.
$$

When that holds, $C^*XC$ is trace class for every bounded insertion $X$, and finite-rank projections tending strongly to the identity recover its trace. (Even a Hilbert–Schmidt operator used alone can have a divergent unreflected trace, as $\operatorname{diag}(1/n)$ shows, whereas its *reflected* closure is finite.)

**Causal diamond.** Equations (5.23)–(5.25) give $C_b^*C_b=e^{-\hat s}f_b(\hat s)$ on $\mathcal H_{\mathscr D}$. Because the clock confines $s$ to a compact interval on which $f_b$ is continuous and strictly positive, there is a constant $c>0$ with $C_b^*C_b\ge c1$, and hence $\operatorname{Tr}(PC_b^*C_b)\ge c\operatorname{rank}P$ for every finite-rank projection $P$. If the doubled preparation has finite norm under this ordinary trace pairing, finite dimensionality already follows immediately. In (5.38), the paper uses finite projections to compare a signed cut amplitude with a positive uncut amplitude, and immediately afterward invokes (4.29) to pass to the uncut closed amplitude. Because both external vectors change with $P$ and their norms diverge if $\dim\mathcal H_{\mathscr D}=\infty$, the open-vector proof does not cover this step; an independently constructed closed amplitude with a proved sewing limit for that insertion is needed. Neither a normalized cutoff ratio nor a one-loop sign establishes convergence of unnormalized closed amplitudes. [§5.2](https://arxiv.org/html/2611.34924v1#S5.SS2) · [Figure 30](https://arxiv.org/html/2611.34924v1#S5.F30)

**AdS cylinder.** In (5.44), summing over a completed diamond index $a$ yields zero for every fixed AdS energy label $i$, yet the proof requires convergence over arbitrary finite subsets of pairs $(i,a)$. Test this with a two-state diamond ($v_+=v_-=p=1/2$, only $+$ in the area band) and the bounded-below Hamiltonian $H=0$ on $\ell^2$ ($w_i=1$). Every row $i$ contains the pair $+1/4,-1/4$: summing full rows gives $0$, but after any finite subset one can still add arbitrarily many fresh $+1/4$ or $-1/4$ terms, so the unrestricted net has no limit. In general, the sum of absolute values is $2p(1-p)\sum_i w_i$, so under the nontrivial-band assumption unconditional convergence is *equivalent* to the heat-trace finiteness being proved. If an independently defined finite closed preparation forces unconditional convergence, the implication is valid; open cut invariance for normalizable external states does not imply it. [Equations (5.43)–(5.46)](https://arxiv.org/html/2611.34924v1#S5.E43)

## Appendix E and the status of the equivalence

- **Axioms (E.1).** Closed pairings, reflection positivity across compatible pairings, factorization, continuous time evolution, and finite closure on the energy-filtered domain are explicitly postulated as axioms; in particular, axiom 5 assumes that every compatible closure of compact-energy-filtered preparations is finite.
- **Reconstruction (E.2).** Under these axioms, (E.6) defines a positive form and cut invariance gives cyclicity on allowed products, with multi-boundary positivity bounding left multiplication. A lower-bounded self-adjoint generator produces a bounded positive semigroup $e^{-sH/\hbar}$, and combining its norm bound with local spectral finiteness gives the compact-energy trace bound (E.9). Conversely, in a Euclidean theory obeying the cited axioms with a finite cylinder trace, the spectral bound (E.12) and positive integer trace weights yield finite-rank energy bands on physical sectors. Equations (E.13)–(E.14) compare completions on the matched, energy-filtered domain; the cited Euclidean theorem itself assumes finite amplitudes for allowed closed configurations. [Colafranceschi, Dong, Marolf and Wang, §§2.2, 4](https://arxiv.org/html/2310.02189v2)
- **Energy growth.** Locally finite spectral weight does not by itself imply a finite unfiltered Euclidean cylinder trace: a Hamiltonian with energies $n\ge 1$ and finite multiplicities $\lceil e^{n^2}\rceil$ has finite compact-band contractions, yet $\sum_n\lceil e^{n^2}\rceil e^{-\beta n}$ diverges for every $\beta>0$. The text after (E.9) properly makes the unfiltered statement conditional on a finite heat trace, showing that full unfiltered Euclidean equivalence carries a genuine additional condition.
- **Gravity realization (E.3).** Equations (E.15)–(E.18) realize the pairings as operator traces: finite diamond dimension gives $|\operatorname{Tr}a|\le d_{\mathscr D}\|a\|$, finite-rank AdS energy bands make filtered contractions finite, and on Hilbert–Schmidt states $\|ba\|_2,\|ab\|_2\le\|b\|\|a\|_2$ holds for bounded $b$. These calculations confirm internal consistency *given* the spectral conclusions of §5.2; because they import those conclusions, they do not independently prove the closed-trace sewing invoked to obtain them. [Appendix E](https://arxiv.org/pdf/2611.34924v1#page=76)
