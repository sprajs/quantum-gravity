# Can a boost distinguish finitely many states from infinitely many?

**The short answer.** *Only if you already know that the closed loop of states sums to the same uncut amplitude regardless of how you order the basis.* Section 5.2 proves a valid conditional finiteness theorem: if one exact, positive, unnormalized amplitude on the smooth uncut geometry must be reproduced by the closed sum over intermediate states for the chosen basis and cycle grouping, then infinite dimension produces a contradiction. However, equation (4.29) proves convergence for a different operation—**open** composition between fixed finite-norm Hilbert-space vectors. As the two-level model below shows, that distinction matters even when every regulated theory has ordinary unitary open sewing, a uniformly bounded area operator, and the exact same nonzero boost signal. [Paper, §4.4, Eqs. (4.29)–(4.30)](https://arxiv.org/pdf/2611.34924v1#page=32) · [§5.2, Eqs. (5.30)–(5.39)](https://arxiv.org/pdf/2611.34924v1#page=41)

## What the cycle proof establishes

Write $H=\mathcal H_{\mathscr D}$, $S=\widehat{\mathscr A}/(4G_N\hbar)$ and $W=C_b^\dagger C_b$. Accept the clock inequality, the half-collar formula and their consequences $0\le S\le s_* I$ and $cI\le W\le I$, with $c=e^{-s_*}\min f_b>0$. If $H$ has infinite dimension, one interval $I_0$ in any finite partition of $[0,s_*]$ has spectral subspace of dimension $\dim H$. A basis respecting $I_0$ can be grouped in blocks of $r$ labels with at most one outside each block. This cardinal argument works for a continuous spectrum and for a nonseparable Hilbert space. A cycle only groups terms. It need not represent a physical diffeomorphism.

For a finite union with projection $P$, at most $1/r$ of the labels are outside $I_0$. If $s_0\in I_0$, positivity and the bounds on $W$ give

$$
\operatorname{Tr}\left[\frac{PWP}{\operatorname{Tr}(PW)}(S-s_0)^2\right]
\le |I_0|^2+\frac{s_*^2}{cr}.
$$

The boost acts on the second component of the doubled state. Equation (5.32) bounds the change of any bounded observable by $|\eta|\|O\|/\pi$ times the square root of the last expression. After fixing a positive vacuum contrast $\delta$, take $I_0$ narrow and $r$ large. Then every partial closed amplitude for $X=\Delta_\eta O-\delta I/2$ is nonpositive. If the uncut amplitude for this same insertion is positive **and** the partial closed amplitudes must converge to it, the contradiction is decisive. A uniform bound on the excitation of every cut state is unnecessary for this conditional argument. [Paper, §5.2, Eqs. (5.31)–(5.38)](https://arxiv.org/pdf/2611.34924v1#page=41) · [Appendix D.2, Eq. (D.25)](https://arxiv.org/pdf/2611.34924v1#page=72)

## The missing sewing estimate

For external vectors $u,v$ of finite norm, an orthonormal basis gives $\sum_i |\langle u,e_i\rangle\langle e_i,v\rangle|\le\|u\|\|v\|$. This is exactly the estimate in §4.4. In (5.31) and Appendix D.2 the unnormalized external vector that one would need for the closed collar has finite truncations

$$
V_P=\sum_{i\in P}C_b e_i\otimes\overline{e_i},
\qquad
\|V_P\|^2=\operatorname{Tr}(PW)\ge c\,\operatorname{rank}P.
$$

As the rank grows, the vectors cannot converge in the Hilbert tensor product. Under its identification with Hilbert–Schmidt operators they represent $C_bP$. The full vector exists there exactly when $C_b$ is Hilbert–Schmidt. Each normalized $V_P/\|V_P\|$ does exist, but its expectation of a bounded observable can depend on the exhaustion. Strong convergence $P\to I$ on each fixed external state supplies no continuity estimate for these varying vectors. It also does not make a double sum with cross terms into an absolutely convergent scalar series. [Paper, §4.4, Eq. (4.30)](https://arxiv.org/pdf/2611.34924v1#page=33) · [§5.2, Eq. (5.31)](https://arxiv.org/pdf/2611.34924v1#page=41) · [Appendix D.2, doubled vector](https://arxiv.org/pdf/2611.34924v1#page=71)

The strongest geometric defense would exhibit an alternative cut on which the uncut preparation and its adjoint are fixed finite-norm external vectors. Equation (4.30) would then apply on that cut. One would still need a sewing map identifying its convergent scalar amplitude with (5.31) for the exhaustive resolutions on the corner. The classical boundary terms canceling in §3.6 and the unitaries changing variables in Appendix C.1 establish invariance of the specified data. Neither calculation provides this norm or this sewing map for the traced collar. [Paper, §3.6](https://arxiv.org/pdf/2611.34924v1#page=24) · [Appendix C.1](https://arxiv.org/pdf/2611.34924v1#page=64)

A fully normalizable uncut collar with ordinary closed sewing would yield an even shorter proof. If $Z[1]=\sup_P\operatorname{Tr}(PW)<\infty$, then $\dim H\le Z[1]/c$. Fable observed that tightening the cycle estimate gives a strictly negative signed margin per state. Boundedness even for that single unnormalized insertion on these exhaustions already forces finite rank. An independently controlled normalized local contrast is a different possible test. Finiteness of $Z[1]$ is sufficient and, given the spectral bounds and the ordinary microscopic trace, equivalent to finite dimension. The fact that $f_b$ peaks at $s_b$ fixes a weight per microscopic state. It gives no concentration in a smooth radiative state within an area eigenspace, and degeneracy can affect even the distribution over area. The bulk saddle and boundary data must establish that the full closed preparation is smooth enough for (D.36). Defining a finite, normalized boost response by cancellation of determinants in (5.27) leaves the normalization of the uncut collar undetermined. [Paper, §§5.2 and D.2, normalized source calculation](https://arxiv.org/pdf/2611.34924v1#page=40)

## An exact two-level stress test

Take $H=\mathbb C^2\otimes\ell^2(\mathbb N)$ with basis $|q,k\rangle$ for $q=0,1$. Fix two finite areas $s_1>s_0\ge0$ and choose the paper's exact weight and boost,

$$
S|q,k\rangle=s_q|q,k\rangle,\quad
w_q=e^{-s_q}f_b(s_q)>0,\quad
C_b|q,k\rangle=\sqrt{w_q}|q,k\rangle,\quad
U_\eta=e^{i\eta S/(2\pi)} .
$$

The measured sector can be given a fixed clock reading compatible with (5.21c). Ordinary open gluing and its absolute-convergence bound hold. One can take the full observable algebra to be $\mathcal B(H)$, which acts irreducibly. Define $F|q,k\rangle=|1-q,k\rangle$ and $O=-F\otimes\overline F$ on $H\otimes\overline H$. The two factors commute and each can be written as a sine of a bounded self-adjoint operator since $\sin(\pi F/2)=F$. Choose a boost for which $\theta=\eta(s_1-s_0)/(2\pi)$ has $\cos\theta\ne1$.

Include the first $n$ labels of charge 1 and the first $(r-1)n$ labels of charge 0, where $r\ge2$ is a fixed integer. These projections increase strongly to identity. Their increments group one charge-1 label with $r-1$ charge-0 labels. Only the $n$ matched pairs contribute to the off-diagonal observable. Direct contraction of (5.31) yields, exactly for every $n$,

$$
\frac{\langle V_P,(O_\eta-O)V_P\rangle}{\|V_P\|^2}
 =D_r=\frac{2\sqrt{w_0w_1}(1-\cos\theta)}{(r-1)w_0+w_1},
\qquad
\|V_P\|^2=n[(r-1)w_0+w_1].
$$

The balanced regulator $r=2$ reproduces a fixed nonzero signal at arbitrarily large finite rank. Along another exhaustion of the same basis, any desired suppression is obtained by increasing the **fixed** block size $r$. For example, $w_1/w_0=1/4$ and $\cos\theta=0$ give $D_2=0.8$, $D_5=4/17$, and $D_9=4/33$. The weight ratio is compatible with the Gaussian in (5.25) by centering it halfway between areas separated by $\log 4$. Setting $X=O_\eta-O-D_2I/2$, the two unnormalized sums have opposite signs and grow linearly with $n$. Both exhausting sequences give identical limits on every fixed open matrix element.

More generally, tensoring a regulated geometric sector with an $N$-dimensional multiplicity space preserves every normalized correlator of insertions acting only on its geometric variables in the product cutoff. The geometric part can therefore retain its entire boost profile. The unnormalized collar trace grows by $N$. The example tests an inference from open sewing and such boost data. Constructing the same multiplicity in vacuum Einstein gravity would additionally require solving the gravitational constraints and showing that its states are physical. The paper's JT example already illustrates the simpler distinction between convergent transitions and a divergent ordinary closed trace at fixed charges. [Paper, §§2.2 and 5.2](https://arxiv.org/pdf/2611.34924v1#page=10)

## How the argument could be completed

1. **Prove closed sewing for the signed insertion.** Construct the exact uncut functional, verify its positive value for the same bounded $X$, and prove that the ordinary unnormalized projections onto any finite union of the prescribed cycles approach that value. Even a proof of positive lower limit along those cycles would be enough. A convergence proof that works only along a preferred geometric regulator leaves the comparison open.
2. **Bound the positive closed collar or its replica ratio independently.** A uniform positive lower bound $R_P(2)\ge\epsilon$ for the exact ordinary ratio in (D.47) along an exhausting family gives $\operatorname{Tr}(PW)\le1/\epsilon$ and hence $\dim H\le1/(c\epsilon)$. Equations (D.45)–(D.49) estimate regular one-loop radiative states at fixed boundary data and integrate over a smooth family of area saddles. To promote this to a rank bound, establish matching to the exact microscopic trace, including the area measure, other sectors reached by the sources, and uniform error as the cutoff is removed. For example, multiplication by a bounded area on $L^2([a,b],ds)$ has fiber multiplicity one throughout, yet its interval projection has infinite rank. A finite saddle integral $\int_a^b w(s)\,ds$ alone gives no bound on the ordinary operator trace. [Paper, Appendix D.3, Eqs. (D.45)–(D.49)](https://arxiv.org/pdf/2611.34924v1#page=75)
3. **Prove compactness directly for the exact clock.** For example, a compact embedding of the form domain of the positive clock operator into the physical Hilbert space, equipped with its graph-form norm, gives finite-rank spectral projections on bounded clock intervals. A coercive lower bound by an operator with compact resolvent would suffice. It would need to control the area and corner degrees of freedom as well as both radiative polarizations on the full state space. This criterion is sufficient and stronger than what one fixed diamond requires.
4. **Make the semiclassical input quantitative.** To use the boost route, control the normalized closed contrast uniformly in the regulator with an error strictly smaller than the margin in (5.37). The Gaussian calculation in Appendix D.2 gives the contrast for a smooth freely falling background and estimates the focusing cost within the linearized description. Loop power counting on that background by itself supplies neither the exact normalization nor a bound uniform over all contributions to the closed functional. Appendix E.1 allows finite closed amplitudes as an axiom. Appendix E.3 uses §5.2 to verify that axiom for gravity, so importing it as independent evidence would reverse that dependency. [Paper, Appendix D.2, Eq. (D.36)](https://arxiv.org/pdf/2611.34924v1#page=73) · [Appendices E.1 and E.3](https://arxiv.org/pdf/2611.34924v1#page=76)

The open question is whether the proposed continuum gravity theory supplies the stronger closed sewing or an independent compactness estimate. The cycle construction pinpoints what such an estimate must exclude. It does not furnish the estimate by itself.
