# Two nonlinear affine clocks at one cylindrical waist

At the same waist of a curved vacuum Einstein–Rosen cylinder, the lower and upper affine clocks have a strictly positive classical cross-bracket. At radial cuts $0.64R$ and $0.81R$, the worked value is $0.0010258692\,G_N$. Two clocks on the **same outgoing face** can also have an unambiguous nonzero sharp limit. At cuts $0.36R$ and $0.81R$ it is $0.0043908526\,G_N$ for the curvature preparation below. Changing that preparation generally restores a dependence on timing order. Both calculations differentiate the actual nonlinear optical readings at a curved solution. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27)

## Prepare the two clocks

Use the regular-axis polarized vacuum metric
$$
 ds^2=e^{2\gamma+q}(-dt^2+dr^2)+r^2e^q d\phi^2+e^{-q}dz^2,
 \qquad \phi\sim\phi+2\pi,\quad z\sim z+2 .
$$
The area radius of a symmetry orbit is $\sqrt r$. Fix the Killing periods, the areal coordinate $r$ and the origin of its harmonic conjugate $t$. The waist is the torus $(T,R)$. The two null faces are $t=T+\sigma(r-R)$ with $\sigma=+1$ for the lower face and $-1$ for the upper. A cap at radial coordinate $a$ has area-radius fraction $\sqrt{a/R}$. Use the regular Cauchy continuation and all smooth polarized radial perturbations. The action fixes the canonical normalization $\{q(t,r), c s q_t(t,s)\}=\delta(r-s)$ with $c=1/(4G_N)$ in these period units. The wave equation $q_{tt}=q_{rr}+q_r/r$ is exactly linear, while $\gamma$ obeys the nonlinear gravitational constraints. [Reduced Einstein action and constraints](joint-polarized.md) · [Kuchař, *Canonical Quantization of Cylindrical Gravitational Waves*](https://doi.org/10.1103/PhysRevD.4.955)

On the measurement region take $q=\alpha(t-T)$, $\gamma=\alpha^2 r^2/8$. Smooth compact Cauchy data giving this preparation follow by taking $q=0$ at $T$ and $q_t=\alpha$ out to slightly beyond $R$, then cutting off smoothly. On either face let $k=\sigma\alpha$ and set
$$
 W_{a,k}(r)=\frac{e^{k(r-a)+\alpha^2(r^2-a^2)/4}}{2\sqrt a},\qquad
 K_{a,k}(r)=\int_r^R W_{a,k}(s)\,ds,\qquad H_{a,k}(r)=(1+kr)K_{a,k}(r).
$$
The affine reading $U=\rho'_c(u_S-u_c)$ is $\int_a^R W_{a,k}\,dr$. For an arbitrary variation of $q$ with face trace $y$, its differential is
$$
 D U[y]=\int_a^R H_{a,k}(r)y'(r)\,dr
       =-H_{a,k}(a)y(a)-\int_a^R H'_{a,k}(r)y(r)\,dr.                 \tag{1}
$$
Indeed on a general solution the exponent in $W$ is $q(r)-q(a)+\tfrac12\int_a^r s(q'(s))^2ds$, with primes and arguments taken along the face. The constraint gives this formula on either ray orientation. Varying it before inserting $q'=k$ gives (1). Thus each clock has a cap atom and a bounded bulk density, and $H(R)=0$ eliminates the waist atom.

## Opposite faces at the same waist

Place the lower cap at $a$, the upper at $b$, with $a+b>R$. For interior source points $r,s$ on the lower and upper faces the time separation $2R-r-s$ exceeds $|r-s|$ and is less than $r+s$. The first condition puts them inside the direct wavefront, and the second excludes the wavefront via the axis. The canonically normalized radial causal kernel is
$$
 \{q(T+r-R,r),q(T+R-s,s)\}=\frac{\mathsf K(m)}{\pi c\sqrt{rs}},
 \quad m=\frac{(R-r)(R-s)}{rs},\qquad
 \mathsf K(m)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-m\sin^2\theta}} .
$$
This follows by integrating the planar retarded wave kernel over relative azimuth. The sign is positive for this ordering by the equal-time momentum normalization. Since $m\le (R-a)(R-b)/(ab)<1$, the power series can be integrated uniformly against both finite signed sources in (1). With $F_n(r)=r^{-1/2}[(R-r)/r]^n$, the answer is
$$
 \{U_{\rm lower},U_{\rm upper}\}
 =\frac{1}{2c}\sum_{n=0}^\infty
 \left[\frac{\binom{2n}{n}}{4^n}\right]^2
 D U_{a,+}[F_n]D U_{b,-}[F_n].                                      \tag{2}
$$
Here the signs on $U$ label $\sigma$. Each $F_n$ decreases strictly in the interior. For $|\alpha|R<1$, both $H$ are positive there. Every term is positive, and the $n=0$ term alone gives a strict lower bound. The same sign argument applies to nearby smooth polarized backgrounds for which $1+r q'$ stays positive on both faces. [Causal kernel and its normalization](joint-peierls.md)

Independently average each reading over its cap fraction and waist time, with positive unit-mass response densities of shrinking compact supports and fixed $R$. The kernel on these collars stays bounded because the axis front remains separated. The direct front can cross the rectangle near $r=R$ or $s=R$. Neither line carries product source mass at the limiting waist, by (1). Separating the cap atoms and parametrizing the two bulk integrations on fixed intervals therefore gives convergence by bounded convergence, with the same result for either timing order and every relative shrinking rate. For $R=1$, $\alpha=1/2$, $a=0.64$, $b=0.81$, (2) gives the first stated value. Both clocks refer to the same waist instant. Their optical paths sample the past and future of that waist.

## Distinct caps on one outgoing face

Take $a<b$ and $k=\alpha$ for both clocks. Write $\mu_i$ for the signed source of (1) divided by $\sqrt r$, for $i=a,b$. Its atom and total mass are
$$
 A_i=-H_i(i)/\sqrt i,\qquad M_i=D U_i[r^{-1/2}]=-	frac12\int_i^R H_i(r)r^{-3/2}dr.
$$
For a small positive delay of the second waist the direct wavefront gives the limit $B_+=(2c)^{-1}\int_{r<s}\mu_a(dr)\mu_b(ds)$. With a negative delay it gives $B_-=-(2c)^{-1}\int_{s<r}\mu_a(dr)\mu_b(ds)$. The cap atoms occur at distinct radii, so the diagonal carries zero product mass. In particular
$$
 B_+-B_-=M_aM_b/(2c).                                                \tag{3}
$$
Shrinking cap and timing windows have these same conditional one-sided limits. Uniformity follows by treating the separated cap atoms explicitly. The remaining diagonal strips have mass $O(|d|)$ at delay $d$, uniformly over nearby cap locations, since at least one measure in each such term is a bounded bulk density. Thus generic data with $M_aM_b\ne0$ retain a timing-order dependence even with distinct caps. [One-face wavefront jump](joint-resolution.md)

Choose the background slope so that $M_a=0$. At $\alpha=-1/a$ the mass is positive, and at $\alpha=-1/R$ it is negative, giving an interior root. On $[b,R]$ the two weights $W_a$ and $W_b$ are proportional because their exponents have the same radial derivative. With $\kappa=W_a(b)/W_b(b)>0$ also $H_a=\kappa H_b$ there. The continuous mass of $\mu_b$ is $L_b=M_b-A_b$. The mass of $\mu_a$ below $b$ is then $-\kappa L_b$. In $2c B_+$ this lower piece contributes $-\kappa L_bM_b$, while the overlapping bulk pieces contribute $\kappa L_b^2/2$. Therefore both one-sided limits give
$$
 B_+=B_-=\frac{\kappa}{4c}(A_b^2-M_b^2).                            \tag{4}
$$
Every shrinking positive independent cap and time average described above gives this value, including asymmetric timing windows.

For the worked example take $R=1$, $a=9/25$, $b=81/100$. To check positivity without relying on a fitted root, interchange the mass integrals to write $M_a=-\int_a^1 W_a(s)(\sqrt{s}-\sqrt a)[\alpha+1/\sqrt{as}]ds$. At any root, $x=-\alpha$ is a positive weighted mean of $1/\sqrt{as}$ and lies between $5/3$ and $25/9$. Consequently $A_b,M_b>0$ and $K_b(r)\le K_b(b)$ gives
$$
 \frac{M_b}{A_b}\le\frac{x-1}{xb-1}(1-\sqrt b)<\frac4{21}.
$$
Bisection gives $\alpha=-1.9432085243$ and (4) gives the second stated bracket. Equation (3) at $\alpha=1/2$ instead gives a jump of $0.0067824253\,G_N$ for the same two caps. The coincidence in (4) is a statement at the calibrated solution. These pairwise limits do not establish closure or the Jacobi identity for an algebra of all sharp clocks. Their toroidal cuts, fixed orbit markings and global Cauchy continuation bound their bearing on the spherical isolated diamond of v1.

## Reproduce the calculation

Run `python3 -B checks/timing_nonlinear.py` from the repository root and `make check` for the suite. The focused check evaluates the opposite-face result both by signed-source quadrature of the elliptic kernel and by the moment series. It locates a zero of the first mass, integrates the separated wavefront at positive and negative delay, and checks the predicted jump after changing the curvature. [Executable calculation](../checks/timing_nonlinear.py)

```text
Opposite faces, curved vacuum: bracket / G = 0.0010258692
Same outgoing face, zero first mass at alpha*R = -1.9432085243
Delay +/-1e-03, earlier 0.0043773265, later 0.0044042462
Delay +/-1e-05, earlier 0.0043907174, later 0.0043909873
Delay +/-1e-07, earlier 0.0043908513, later 0.0043908540
Common sharp bracket / G = 0.0043908526
Uncalibrated same-face jump / G = 0.0067824253
```
