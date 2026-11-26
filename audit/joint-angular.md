# The angular cap charge on a round diamond

A narrowing gravitational quadrupole leaves a finite change of the normal connection at the cap. In the one-third-radius experiment an independently displaced angular frame could reproduce the clock Hessian of $-1/30$ through this charge alone. The required displacement stretches the round metric. At a common rim of the same smooth spacetime, the cap and sheet cannot undergo that relative stretch while their induced metrics agree. [Spherical wave and clock Hessian](joint-flat-hessian.md) · [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.56)–(3.57)](https://arxiv.org/html/2611.34924v1#S3.E57.3)

Let $R$ be the flat waist radius, $s$ the vertex-normalized affine distance, $v=s/R$, and $r_c=aR$ the radius of the initial rim $C$. Write $\gamma$ for the unit sphere metric and $D_A$ for its derivative. On fixed affine cuts the first-order angular metric is $s^2(\gamma_{AB}+H_{AB})$, with $H$ trace-free. Vacuum focusing and the regular initial slope give $\delta\theta=0$, and the mixed-index shear is $\delta\sigma^B{}_A=\tfrac12\partial_s H^B{}_A$. In the convention $\varpi_A=-n\cdot\nabla_A\ell$ with $\ell\cdot n=-1$, (3.57c) then integrates from the regular vertex to give

$$
\delta\varpi_A(s)
=-\frac{1}{2s^2}\int_0^s t^2 D^B\partial_tH_{AB}\,dt
=-\frac12D^B H_{AB}(s)+\frac{1}{s^2}\int_0^s tD^B H_{AB}\,dt .
\tag{1}
$$

For the pulse of width $\eta$ in the spherical experiment, $H$ and its angular derivatives are bounded and supported in a shrinking collar of $C$ on the first cone. The integral in the last expression tends to zero at $C$. The moving area-ratio rim has the same limit. Its first affine displacement is $a\,\delta\rho_S$, which tends to zero with its angular derivatives in that experiment. Equation (1) also gives zero limiting twist beyond the pulse. The null frame here remains vertex-normalized. A change $\ell\mapsto e^\beta\ell$ would add $D_A\beta$ to $\varpi_A$. The harmonic version of the transport equation appears in v1. [Eq. (D.39)](https://arxiv.org/html/2611.34924v1#A4.E39)

Orient the null sheet from $S$ to $C$ and write its one-sided angular endpoint potential as $\Theta_C=(8\pi G_N)^{-1}\int_C\mu_C\varpi_A\,\delta F^A$ at the identity angular map $F$. Take $\Omega=d\Theta$ and contract the response in the first slot. On the round background $\varpi=0$ and $\mu_C=r_c^2d\Omega$. Let $V=\delta_XF$ and keep the independent angular map fixed on the test $Z$. Then (1) and integration by parts on the sphere give

$$
\lim_{\eta\to0}\Omega_C(X,Z_\eta)
=-\frac{r_c^2}{16\pi G_N}\int_{S^2}
   (D_{(A}V_{B)})^{\rm TF} H_C^{AB}\,d\Omega ,
\tag{2}
$$

where $H_C$ is the limiting rim strain. Reversing the orientation reverses this one-sided charge. On the smooth joined slice the two orientations at an internal seam are opposite. [Derivation of the angular endpoint potential, Eq. (5)](rim-potential.md)

The shear contribution to the Hessian of the averaged clock is $-Ra(1-a)\int H'_W:H_C\,d\Omega/(16\pi)$, where the prime is $\partial_v$ and $W$ is the fixed wave. Hence an angular term supplying the whole coefficient for arbitrary rim polarizations would have to satisfy

$$
(D_{(A}V_{B)})^{\rm TF}
=\frac{G_N(1-a)}{aR}\,H'_{W,AB}(a).
\tag{3}
$$

For the test quadrupole let $Q(\theta)=(3\cos^2\theta-1)/2$. Its screen tensor $B$ is the trace-free projection of $\operatorname{diag}(-1/2,-1/2,1)$ and obeys $B_{AB}=\tfrac12(D_AD_BQ)^{\rm TF}$. The sphere curvature and $\Delta Q=-6Q$ give $D^BB_{AB}=-D_AQ$. The fixed wave has $H'_W(a)=B$, and the pulse has $H_C=B$. A solution of (3) is therefore

$$
 V_A=\frac{G_N(1-a)}{2aR}\,D_AQ .
$$

One can add a conformal Killing field without changing (3). Testing only the displayed wave fixes the projection of $V$ onto $D^AQ$. For $R=1$ and $a=1/3$, equation (1) gives $\delta\varpi\to dQ/2$ and the representative is $V=G_N\,\mathrm{grad}\,Q$. Since $\langle |DQ|^2\rangle=9(1/3-1/5)=6/5$, equation (2) gives $-(1/3)^2(6/5)/4=-1/30$.

At fixed angular labels a one-sided displacement changes the area density by $\delta\mu_C/\mu_C=D_AV^A$. For this representative it equals $-3G_N(1-a)Q/(aR)$. An affine displacement $f\ell$ contributes $2f/r_c$ on the round cut. With the waist density and bulk metric held fixed, $f=-r_cD_AV^A/2$ restores the area at first order. The full metric matching condition is stronger. Both normal second fundamental forms of the round Minkowski sphere are pure trace. If the two faces have the same smooth metric perturbation and their embeddings differ by a tangential $V$ and any normal displacement, the trace-free difference of the two pulled-back metrics at the common rim is $2r_c^2(D_{(A}V_{B)})^{\rm TF}$. Thus a relative motion preserving that equality in the common marked chart must be conformal Killing. The quadrupole in (3) fails this test even with the compensating $f$.

An independent comparison map between the two faces also acts by a Lie derivative in the matching equation. Its displacement must be included in the net relative $V$. If the two sides instead carry independent metric perturbations, their trace-free difference enters that equation as well. A proposed extension with an independent angular cap charge must specify its matching and show that the residual charge survives reduction. Equation (2) fixes the coefficient it would need on this test. [Cap and sheet matching](joint-edges.md) · [Moving pullbacks, v1 (3.40)](https://arxiv.org/html/2611.34924v1#S3.E40)

To check the angular coefficient exactly, run the following from the repository root. The first command prints `-1/30`. The second independently integrates the mixed clock Hessian for the spherical quadrupoles and approaches the same value. Run the full suite with `make check`. [Spherical-wave check](../checks/joint_spherical_hessian.py)

~~~sh
python3 -c 'from fractions import Fraction as F; a=F(1,3); g=9*(F(1,3)-F(1,5)); print(-a*a*g/4)'
python3 -B checks/joint_spherical_hessian.py
~~~
