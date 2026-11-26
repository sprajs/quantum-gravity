# A single-emitter clock and a compact quadrupole probe outside a black hole

A short diamond launched outside a Schwarzschild black hole has a nonzero linearized Peierls pairing with a smooth vacuum quadrupole. The emitter starts at rest according to local curvature measurements and falls freely. Its past-tip clock uses the full sky and a fixed measured waist size. For an emitter placed on the wave axis at four gravitational mass lengths, the dimensionless leading coefficient is $-39/204800$ at cap fraction $1/2$. Measuring the launch radius and measuring the launch tidal curvature give different results. This is an ambient linearized observable based at a specified background event. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.27)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Optical first variation](joint-jacobi.md)

## Selecting the velocity and varying the launch event

Use signature $(-+++)$, $c=1$, a mass parameter $m>0$ in length units, and the time-oriented Schwarzschild exterior $r>2m$. Let $K=C_{abcd}C^{abcd}$, with $C$ the Weyl tensor. On this background $K=48m^2/r^6$ and its gradient is spacelike. Define the outward unit vector $n=-\nabla K/|\nabla K|$ and on $n^\perp$ the self-adjoint endomorphism $C^a{}_{cbd}n^cn^d$. In the static orthonormal frame, with $q=m/r^3$ and $C_{i0j0}=\mathrm{diag}(-2q,q,q)$ in radial-first order, its mixed eigenvalues are $2q,-q,-q$. Its simple timelike eigenline gives a unique future unit velocity $V$. This prescription persists under small smooth metric variations. The separated real simple eigenvalue and its eigenspace vary smoothly, and timelikeness is open. The angular average over $V$'s unit sky dispenses with any choice between the two angular axes. $V$ fixes the initial velocity only.

Two alternative scalar conditions for the launch event are $I=K$ and $I=\rho$, where
$$
 \rho=\left[\frac{\nabla_aK\nabla^aK}{36K^2}
                    +2\sqrt{K/48}\right]^{-1/2}.
$$
In Schwarzschild the two terms inside the brackets are $(1-2m/r)/r^2$ and $2m/r^3$, hence $\rho=r$. Both choices define regular levels throughout the exterior. Away from spherical symmetry $\rho$ denotes this local measurement. Its definition requires derivatives through third order in the metric.

Choose a background point $p$ on the desired level. From $p$ emit a flash and receive its immediate echoes on the emitter geodesic after proper time $2L$. For the past-tip cone let $S$ be the affine distance to the intersection with the future-tip cone and $D(s)$ the area distance per unit emission solid angle. Use $D(C)=\epsilon D(S)$ with fixed $0<\epsilon<1$, and set $U=D'(C)(S-C)$. Choose $L$ by $M=\langle D(S)^2\rangle/\langle D(S)\rangle=R$, where angle brackets average over the sky and $R$ is a fixed length. Denote $\langle D(S)U\rangle/\langle D(S)\rangle$ at an arbitrary nearby point by $A(g,p)$. Take a short convex-normal diamond with transverse waist, positive cap slope, no generator crossings and $\partial_L M\ne0$. These conditions hold for sufficiently small $R>0$ by the locally flat limit. [Two-cone and moving-cap formulas](joint-jacobi.md)

In a varying metric take any smooth continuation of $p$ on its specified level. For example intersect that level with a fixed auxiliary curve transverse to it through $p$. In the background $A(g,p)$ depends only on $r$ because time translations and rotations act transitively on each level. If $J_p$ denotes the resulting linear clock functional, then
$$
 J_p[h]=\delta_g A(g,p)[h]
           -\frac{\partial_r A}{\partial_r I}\,\delta_g I(g,p)[h].
 \tag{1}
$$
The first terms in both variations hold the point fixed. Differentiating the level condition fixes the radial displacement used in (1). All remaining displacements of this *same base point* are tangent to the level and cancel. For $h=\mathcal L_Xg$ the two fixed-point variations are $X^r\partial_r A$ and $X^r\partial_r I$ by covariance. This proves $J_p[\mathcal L_Xg]=0$ for every smooth $X$. Regular finite-time geodesic and optical transport with the two implicit roots gives a compactly supported finite-order distribution in $h$. It includes both cones, the observer and its launch jets. The Ward identity makes this source distributionally conserved. On this globally hyperbolic exterior, the gauge-fixed causal propagator defines its weak response by duality on smooth compact conserved probes. Schwarzschild time slices are Cauchy since a causal curve traverses at most unit tortoise-coordinate distance per unit time and the angular sphere is compact. [Linearized Einstein causal propagator](https://arxiv.org/abs/1203.0261) · [Curved optical source and propagation](weak-curved.md)

The quotient in (1) is by *infinitesimal metric gauges at the background*. Isometries carrying $p$ to $p'$ carry $J_p$ to $J_{p'}$. The two covectors can give different readings on the same nonsymmetric wave. The level alone therefore does not designate a unique emitter on the nonlinear space of metrics. Indeed the differential of a fully unmarked differentiable scalar invariant under the rotation group would annihilate a pure quadrupole, whose rotation average is zero. There is also a compact-support obstruction. If the scalar is invariant under all background time translations, the support of its differential is time-translation invariant. Every exterior time orbit has unbounded Schwarzschild time, so a compactly supported such differential must vanish. Specifying a base point gives the local experiment below its time and position.

## What the short clock measures

Put $B_\epsilon=1-5\epsilon^4+4\epsilon^5$. For each vacuum ray the shear deformation begins as $sQ/3+O(s^2)$ with $Q_{AB}=-C_{AkBk}$ at launch, $k=V+\hat s$. Integrating the optical focusing equation from cap to waist gives
$$
 U-(1-\epsilon)D(S)=\frac{B_\epsilon R^5}{360}\,\mathrm{tr}(Q^2)+O(R^6).
$$
Since $S=R+O(R^3)$ and $D(S)/\langle D(S)\rangle=1+O(R^2)$, the matched waist makes the averaged first term exactly $(1-\epsilon)R$. Write $E_{ij}=C_{i0j0}$ and $H_{ij}={}^*C_{i0j0}$ in the emitter frame. For a purely electric field the sky average of $\mathrm{tr}(Q^2)$ is $8\,\mathrm{tr}(E^2)/5$. Its first variation at such a field has no electric–magnetic cross term since the magnetic piece of $Q$ is odd under reversal of the ray's spatial direction and the electric piece is even. Using $K=8[\mathrm{tr}(E^2)-\mathrm{tr}(H^2)]$ and $H=0$ at Schwarzschild gives for smooth vacuum perturbations
$$
 A=(1-\epsilon)R+\frac{B_\epsilon K R^5}{1800}+O(R^6)
 \quad\text{on Schwarzschild},\qquad
 J_p[h]=\frac{B_\epsilon R^5}{1800}\,\delta K\big|_I+O(R^6),
 \tag{2}
$$
where $\delta K|_I=\delta_g K-(\partial_rK/\partial_r I)\delta_g I$. The expansion at fixed cap fraction permits one differentiation along the smooth wave. Rescaling the light-travel distances by $L$ gives regular ODEs and simple matching roots at $L=0$, and $\partial_L M\to1$. The remainder uses local curvature and its derivatives at the chosen background and perturbation. [Ray integral, sky moments and matching](joint-jacobi.md)

At fixed measured $K$ the order-$R^5$ differential vanishes for every vacuum wave at this background. At fixed $\rho$ the Schwarzschild mass family gives $\partial_m A=B_\epsilon K R^5/(900m)+O(R^6)$. That family changes the asymptotic mass. A wave with a compact probe supplies a different test.

## A compact probe with a nonzero bracket

In outgoing coordinates $u=t-r_*$, $dr_*/dr=(1-2m/r)^{-1}$, take the linearized vacuum Robinson–Trautman quadrupole. With $d\Omega^2$ the round unit metric and $\Delta_0$ its Laplacian, write the local metric as
$$
 ds^2=-\big[\mathcal K-2r\partial_u w-2m/r\big]du^2
       -2du\,dr+r^2e^{-2w}d\Omega^2,\qquad
 \mathcal K=e^{2w}(1+\Delta_0 w).
$$
Use $w=\alpha F+O(\alpha^2)$ with $F=e^{-2(u-u_0)/m}P_2(\cos\theta)$. The vacuum equation at first order is $12m\partial_u F=-\Delta_0(\Delta_0+2)F$. The exact curvature contraction in this family is $K=48m^2/r^6$ because the two positive-boost-weight Weyl components vanish and $\Psi_2=-m/r^3$. The inverse radial component varies as $\delta g^{rr}=4(r/m-1)F$. Consequently $\rho=r[\mathcal K-2r\partial_u w]^{-1/2}$ and
$$
 \delta r\big|_\rho=2r(r/m-1)F,\qquad
 \delta K\big|_\rho=-12K(r/m-1)F .
 \tag{3}
$$
The sign follows because the same radius reading moves the emission event outward at the positive pole of the wave. [Robinson–Trautman metric, field equation and Weyl components, Eqs. (2.1)–(2.8)](https://utf.mff.cuni.cz/~podolsky/2009/RThorizons.pdf#page=2) · [Qi and Schutz, linearized mode, Eqs. (11)–(15)](https://pure.mpg.de/rest/items/item_52213_3/component/file_52214/content)

The exponential mode need only agree with the chosen wave on a neighborhood of the diamond. Factoring out $P_2$, its Zerilli–Moncrief amplitude in the conventional normalization is
$$
 Z_{\rm loc}(t,r)=-\frac{2mr}{2r+3m}e^{-2(u-u_0)/m}.
$$
Indeed the angular metric trace coefficient is $-2e^{-2(u-u_0)/m}$ and the $uu$ coefficient is $-4(r/m-1)e^{-2(u-u_0)/m}$ in outgoing Regge–Wheeler gauge. Substitution in the master formula gives the displayed $Z_{\rm loc}$. On a Schwarzschild time slice multiply both its Cauchy data by a smooth compact cutoff in $r_*$ equal to one on an interval whose domain of dependence contains the whole experiment. Evolve the homogeneous Zerilli equation and reconstruct the metric $k$ in Regge–Wheeler gauge. For $\ell=2$ the vacuum reconstruction is a local differential operator with smooth coefficients on $2m<r<\infty$. It preserves spacelike compactness, and domain of dependence reproduces the original metric on the experiment. [Martel and Poisson, Eq. (4.23) and Appendix D](https://arxiv.org/pdf/gr-qc/0502028#page=17) · [Sarbach and Tiglio, inverse reconstruction](https://arxiv.org/pdf/gr-qc/0104061#page=12)

Choose any smooth temporal step $\chi$ from zero to one over a bounded Schwarzschild-time slab. The Einstein–Hilbert Hessian $\mathcal J k=-\delta G[k]^{ab}/(16\pi G_N)$ defines the smooth source $f=\mathcal J(\chi k)$ and linear probe $P_f[h]=\int f^{ab}h_{ab}\,dV$. The source is supported on the intersection of the slab with the wave support, which is compact by finite propagation. The linearized Bianchi identity gives $\nabla_a f^{ab}=0$. Representatives of the retarded and advanced solutions are $\chi k$ and $(\chi-1)k$ modulo gauge. Thus $[E f]=[k]$ for $E=E_{\rm ret}-E_{\rm adv}$. Equation (1) makes $\{J_p,P_f\}=J_p[Ef]$ independent of this gauge choice. Different radial cutoffs preserving the experiment can give different probes with the same pairing. [Source normalization and cutoff argument](joint-scaling.md)

At $r=4m$, $u=u_0$, on the wave axis, $F=1$, $m^4K=3/256$ and $m^4\delta K|_\rho=-27/64$. For $\epsilon=1/2$ this gives
$$
 \boxed{\displaystyle
  \{J_p,P_f\}=-\frac{39}{204800}\frac{R^5}{m^4}
                 +O(R^6/m^5).}
$$
It is nonzero for sufficiently short diamonds. At the equator the same wave gives minus one half of the polar coefficient. The compact source tests the linear gravitational field in the exterior. Deriving the same causal pairing from a phase space with only capped-diamond data and its own corner dynamics remains a **proof gap**.

## Reproducing the coefficient

Run `python3 -B checks/weak_schwarzschild.py` from the repository root. The check tests the master equation and the radial calibration, then integrates the leading directional optics using exact constant-tide Jacobi solutions. Replacing the curvature along each ray by its value at the wave pole tests the leading angular coefficient. The finite-size remainder of the curved diamond comes from the analytic expansion. The last line reads `Compact quadrupole bracket coefficient = -39/204800`. Run `make check` for the full suite. [Executable calculation](../checks/weak_schwarzschild.py)
