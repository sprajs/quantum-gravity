# The cap boost and the electric quadrupole

Tilting a spacelike cap about its fixed rim changes the angle in the gravitational joint action. The induced ADM data change at the same time. On a smooth vacuum cap with the usual ADM and joint potentials, these two contributions cancel against every constrained variation. An explicit quadrupole on a flat ball checks both signs. An independently marked normal frame obeys a different test. If its local boost charge is the area density, the Hamilton equation for a boost-invariant clock requires its flow to preserve that density. These statements constrain two proposed sources of the sharp clock response. [Venkatesa Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Spherical clock Hessian](joint-flat-hessian.md)

## Tangential momentum in the cap frame

Use the future cap normal $T$, the unit outward spatial normal $s$ of the initial ball, the outgoing null generator $\ell=e^u(T+s)$ and its partner $n=e^{-u}(T-s)/2$. Write $k=\mu/(8\pi G_N)$ for the positive area density, $K_{ij}=g(\nabla_iT,e_j)$ and $\omega_A=-n\cdot\nabla_A\ell$. Differentiating the null generator gives

$$
 u=\log(-T\cdot\ell),\qquad
 j_A=k K_{As}=k(\omega_A-\partial_A u).
 \tag{1}
$$

A rescaling $\ell\mapsto e^\beta\ell$ adds $d\beta$ to $\omega$ and $\beta$ to $u$. Their difference in (1) is the angular momentum in the specified cap frame. Its normalization follows directly by integrating $\int_\Sigma\pi^{ij}\mathcal L_Vh_{ij}$ by parts on the cap momentum constraint for $V$ tangent to its rim. The boundary term is $2\int_C (\pi^{ij}/\sqrt h)s_i V_j\,\mu=\int_C j(V)$ for $\pi^{ij}=\sqrt h(K^{ij}-Kh^{ij})/(16\pi G_N)$. [Cap normal, v1 (3.12)](https://arxiv.org/html/2611.34924v1#S3.E12) · [Optical and cap matching](joint-edges.md)

In a chosen null-frame section, a tangential displacement $V$ and vertical rapidity rate $b$ have one-sided charge $H(V,b)=\int_C k[\omega(V)+b]$, up to the orientation of the endpoint. The coordinate vector fields $V+b\partial_t$ on the bundle of normal rapidities $t$ have bracket $([V,W],V(c)-W(b))$ with $W+c\partial_t$. This is the Lie algebra of angular diffeomorphisms acting on local boosts. If the two frame sections obey $\ell_+=e^\lambda Y^*\ell_-$, the fibre coordinates for the same normal obey $t_+=Y^*t_- -\lambda$. A common bundle displacement therefore has $V_-=Y_*V_+$ and $b_+=Y^*b_--V_+(\lambda)$. Metric and normal-connection matching give $k_+=Y^*k_-$ and $\omega_+=Y^*\omega_-+d\lambda$. Substitution cancels the two oppositely oriented charges pointwise after pullback, even for angle-dependent $\lambda$. Relative comparison maps between independently marked cuts can instead have momenta. [V1, (3.61)–(3.66)](https://arxiv.org/html/2611.34924v1#S3.E61) · [One-sided angular potential](rim-potential.md)

The same cancellation can be seen using the cap potential. Choose the sign giving $+\int j(V)$ for the ADM cap and $-\int k\omega(V)$ for the adjacent sheet. In this orientation (A.18) gives $-\int_C u\,Dk$, where $D$ varies the pulled-back density. Under a common angular relabeling $Dk=\mathcal L_Vk$. The two angular pieces sum to $-\int_C kV(u)$, and $-\int_C u\mathcal L_Vk=+\int_C kV(u)$ on the closed cut. Reversing the entire orientation reverses all three terms. This is one accounting of the frame transport in the previous paragraph. In a fixed marked chart the genuine variation of the joint is $\Omega_{\rm joint}=-\int_C Du\wedge Dk$. [Outer-cut potential, v1 (A.18)](https://arxiv.org/html/2611.34924v1#A1.E18) · [Moving pullbacks, v1 (3.40)](https://arxiv.org/html/2611.34924v1#S3.E40)

## An actual cap tilt about the rim

Take the cap to be a Euclidean ball at constant Minkowski time $t_0$, with $T=\partial_t$ and background $\ell=T+s$ at its rim $C$. Deform it to the graph $t=t_0+\tau N(x)$ at fixed spacetime metric, keeping $N|_C=0$. The normal derivative $f=\partial_s N|_C$ can be any smooth function on the sphere. The tangent $B=\partial_\tau|_0$ fixes the rim, the sheet and its null frame. The future normal changes by $f s$ on $C$, so $D_Bu=-f$. On the ball,

$$
 D_Bh_{ij}=0,\qquad
 D_B\pi^{ij}=(\partial_i\partial_jN-\delta^{ij}\Delta N)/(16\pi G_N).
$$

Let $p_{ij}=D_X h_{ij}$ for any allowed linearized vacuum variation in the cap chart. At this time-symmetric flat background the Hamiltonian constraint is $\partial_i\partial_j p_{ij}-\Delta p_{ii}=0$. Take $\Omega=D\Theta$ and evaluate the test $B$ in the second slot. Integrating twice by parts and using $N|_C=0$ gives

$$
 \begin{aligned}
 \Omega_{\rm ADM}(X,B)
 &=-\frac1{16\pi G_N}\int_\Sigma
       (\partial_i\partial_jN-\delta_{ij}\Delta N)p_{ij}\,d^3x \\
 &=\frac1{16\pi G_N}\int_C f(p_{ii}-p_{ss})\,\mu
 =\int_C f D_Xk, \\
 \Omega_{\rm joint}(X,B)&=-\int_C fD_X k .
 \end{aligned}\tag{2}
$$

The null sheet has zero variation along $B$ in this calculation. Thus the slope of an actual flat cap, with its usual ADM potential and (A.18), supplies zero total pairing on these tests. The normal-connection matching is also preserved: $D_B K_{As}=\partial_A f$ and $\partial_A D_Bu=-\partial_A f$. Equations (1) and (2) use the same geometric cap normal. Adding a separate boost charge for this graph deformation would require specifying an additional frame or modifying the potential. [Cap joint, v1 (A.18)](https://arxiv.org/html/2611.34924v1#A1.E18) · [Extended gravitational potential, v1 (B.21)](https://arxiv.org/html/2611.34924v1#A2.E21)

The cancellation extends to a curved vacuum cap. Use zero shift and a smooth lapse $N$ vanishing on $C$. Let $B_N$ be the deformation of the cap by $NT$ along the same solution, and $H[N]$ the bulk ADM Hamiltonian constraint smeared by this fixed lapse. In $D_XH[N]$ the algebraic terms in $h,\pi$ and the cosmological constant give no boundary integral. Only $-(16\pi G_N)^{-1}\int_\Sigma N\,R[h]\sqrt h$ contains derivatives of $p_{ij}=D_Xh_{ij}$. Their combination is $\nabla^i\nabla^j p_{ij}-\nabla^2(p^i{}_i)$. After integrating by parts, $N|_C=0$ leaves the boundary integral $-\int_C fD_Xk$, $f=s^i\nabla_iN$. The volume variation is $\Omega_{\rm ADM}(X,B_N)$ by the ADM evolution equations. Since $X$ obeys the linearized constraints, $D_XH[N]=0$. At the fixed rim, $D_{B_N}T=\nabla_\Sigma N=f s$, $D_{B_N}u=-f$, and $D_{B_N}k=0$. Equation (2) follows with the same signs. Only the lapse is held fixed in the Hamiltonian variation. The coefficient $f$ is evaluated in the background cap geometry. This argument concerns a geometric change of slicing with unchanged sheet and no additional normal-frame variables. [Arnowitt, Deser and Misner, canonical evolution](https://arxiv.org/abs/gr-qc/0405109) · [Cap joint, v1 (A.18)](https://arxiv.org/html/2611.34924v1#A1.E18)

There is also a direct way to lift a deformed, area-selected rim when the cap collar is free. Prescribe $e^u=a_0(y)>0$ in the vertex-normalized null frame and put $T=\ell/(2a_0)+a_0 n$, $s=\ell/(2a_0)-a_0 n$. For inward distance $z\ge0$, the spacelike collar $\exp_{C(y)}[-z s(y)]$ has normal $T$ at the rim. A smooth cutoff of the infinitesimal change extends the collar variation into the original ball. Each fixed smooth wave admits this construction near the flat solution. The cap and sheet inherit their geometric data from the same spacetime, and $D_Zu=0$ for this lift. A prescription fixing the cap by additional physical data needs its own tilt calculation.

## What a separately measured boost could detect

Suppose an external normal-frame angle $g(y)$ survives with a pure boost $B_f$ shifting $g$ by arbitrary smooth $f$ and obeying $\Omega(X,B_f)=\int_C fD_Xk$. This moment-map identity specifies what it means here for the independent boost to carry the area charge. If this motion preserves the capped clock $U$ and $X_U$ solves $\Omega(X_U,\cdot)=dU$, then $D_{X_U}k=0$ pointwise. If only some boost profiles act, this identity holds against those profiles. The affine clock $p_C(u_S-u_C)$ is invariant under recalibration of the affine normal, and an independent cap tilt at fixed rim and fixed rays also leaves it unchanged. A frame transformation moving one of the physical cuts needs a separate test of invariance. [V1 clock (3.27)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Area and relative boosts at $S$, v1 (3.64)](https://arxiv.org/html/2611.34924v1#S3.E64)

For the clock excess critical at the flat solution, choose a regular reduction and differentiate a proposed smooth Hamiltonian assignment in the fixed wave direction $W$. Its derivative $X$ also has $D_Xk=0$ there, since the assignment vanishes at the critical point. In the spherical pulse $Z_\eta$, $D_Z k=a^2D_Z k_S\to0$ in the marked chart by the area-ratio condition and the small waist displacement. Consequently a surviving *isolated* term $\int_C Dk\wedge Dg$ paired with $(X,Z_\eta)$ tends to zero, even for nonzero $D_Zg$. The one-sided $D_Z\omega\to dP_2/2$ can still be measured in a frame with fixed $u$. A common displacement cancels between the two faces. A relative angular motion preserving the matched round metric up to normal motion must be conformal Killing and has zero pairing with $dP_2$, since its divergence is zero or a first harmonic. These conclusions apply to the specified common geometry and boost charge. A different mixed term for independently anchored frames would have to survive the full constrained gravitational reduction and provide the missing clock Hessian of $-1/30$ on the specified wave. Against a second family of wave profiles, boundary terms with finitely many independent linear responses in this harmonic cannot supply every required pairing on the stated smooth reduction. [Packet and rank tests](match-packets.md) [Spherical wave and waist estimates](joint-flat-hessian.md) · [Electric angular charge and metric matching](joint-angular.md)

## Reproduce the two cancellations

Set $G_N=1$ and take the unit ball. For the common angular test use $u=Q=P_2(\cos\theta)$ and $V=\nabla Q$. For the cap tilt take $S=\operatorname{diag}(-1/2,-1/2,1)$, $p_{ij}=2S_{ij}$ and $N=(r^2-1)(x^iS_{ij}x^j)/2$. Then $f=Q$ and $D_Xk=-kQ$. The script integrates the polynomial ADM volume and joint area terms separately. Run `python3 checks/match_boost.py` from the repository root. The expected output is

~~~text
Common angular displacement: -3/5 + 3/5 = 0
Geometric cap tilt (ADM and joint): -1/10 + 1/10 = 0
~~~

Run `make check` for the full suite. [Executable check](../checks/match_boost.py)
