# A spherical vacuum wave tests the sharp cap clock

In a flat four-dimensional diamond of waist radius one, choose the cap at one third of the waist radius. Send a smooth quadrupole gravitational wave across the cap rim. Its mixed second variation of the averaged clock with a second, fixed quadrupole tends to **$-1/30$** as the first wave narrows. Its symplectic product with every fixed smooth metric perturbation tends to zero. This excludes a continuously differentiable assignment of smooth Hamiltonian vectors through flat space for the matched-radius clock in the joined Einstein phase space specified below. The measurement uses the affine calibration and the angular average of Chandrasekaran's version 1. [Clock and average, (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27)

## Preparing the diamond

Mark a freely falling observer and two events on its worldline. Use its past-event frame to label the outgoing generators by solid angle, and form the waist $S$ where they meet the past cone of the later event. Assume both cuts are regular, the area radius is increasing and the intersection is transverse. Put $\langle f\rangle=(4\pi)^{-1}\int f\,d\Omega$, $\rho=\varrho_S$ and $M=\langle\rho^2\rangle/\langle\rho\rangle$. In the matched-radius preparation adjust the later event so that $M=R$. In flat space $M$ is half the proper time between the events, so the implicit-function theorem defines this adjustment locally. The finite initial rim $C$ is the cut $v=\varrho/\rho=a$, $0<a<1$. Its spacelike cap and incoming null sheet carry the same gravitational fields across their seam.

Use the ordinary vacuum covariant symplectic current on this joined slice, or its ADM integral on a spacelike disk ending at $S$. The two integrals agree for smooth matched solutions by $d\omega=0$. If the common boundary is dressed, retain its common embedding and frame at $S$. This argument allows the cut at $C$ to move with the metric. It assumes that changing the surface used for the integral introduces no independent physical canonical pair at $C$. On a marked global vacuum solution the ordinary Cauchy form supplies a second setting for the same test. For the Hamiltonian statement, take a regular reduction by gauge degeneracies, or assume a representative of any smooth Hamiltonian assignment that vanishes at a critical point. [Covariant current, Iyer and Wald](https://arxiv.org/abs/gr-qc/9403028) · [Embeddings, v1 (B.21)](https://arxiv.org/html/2611.34924v1#A2.E21)

The clock excess $D=\bar u_*-(1-a)M$ has a critical point at the flat solution for all perturbations. On the preparation with $M=R$ it differs from the clock by a constant. Write $H_W$ for the first variation of the determinant-one screen metric along a vacuum solution variation $W$, measured in the round orthonormal screen in the vertex frame. A prime denotes $\partial_v$. Directly differentiating (3.26)–(3.28) at the flat solution gives

$$
 d^2D(W,Z)=\frac{R}{4}
 \left\langle\int_a^1 v(1-v) H'_W:H'_Z\,dv\right\rangle .
 \tag{1}
$$

The first derivative of the focusing exponent vanishes there. Derivatives of the angular weights and both optical endpoints therefore drop out of (1). A change of generator labels adds a $v$-independent term to the first variation of the round screen metric. The radial derivative removes it. At fixed vertex-normalized affine parameter $s$, the first area variation vanishes along every generator by the vacuum Raychaudhuri equation with regular initial slope. At the background $s=Rv$. This derives (1) for genuine cone cuts, including the effect of adjusting the later event.

## Two smooth linearized Einstein waves

Set $R=1$ and put the tips at $(t,\mathbf x)=(0,\mathbf0),(2,\mathbf0)$. Choose $S_{ij}=\operatorname{diag}(-1/2,-1/2,1)$ and a smooth function $F$ compactly supported in $(0,2)$. With $r=|\mathbf x|$ and $P_{ij}=\delta_{ij}\Delta-\partial_i\partial_j$, set

$$
 \phi_F=\frac{F(t+r)-F(t-r)}{r},\qquad
 h_{ij}=(P_{ik}P_{jl}-\tfrac12P_{ij}P_{kl}) S_{kl}\phi_F,\qquad h_{0\mu}=0 .
$$

The regular radial wave has limit $2F'(t)$ at the origin and is smooth there. The spatial perturbation is transverse and trace-free because $\partial_iP_{ij}=0$ and $P_{ik}P_{il}=\Delta P_{kl}$. It obeys the wave equation and hence the linearized vacuum Einstein equations. These waves also give tangents to smooth vacuum data on a ball larger than the diamond. One can use their TT metric and curvature perturbations as conformal initial data. The Dirichlet vector constraint corrects the divergence of the trace-free seed and the Dirichlet Lichnerowicz equation corrects the scalar curvature. Choose maximal data. The correcting equations are $\widetilde D_j(\widetilde L U)^{ij}=-\widetilde D_j\widetilde A^{ij}$ and $-8\widetilde\Delta\varphi+\widetilde R\varphi-|\widetilde A+\widetilde L U|^2\varphi^{-7}=0$, with $U=0$ and $\varphi=1$ on the auxiliary boundary. Both residuals start at second order, since the first-order data obey the flat constraints. The linearized correcting operators are the flat conformal vector Laplacian and scalar Laplacian with zero Dirichlet data, both invertible. Small amplitudes therefore yield corrections of second order and regular finite-time vacuum developments, with the allowed amplitude chosen separately for each wave. [Conformal equations, Choquet-Bruhat, Isenberg and Pollack](https://arxiv.org/abs/gr-qc/0506101)

Let $n=\mathbf x/r$, let $B_{AB}(n)$ be the two-dimensional trace-free projection of $S_{ij}$ into the screen orthogonal to $n$, and use the flat outgoing ray $t=r=s$. Its linearized conformal metric is $H_F=G_F(s)B$, where

$$
 G_F(s)=\frac{F^{(4)}(2s)}{s}
       -\frac{2F^{(3)}(2s)}{s^2}
       +\frac{F''(2s)}{s^3}. \tag{2}
$$

To check (2), contract the linearized Riemann tensor with the outgoing tangent twice and project into the screen. With Jacobi convention $J''=-R_{\cdot k\cdot k}J$, the trace-free part of $-R_{\cdot k\cdot k}$ divided by $B$ has coefficients $2/s,-4/s^2,6/s^3,-6/s^4,3/s^5$ multiplying $F^{(6)},F^{(5)},F^{(4)},F^{(3)},F''$ at $2s$. The same expression is $(s^2G'_F)'/(2s^2)$. The perturbation and its initial data vanish near the vertex. Thus the integration constants are fixed and (2) includes the deflection of the bundle. The round average of $B:B$ equals $(2/5)S:S=3/5$, by the second and fourth moments of $n$ on the unit sphere.

For the fixed wave $W$ take $F_W(u)=a(u-2a)^5/240$ on a neighborhood of $2a$, smoothly cut off inside $(0,2)$. Then $G'_W(a)=1$. For the narrowing wave $Z_\eta$, take $F_\eta(u)=a\eta^4 f((u-2a)/\eta)$ with $f$ a smooth compact bump satisfying $f^{(4)}(0)=1$ and $f''(0)=f^{(3)}(0)=0$. Equation (2) gives $G_\eta(a)=1$, bounded $G_\eta$ and support of width $O(\eta)$. Integrating (1) by parts now gives

$$
 d^2D(W,Z_\eta)=
 -\frac{3}{20}a(1-a)
 -\frac{3}{20}\int_a^1 [v(1-v)G'_W]'G_\eta\,dv
 \ \longrightarrow\ -\frac{1}{30}\quad(a=1/3).
 \tag{3}
$$

The finite contribution comes from the wave's value at the physical rim. At a smooth vertex the factor $a$ vanishes.

## What a smooth Hamiltonian vector would give

On the waist disk $t=1$, the Cauchy data of $Z_\eta$ are supported in the interior near $r=1-2a=1/3$. They tend to zero as distributions. For example, after moving the four spatial derivatives onto a smooth test by parts, the radial scalar has size $O(\eta^4)$ on an annulus of thickness $O(\eta)$ and its time derivative has size $O(\eta^3)$. The ADM product $\Omega_{\rm flat}(V,Z_\eta)$ tends to zero for every fixed smooth tangent $V$. Compact support inside the disk removes its boundary terms.

The spacetime metric perturbation vanishes near both tips and $S$. The central observer stays on the same timelike geodesic to first order because $h_{0\mu}=0$ in this gauge. There is also a check on movement of the physical waist. Integrate the linearized geodesic equation from each tip to $S$. On each unperturbed ray the perturbed Christoffel symbols are finite sums of derivatives of $F_\eta(2s)$ or $F_\eta(2-2s)$ against coefficients smooth on the annulus where the wave is supported. The other phase has constant argument outside the support. Both endpoints are outside either pulse. Integrating by parts moves all derivatives onto the smooth coefficients, giving $O(\eta^5)$ changes in the arrival positions and tangents, also after angular differentiation. Transversality gives the same bound for the waist displacement, its local normal frame and the proper-time adjustment keeping $M$ fixed. These boundary variations pair to zero in the limit with any fixed smooth waist charge. This argument for the endpoint estimates requires only the integrated geodesic equation, independently of (2).

If $X_D$ were a $C^1$ assignment of smooth physical tangents through the flat solution, $\Omega(X_D,\cdot)=dD$ and $dD_{\rm flat}=0$ would imply $X_D|_{\rm flat}=0$ after reduction. Differentiation in the $W$ direction would give

$$
 d^2D(W,Z_\eta)=\Omega_{\rm flat}((d_W X_D)_{\rm flat},Z_\eta)\longrightarrow0 .
$$

Equation (3) contradicts this implication. On the matched-radius preparation the same argument applies to the clock itself. On a phase space where $M$ varies it applies directly to the excess and transfers to the original clock if $M$ has a smooth Hamiltonian assignment. For example, in a fixed angular chart implementing the pointwise area boost charges of (3.42), $dM$ is a smooth weighted integral of the area-density differentials and their boost fields supply that assignment. A different rim phase space could retain independent fields with their own two-form, or impose boundary conditions excluding these waves. Its reduction would have to give the pairing in (3) to support a smooth generator. This is a regularity obstruction near the flat solution. At the critical point itself the zero vector solves its Hamilton equation. A weak response can still give brackets with smooth test observables. The quantum projector requires its own domain and rank analysis. [Area and boosts, v1 (3.42)–(3.44)](https://arxiv.org/html/2611.34924v1#S3.E42) · [Mixed Peierls bracket with a smooth source](joint-jacobi.md)

There is a conclusion for the freely varying radius that needs no Hamiltonian for $M$. Read two cap ratios $a\ne c$ on the same extended cones, using one marked preparation and the same symplectic form. The difference $\bar u_a/(1-a)-\bar u_c/(1-c)$ is critical at flat space because its two radius terms cancel. Interchange the ratio names if necessary so that $a\ne1/2$. The Cauchy shell then lies at the positive radius $|1-2a|$ strictly inside the waist disk. For a pulse centered at $a$, the $c$-excess has vanishing limiting Hessian. If $c>a$ it misses the pulse, and if $c<a$ integration by parts covers both halves with a smooth kernel. The difference therefore has the nonzero limit $-3a/20$ with the normalized preparation above. Two distinct raw clocks on this common phase space cannot both have $C^1$ assignments through flat space. Comparing regulators by this argument requires identifying their solutions, embeddings and symplectic form on the common extension.

## Reproduce the test

The executable uses $f(x)=x^4(1-x^2)^{12}/24$ inside the unit interval and zero outside. It is $C^{11}$, sufficient for the six derivatives in the curvature check. A smooth compact bump with the same center jets gives the identical analytic limit. Run `python3 -B checks/joint_spherical_hessian.py` from the repository root. The script checks the angular norm $3/5$ and the unit reference slope. Its compact piecewise polynomial test profile has eleven continuous derivatives, sufficient for both the curvature and direct clock integrals. The analytic proof allows a smooth bump with the same jets at its center. The five printed rim strains should all be one, and the final line should read `sharp analytic limit=-0.0333333333  (-1/30)`. Run `make check` for the complete suite. [Executable check](../checks/joint_spherical_hessian.py)
