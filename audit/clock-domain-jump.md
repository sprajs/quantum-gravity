# An arbitrarily small second polarization can close the clock window

In a one-oscillator restriction of the fixed-area-density null radiation, a smooth second-polarization profile of amplitude $\delta$ changes the space of finite clock energy discontinuously. At $\delta=0$ this space is dense. At every $\delta\ne0$ it contains only the zero vector. Two angular patches force incompatible position and momentum tails. A third supplies their canonical pairing from the fixed-density shear potential. The focusing integral uses the full hyperbolic target metric. It tests whether small classical shear suffices to preserve finite-reading quantum states. Fable previously identified both a divergent Gaussian mean and a three-cut example with incompatible domains. Here the radial profiles are explicit and the perturbation can approach zero in every smooth norm. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (4.21)–(4.27)](https://arxiv.org/html/2611.34924v1#S4.E21) · [Fable’s clock review](../reviews/fable-clock-sewing.md)

## Two rays measuring a conjugate pair

Use units with round radius and $\hbar$ equal to one. On $L^2(\mathbb R)$ take $X_1=Q=x$ and $X_2=P=-i\partial_x$. Assign these operators to two angular cells of equal weight. Choose $0<\epsilon<r_*<1$ and real $h,g\in C_c^\infty((\epsilon,r_*))$. Let $h$ have plateaus at $+1$ and $-1$. Choose $g$ as the sum of two bumps, one inside each plateau, scaling them so that $\tfrac14\int r(g')^2\,dr=B>0$ on each. In cell $j$ set $z^1=\alpha h X_j$, $z^2=\delta g\,I$ with $\alpha>0$. Both fields vanish at the cap and waist. The ordered focusing through cut $v$ is the spectral function $\Xi_\delta(v,X_j)$, where

$$
\Xi_\delta(v,t)=\frac14\int_\epsilon^v r\left[\alpha^2(h')^2t^2+\delta^2(g')^2 e^{2\alpha h t}\right]dr.
$$

For the whole interval $r_*\le v\le1$ this equals

$$
F_\delta(t)=A t^2+B\delta^2(e^{2\alpha t}+e^{-2\alpha t}),
\qquad A=\frac{\alpha^2}{4}\int_\epsilon^1 r(h')^2dr.
$$

Choose $\alpha$ so that $0<A<1$. The capped clock form is

$$
q_R[\psi]=\frac12\sum_{j=1}^2\int_\epsilon^1
 \bigl\|e^{\min(\Xi_\delta(v,X_j),R)/2}\psi\bigr\|^2\,dv.
$$

Every summand uses the spectral calculus for its own cell. Within each cell the prefix is an increasing scalar function of the cut at fixed $t$, attaining $F_\delta(t)$ on a set of length $1-r_*>0$. Monotone convergence therefore gives the exact domain

$$
D(q)=\{\psi:\sup_R q_R[\psi]<\infty\}
=D(e^{F_\delta(Q)/2})\cap D(e^{F_\delta(P)/2}).
$$

At $\delta=0$, every Hermite function belongs to both domains. Its position and Fourier wavefunctions are polynomials times $e^{-t^2/2}$, and the squared weighted norm has Gaussian factor $e^{-(1-A)t^2}$. Their span is dense. For $\delta\ne0$, $F_\delta(t)/t^2\to\infty$ as $|t|\to\infty$. A finite-form vector must then satisfy $e^{c x^2}\psi\in L^2$ and $e^{c\xi^2}\widehat\psi\in L^2$ for every $c>0$. With Fourier kernel $(2\pi)^{-1/2}e^{-ix\xi}$, the $L^2$ Hardy uncertainty theorem forces such a vector to vanish already at $c=1$. Consequently the extended resolvent in (C.13) has zero strong limit as the cap is removed, and every finite-reading projection of the limiting clock is zero. [Escauriaza, Kenig, Ponce and Vega, p. 2, first displayed assertion](https://arxiv.org/pdf/1506.05670v1#page=2) · [Chandrasekaran, Eq. (C.13)](https://arxiv.org/html/2611.34924v1#A3.E13)

At fixed $R$ each capped cell integrand converges strongly to its $\delta=0$ value by dominated convergence, with norm bounded by $e^R$. The averaged clock $T_{R,\delta}$ and its filter $L(L+T_{R,\delta})^{-1}$ therefore converge strongly as $\delta\to0$ for $L>0$. Taking $\delta\to0$ first and then removing the cap gives the nonzero filter of the dense-domain clock. Removing the cap first at $\delta\ne0$ gives zero. Fixed-cap continuity alone cannot justify exchanging the limits.

## A commuting control

Keep the same two profiles and use independent position coordinates $X_j=x_j$ on $L^2(\mathbb R^2)$. The clock now multiplies by the continuous, finite function $T(x_1,x_2)=\tfrac12\sum_j\int_\epsilon^1 e^{\Xi_\delta(v,x_j)}dv$. Compactly supported wavefunctions give a dense form domain for every $\delta$. A product oscillator vacuum still has infinite mean at $\delta\ne0$, as its one-coordinate Gaussian density cannot integrate $e^{F_\delta(t)}$. Yet for any $\ell>T(0,0)$ a neighborhood of the origin has positive vacuum probability and supplies infinitely many orthogonal accepted states. The two models thus have identical single-cell vacuum distributions and opposite answers about the joint domain.

## A smooth symplectic realization on the fixed-density sheet

The profiles of the two-cell test alone have zero bulk symplectic pairing. Each cell varies in just one direction. The following addition realizes the same domain jump after pulling back the radiative symplectic form and quantizing the resulting canonical pair.

**Theorem.** On the fixed round density $\varrho(r,y)=br$ block of one null sheet, at sufficiently large $b^2/(G_N\hbar)$, there is a smooth two-dimensional symplectic family for each prescribed $\delta$. Its quantized clock has dense form domain at $\delta=0$ and zero form domain at every $\delta\ne0$.

**Proof.** Restore $b$ and $\hbar$ in the symplectic normalization and measure the clock in units of $b$. Take three disjoint angular patches. In each take a smooth bump $0\le a_j\le1$ supported in a local orthonormal dyad and equal to one on an open set. Use the round metric off their supports. Let $U=\chi\cos\theta$, $W=-\chi\sin\theta$ where $\chi\ne0$ is a smooth bump supported strictly between $r_*$ and $1$, and $\theta'>0$ on its support. For real dimensionless coordinates $q,p$ take

$$
 z^1=\alpha h(a_1q+a_2p)+\lambda a_3(Uq+Wp),\qquad
 z^2=\delta g(a_1+a_2).
$$

All pulses and variations vanish in neighborhoods of the cap and the corner. Fix their locations, the angular labels and frames. The radial constraint (A.30b) sets $\mu=1/r+(r/4)[(z^{1\prime})^2+e^{2z^1}(z^{2\prime})^2]$ for this choice of $\varrho$. With field-space derivative $D$ at fixed $\delta$, the spin-zero term of (A.30a) vanishes since $D\varrho^2=0$. Its complete bulk shear potential on this family is

$$
 \Theta_{\rm sh}=\frac{b^2}{16\pi G_N}\int d\Omega\int_1^\epsilon r^2
   [z^{1\prime}Dz^1+e^{2z^1} z^{2\prime}Dz^2]dr .
$$

Here $Dz^2=0$. Differentiating the target weight also gives zero in the two-form because its derivative is wedged with $Dz^2$. The first two patches each give a multiple of $dq\wedge dq$ or $dp\wedge dp$. The last patch contributes $U'W-W'U=\chi^2\theta'$. With the corner-to-cap orientation of (A.14) this gives

$$
 D\Theta_{\rm sh}=\frac{b^2\lambda^2 H}{16\pi G_N}\,dp\wedge dq,\qquad
 H=\int a_3^2 d\Omega\int_\epsilon^1 r^2\chi^2\theta' dr>0 .
$$

Taking $\lambda^2=16\pi G_N\hbar/(b^2 H)$ gives $\hbar\,dp\wedge dq$ and hence the dimensionless Schrödinger pair $[Q,P]=iI$. The covariant two-form (A.14) gives the same pullback directly. Its mixed terms vanish for fixed density and labels, and $\nabla_r(Dz)^1=\partial_r Dz^1$ since $Dz^2=0$ and $\Gamma^1{}_{11}=\Gamma^1{}_{21}=0$. The compact angular support lets the deformed conformal metrics join the round metric smoothly across dyad charts. [Oriented sheet two-form (A.14)](https://arxiv.org/html/2611.34924v1#A1.E14X) · [Fixed-density potential and radial constraint (A.30)](https://arxiv.org/html/2611.34924v1#A1.E30) · [Finite-rim variation on a null sheet](rim-potential.md)

In the full angular average, the plateaus $a_1=1$ and $a_2=1$ retain strictly positive weight. After the early profiles end they measure exactly $F_\delta(Q)$ and $F_\delta(P)$, including on a positive-length interval before the added pulse begins. Positivity and the Hardy argument force zero domain at every $\delta\ne0$. This uses only those two terms of the clock. The pulse in the third patch contributes a separate positive quadratic focusing at all cuts.

At $\delta=0$ every prefix on every ray is a positive quadratic in the canonical pair. Its integrated vacuum variance is bounded by

$$
 V_* = \max\!\left\{\frac A2,\,
 \frac{\lambda^2}{8}\int_\epsilon^1 r[(U')^2+(W')^2]dr\right\}.
$$

This follows from $\langle Q^2\rangle=\langle P^2\rangle=1/2$ and $\langle QP+PQ\rangle=0$. Hold $A<1$ and choose $b^2/(G_N\hbar)>(4\pi/H)\int_\epsilon^1 r[(U')^2+(W')^2]dr$. This fixes the same area for all $\delta$ and gives $V_*<1/2$. For every positive quadratic prefix $X$, ordered Gaussian contractions give $\langle X^n\rangle\le (2n-1)!! V_*^n$. The exponential series converges uniformly. For a fixed Hermite excitation the extra external field factors multiply this summable bound by a fixed-degree polynomial in $n$. Thus the entire Hermite span has finite clock energy and is dense. In particular the vacuum has positive spectral probability below every threshold strictly larger than its finite mean. This proves the theorem. Smooth angular transition regions satisfy the same variance bound. At fixed cap their early clocks converge strongly as $\delta\to0$ by the scalar dominated-convergence argument above. The third patch is independent of $\delta$. [Uniform moment estimate](clock-construction.md)

This procedure restricts the fixed-density bulk radiation to a symplectic surface **before quantization** and keeps the second polarization as a classical background. Quantization of the whole null sheet need not preserve that surface as a Hilbert subspace. The cap interiors, corner operators and constraints matching two sheets would enter a claim about the physical four-dimensional clock. Its finite-reading probability remains open. [Full reduction and clock ordering](https://arxiv.org/html/2611.34924v1#S4.E22)
