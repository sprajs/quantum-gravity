# Can open preparations bound the number of diamond states?

A finite list of outgoing packets would give a rank bound if it captured every norm-bounded source preparation with a uniform error smaller than one. In Chandrasekaran's pure representation the source algebra is large enough for this test to count the entire clock window. The missing physical step is to bound the error for all those sources, including ones that change the corner data. A model below shows exactly how the test fails when the estimate covers only a cyclic subalgebra. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Earlier spectral projection criterion](regulator-program.md)

## Which preparations does one packet reach?

Assume a positive self-adjoint clock $T$ in the chosen representation on $K=\mathcal H_\omega$, and a nonzero window $P=\mathbf1_{[0,\ell]}(T)$ with $H=PK$. Fix one normalized packet $\psi\in H$. Write $\mathcal B=\pi_\omega(\mathcal A)$ for the full represented source $C^*$-algebra with its operator norm. Eq. (4.17) gives $\mathcal B''=B(K)$. Eq. (5.20) applies the clock projection **after the final insertion** in a source product. Define the open preparation map $\Theta(A)=PA\psi$. [Eq. (4.17)](https://arxiv.org/html/2611.34924v1#S4.E17) · [Eq. (5.20)](https://arxiv.org/html/2611.34924v1#S5.E20)

For every $\eta\in H$ of norm at most one, $|\eta\rangle\langle\psi|$ is a contraction on $K$. Kaplansky density supplies contractions in $\mathcal B$ approaching this operator strongly. Applying them to $\psi$ and projecting gives preparations approaching $\eta$ in norm. Thus the closure of $\Theta$ on the source unit ball is **the entire Hilbert unit ball** of $H$. This sharpens the dense-span statement by controlling the operator norm of the source. The number and spatial complexity of its constituent insertions may still grow. [Kaplansky, Theorem 1](https://msp.org/pjm/1951/1-2/pjm-v1-n2-p06-p.pdf)

For any source map $F$ with outputs in a fixed space of dimension at most $N<\dim H$, take a unit vector in $H$ perpendicular to its output space. The preparations approaching this vector satisfy $\sup_{\|A\|\le1}\|\Theta(A)-F(A)\|\ge1$. The zero map attains one. If $\dim H\le N$, $\Theta$ itself attains zero. This proves a threshold for finite rank independent of closed sewing. A calculation for one source at a time must supply a *uniform* error to use it.

## A clock-damped estimate from open amplitudes

At any fixed $\beta>0$ of inverse clock dimension, form $\Phi_\beta(A)=e^{-\beta T}A\psi$. Suppose gravity supplies $N$ output vectors $u_j$ and bounded source functionals $f_j$ such that

$$
\sup_{\|A\|\le1}\left\|\Phi_\beta(A)-\sum_{j=1}^N f_j(A)u_j\right\|
\le \delta < e^{-\beta\ell}.
$$

Applying the bounded spectral function $P e^{\beta T}$ recovers $\Theta$ with error at most $e^{\beta\ell}\delta<1$. The threshold above proves $\dim H\le N$. If $\Phi_\beta$ is compact, its image of the unit ball has a finite norm net at any desired accuracy. Orthogonally projecting the output onto the span of that net gives the required approximation. A nuclear decomposition $\Phi_\beta(A)=\sum_j f_j(A)u_j$ with $\sum_j\|f_j\|\|u_j\|<\infty$ gives an explicit error from the omitted tail. Buchholz and Wichmann impose nuclearity on energy-damped maps for *local* source algebras in quantum field theory. Applying such an estimate to the full source algebra and the gravitational clock is an extra hypothesis. [Buchholz and Wichmann, energy nuclearity](https://doi.org/10.1007/BF01454978)

The strength of this demand can be specified exactly. Write $\nu$ for the infimum of nuclear sums, with value infinity when there is no nuclear expansion. For **any bounded positive filter** $B$ on $K$,

$$
\nu\big(A\mapsto B A\psi\big)=\operatorname{Tr}_K B.
$$

When the trace is finite, expanding $B$ in its orthonormal eigenvectors proves the upper bound. For the reverse inequality the representation of $\mathcal B$ extends normally from its bidual $\mathcal B^{**}$ onto $B(K)$. The kernel is a central summand, so the complementary summand gives an isometric linear inclusion of $B(K)$ into $\mathcal B^{**}$. Compose $\eta\mapsto|\eta\rangle\langle\psi|$ with that inclusion. The double adjoint of the preparation map sends the result to $B\eta$, as follows by evaluating against vector functionals. Every nuclear expansion of the map extends to its double adjoint with the same bound, by pairing each $f_j$ with the bidual and using the summable tail. Its composition with the rank-one inclusion would therefore give an expansion of $B$ with the same bound. Compressing to any finite-dimensional subspace and taking its trace bounds that trace by the nuclear sum. Taking the supremum gives the claim, including infinite trace.

Thus $\nu(\Theta)=\dim H$ and $\nu(\Phi_\beta)=\operatorname{Tr}e^{-\beta T}$. A dynamical bound $\nu(\Phi_\beta)\le b_\beta$ implies $\dim H\le e^{\beta\ell} b_\beta$. Full-source nuclearity asks for exactly an ordinary heat-trace estimate. The finite approximation at a single tolerance tests one clock window directly with open amplitudes.

## A model where the choice of sources changes the verdict

Measure clock readings in units of a level spacing, with $T|n,k\rangle=n|n,k\rangle$ for $n=0,1,\ldots$. Set $\beta=\log 2$ and $\ell=4$. With one copy $k$, retaining $n<N$ gives worst open damping error $2^{-N}$ on the full source algebra. At $N=4$ the error equals $e^{-\beta\ell}=1/16$ and the window has five states. At $N=5$ the error is $1/32$ and proves that five states suffice. The strict inequality matters at an occupied endpoint.

Now take infinitely many copies $k=1,2,\ldots$ and the normalized seed $\psi=\sum_k c_k|0,k\rangle$, $c_k=\sqrt3\,2^{-k}$. Restrict sources to bounded block-diagonal families $A=(A_k)$, with $\|A\|=\sup_k\|A_k\|$. This seed is cyclic for that algebra because each finite-support vector can be prepared by scaling finitely many blocks. Its damped map is even nuclear. The expansion in $|n,k\rangle$ has coefficient $2^{-n}c_k\langle n|A_k|0\rangle$ and nuclear sum at most $2\sqrt3$. Nevertheless the clock window contains every $|0,k\rangle$.

For a rectangular approximation retaining $n<N$ and $k\le D$, every retained copy can place its seed component in the first omitted level $n=N$. Each omitted copy can place its component at $n=0$. The blocks can make these choices independently, so the squared worst error is exactly

$$
4^{-N}(1-4^{-D})+4^{-D}.
$$

At $N=D=5$, the error is $0.04418338$, below $1/16$. The full source algebra admits the contraction $|0,D+1\rangle\langle\psi|$. It has error one for the same approximation. Indeed every finite-dimensional approximation misses some unit vector in the infinite ground space. A restricted, cyclic preparation can therefore pass the quantitative test while the full window has infinite rank. In v1 the one-loop count uses regular radiative data with specified cap and corner data. An open estimate on the whole unit ball would have to cover varying data, both polarizations and the states reached by the chosen pure extension. [Eqs. (D.45)–(D.46)](https://arxiv.org/html/2611.34924v1#A4.E45.1)

Run `python3 checks/sewing_repair.py` from the repository root. Expect errors $0.062500$ and $0.031250$ for four and five retained levels in the single copy. The last line compares the restricted error $0.04418338$ with the full-source error $1.0$. The check computes the worst omitted damped level in each block of finite models and compares it with the analytic expression. [Executable check](../checks/sewing_repair.py)

## A one-copy detector for a closed preparation

For the cap $C$ on $H$, suppose $mI\le C^\dagger C\le MI$ with $m>0$, as in Eq. (5.30). Choose a single normalized **output** packet $\chi$, for example $C\psi/\|C\psi\|$. For an orthonormal basis of a rank-$r$ input projection $Q$, prepare a uniformly chosen input, apply $C/\sqrt M$, and condition on success. The probability of projecting the entire output onto $\chi$ is

$$
p_Q(\chi)=
\frac{\sum_{i=1}^r|\langle\chi,Ce_i\rangle|^2}{\sum_{i=1}^r\|Ce_i\|^2}
=\frac{\|QC^\dagger\chi\|^2}{\sum_{i=1}^r\|Ce_i\|^2}
\le\frac{M}{mr}.
$$

The numerator is bounded by a single open-vector norm. A microscopic calculation giving $\limsup p_Q(\chi)\ge p_*>0$ on one increasing exhaustive family proves $\dim H\le\lfloor M/(mp_*)\rfloor$. In infinite dimension every fixed finite-rank output detector loses all probability, even while a local, infinite-rank observable has a finite expectation. Thus a proposed uncut probability needs matching for one *exclusive* outgoing packet on such an exhaustion. Measuring a smooth graviton with the remaining state unobserved uses an inclusive detector of unknown rank. This criterion and the open-source estimate isolate proof gaps. Neither has yet been established for the four-dimensional gravitational clock. [Cap bounds, Eq. (5.30)](https://arxiv.org/html/2611.34924v1#S5.E30.1) · [Two-copy return test](purity-test.md)

In the regular fixed-data graviton model, let $s=\mathscr A/(4G_N\hbar)$ be the fixed dimensionless area. Take Eq. (D.45a)'s one-particle count $N(\nu)\le C_\epsilon(s\nu)^3$ and the excitation budget $\sum_i n_i\nu_i\le Q_*$. Integration by parts yields $\sum_i e^{-t\nu_i}\le6C_\epsilon s^3/t^3$. Summing this bound at $t=m\beta$ with coefficients $1/m$ bounds the bosonic log partition function by $D s^3/\beta^3$, where $D=6C_\epsilon\zeta(4)$. Minimizing $\beta Q_*+Ds^3/\beta^3$ gives

$$
\log d_{\rm rad}\le \frac{4D^{1/4}}{3^{3/4}}(sQ_*)^{3/4}.
$$

For an ordinary cap with constant weight at this fixed area, the return to the image of any chosen normalized allowed packet is exactly $1/d_{\rm rad}$ in the uniform ensemble over all allowed occupations. This gives an explicit positive lower bound there. Replacing the fixed-area ensemble and the excitation-energy budget by the full microscopic clock window is precisely the missing comparison. [Eq. (D.45a)](https://arxiv.org/html/2611.34924v1#A4.E45.1) · [Eq. (D.46c)](https://arxiv.org/html/2611.34924v1#A4.E46.3)

## Which cyclic sewing identity would suffice?

There is also a test using normalized amplitudes. Assume the uncut collar supplies a positive normalized functional $\phi$ on the full microscopic $B(H)$ at its input boundary. For $W=C^\dagger C$ form the normalized functional

$$
\tau(A)=\frac{\phi(W^{-1/2}AW^{-1/2})}{\phi(W^{-1})}.
$$

The bounds on $W$ make the filter bounded and the denominator strictly positive. For the ordinary finite-dimensional cap $\phi(A)=\operatorname{Tr}(WA)/\operatorname{Tr}W$, this compensates its area weight and gives $\tau(A)=\operatorname{Tr}(A)/\dim H$. A geometry-based derivation would have to implement the compensation and justify moving the cut past the selected insertions. Appendix E uses cyclic cutting for its admissible closed preparations. [Appendix E.2](https://arxiv.org/html/2611.34924v1#A5.SS2)

If $H$ were infinite-dimensional, split an orthonormal basis into two sets of the same cardinality as the original. The resulting isometries $V_0,V_1$ from $H$ onto the two orthogonal subspaces satisfy $V_i^\dagger V_i=I$ and $V_0V_0^\dagger+V_1V_1^\dagger=I$. For **every** normalized state $\tau$, including a singular state,

$$
\sum_{i=0}^1\bigl[\tau(V_i^\dagger V_i)-\tau(V_iV_i^\dagger)\bigr]=1.
$$

At least one cyclic exchange changes the answer by $1/2$ or more. Hence a physical sewing law that covers such a pair whenever the window is infinite, with errors strictly below $1/2$ for both exchanges, would rule out infinite rank. The argument needs neither normality nor an unnormalized partition function. Implementing the isometries, or extending the physical rule to them, is essential. [Cuntz, isometries with orthogonal ranges](https://doi.org/10.1007/BF01625776)

For example, the compact operators plus scalar multiples of the identity act irreducibly on an infinite-dimensional $H$ and are strongly dense in $B(H)$. They carry the tracial state $K+\lambda I\mapsto\lambda$. With $W=I$, rank-normalized traces on **every** exhausting family give precisely this answer for each such source. The contribution of a finite-rank $K$ tends to zero by division by the growing rank, and norm approximation gives the same result for every compact $K$. Thus even exact cyclicity on all sources in a strongly dense algebra can coexist with infinite rank. The two proposed isometries concern the microscopic algebra where the exchanges must be justified.
