# The weak Einstein field of the spherical cap clock

A smooth vacuum perturbation $W$ of a round Minkowski diamond changes the shear seen by an emitter. The mixed response of the sharp clock to a second perturbation is a weighted integral of its linearized Weyl tensor over the emitter's light cone. Both gravitational polarizations and the entire sky enter the integral. The adjoint curvature operator then gives a conserved metric source, and the Minkowski causal propagator gives its weak Hamiltonian field. The construction is for the mixed derivative of the vacuum clock excess on a marked global continuation. It applies to the raw clock when the preparation fixes the weighted waist radius. [Venkatesa Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Flat Hessian](joint-flat-hessian.md)

## The moving physical cuts

Use signature $(-,+,+,+)$ and the flat tips $(0,\mathbf0)$ and $(2R,\mathbf0)$. The lower cone consists of $x(s,n)=s k$, with $k=(1,n)$ for $n\in S^2$. Use the emitter's orthonormal sky, $\langle\,\cdot\,\rangle=\int d\Omega/(4\pi)$, and calibrate the affine parameter by $-k\cdot V=1$ for its unit velocity $V$. Specify the perturbed observer and its frame smoothly, carrying the marks under a diffeomorphism. Let $\rho(s)=\sqrt{\det J(s)}$ be the area radius per physical solid angle for a regular-vertex Jacobi map. Write $S(n)$ and $C(n)$ for the affine waist and cap distances. The return cone picks $S$, and $\rho(C)=a\rho(S)$, $0<a<1$, picks $C$. Both conditions are regular near the flat experiment. The flat squared-interval function from the future tip, divided by two and evaluated on the lower ray, equals $2R(s-R)$; its derivative $2R$ gives transversality. At the flat cap $\partial_s\rho=1$. Smooth ODE dependence, regular vertex data and compactness of the sky keep the Jacobi map nonsingular away from its vertex and the cuts smooth for sufficiently small smooth variations. If $M=\langle\rho(S)^2\rangle/\langle\rho(S)\rangle$ is held fixed, its flat derivative in the return proper time is $1/2$, so this last adjustment is also regular. [v1, cap condition (3.18)](https://arxiv.org/html/2611.34924v1#S3.E18) · [Derivatives of the moving cuts](joint-jacobi.md)

Let $D=\bar u_*-(1-a)M$. On each ray $u_*=\rho'(C)(S-C)$. Taylor's formula with integral remainder and the vacuum Raychaudhuri equation give
$$
 u_*-(1-a)\rho(S)
 =-\int_C^S(S-s)\rho''(s)\,ds
 =\tfrac12\int_C^S(S-s)\rho(s)\,\sigma^A{}_B\sigma^B{}_A\,ds .
$$
The sky average for $D$ weights each ray by $\rho(S)/\langle\rho(S)\rangle$. In the flat experiment the background shear vanishes at every point. Thus the integrand and its first variation both vanish, including at the moving limits. Derivatives of either cut, of the observer-dependent weights, and of the weight inside the integral multiply these zeros at second order. The two first shear variations give the entire Hessian. With $c=aR$, $H_h$ the variation of the determinant-one screen metric, and a prime now denoting the **dimensional affine derivative** $\partial_s$, the shear variation is $H'_h/2$. For smooth vacuum solution tangents $W,Z$,
$$
 {\cal L}_W[Z]=d^2D_{\rm flat}(W,Z)
 =\tfrac14\left\langle\int_c^R s(R-s)H'_W(s):H'_Z(s)\,ds\right\rangle . \tag{1}
$$
A radial or angular shift of the perturbed marks does not affect the linearized shear about this shear-free experiment. A common smooth cap and sheet supply their shared metric at the physical cut. No metric test is required to vanish there or at the waist. An independently dynamical cap, with its own evolution or boundary conditions, would require its own symplectic inverse.

## Jacobi transport and the adjoint curvature operator

Choose parallel orthonormal screens $e_A=(0,\mathbf e_A)$ locally on the sky. Tensor contractions patch across choices of the screen basis. Adopt $J''=-R_{\cdot k\cdot k}J$, with $J(0)=0$ and $J'(0)=I$. In flat space $J=sI$, so the linearized trace-free part obeys $\delta J''{}^{\rm TF}=-s\, C^{(1)}_{\cdot k\cdot k}[h]$. The Ricci part of $R_{AkBk}$ is $\delta_{AB}R_{kk}/2$. It drops out for an arbitrary smooth spacetime metric test $h$. Motion of the ray and its parallel screen in the curvature contraction multiplies the zero background curvature. Since $H_h=2(\delta J)^{\rm TF}/s$ in the emitter sky, the regular-vertex solution is
$$
 H'_h(s)=-\frac{2}{s^2}\int_0^s t^2 C^{(1)}_{\cdot k\cdot k}[h](tk)\,dt .
 \tag{2}
$$
Interchanging the order of integration defines a continuous extension of (1) to every smooth $h$ near the cone,
$$
 \begin{aligned}
 {\cal L}_W[h]&=\left\langle\int_0^R K_W^{AB}(t,n)\,
                             C^{(1)}_{AkBk}[h](tk)\,dt\right\rangle ,\\
 K_W^{AB}(t,n)&=-\frac{t^2}{2}\int_{\max(c,t)}^R
                    \frac{R-s}{s}\,H'_W{}^{AB}(s,n)\,ds .
 \end{aligned} \tag{3}
$$
Curvature below the cap contributes through the shear transported to the rim. Equation (3) specifies a representative on off-shell tests. The geometric clock on arbitrary nonvacuum metrics has an additional Ricci focusing term. Equation (1) identifies the physical mixed derivative on vacuum tangents, for which the representative suffices.

Define $P_A^{\alpha\mu}=e_A^\alpha k^\mu-k^\alpha e_A^\mu$. For every fixed ray,
$$
 K^{AB}C^{(1)}_{AkBk}[h]
 =-\tfrac12 K^{AB}P_A^{\alpha\mu}P_B^{\beta\nu}
                     \partial_\alpha\partial_\beta h_{\mu\nu}.
$$
Here and below $K=K_W$. The symmetric tensor distribution, with respect to Cartesian $d^4x$, is therefore
$$
 J_W^{\mu\nu}(x)=-\tfrac12\partial_\alpha\partial_\beta
     \left\langle\int_0^R K^{AB}P_A^{\alpha\mu}P_B^{\beta\nu}
                                  \delta^{(4)}(x-tk)\,dt\right\rangle ,
 \qquad {\cal L}_W[h]=\langle J_W,h\rangle . \tag{4}
$$
Its support lies on the compact truncated cone and its distributional order is at most two. Symmetry follows by exchanging $(A,\alpha)$ and $(B,\beta)$. Antisymmetry of $P_A^{\alpha\mu}$ gives $\partial_\mu J_W^{\mu\nu}=0$ on the entire spacetime, including the cuts. Also $\eta_{\mu\nu}P_A^{\alpha\mu}P_B^{\beta\nu}=\delta_{AB}k^\alpha k^\beta$ and $K$ is trace-free, so $\eta_{\mu\nu}J_W^{\mu\nu}=0$. Thus pure diffeomorphisms and infinitesimal conformal rescalings have zero pairing. The construction treats arbitrary $h_{00},h_{0i},h_{ij}$ and arbitrary angular dependence.

## The metric term at the rim

Let $\partial_A=e_A^\mu\partial_\mu$ act in Cartesian coordinates on the metric with the contracting vectors $k,e_A$ held fixed. This is distinct from differentiating the basis on the sky. Integrate the $\partial_k=d/dt$ derivatives in (4) along each ray. Extending $K$ by zero outside $[0,R]$ gives $K=K'=0$ at the vertex and the waist. Its value is continuous at $c$ and its derivative jumps by
$$
 [K']_c=\tfrac12 c(R-c)H'_W(c).
$$
With $K''_{\rm pw}$ the ordinary second derivative on the two open intervals, one obtains
$$
 {\cal L}_W[h]=-\tfrac12\left\langle
 \int_0^R \left(K^{AB}\partial_A\partial_B h_{kk}
      +2K'{}^{AB}\partial_A h_{Bk}+K''_{\rm pw}{}^{AB}h_{AB}\right)dt
       +[K']_c^{AB}h_{AB}(ck)\right\rangle . \tag{5}
$$
The coefficient of the explicit metric evaluation is $-c(R-c)H'_W(c)/4$. There is no radial-integration endpoint term at $R$ or $0$. The split (5) displays derivatives left on the tests. The separate terms depend on gauge, and derivatives on the sky cannot be applied to a frozen screen basis as if it were constant over the sphere. The covariant quantity is their sum. If $H'_W$ has a zero of finite order at $c$, the first nonzero jump moves to a higher derivative of $K$. If $H'_W$ vanishes to all orders, $K$ is smooth across $c$. For a reference with a fifth-order zero, two separated packets detect the higher-order jump even with unchanged local data at the rim. [Two-packet experiment](match-packets.md)

## The causal field and its sign

Take the ordinary Einstein symplectic form on a complete Minkowski Cauchy plane with $\Omega=\int\delta\pi^{ij}\wedge\delta q_{ij}$, $K_{ij}=\partial_tq_{ij}/2$ in unit lapse and zero shift, and $\Omega(X_W,Z)={\cal L}_W[Z]$. Use $P=\partial_t^2-\Delta$, $E_P=G_{\rm ret}-G_{\rm adv}$ for $P$. In de Donder gauge the Einstein–Hilbert Hessian with covariant metric variations is $P_{\rm EH}h=\Box\bar h/(32\pi G_N)$, where $\Box=-P$ and $\bar h=h-\eta\,\mathrm{tr}(h)/2$. This follows from $-\delta G^{\mu\nu}/(16\pi G_N)$ and $\delta G_{\mu\nu}=-\Box\bar h_{\mu\nu}/2$. Equation (4) is already trace-free and conserved. Consequently a de Donder representative of the weak first-slot Hamiltonian field is
$$
 X_{W,\mu\nu}=32\pi G_N E_P J_{W,\mu\nu}
             =-E_{\rm EH}J_{W,\mu\nu},\qquad
 E_P(\tau,\mathbf z)=
 \frac{\delta(\tau-|\mathbf z|)-\delta(\tau+|\mathbf z|)}
      {4\pi|\mathbf z|}. \tag{6}
$$
Here $E_{\rm EH}$ is the retarded minus advanced inverse of the gauge-fixed Einstein–Hilbert Hessian. To calibrate the sign, a transverse trace-free spatial source $j_{ij}(\mathbf x)\delta(t)$ produces $X_{ij}(0)=0$, $\dot X_{ij}(0)=32\pi G_N j_{ij}$. The first-slot ADM pairing at that instant is $\int j^{ij}Z_{ij}d^3x$. For general conserved smooth sources Green's identity gives the same normalization on smooth solutions modulo gauge. For (4) one can convolve with a compact smooth spacetime mollifier, preserving both Ward identities, and take the limit by distributional duality. Equivalently, for any compact smooth conserved $f$, the mixed Peierls bracket in this order is
$$
 {\cal L}_W[E_{\rm EH} f]=-\langle f,E_{\rm EH}J_W\rangle
                         =\langle f,X_W\rangle .
$$
The causal operator acts on compactly supported distributions. Its output solves the homogeneous linearized equations distributionally, with spacelike-compact support. The Cauchy pairing can use spacelike restrictions because the wave equation allows only null singular covectors. The mixed bracket already follows by testing a smooth wave; no product of distributions on a characteristic cut occurs. [Fewster and Hunt, §§3–4](https://arxiv.org/pdf/1203.0261#page=15) · [Bär, Lemma 4.1 and Theorem 4.3](https://arxiv.org/pdf/1310.0738#page=18)

For a spacelike-compact TT packet $Z_\eta$ of the one-third-radius experiment, choose a smooth time step $\chi$ which is zero early and one late. Then $f_\eta=P_{\rm EH}(\chi Z_\eta)$ is a compact smooth conserved TT source. Time multiplication preserves the de Donder condition because $Z_{0\mu}=0$. Its retarded and advanced solutions are $\chi Z_\eta$ and $(\chi-1)Z_\eta$, so $E_{\rm EH} f_\eta=Z_\eta$. The known limits $-1/30$ and, with the separately calibrated two-packet reference, $-3/4$ are therefore smooth-source probes of (6). Their Cauchy data converge distributionally to zero while their pairings survive. In each such direction a smooth representative for this mixed response is excluded. At flat space itself the first derivative of $D$ is zero. The result concerns the derivative of the field there and leaves nonlinear sharp-clock flows, brackets of coincident singular observables, and the isolated cap phase space open. [Single-packet normalization](joint-flat-hessian.md) · [Two-packet normalization](match-packets.md)

## Exact check

Set $R=2$, $c=2/3$, $S_{ij}=\operatorname{diag}(-1/2,-1/2,1)$ and let $B$ be its trace-free screen projection. The static linearized vacuum metric $W_{00}=-2\Phi$, $W_{ij}=-2\Phi\delta_{ij}$, $W_{0i}=0$, with $\Phi=-3S_{ij}x^ix^j/8$, has harmonic potential and screen Weyl tensor $-3B/2$. It gives $H'_W=sB$ and $K=-t^2(R-\max(c,t))^2B/4$. Pairing the reference with itself gives the vacuum Hessian $464/2025$ in each representation. No falloff of this reference is needed outside the sampled region. For the smooth off-shell test $h_{ij}=t^3 S_{ij}$, $h_{0\mu}=0$, the Weyl contraction is $-3tB$ and $H'_h=3s^2B/2$. Equations (1), as extended by (2), (3) and (5) can all be integrated exactly since $\langle B:B\rangle=3/5$. A second test sets $h_{\mu\nu}=2\partial_{(\mu}\xi_{\nu)}$, with $\xi_0=t^3 S_{ij}x^ix^j$, $\xi_i=t^2S_{ij}x^j$. Each of the three terms in the metric integrand contributes. The rim alone pairs nontrivially with this pure gauge. One may cut each test off smoothly outside a neighborhood of the compact cone.

Run the following command from the repository root. The three rational values in the second output line must agree, and the final pure gauge pairing must vanish. Run the full suite with `make check`. [Executable calculation](../checks/weak_tidal.py)

```sh
python3 -B checks/weak_tidal.py
```

```text
Vacuum self-pairing: 464/2025
Jacobi, Weyl and metric pairings: 2864/6075, 2864/6075, 2864/6075
Metric rim term: -32/1215
Pure gauge pairing: 0 (rim alone: -32/405)
```
