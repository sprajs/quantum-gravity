# Independent cross-check of the finite-dimension argument

**The physical question.** *When we independently rederive both halves of the paper's finite-dimension contradiction—the finite-cutoff boost bound and the flat-space boost signal—does the contradiction force a finite-dimensional causal diamond?*

**The short answer.** **The finite-projection bounds and the smooth-vacuum boost signal both survive scrutiny, but the inference to a finite dimension requires an additional closed-sewing limit.** Equation (5.38) is a sign test for an *unnormalized* amplitude. Its validity depends on whether every complete-cycle exhaustion evaluates the same physical closed amplitude. Equations (4.29)–(4.31) establish convergence only for open amplitudes with fixed, finite-norm external Hilbert-space vectors; the reflected preparation used in (5.38) needs a further argument to satisfy that hypothesis. That gap leaves the proposed dimension open. [Paper, §§4.4 and 5.2, Appendix D.2](https://arxiv.org/pdf/2611.34924v1#page=40)

## What the finite-cutoff argument establishes

On the physical clock subspace, assume the bounds in (5.21) and the cap map in (5.23). Write $S=\widehat{\mathscr A}/(4G_N\hbar)$, $W=C_b^\dagger C_b=e^{-S}f_b(S)$, and $a=e^{-s_*}\min_{[0,s_*]}f_b>0$. Then $a1\le W\le1$. For any nonzero finite-rank projection $P$, the unnormalized paired vector in (D.22) is the vectorization of $C_bP$ and has squared norm

$$
Z_P=\|C_bP\|_{\rm HS}^2=\operatorname{Tr}(PW)\ge a\,\operatorname{rank}P .
$$

Its normalized right marginal is the conjugate of $PWP/Z_P$. The spectral theorem applied to $|e^{ix}-1|\le|x|$, followed by the triangle inequality for expectations in two unit vectors, gives (5.32). If the space is infinite dimensional, a finite partition of $[0,s_*]$ has a cell $I$ whose spectral subspace has full Hilbert dimension. A basis adapted to that cell can be arranged into cycles of length $r$, with at most one outside vector per cycle. For every finite union of cycles and $s_0\in I$,

$$
\operatorname{Tr}\!\left[(PWP/Z_P)(S-s_0)^2\right]
\le |I|^2+\frac{s_*^2}{ar}.
$$

This needs no area eigenbasis. The cycle projections commute with the cell projection, and $PWP\le P$. Choose the cell width first and $r$ second to make the boost response smaller than any fixed positive tolerance. Complete cycles also form a cofinal family among finite *subsets of this basis*. This handles the paper's cardinality and ordering claims. In particular, the small response is a genuine consequence of its finite-dimensional formula even when the spectrum has a continuous part. [Equations (5.30)–(5.32), (D.22)–(D.25)](https://arxiv.org/pdf/2611.34924v1#page=72)

## What the smooth correlator establishes

On the flat null plane the positive-frequency measure gives $G_0(u,v)=-c_\perp/(u-v)^2$ at distinct points. For two real unit-integral profiles centered at $-d,d$, the boosted mixed contraction is

$$
G_\eta=-c_\perp\int du\,dv\ p_L(u)p_R(v)\frac{e^\eta}{(u-e^\eta v)^2}.
$$

The factor $e^\eta$ follows from the shear's null tangent. For reflected even narrow bumps, Taylor expansion of the smooth separated-point kernel gives $G_\eta/G_0=\operatorname{sech}^2(\eta/2)+O((\Delta u/d)^2)$. As a check, at $\eta=1$ normalized bumps proportional to $\exp[-1/(1-t^2)]$ for $|t|<1$ give ratios 0.787024, 0.786591 and 0.786484 for $\Delta u/d=0.12,0.06,0.03$, respectively (400-point midpoint integration per profile). The point-support answer is 0.786448.

In the Gaussian vacuum, disjoint smeared operators commute at this order. Expanding the sine product into two cosines gives (D.20), $\exp[-(j_L^2G_{LL}+j_R^2G_{RR})/2]\sinh(j_Lj_RG_{LR})$. The dilation preserves the right self-contraction. Hence one can use fixed real sources with a nonzero response $\delta_\eta$ in a bounded observable. This avoids passing a source derivative through an arbitrary cutoff limit.

Appendix D.2 gives additional control within the linearized current theory. Equations (D.28)–(D.35) relate a discrepancy from this bounded vacuum response to positive smeared mode occupation. Given the smooth-background bound $\langle:\sigma_\perp^2:\rangle_{C_b}=O(c_f/b^2)$, (D.36) bounds the *squared absolute* error by a constant times $d/B+dB/b^2$. The comparison can be favorable at a fixed shape and sufficient separation of scales. The size of the normal-ordered shear in the full closed preparation, and persistence of the signal with higher orders and all allowed sectors included, require independent control. The paper evaluates the Hessian about a shear-free smooth solution and identifies the local singularity through one loop. The profile width, physical short-distance regulator and finite-rank projection on gravitational states perform different operations. [Equations (5.26)–(5.36), (D.15)–(D.21), (D.35)–(D.36)](https://arxiv.org/pdf/2611.34924v1#page=71)

## The limit in the sign test

Choose the sign of the source so $\delta_\eta>0$, and put $X=\Delta_\eta O-\delta_\eta 1/2$. On the cycle cutoffs, (5.38) gives $Z_P[X]\le0$. One may choose the tolerance strictly smaller, for example $\delta_\eta/4$. Then $Z_P[X]\le-\delta_\eta Z_P/4$, which tends to minus infinity under the infinite-dimension hypothesis. The paper obtains a positive sign on the smooth uncut preparation. These conclusions are inconsistent **if the two prescriptions evaluate the same closed functional on this insertion**. No equality of infinite ratios is part of this sign argument.

In (4.29)–(4.31), Cauchy–Schwarz applies because the incoming and outgoing vectors are fixed and square summable. For an uncut cap pairing, the candidate external vector is the vectorization of $C_b$, with squared norm $\operatorname{Tr}W$. It belongs to the tensor-product Hilbert space precisely when $C_b$ is Hilbert–Schmidt. Here $W\ge a1$ makes that condition equivalent to finite dimension. Under the opposite hypothesis the *normalized* vectors even converge weakly to zero: their inner products with simple tensor test vectors are bounded by $\|C_b\|\|u\|\|v\|/\sqrt{Z_P}$, and those tests span a dense subspace. Strong convergence $P\to1$ therefore does not supply a unit-vector limit or determine the normalized response of a bounded two-sided observable. Diffeomorphism invariance can constrain a closed functional once constructed. The open composition law alone supplies no summability estimate for this closed contraction. [Equations (4.29)–(4.31), (5.37)–(5.38) and Figure 30](https://arxiv.org/pdf/2611.34924v1#page=43)

The author supplies an instructive check in the JT prologue. Open evolution there is isometric, yet every member of an infinite orthonormal family contributes the same positive weight to the reflected trace. Equation (2.17) gives its divergence explicitly. The four-dimensional focusing dynamics and boost response are additional inputs. The JT result shows within the paper's own framework why general open gluing cannot settle the closed norm. [Section 2.2, equation (2.17)](https://arxiv.org/pdf/2611.34924v1#page=10)

## An explicit two-sided test

Take $\mathcal H=\mathbb C^2\otimes\ell^2(\mathbb N)$, with area eigenvalues $s_0,s_1$ on the two labels and weights $w_i=e^{-s_i}f_b(s_i)>0$. Take $C=W^{1/2}$, and let $F$ exchange the two labels at each integer. Use the bounded observable $O=-F\otimes\overline F$ on the paired space. It is a product of sine observables, since $\sin(\pi F/2)=F$. A right boost gives relative phase $\theta=\eta(s_1-s_0)/(2\pi)$. For finite label-wise index sets $J_0,J_1$, direct evaluation of (5.31) gives

$$
\langle\Delta_\eta O\rangle_P
=\frac{2\sqrt{w_0w_1}\,|J_0\cap J_1|(1-\cos\theta)}
{w_0|J_0|+w_1|J_1|}.
$$

For $J_0=J_1=\{1,\dots,N\}$ the response is a positive constant whenever $\theta\notin2\pi\mathbb Z$. For $J_1=\{1,\dots,N\}$, $J_0=\{1,\dots,(r-1)N\}$, it equals $2\sqrt{w_0w_1}(1-\cos\theta)/[(r-1)w_0+w_1]$. This second exhaustion adds one complete length-$r$ cycle at each step. Both families increase strongly to the identity and resolve the same basis. Choosing $r$ large puts the second response below half the first. Subtracting that half as in (5.37a) produces unnormalized signs of opposite sign, with magnitudes growing linearly in $N$. All fixed-vector open-sewing identities still hold. The example isolates the operator limit. It makes no claim to reproduce gravitational dynamics, local smoothness or gravitational diffeomorphisms.

## Independent hypotheses that would close the argument

- A theorem for the *single bounded observable* could identify its normalized boost response on every cycle exhaustion with that of the uncut preparation, with a strictly positive lower bound on the exact response. The finite-projection estimate already rules out infinite dimension under that hypothesis. A suitably uniform shear-energy estimate for those projections in the physical continuum theory would also suffice. Agreement along one physically preferred regulator leaves the cycle comparison open.
- Equation (D.47) gives a different sufficient condition. An exact positive lower bound on the cutoff purity $R_P(2)=\operatorname{Tr}[(PWP)^2]/Z_P^2$ along a complete exhaustion would yield $Z_P\le1/R_P(2)$ because $W\le1$, and then $a\operatorname{rank}P\le Z_P$. The positive result (D.49) computes a regular one-loop saddle integral with finite mode counts per area. An integral over continuous area labels is different from the Hilbert trace on a direct integral. Even multiplicity one on a bounded interval yields infinitely many orthogonal vectors in $L^2$ of that interval.
- A nonperturbative compactness estimate for $C_b$, or a finite-rank theorem for the clock projector including corner and radiative sectors, would settle the dimension directly. A finite *ordinary* closed norm with the paper's weights would do so immediately by $W\ge a1$. Appendix E's axiom of finite amplitudes for energy- or boost-smeared closures is an independent assumption when used in this direction. Its claimed realization appeals to §5.2. [Appendix D.3, (D.45)–(D.49), and Appendix E.1, condition 5](https://arxiv.org/pdf/2611.34924v1#page=76)

The argument thus supplies a precise implication from exact closed sewing and a nonzero physical boost signal to finite dimension. The Gaussian calculation, the finite-rank inequality, and the one-loop focusing count furnish distinct evidence for those inputs. A proof that their continuum limits agree for the stated preparation would be the step that converts the implication into the advertised result.
