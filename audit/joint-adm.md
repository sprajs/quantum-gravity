# What the spacelike cap supplies on a spherical light cone

The cap can supply a nonzero boundary contribution to a shear test. On a spherical null cone that extends to a regular vertex, its gravitational symplectic current has a particularly simple evaluation. It equals the current on the discarded segment of the same cone. The two sides of the artificial division cancel their shear trace for every smooth jointly matched variation. The *capped clock* retains that trace. This gives a range obstruction for the metric current with a common embedding and fixed endpoint frames. An independently marked cap can have additional surface charges. [Chandrasekaran, arXiv:2611.34924v1, (3.18)–(3.19)](https://arxiv.org/html/2611.34924v1#S3.E18) · [Metric potential (A.6)](https://arxiv.org/html/2611.34924v1#A1.E6)

## Fill the past of the cap

Let the expanding incoming sheet be part of a smooth vacuum light cone from a point, free of caustics through the waist $S$. Choose a spacelike initial ball $\Sigma$ whose boundary $C$ is at $v=b$, $0<b<1$, and whose past domain of dependence is bounded by the segment $N_<$ of that cone. Write $N_>$ for its retained segment, from $C$ to $S$. For fixed reference embeddings use the metric current $\omega=D\theta$ of (A.6). Use one smooth pullback through the cap–sheet joint and fix the generator labels and external normal frames. Equivalently the following calculation tests the part of the pairing obtained by integrating that current. Independent surface fields enter separately.

Let $X,Y$ be smooth linearized vacuum solutions on the filled region. With Cauchy orientations, conservation of $\omega$ gives
$$
 \int_\Sigma\omega(X,Y)+\int_{N_>}\omega(X,Y)
 =\int_{N_<\cup N_>}\omega(X,Y).
 \tag{1}
$$
The shrinking sphere at the regular vertex gives no current contribution. The left cap integral is the covariant representative of the ADM pairing. Rewriting it as $\int_\Sigma D\pi^{ij}\wedge Dh_{ij}$ requires keeping the cut term produced by that change of potential. Counting (A.18) twice would change (1). The cap metric and momentum satisfy the linearized Hamiltonian and momentum constraints. One way to cover the filled region for a candidate smooth $X$ is to evolve its cap Cauchy data backwards in a hyperbolic gauge. An arbitrary smooth extension of the initial data outside the ball suffices locally for the reduced hyperbolic equations. Constraint propagation and domain of dependence determine the vacuum perturbation inside. The background and its backwards development must be regular on the region used in (1). [Cap potential (3.46)](https://arxiv.org/html/2611.34924v1#S3.E46) · [Joint (A.18)](https://arxiv.org/html/2611.34924v1#A1.E18) · [Metric symplectic current on a null sheet](rim-potential.md)

Spherical regularity permits nonzero shear at the rim. For example, in the exact vacuum plane wave $ds^2=-2du\,dw+dx^2+dy^2+(x^2-y^2)du^2$, the Jacobi lengths on the axial ray from a point are $\sinh u$ and $\sin u$. Their logarithmic derivatives $\coth u$ and $\cot u$ differ at every sufficiently small positive $u$. Shear therefore persists on an open patch of the spherical light cone, well before a caustic. A small causally convex diamond has regular cuts on both branches. This example verifies the background hypothesis in a vacuum geometry. [Point-cone Jacobi calculation](03-2.md)

## A trace in the clock and its absence in the smooth pairing

Work first at fixed pointwise $\rho_S$ and generator labels. In an orthonormal polarization frame parallel transported along the generator, use the area-weighted perturbations $X=\rho_S v\,\delta_X z$, $Y=\rho_S v\,\delta_Y z$. The right side of (1) in this block is, with increasing-$v$ orientation and $c=(16\pi G_N)^{-1}$,
$$
 c\int_S\epsilon_0\int_0^1(X'\cdot Y-Y'\cdot X)\,dv.
$$
Choose $Y_d=B(y)\phi((v-b)/d)$ with $\phi\in C^\infty_c(\mathbb R)$ supported in $[-1,1]$ and $\phi(0)=1$. Take $B$ to be a smooth polarization section and $d<\min(b,1-b)$. For smooth $X$, integration by parts on the *whole* interval gives $2c\int X'\cdot Y_d=O(d)$. On the two intervals separately the $-Y_d'\cdot X$ term yields opposite evaluations at $C$. Retaining the spacelike cap therefore changes the boundary equation for a smooth metric variation.

The same estimate allows a smooth $X$ that changes $\rho_S$, in a chart with fixed angular labels and endpoint frames. The fixed-label sheet potential is proportional, modulo endpoint and field-exact terms, to $P-E\,D(\rho_S^2)$ of the [metric calculation](rim-potential.md). Its differential against $Y_d$ has only smooth coefficients multiplying $Y_d$ and its first radial derivative near $C$. Integrating the latter by parts over the whole cone gives $O(d)$ again. The singular area chart at the vertex does not enter the collar integral.

In the same variables let $T$ be the transported background $z'$, $K(v)=\int_v^1e^{\Xi(s)}ds$ with $\Xi$ integrated from $b$, and $w(y)=\rho_S(y)/\int_S\rho_S\epsilon_0$. The capped, angularly averaged clock has the limit
$$
 \lim_{d\downarrow0}D\bar u_*[Y_d]
 =-\tfrac12\int_S w(y)K(b,y)\,T(b,y)\cdot B(y)\,\epsilon_0 .
 \tag{2}
$$
Indeed its differential is the mean of $\tfrac12\int_b^1 KT\cdot(Y_d'-Y_d/v)dv$. Integration by parts on $[b,1]$ leaves (2) and a smooth integral of size $O(d)$. Choosing $B$ proportional to $T(b)$ with a nonnegative localization gives a strictly negative limit wherever the initial shear is nonzero on an open set. The clock uses a new affine slope at $C$ after the initial cone is truncated. [Clock (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Differential in transported coordinates](endpoint-inverse.md)

Consequently, on any such common-embedding phase space admitting these characteristic variations and having (1) as its pairing with them, the capped clock has **no smooth Hamiltonian vector** at a sheared rim. This tests an angularly averaged clock and includes the constrained cap current. It does not require an orthogonal endpoint identification or an assumption that $X$ vanishes on the cap. Characteristic radiation supported away from the regular vertex preserves the vertex compatibility conditions. Applying the conclusion to a prescribed finite diamond requires development of those data through both caps and satisfaction of its boundary and frame conditions. Local characteristic existence supplies smooth vacuum developments near suitable data; it does not define the physical surface charges. [Vacuum characteristic existence](https://arxiv.org/abs/1209.1971)

In the fixed-density full-cone test, a distributional inverse would instead have $2c\,\partial_vX$ equal to the bulk source plus the delta density of (2), using the distributional extension of the displayed whole-cone pairing. The coefficient of the delta fixes the jump of $X$ across $C$. Such a jump is outside the smooth matched metric tangent space. In cap canonical coordinates a rim momentum measure can likewise reproduce a trace against $Dh_{AB}$. Its tangency to the vacuum constraints and its brackets would require a new domain.

## Which angular and frame variations could change the result?

For a common displacement of the two faces, the $Q_\chi$ integrals of (B.21) have opposite orientations at $C$ when they use the same spacetime extension of $\chi$. Each individual integral can be nonzero. For an independently varied cap frame, (A.18) contains $D\log(-n_C\cdot\ell)\wedge D\mu_C$. Setting $D_Y\mu_C=0$ leaves the contraction $D_Y\log(-n_C\cdot\ell)D_X\mu_C$. An independent marked angular identification also contributes the variation of its angular momentum against the angular displacement of $X$. Both terms require the actual matching map. [Extended potential (B.21)](https://arxiv.org/html/2611.34924v1#A2.E21) · [Angular charge and its constraint](rim-potential.md)

There is a spherical reason to retain the last possibility. In an orthonormal polar dyad on the round sphere,
$$
 (D_A D_B P_2(\cos\theta))^{\rm TF}
 =\tfrac32\sin^2\theta\,
 (e^\theta_Ae^\theta_B-e^\varphi_Ae^\varphi_B).
$$
Thus the test polarization below occurs in the trace-free metric change generated by a smooth angular gradient. This identity alone does not show that an angular displacement solves the joint equation. It explains why the allowed relative displacement, its divergence and its charge must be checked even for an axisymmetric test. To settle the full v1 bracket one must evaluate these surviving terms against $Y_d$, along with the other Hamilton equations, or prove that the coupled phase space admits (1) as its entire pairing on these tests. This is a **proof gap** for the four-dimensional finite-diamond construction.

## Reproduce a spherical calculation

Use $\rho_S=1$, $b=1/2$, $a=\sin^2\theta$, and in the polar dyad put $z^2=0$, $z^1=2a\log(v/b)$ from a collar below $b$ to $S$. Extend this radial function smoothly to zero in a neighborhood of the vertex. Its polarization tensor extends smoothly across both poles since its anisotropy vanishes as $\sin^2\theta$. Choose $B=a$ in the same dyad. Then $e^\Xi=(v/b)^{a^2}$ for $v\ge b$ and the bulk density in the clock differential is $a e^\Xi/v$. The check uses $\phi(s)=e^{1-1/(1-s^2)}$ for $|s|<1$, zero elsewhere. It compares the original differentiated clock integral against (2) plus its bulk remainder. For the joint metric pairing it uses $X=v^2 a$ on the collar, smoothly extendible away from the collar, and units $c=1$ with spherical mean angular integration. These computations test the cone integrals; they do not construct a cap frame action.

Run `python3 checks/joint_adm.py` and `make check` from the repository root. The focused calculation has the following output. [Executable calculation](../checks/joint_adm.py)

~~~text
Spherical clock trace limit -0.728179777
width 0.03125000  clock -0.708162749  full-cone pairing 0.040230013
width 0.01562500  clock -0.718147031  full-cone pairing 0.020115006
width 0.00781250  clock -0.723157248  full-cone pairing 0.010057503
width 0.00390625  clock -0.725666961  full-cone pairing 0.005028752
~~~
