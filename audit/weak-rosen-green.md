# The metric Green kernel on the vacuum Rosen strip

The spherical clock's metric current on the symmetric plane wave can be propagated by an explicit position-space Green kernel, Eq. (3a). The resulting tensor kernel has a term strictly inside the null cone. We compute one such component and give the pairing that measures the clock on smooth conserved probes. Plane-wave gravitational tails and their physical interpretation have been studied by Harte, who derives the Lorenz-gauge Green function in a normal neighborhood. Here the propagation region is the entire globally hyperbolic Rosen strip with periodic transverse directions used in the calibrated experiment. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Calibrated spherical clock and source, Eqs. (4)–(7)](weak-curved.md) · [Harte, §IV](https://arxiv.org/abs/1309.5020v2)

## Retarded and advanced solutions

Use $g=-2\,du\,dv+\sum_{i=1}^2 a_i(u)^2 dx_i^2$, $a_1=\cosh(\kappa u)$, $a_2=\cos(\kappa u)$, with the strip closure inside $|\kappa u|<\pi/2$. Write $\rho=a_1a_2$ and $H_i=a_i'/a_i$. The transverse coordinate periods are $d_i$ and $v\in\mathbb R$. Let $P h=\nabla^c\nabla_c h_{ab}+2R_{acbd}h^{cd}$ on covariant symmetric tensors. Our convention gives $R_{uiui}=-a_i a_i''$. A source $f_{ab}$ is integrated against $\rho(s)\,ds\,dv'\,d^2x'$, so the kernel solves $P K=\rho(s)^{-1}\delta(u-s)\delta(v-v')\delta_{\mathbb T^2}(x-x')\,\mathrm{Id}$.

Put $\sigma=+1$ for the retarded and $-1$ for the advanced kernel, $U=\sigma(u-s)$, $V=\sigma(v-v')$, and $y=x-x'$. Transform distributions supported in $V\ge0$ with $e^{-pV}$, $\operatorname{Re}p>0$, including their full mass at zero. The inverse transverse transform is $(d_1d_2)^{-1}\sum_k e^{ik\cdot y}$ with $k_i=2\pi n_i/d_i$. On either covariant slot let $C_\mu$ act as minus the Christoffel matrix, summed over the two slots, so $D_\mu=\partial_\mu+C_\mu$. The only nonzero symbols are $\Gamma^i{}_{ui}=\Gamma^i{}_{iu}=H_i$ and $\Gamma^v{}_{ii}=a_i a_i'$ (no sum). Thus $C_v=0$. Contracting the connection on the derivative index gives the volume term in
$$
 P=-2D_u\partial_v-(\rho'/\rho)\partial_v
       +\sum_i a_i^{-2}(\partial_i+C_i)^2+2R\mathbin{\star},
 \qquad (R\mathbin{\star} h)_{ab}=R_{acbd}h^{cd}.
$$

In the following integrals evaluate the coefficients at $s+\sigma w$, $0\le w\le U$. Put $I_i(U)=\int_0^U a_i^{-2}\,dw$ and $b=\tfrac12\sum_i k_i^2 I_i$. The diagonal matrix $\Pi(w)$ multiplies a tensor component by $a_i(s+\sigma w)/a_i(s)$ for each transverse index $i$. This is parallel transport along the coordinate $u$ line. Define
$$
 N(w)=\Pi(w)^{-1}
    \left[\sum_i a_i^{-2}\big(2ik_i C_i+C_i^2\big)+2R\mathbin{\star}\right]\Pi(w).
$$
The full ten-component Fourier–Laplace kernel is
$$
 \widehat K_\sigma(U,p,k)=
 -\frac{\Theta(U)e^{-b/p}\,\Pi(U)}{2p\sqrt{\rho(u)\rho(s)}}
 \left[\mathrm{Id}+\sum_{m=1}^{4}\frac{1}{(2p)^m}
 \int_{0<w_1<\dots<w_m<U}N(w_m)\cdots N(w_1)\,d^mw\right].                 \tag{1}
$$
Integrating the transformed equation across $U=0$ gives $-2p\widehat K_\sigma(0+)=\mathrm{Id}/\rho(s)$. For $U>0$ the differential equation is
$$
 \partial_U\widehat K_\sigma=
 \left[-\sigma C_u-\frac{\sigma\rho'}{2\rho}
       +\frac{\sum_i a_i^{-2}(ik_i+C_i)^2+2R\mathbin{\star}}{2p}\right]\widehat K_\sigma.
$$
Factoring out $e^{-b/p}\Pi(U)/\sqrt{\rho(u)}$ gives the ordered series in (1). Assign grades $0,1,2$ to a $v$, transverse, and $u$ lower index respectively, and add the two grades. Each $C_i$ raises grade by one. Since $R_{uiui}$ and its symmetry partners are the only curvature entries, $R\mathbin{\star}$ raises it by two. Every product of five $N$'s is therefore zero. The formula involves no long-wavelength or small-curvature approximation.

On this symmetric wave the ordered integrals can also be evaluated algebraically. Use the parallel coframe $du,dv,a_i dx_i$ along $u$, in which $R_{uiui}=-a_i''/a_i=\mp\kappa^2$ is constant. Denote this curvature endomorphism by $R_0\mathbin{\star}$. On one covariant slot put $(J_i z)_u=z_i$, $(J_i z)_i=z_v$, with other entries zero; on a tensor sum the two slot actions. In this coframe $C_i=-a_i' J_i$. The $J_i$ commute with each other. Each $J_i$ preserves the metric and kills every two-form $du\wedge(a_j dx_j)$, so it commutes with the curvature endomorphism built from these two-forms. Define
$$
 L_i=\sigma(1/a_i(s)-1/a_i(u)),\qquad
 B_i=\int_0^U H_i^2\,dw=U\,a_i''/a_i-\sigma[H_i(u)-H_i(s)] .
$$
Express the input in that coframe at $s$ and the output in that coframe at $u$. Then the entire matrix $\Pi(U)[\cdots]$ in (1) is represented by
$$
 \sum_{m=0}^{4}\frac{1}{m!}\left(\frac{
  \sum_i(-2ik_i L_i J_i+B_i J_i^2)+2U R_0\mathbin{\star}}{2p}\right)^m .       \tag{1a}
$$
The identity follows by integrating commuting matrices. For example $I_1=\sigma[\tanh(\kappa u)-\tanh(\kappa s)]/\kappa$ and $I_2=\sigma[\tan(\kappa u)-\tan(\kappa s)]/\kappa$, so (1a) requires only the endpoint coordinates and the curvature scale.

## Inversion, contact terms and support

For each $k$ the inverse transform of $p^{-m-1}e^{-b/p}$ is
$$
 \Theta(V)\,(V/b)^{m/2}J_m(2\sqrt{bV}),\qquad
 b=0:\quad \Theta(V)V^m/m! .                                              \tag{2}
$$
Its power series follows by inverting each $p^{-m-j-1}$. For real $b,V\ge0$, the integer-order Bessel functions are bounded, and their series at zero gives $|J_m(z)|\le c_m z^m$ globally for $z\ge0$. Thus (2) is bounded by $c'_m V^m$, uniformly in $k$ and $U$. On compact $u,s$ intervals the integral coefficients in (1) grow at most like $(1+|k|)^4$. The torus sum converges on smooth test functions and grows at most polynomially in $V$ in this distributional sense. This proves the existence of its one-sided Laplace transform and its use in the differential equation, including on the characteristic face. Smooth tests have rapidly decaying Fourier coefficients, so the one-sided $U\downarrow0$ limit of the kernel is $-\Theta(V)\delta_{\mathbb T^2}(y)\mathrm{Id}/(2\rho(s))$. Its $V$ derivative supplies the corner delta in the jump. At $k=0$ the identity term gives a step and the curvature and connection terms give the powers in (2). In particular the zero Fourier mode in the transverse torus must be kept. Possible additions supported at zero real longitudinal frequency would be polynomials in $V$ on the whole line, incompatible with one-sided support.

Spatial inversion also shows the full causal support. For $U>0$ the Fourier inverse of $e^{-b/p}/p$ is a sum over lifted displacements $y^{(n)}=y+(n_1d_1,n_2d_2)$. Its term on each image is
$$
 \frac{e^{-p\Phi_n}}{2\pi\sqrt{I_1 I_2}},\qquad
 \Phi_n=\frac12\sum_i (y_i^{(n)})^2/I_i .                                 \tag{3}
$$
The polynomial in $ik$ in each ordered integral acts by spatial differentiation. Each extra $p^{-1}$ integrates once from the past in $V$. Hence every image is supported in $V\ge\Phi_n$. This inequality is the causal relation on that lift. The least possible $V$ is the minimum of $\tfrac12\int_0^U\sum_i a_i^2(\partial_w x_i)^2 dw$ at fixed displacement, attained at $\partial_w x_i=y_i^{(n)}a_i^{-2}/I_i$. Only finitely many images meet any compact observation and source set. At $U=0$ the distribution is fixed by (1)–(2) and transverse displacement vanishes. The source identity and these support properties identify the unique retarded and advanced inverses on the surrounding globally hyperbolic spacetime. [Distributional Green operators, Bär §4](https://arxiv.org/abs/1310.0738v2)

All ten components on one image have a short position-space expression on this symmetric wave. In the endpoint coframes of (1a) set
$$
 \Lambda_n=\exp\!\left(\sum_i\frac{y_i^{(n)} L_i}{I_i}J_i\right),\qquad
 C=U R_0\mathbin{\star}+\frac12\sum_i(B_i-L_i^2/I_i)J_i^2,\qquad z_n=V-\Phi_n .
$$
For $U>0$ the image contributes
$$
 K_{\sigma,n}=
 -\frac{\Lambda_n}{4\pi\sqrt{\rho(u)\rho(s)I_1I_2}}
 \left[\mathrm{Id}\,\delta(z_n)+ C\,\Theta(z_n)
                     +\tfrac12 C^2 (z_n)_+\right],\qquad (z)_+=\max(z,0).    \tag{3a}
$$
Indeed spatial Fourier inversion of (1a) differentiates the Gaussian (3). Equivalently its displacement on each transverse axis becomes $y_i^{(n)}-L_i J_i/p$. Expanding the resulting square gives $\Lambda_n$ and subtracts $L_i^2 J_i^2/(2pI_i)$ in the exponent. This substitution is a finite Taylor expansion in commuting nilpotent matrices. The remaining matrix exponential is $\mathrm{Id}+C/p+C^2/(2p^2)$ since $C$ raises grade by two. Inverting the three Laplace powers gives (3a). The image sum and the characteristic extension at $U=0$ use (1)–(3).

For $a_1=a_2=1$ all $N$ vanish. Every component has the flat scalar kernel times the identity. Formula (3) gives a single-image contribution $-\Theta(U)\delta(V-|y^{(n)}|^2/(2U))/(4\pi U)$ for $U>0$. In standard inertial coordinates this is the familiar $-\delta(t-t'-r)/(4\pi r)$ for the retarded inverse of $\Box=-\partial_t^2+\Delta$. For a spatially constant transverse source, integration over the lifted transverse plane gives $-\Theta(U)\Theta(V)/2$.

## One component behind the wavefront

Take an input covariant $11$ component, and read out $uu$. Put $H=H_1$, $L=\int_0^U H/a_1\,dw=\sigma(1/a_1(s)-1/a_1(u))$ and $\Delta H=H(u)-H(s)$. In (1) the single grade-two step from $11$ to $uu$ has integrand $-2H'/a_1(s)^2$, using $H'=a_1''/a_1-H^2$. The two grade-one steps pass through $u1$, with coefficients $-2ik_1 H/[a_1a_1(s)]$ and $-4ik_1 H/[a_1a_1(s)]$. Thus the scalar part of (1) is multiplied by $[-\sigma\Delta H/p-k_1^2L^2/p^2]/a_1(s)^2$. Applying (3) gives, on each image and for $U>0$,
$$
 (K_\sigma)_{uu\leftarrow11}=
 \frac{(\sigma\Delta H+L^2/I_1)\Theta(V-\Phi_n)
       -L^2(y^{(n)}_1/I_1)^2\delta(V-\Phi_n)}
      {4\pi a_1(s)^2\sqrt{\rho(u)\rho(s)I_1I_2}}.                         \tag{4}
$$
In particular the transverse zero mode is $\sigma\Delta H\,V\Theta(V)/(2a_1(s)^2\sqrt{\rho(u)\rho(s)})$. On the curved example $H'=\kappa^2/a_1^2$, so $\sigma\Delta H=\kappa^2 I_1>0$. The smooth coefficient inside the future cone is positive. For a flat metric written with affine positive scale factors, $L=a_1'I_1$ and $\sigma\Delta H=-(a_1')^2 I_1$. Its interior term cancels even in these non-inertial coordinates. A single $11$ point source generally fails conservation. Equation (4) concerns a component of the gauge-fixed inverse; a physical clock bracket requires the contraction with its full conserved current.

For a compact metric current $j^{ab}$ relative to invariant volume, lower its indices at the source and put $\mathcal T h=h-\tfrac12g\,\mathrm{tr}_g h$. With the Einstein–Hilbert action $(16\pi G_N)^{-1}\int R\,d\mathrm{vol}$ and covariant metric variations, the de Donder Hessian with the output indices lowered is $P\mathcal T/(32\pi G_N)$. The mixed bracket is $j[E_{\rm EH}f]$ with $E_{\rm EH}=32\pi G_N\mathcal T(K_+-K_-)$ on lowered sources. Skew adjointness in invariant volume defines $E_{\rm EH}j$ by duality. With $\Omega=\int\delta\pi\wedge\delta q$ and $\Omega(X_j,h)=j[h]$, the first-slot field is $X_j=-E_{\rm EH}j$. Applying this kernel to the calibrated spherical current gives the same smooth-probe measurement as the time-switched Einstein packet. Products of two singular currents and intrinsic boundary conditions for an isolated diamond remain separate proof gaps. [Probe convention](weak-domain.md) · [Clock packet and measured limit](weak-curved.md) · [Fewster and Hunt, gravitational propagator](https://arxiv.org/abs/1203.0261v4)

Run `python3 -B checks/weak_rosen_green.py` and `make check` from the repository root. The focused check compares the flat image and mode sums, integrates all ten columns of the tensor equation in both time directions, and tests the zero transverse mode and reciprocity. At $s=0.14$, $u=0.76$ and $\kappa=1$ the final line reads `Interior uu <- 11 coefficient: curved=0.07569275, flat affine=0.` [Executable calculation](../checks/weak_rosen_green.py)
