# A nonlinear vacuum clock and its conjugate on a spacelike cap and null sheet

In the polarized Einstein–Rosen family, the geometric clock has an exact canonical bracket on a two-parameter space of curved vacuum solutions. The conjugate displacement changes the proper length of a periodic Killing orbit. Allowing arbitrary radial waves gives a different result. The sharp clock still has brackets with smooth probes, but its differential has no smooth Hamiltonian vector on the matched cap and sheet whenever the shear at the rim is nonzero. Both statements follow from the same four-dimensional action. The calculation uses toroidal cuts with fixed areal embeddings. The corresponding problem on Chandrasekaran's spherical diamond with its allowed corner variations remains open. [Chandrasekaran, arXiv:2611.34924v1, (3.18)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E18) · [Kuchař, canonical reduction of cylindrical gravitational waves](https://doi.org/10.1103/PhysRevD.4.955)

## The Einstein action on the mixed initial surface

Use fixed length units, azimuthal period $2\pi$, axial period $2$, and reference measure $d\varphi\,dz$ with integral $4\pi$. The regular-axis, twist-free vacuum metric is
$$
 ds^2=e^{2\gamma+q}(-dt^2+dr^2)+r^2e^q d\varphi^2+e^{-q}dz^2 .
$$
The orbit area density is $r$, its area radius is $\rho=\sqrt r$, and its unit-determinant polarization is $P=\log r+q$. Fix the areal coordinate $r$ and its harmonic conjugate $t$, including the origin of $t$. The initial surface consists of the solid torus $t=0$, $0\le r\le a$, and the null sheet $t=r-a$, $a\le r\le R$. The cap ratio $\sqrt{a/R}$, the density at each end, the angular identifications and the embeddings in these coordinates are fixed. The orbit shape can vary at both ends. The axis has a periodic line of origins.

Here is the action reduction. Write $h$ for the Lorentzian base metric and $c=\int d\varphi\,dz/(16\pi G_N)$. Substitution of the diagonal orbit metric into Einstein–Hilbert gives, up to a base divergence,
$$
 I=c\int \sqrt{-h}\left[r\mathcal R(h)+\frac{(\nabla r)^2}{2r}
                       -\frac r2(\nabla P)^2\right]d^2x .
$$
For $h=e^{2\gamma+q}\eta$, the curvature term is $-r\Box_\eta(2\gamma+q)$, a divergence since $\Box_\eta r=0$. The mixed term from $P=\log r+q$ is a radial derivative, and the two terms independent of $q$ from the gradients cancel. The reduced kinetic action and the remaining vacuum equations are
$$
 I_q=\frac c2\int r(q_t^2-q_r^2)\,dt\,dr,\qquad
 q_{tt}=q_{rr}+q_r/r,\qquad
 \gamma_r=\frac r4(q_t^2+q_r^2),\quad
 \gamma_t=\frac r2 q_t q_r .                                      \tag{1}
$$
The last two equations come from the base Einstein equations before fixing the areal gauge. Their compatibility follows from $\partial_t\gamma_r-\partial_r\gamma_t=(r/2)q_t(q_{tt}-q_{rr}-q_r/r)$. Smooth radial data and $\gamma(t,0)=0$ fix the integration constant on the cap.

The potential from $I_q$ on $t=f(r)$ is $c\int r(q_t+f'q_r)Dq\,dr$. This also follows directly from the four-dimensional metric potential. With $h=e^{2\lambda}\eta$, the base density in the Einstein potential is proportional to $-2r\partial^aD\lambda+2\partial^a r\,D\lambda-r\partial^aP\,DP$ with indices raised by $\eta$. The terms linear in $D\lambda$ and the background $\log r$ are field-exact in this gauge. The area–angle corner two-forms vanish since both cut areas are fixed, the twist vanishes by symmetry, and the regular axis carries zero orbit area. Thus the joint form on matched smooth solutions, with $x(s)=X(s-a,s)$ and $y(s)=Y(s-a,s)$, is
$$
 \Omega(X,Y)=c\int_0^a r(X_tY-Y_tX)_{t=0}\,dr
             +c\int_a^R r(x'y-y'x)\,dr .                          \tag{2}
$$
In particular the field has one common trace at the rim. Conservation of the radial wave current identifies (2) with the spacelike integral over $0\le r\le R$ at $t=R-a$. The apex of this deformation at $R$ has fixed coordinates and area. [Original cap and corner potentials, (3.46) and (A.18)](https://arxiv.org/html/2611.34924v1#S3.E46) · [Fixed-label sheet reduction](rim-potential.md)

## The exact clock on a curved solution

Write $q_s(r)=q(r-a,r)$. Affine tangents to the outgoing generator satisfy $d u/dr\propto e^{2\gamma+q}$ there. Normalizing by $\partial_u\sqrt r$ at $a$ and using (1), which gives $\gamma_s'=r(q_s')^2/4$, yields
$$
 U=\int_a^R W(r)\,dr,\qquad
 W(r)=\frac1{2\sqrt a}\exp\left[q_s(r)-q_s(a)
                       +\frac12\int_a^r s\,q_s'(s)^2ds\right].
                                                                    \tag{3}
$$
Since $P_s'=1/r+q_s'$, the exponent in the focusing formula is $\Xi(r)=\tfrac12\int_a^r s(P_s')^2ds$. Multiplication by $d\rho=dr/(2\sqrt r)$ reproduces (3). The angular average is the same $U$ by symmetry. [Affine clock and angular average, v1 (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27)

Now take the invariant family $q=B+\alpha t$, $\gamma=\alpha^2r^2/8$. For $\alpha\ne0$ the spacetime is curved. For example the sectional curvature of the two Killing directions is $-e^{-2\gamma-q}\alpha^2/4$ in the convention where a round sphere has positive sectional curvature. The cut shear is proportional to $P_s'=1/r+\alpha$. The fixed period of $z$ makes $B$ physical, with axial circumference $2e^{-B/2}$ on the cap. The induced form and clock are
$$
 \Omega_{\rm hom}=\frac{cR^2}{2}\,D\alpha\wedge DB,\qquad
 U(\alpha)=\frac1{2\sqrt a}\int_a^R
   e^{\alpha(r-a)+\alpha^2(r^2-a^2)/4}\,dr .
$$
The cap contributes $ca^2/2$ to the coefficient of $D\alpha\wedge DB$ and the sheet contributes $c(R^2-a^2)/2$. In the canonical convention $\{B,cR^2\alpha/2\}=1$ one obtains
$$
 \boxed{\{B,U\}_{\rm hom}=\frac{2U'(\alpha)}{cR^2}}.            \tag{4}
$$
Equivalently, the convention $\Omega(X_U,Y)=dU(Y)$ gives $X_U=-2U'(\alpha)\partial_B/(cR^2)$. At $(a,R)=(1/4,1)$ and $\alpha=1/2$, $U=0.93341852$ and $c\{B,U\}_{\rm hom}=0.94161524$.

At $\alpha=0$ the same data have $U=3/4$, $U'=9/32$ and $P=2\log v+B$ with $v=\sqrt r$. The tangent $Y(t,r)=2-16t/3$ has weighted rim trace $\sqrt a\,Y(0,a)=1$ and $\int_a^R y(r)dr=0$. It changes $U$ by $-16U'/3=-3/2$. This reproduces the endpoint example with actual cap and sheet data. Its variation within the homogeneous family is paired by (4). A separate inhomogeneous curvature perturbation realizes the same value. [Fixed-area endpoint example](endpoint-inverse.md) · [Independent curved perturbation of the flat background](joint-peierls.md)

## Allowing radial dependence

Define the functions
$$
 K(r)=\int_r^R W(s)ds,\qquad H(r)=rP_s'(r) K(r).
$$
Varying (3), or interchanging the radial integrals in $d\Xi$, gives
$$
 dU(Y)=\int_a^R H\,y'\,dr=-H(a)y(a)-\int_a^R H' y\,dr .        \tag{5}
$$
This identity holds at arbitrary smooth cylindrical backgrounds, including those with nonlinear backreaction. The coefficient of the cap trace at $\alpha=1/2$ in this example is $-1.05009584$.

Suppose a smooth matched $X$ represented (5) through (2). Arbitrary smooth variations of each of the two Cauchy data supported strictly inside the cap have zero outgoing sheet trace by finite propagation. The wave constraints (1) reconstruct $D\gamma$ for those variations. A constant change of $D\gamma$ along the sheet cancels between the sheet metric exponent and its rim value in (3). Testing both Cauchy data forces $X=X_t=0$ in the open cap and hence $x(a)=0$ by smooth matching. Now take a bounded smooth sheet test equal to one on a collar of $a$ and zero past $a+\delta$, matched to constant cap field and zero cap velocity. These data can be realized on solutions. In null coordinates $u=t-r+a$, $v=t+r-a$, $w=\sqrt r\,Y$ satisfies $4w_{uv}=w/(4r^2)$ near the rim. Give the incoming characteristic its constant-field solution data and change the outgoing data only beyond the collar. Integrating this equation in $u$ and $v$ gives the smooth continuation, agreeing with the cap solution near the seam. In (2), integration by parts gives a sheet density $c(2rx'+x)$ against $y$, and zero boundary contribution for these tests. Its integral tends to zero as $\delta\downarrow0$. Equation (5) tends to $-H(a)$, nonzero when $P_s'(a)\ne0$. Therefore (4) inverts the form **only on the homogeneous subspace**. The smooth-vector obstruction on the larger space holds even though the two-form comes from a complete symmetry-reduced vacuum action.

Brackets against smooth wave probes still have a distributional representation. On a regular radial Cauchy continuation through the waist, define
$$
 E(\tau;r,s)=\int_0^\infty J_0(kr)J_0(ks)\sin(k\tau)\,dk .
$$
This wave propagator has $E(0)=0$, $\partial_\tau E(0;r,s)=\delta(r-s)/s$ with respect to radial measure $s\,ds$. The field
$$
 X_U(t,r)=\frac1c\left[-H(a)E(t;r,a)
                 -\int_a^R H'(s)E(t-s+a;r,s)\,ds\right]           \tag{6}
$$
satisfies $\Omega(X_U,Y)=dU(Y)$ distributionally on an ordinary spacelike slice of that continuation. Indeed the conserved wave pairing of $E(t-t_0;r,s)/c$ with any regular wave $Y$ evaluates $Y(t_0,s)$. Compact extensions of the test data outside the past or future domain used in (5) give the same response. The kernel is independent of $\gamma$ because the Einstein–Rosen polarization equation is exactly linear in areal gauge. The dependence on the curved background is in $H$.

For a smooth radial probe take the wave $Y=J_0(r)\cos(t-R+a)$, with Cauchy data smoothly cut off beyond the region of dependence if a compact preparation is desired. At $\alpha=1/2$ its response $dU(Y)$ is $0.09604973$. Computing the perturbed affine length using $\gamma$ reconstructed from the **spacelike** radial constraint in (1) gives the same derivative. Formula (6) pairs a single sharp clock with regular probes. Brackets of two distributions at coincident cuts require an additional prescription. The topology of this cap, the frozen corner densities and the absence of the second polarization all limit the conclusion for a spherical diamond.

## Reproduce the calculation

Run `python3 checks/joint_polarized.py` and `make check` from the repository root. The focused check compares the conserved mixed and spacelike currents on a Bessel mode, differentiates the affine clock reconstructed from the spacelike constraint, and checks the split between the bulk density and the cap trace. Expected output follows. [Executable calculation](../checks/joint_polarized.py)

```text
alpha=0 U=0.75000000 U'=0.28125000 rim coefficient=-0.75000000 Bessel response=0.06603210
alpha=0.5 U=0.93341852 U'=0.47080762 rim coefficient=-1.05009584 Bessel response=0.09604973
unit weighted rim trace dU=-1.50000000; mixed current conserved
```
