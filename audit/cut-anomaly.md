# A shear measurement in affine and area coordinates

Two compact shear probes can distinguish the Gaussian states obtained by declaring positive frequency separately in affine distance and in area radius. The distinction occurs on an exactly Ricci-flat, expanding light cone. For the pulse and probes below, the difference in their covariance is $-0.06234985\,C$, where $C>0$ fixes the current normalization. Describing the same prepared state in both coordinates gives exact agreement. This comparison isolates one piece of the quantum change-of-cut problem in Venkatesa Chandrasekaran’s [arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1). The paper allows a choice of Gaussian widths and does not prescribe resetting the vacuum under an affine-to-area change. [Incoming Gaussian state, §4.2](https://arxiv.org/html/2611.34924v1#S4.SS2) · [Existing two-cut tests](refoliation-test.md)

## A smooth vacuum pulse with a prescribed area radius

Measure lengths in units of the pulse duration. Choose a smooth probability density $p(t)$ supported on $[1,2]$, symmetric about $m=3/2$, with a smooth square root. In the executable example $p(t)$ is proportional to $\exp[4-1/((t-1)(2-t))]$ inside the interval and zero outside. For $0<\delta<1$ prescribe the optical radius along the outgoing cone by

$$
D(x)=x-\delta\int_1^2(x-t)_+p(t)\,dt,\qquad
D''=-\delta p,\qquad 1-\delta\le D'\le1 .
$$

Here $x$ is affine distance from the vertex. Before the pulse $D=x$. After it $D=cx+(1-c)m$, with $c=1-\delta$. The positive radius increases everywhere on $x>0$, including throughout the pulse. The manuscript’s area coordinate for a corner at $x_S$ is $v=D(x)/D(x_S)$. This constant rescaling preserves the choice of positive frequencies. The affine coordinate $x$ and the area coordinate agree up to rescaling on each shear-free stretch separately. No single Möbius transformation agrees with $D$ across the pulse, since one agreeing with the identity on an open interval is the identity everywhere. [Area coordinate and focusing, Eqs. (3.25)–(3.27)](https://arxiv.org/html/2611.34924v1#S3.E25)

Choose $F=0$ before the pulse and $F'=\sqrt{\delta p/D}$ on its support, extended by zero on either side. The Jacobi lengths $J_\pm=D e^{\pm F}$ have $J_\pm(0)=0$, $J_\pm'(0)=1$ and

$$
J_\pm''=\pm QJ_\pm,\qquad
Q=F''+2(D'/D)F',\qquad D''/D+(F')^2=0 .
$$

Set $Q=0$ outside the pulse. The Brinkmann metric $ds^2=-2\,dx\,dV+dX^2+dY^2+Q(x)(X^2-Y^2)\,dx^2$ is smooth and Ricci-flat. Its transverse geodesic equations give the two Jacobi lengths directly. Label generators by their initial transverse velocities $\theta_1,\theta_2$ and fix their affine scale by $dx/ds=1$. Then $X=J_+\theta_1$, $Y=J_-\theta_2$. The induced metric at fixed $x$ is $J_+^2d\theta_1^2+J_-^2d\theta_2^2$, giving the same area radius throughout an angular patch relative to $d\theta_1d\theta_2$. Thus a smooth, normalized transverse smearing can be used across the calculation. The optical shear eigenvalues are $\pm F'$. This constructs the background at finite pulse strength. [Harte, exact plane-wave optics](https://arxiv.org/abs/1502.03658v2)

## Which gravitational variable the probes measure

On one branch fix the corner area density, angular frame and affine origin and scale. Take compactly supported radiative variations in the cross polarization around this diagonal background. In the coordinates of (4.21) the conformal metric has $z^1=2F$, $z^2=0$ and its space of possible shapes has line element $(dz^1)^2+e^{2z^1}(dz^2)^2$. The unit normal to the background path, $e^{-z^1}\partial_{z^2}$, is parallel along that path. Write the physical cross strain in this frame as $h=e^{z^1}\delta z^2$. The focusing source $(\partial_x z^1)^2+e^{2z^1}(\partial_x z^2)^2$ has zero first variation in this sector. With fixed initial optical data the first-order variations of $D$ and the affine-to-area map vanish. [Conformal metric, Eq. (4.21)](https://arxiv.org/html/2611.34924v1#S4.E21) · [Affine variations, Eqs. (A.19)–(A.25)](https://arxiv.org/html/2611.34924v1#A1.E19)

For this block of the linearized radiative data, the bulk symplectic form (A.20) reduces, up to a constant set by $G_N$ and angular normalization, to

$$
\Omega(h_1,h_2)\ \propto\ \int D^2(h_2h_1'-h_1h_2')\,dx
=\int(H_2H_1'-H_1H_2')\,dx,\qquad H=Dh .
$$

We use the free chiral Gaussian states of this characteristic field, with the scalar zero mode omitted. Its current $J=\partial_x H$ has off-diagonal symmetrized covariance $-C/(x-y)^2$ in the positive-$x$-frequency state, by the damped integral $C\int_0^\infty k\cos[k(x-y)]e^{-\tau k}dk$ as $\tau\downarrow0$. Equation (D.19) gives the same current kernel for transversely smeared shear on a flat null plane. The factor $D$ in $H=Dh$ matters on the expanding cone. [Radiative symplectic form, Eq. (A.20)](https://arxiv.org/html/2611.34924v1#A1.E20) · [Locally flat kernel, Eq. (D.19)](https://arxiv.org/html/2611.34924v1#A4.E19)

Compare two prescriptions for the **same** current $J$ at fixed physical positions $x,y$. Preparing the vacuum using modes $e^{-ikx}$ gives $G_x$. Using modes $e^{-i\omega D}$ instead gives $G_D$ after transforming the current as a one-form. Away from coincidence,

$$
G_x=-\frac C{(y-x)^2},\qquad
G_D=-C\frac{D'(x)D'(y)}{[D(y)-D(x)]^2},\qquad R=\frac{G_D}{G_x}.
$$

For $x=1/4$, $y=9/4$ and $\delta=1/4$, the affine separation is $2$, the optical separation is $29/16$, and

$$
R=\frac{768}{841},\qquad G_D-G_x=\frac{73}{3364}\,C .
$$

Preparing the affine vacuum and then using the area chart gives the covariance in that chart by multiplying $G_x$ by $(dx/dD)(dy/dD)$. Pulling it back gives precisely $G_x$. The discrepancy above therefore measures a change of state under a fresh choice of positive frequency.

**Compact optical shear sources.** Both probe regions have zero background shear. There the orthonormal-screen component of the perturbed optical shear is $\delta\sigma_\times=h'/2$, by (3.25d). Let $B$ be a smooth bump supported in either of those regions and put $f=B'$, $g=D f-D'B$. Since $D''=0$ there, $g'=Df'$. Integration by parts gives a compact source for pure shear,

$$
\int fJ\,dx=-\int Df'h\,dx=\int gh'\,dx
=2\int g\,\delta\sigma_\times\,dx .
$$

Choose two nonnegative unit-integral bumps $B_1,B_2$, with $x$ in $[0.20,0.30]$ and $y$ in $[2.20,2.30]$. For $x+y<2m$, $R=c[1-\delta(y-m)/(y-x)]^{-2}<1$. Integrating the two $B'$ smearings by parts gives a difference of the shear-source covariances with a strict sign,

$$
\iint B_1(x)B_2(y)\,\partial_x\partial_y(G_D-G_x)\,dx\,dy
=6C\iint B_1(x)B_2(y)\frac{R^2-1}{(y-x)^4}\,dx\,dy<0 .
$$

For $\delta=1/4$ and the translates and rescalings of $p$ to the indicated supports, this difference divided by $C$ is $-0.06234985$. The sign and the pointwise ratio depend only on data on a finite expanding segment containing the sources and the pulse. No infrared limit or coincident-point subtraction enters these two-shear measurements. [Optical shear, Eq. (3.25d)](https://arxiv.org/html/2611.34924v1#S3.E25.4)

## A finite-cone test with unlimited angular resolution

Suppose that each frequency prescription is used independently in every orthogonal angular mode of the linearized radiative block. Equivalently, let its covariance factor into the radial kernel above times the angular $L^2$ inner product. This choice adds a hypothesis about the state to the ultralocal radiative symplectic form. Angular correlations or a finite angular cutoff change the test.

Choose normalized real smooth angular functions $e_n$ on disjoint patches within the coordinate chart and use the same radial source $f=B_1'+B_2'$ in each. Write $Y_n=J(e_n f)$, which is the sum of the two compact physical shear sources. In either product Gaussian state the $Y_n$ are independent, centered, commuting Gaussians of a common variance $V$. Each single-support variance agrees between the states because $D$ is affine on each support, including at coincident points in the smeared distribution. The mixed covariance differs, so $V_D-V_x=-0.12469969\,C$ for the example.

For fixed real $t\ne0$, the bounded observable $A_N=N^{-1}\sum_{n=1}^N\cos(tY_n)$ has

$$
\langle A_N\rangle=e^{-t^2 V/2},\qquad
\operatorname{Var}(A_N)=\frac{(1-e^{-t^2V})^2}{2N}.
$$

In the affine product Fock representation $A_N$ converges strongly to $e^{-t^2V_x/2}I$. Indeed, on vectors exciting only finitely many angular factors their contribution to the mean is $O(1/N)$ in norm. The remaining vacuum factors give the variance above. Such vectors span a dense subspace after including the complementary angular modes, and $\|A_N\|\le1$. The same proof works in the cyclic representation of the restricted product state on the finite segment, where finite-factor local excitations of the cyclic vector are dense. Every normal state in either representation therefore has expectation tending to the same constant. The area-frequency Gaussian instead gives $e^{-t^2V_D/2}$ for every $N$. **It cannot be a normal state in the affine representation even on this finite segment’s algebra of bounded shear probes.** In particular, a unitary on that Fock space cannot perform this angle-by-angle vacuum reset. The proof uses arbitrarily fine transverse resolution with fixed radial smearings. It supplies neither the angular covariance of v1’s physical state nor the transport to a different cap.

## A Bogoliubov coefficient with a specified infrared completion

For a plane-wave mode expansion, continue the comparison field to $x\in\mathbb R$, using $D=x$ for $x<0$ and keeping the late affine branch out to $+\infty$. The continuation uses signed $D$ through the vertex. Only the portion $x>0$ describes the outgoing cone. These boundary conditions define two full-line states whose restrictions give the covariances above.

Let $u_k=e^{-ikx}/\sqrt{4\pi k}$ and $v_\omega=e^{-i\omega D(x)}/\sqrt{4\pi\omega}$. Take $\beta_{k\omega}$ to be the coefficient of $u_k^*$ in $v_\omega$. The chiral inner product $i\int f^*\overleftrightarrow{\partial_x}g\,dx$ gives $- (u_k^*,v_\omega)$. Writing $\Phi=kx+\omega D(x)$ and integrating by parts with the affine tails regulated in the Abel sense yields, for $k,\omega>0$,

$$
\beta_{k\omega}
=\frac{1}{4\pi\sqrt{k\omega}}\int(k-\omega D')e^{-i\Phi}\,dx
=\frac{\sqrt{k/\omega}}{2\pi}\int e^{-i\Phi}\,dx
=\frac{i\sqrt{k\omega}}{2\pi}\int_1^2
\frac{D''(x)e^{-i\Phi(x)}}{[k+\omega D'(x)]^2}\,dx .
$$

At $k=\omega=1/2$ the phase varies by at most one radian on the support of $D''$. Since $D''$ has one sign there, the integral is nonzero for every $0<\delta<1$. At $\delta=1/4$ the coefficient is $-0.02249044-0.00159372\,i$. It is a continuum-normalized mode coefficient. Narrow normalized frequency packets also give a nonzero mixing amplitude by continuity. [Walker, Bogoliubov calculation for chiral ray maps](https://doi.org/10.1103/PhysRevD.31.767)

The dependence on the infrared completion is visible at $k=r\lambda$, $\omega=(1-r)\lambda$, $0<r<1$. The compact integral allows $\lambda\downarrow0$ inside the integrand. Integration using $D'$ as variable gives

$$
\lim_{\lambda\downarrow0}\lambda\beta_{r\lambda,(1-r)\lambda}
=\frac{i\sqrt{r(1-r)}}{2\pi}\,
\frac{c-1}{r+(1-r)c}.
$$

On every closed $r$-interval inside $(0,1)$ this convergence is uniform and the limit is bounded away from zero. The Jacobian is $dk\,d\omega=\lambda\,d\lambda\,dr$. Consequently the squared Bogoliubov kernel has a logarithmically divergent integral at the origin. The two full-line Fock polarizations fail the Hilbert–Schmidt criterion for unitary equivalence. The unequal asymptotic slopes cause this divergence. Replacing the far extension so that the slopes match makes the displayed soft coefficient vanish. A finite cap by itself specifies neither extension. [Shale, unitary implementation of bosonic symplectic maps](https://www.jstor.org/stable/1993745)

## What remains open in gravity

This is an exact classical cone and a linearized, fixed-corner quantum comparison on its radiative data. Even the separated, compact shear sources distinguish the two Gaussian preparations, so an endpoint phase alone cannot identify those preparations. Moving the corner on one cone from $x_S$ to another value simply rescales $v$ by a positive constant. The non-Möbius map calculated here changes from affine to area parametrization. To test the physical refoliation claim one still needs the quantum transport for two different internal caps with fixed external states, the second null branch, the edge variables and the source couplings. A nonzero difference after that transport would be evidence against cut independence for those hypotheses. The independently chosen Gaussian polarizations give a conditional obstruction to a proposed state-identification rule. A physical refutation would require the theory to impose that rule or the transported physical amplitudes themselves to disagree. [Change of cap in v1, §5.2](https://arxiv.org/html/2611.34924v1#S5.SS2) · [Nonlinear transport test](refoliation-test.md)

Run `python3 checks/cut_anomaly.py` from the repository root. Expect the exact fractions $768/841$ and $73/3364$, the compact-source difference $-0.06234985$ in units of $C$, a maximum vacuum Jacobi trace residual below $2\times10^{-5}$, and $\beta_{1/2,1/2}=-0.02249044-0.00159372\,i$. The check independently integrates the mode overlap using its analytic affine tails and checks the soft limit at three frequency ratios. The repository suite runs with `make check`. [Executable calculation](../checks/cut_anomaly.py)
