# A weak clock response on a closed spherical diamond

The mixed variation of the sharp clock excess at flat space has a regional weak Hamiltonian pairing. Its Cauchy data act as distributions on the **closed waist disk**. Equivalently, smooth the source inside the diamond, add the gravitational currents on the spacelike cap and incoming null sheet, and then take the limit. Both prescriptions give the clock Hessian on every smooth test solution extending to the boundary. This result uses the filled, two-tip Minkowski preparation, its common metric current and the vertex frame used for the clock. A curvature measurement at the waist shows why the open-diamond field alone need not determine such a pairing. [Chandrasekaran, arXiv:2611.34924v1, clock (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Flat-space clock Hessian](joint-flat-hessian.md)

## Smooth the source inside the diamond

Let the tips be at $(0,0)$ and $(2R,0)$. Write the open diamond as $O=\{(t,\mathbf x):|t-R|+|\mathbf x|<R\}$, its waist disk as $B_R=\{t=R,|\mathbf x|<R\}$, and its waist sphere as $S=\partial B_R$. For the clock formula set $R=1$. Fix a smooth reference perturbation $W$, the vertex tetrad and generator labels, and use the excess $D=\bar u_*-(1-a)M$ with cap fraction $0<a<1$. With $H_Y$ the trace-free conformal screen variation of a test $Y$, its Hessian is
$$
 T_W[Y]=d^2D(W,Y)
 =\frac14\left\langle\int_a^1 s(1-s)H'_W(s):H'_Y(s)\,ds\right\rangle .
$$
Here $\langle\cdot\rangle$ is the average over the marked sky. Write $\mathcal R_Y$ for the trace-free linearized optical tidal matrix in the parallel screen, with Jacobi equation $J''=-\mathcal R J$ in vacuum. Varying the round solution $J=sI$ gives $H'_Y(s)=-2s^{-2}\int_0^s u^2\mathcal R_Y(u)du$. Interchanging the integrals therefore gives
$$
 T_W[Y]=-\frac12\left\langle\int_0^1 u^2\mathcal R_Y(u):
 \left[\int_{\max(a,u)}^1\frac{1-s}{s}H'_W(s)\,ds\right]du\right\rangle . \tag{1}
$$
All factors are bounded on their integration intervals. Equation (1) acts on at most two derivatives of the spacetime test metric on the closed lower cone, including the segment from the vertex to the cap. Applying the tidal-curvature expression to arbitrary smooth tests defines a compact tensor distribution. Linearized curvature at flat space annihilates every infinitesimal diffeomorphism, so its metric source obeys $\partial_\mu T_W^{\mu\nu}=0$ distributionally. This supplies the gauge condition needed for a de Donder causal response. [Optical wave calculation](joint-flat-hessian.md) · [Fewster and Hunt, Theorems 4.7–4.8](https://arxiv.org/pdf/1203.0261#page=22)

For any such compact conserved source $T$ in $\overline O$, contract it toward $(R,0)$ by the affine map $x\mapsto (R,0)+(1-\epsilon)[x-(R,0)]$, $0<\epsilon<1$. Push forward each distributional component and convolve with a unit-mass smooth bump supported in $|\Delta t|+|\Delta\mathbf x|<\epsilon R/2$. The result $T_\epsilon$ is smooth, compactly supported in $O$, conserved and converges to $T$ as a distribution. The contraction scales every Cartesian derivative by the same constant, and differentiation commutes with convolution. Each $T_\epsilon$ therefore has a smooth gravitational response $X_\epsilon$ from the trace-reversed de Donder causal propagator. Fix its sign and Newton-constant normalization by $\Omega(X_\epsilon,Y)=T_\epsilon[Y]$ on a complete Cauchy surface. Causal convexity gives the identical propagator on $O$ for smooth compact interior sources. [Bär, Lemma 3.6](https://arxiv.org/pdf/1310.0738#page=12) · [Fewster and Hunt, symplectic pairing (4.23)](https://arxiv.org/pdf/1203.0261#page=24)

## A closed-disk pairing and its flux on the cap and sheet

At time $R$, a point causally related to $(t',\mathbf y)\in\overline O$ satisfies
$$
 |\mathbf x|\le |\mathbf y|+|R-t'|\le R . \tag{2}
$$
For each interior source $T_\epsilon$ the final inequality has a uniform positive margin. Its response has compact Cauchy data in $B_R$. For the sharp $T$, the metric Cauchy data of $X$ and their normal derivatives have distributional support in $\overline B_R$. They are well defined on this spacelike slice by duality with smooth wave evolution from test Cauchy data. The same duality gives convergence of the Cauchy distributions for $X_\epsilon$. The resulting canonical pairing takes the form
$$
 \Omega_{\overline B_R}(X,Y)
 =\langle\pi_X,h_Y\rangle-\langle h_X,\pi_Y\rangle
 = T[Y] . \tag{3}
$$
Here $h$ and $\pi$ are the linearized spatial metric and ADM momentum, with the first-slot convention above. Each distribution acts on any smooth extension of the indicated test data across the waist. Indeed two extensions agreeing in the open ball have the same jets of every order on its closure. A compact finite-order distribution supported there annihilates their difference. One can also take the limit of the ordinary compact-interior pairings for $X_\epsilon$, which agree before taking the limit. For a test smooth up to the closed, filled diamond, only a smooth extension of its jets is needed to evaluate $T[Y]$. The smooth identity on $O$ follows from Green's formula there and compact support of the interior source. No choice of exterior physical Cauchy data enters (3).

Let $\Sigma_C$ be a smooth spacelike initial cap and $N_{CS}$ the retained lower sheet from its rim $C$ to $S$. Use one smooth metric and common embeddings at the seams. For each $\epsilon$, the closed Einstein symplectic current and the volume between the joined surface and the waist give, with Cauchy orientations,
$$
 \int_{\Sigma_C}\omega(X_\epsilon,Y)+\int_{N_{CS}}\omega(X_\epsilon,Y)
 =\int_{B_R}\omega(X_\epsilon,Y)=T_\epsilon[Y] . \tag{4}
$$
There is no additional lateral hypersurface between these two surfaces with common waist. For surfaces ending at different exterior cuts, Stokes' formula adds the current through the intervening lateral face with its boundary orientation. At a common internal seam the opposite orientations cancel any shared cut term if one rewrites the same potential on both pieces. Because $X_\epsilon$ vanishes near $S$ on the waist slice, changing from the covariant to the ADM representative there introduces no term at finite resolution. [Iyer and Wald, symplectic current (44)–(45)](https://arxiv.org/pdf/gr-qc/9403028#page=9) · [Cap and sheet current](joint-adm.md) · [Relative flux between exterior cuts](radiative-flux.md)

Taking the limit of the **sum** in (4) gives (3) for every fixed smooth test. This limit is independent of the choice of smooth, conserved interior approximants converging to the given $T$ with common compact ambient support. It defines a joined pairing even when a characteristic face has no separate distributional trace. In particular it reproduces the two-packet tests of (1), with their mixed variations approaching $-3/4$ at $a=1/3$ in the specified normalization. The test perturbation is held smooth when removing the source regulator. Two simultaneously sharpening observables require further control. [Two-packet calibration](match-packets.md) · [A characteristic trace in a cylindrical vacuum model](joint-peierls.md) · [Two sharp readings](joint-resolution.md)

## Information lost by restriction to the open diamond

Put a marked curvature detector at $p=(R,0,0,R)\in S$ and consider $F_p[Y]=(R^{(1)}[Y])_{0x0x}(p)$. This observable is invariant under linearized diffeomorphisms at flat space and equals the indicated Weyl component on vacuum solutions. For every $(t,\mathbf x)\in O$ one has
$$
 |\mathbf x-R\hat z|\ge R-|\mathbf x|>|t-R| .
$$
The causal response to $F_p$ thus vanishes throughout the open diamond. Nonetheless the smooth transverse-traceless vacuum wave $h_{xx}=-h_{yy}=\cos(k(t-z))$, all other components zero, gives $F_p[h]=-\partial_t^2 h_{xx}(p)/2=k^2/2$. On the time-$R$ slice the response is supported at $p$. The closed-disk current (3) preserves this measurement. Any rule keeping only the open-diamond distribution identifies its response with zero. The example identifies an ambiguity in reconstructing general boundary observables from interior responses. Deciding the individual waist-supported terms of the clock requires its own source (1).

The regional result is a weak inverse for the flat clock **Hessian in a fixed direction** on smooth metric tests. A finite diamond with independently marked caps, boundary conditions that exclude the approximating solutions, or a physical corner two-form has a different Hamilton equation. In those ensembles one must specify the corner current, demonstrate tangency of the weak response and account for any separate frame variations. This is a proof gap for a general sharp-clock algebra and leaves the physical conjecture open. [v1, boundary embeddings (B.21)](https://arxiv.org/html/2611.34924v1#A2.E21) · [Two-frame reduction](match-reduction.md)

## A finite-width calibration

Restore $R=2$ and set $a=1/3$. For the static vacuum quadrupole with harmonic potential $\Phi=-3S_{ij}x^ix^j/8$, use $W_{00}=-2\Phi$, $W_{ij}=-2\Phi\delta_{ij}$, $W_{0i}=0$ and $S_{ij}=\operatorname{diag}(-1/2,-1/2,1)$. Its screen strain derivative is $sB$, where $B$ is the trace-free screen projection of $S_{ij}$ and $\langle B:B\rangle=3/5$. The sharp self-pairing is $(3/20)\int_{2/3}^2 s^3(2-s)ds=464/2025$. Each metric component is quadratic, so averaging over translations by the smoothing bump preserves its constant second derivatives. Composing this averaged test metric componentwise with the contraction multiplies its second derivatives by $(1-\epsilon)^2$. Since (1) uses only the linearized curvature with its weight held fixed, the smooth joined current on this test is **exactly $29/225$ at $\epsilon=1/4$**, for every unit-mass bump satisfying the support condition above. In the limit it recovers $464/2025$. [Metric source and exact quadrupole calculation](weak-tidal.md)

Run `python3 -B checks/weak_tidal.py` for the sharp reference value `Vacuum self-pairing: 464/2025`. Run `python3 -B checks/match_packets.py` for the separate packet test, which ends with `Limiting clock Hessian: -3/4`. The repository suite runs with `make check` and should exit successfully. [Quadrupole source check](../checks/weak_tidal.py) · [Packet check](../checks/match_packets.py)
