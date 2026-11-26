# A smooth spacetime probe for the sharp geometric clock

On a spatially compact Ricci-flat spacetime, a smooth metric source can produce an infinitesimal constant rescaling of the metric. On a diamond whose marks follow that rescaling, the response of either of Chandrasekaran's finite-cap clocks equals its original reading. The result applies on a radiating background and keeps the two clock readings distinct. It uses the causal response on the surrounding spacetime. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E26) · [Fewster and Hunt, linearized vacuum gravity](https://arxiv.org/abs/1203.0261)

## Constructing the source and fixing the sign

Let $(M,g)$ be a smooth globally hyperbolic four-dimensional vacuum solution with $\Lambda=0$ and compact Cauchy surfaces without boundary. Identify the tangent metric $w$ by its covariant components $w_{ab}$. With the Einstein–Hilbert action $S=(16\pi G_N)^{-1}\int R\,dV_g$, its Hessian on compact variations is represented on shell by
$$
 (J_g w)^{ab}=-\frac{1}{16\pi G_N}(\delta G[w])^{ab}.
$$
Choose a smooth temporal cutoff $\chi$ equal to zero before one Cauchy surface and one after another. The slab can lie strictly to the past of the entire diamond. The exact solution family $g_s=e^{2s}g$ has tangent $k=2g$ and $J_g k=0$. The four-dimensional conformal variation $\delta G[2\chi g]_{ab}=2(g_{ab}\Box\chi-\nabla_a\nabla_b\chi)$ gives the source and its linear observable
$$
 f^{ab}=J_g(\chi k)^{ab}
   =\frac{\nabla^a\nabla^b\chi-g^{ab}\Box\chi}{8\pi G_N},
 \qquad F_f(w)=\int_M f^{ab}w_{ab}\,dV_g .
$$
Only derivatives of $\chi$ occur, so $f$ is smooth and compactly supported. Commuting derivatives on $\nabla^b\chi$ gives $\nabla_a f^{ab}=R^b{}_c\nabla^c\chi/(8\pi G_N)=0$. Integration by parts gives $F_f(\mathcal L_V g)=0$ even for a gauge vector $V$ extending beyond the slab.

Use the source sign $S-jF_f$ in the tangent theory, so the equation of response is $J_g w=f$. Define $E$ as retarded response minus advanced response, and the mixed pairing as $\{T,F_f\}_g=dT_g(Ef)$. Representatives vanishing in the past and future, respectively, are
$$
 w_{\rm ret}=\chi k,\qquad w_{\rm adv}=(\chi-1)k,\qquad [Ef]=[2g].
$$
The two representatives solve the same inhomogeneous equation. Gauge fixing may add Lie derivatives. Hyperbolic uniqueness in the gauge quotient identifies the retarded and advanced classes by their vanishing initial or final data. Changing the cutoff changes $f$ by $J_g((\chi_1-\chi_2)k)$, with compact argument. Formal self-adjointness of $J_g$ shows that the two probes agree on every smooth linearized solution. The argument $\chi k$ itself extends to the entire future, which is how the individual probe can be nonzero. [Fewster and Hunt, §§3–4](https://arxiv.org/abs/1203.0261) · [Khavkine, covariant phase space and the Peierls formula](https://arxiv.org/abs/1402.1282)

For a direct check of its sign, use a finite time interval times a flat spatial three-torus of coordinate volume $V_0$. There $f^{ij}=\delta^{ij}\chi''/(8\pi G_N)$ and its other components vanish. The metrics $-dt^2+(1+a t)^2dx^2+dy^2+dz^2$ are exactly flat for $1+a t>0$, with tangent $w_{xx}=2t$ at $a=0$. Hence $F_f(w)=(V_0/4\pi G_N)\int t\chi''dt=-V_0/(4\pi G_N)$. This check uses the periodic spatial identifications.

## The two faces and the choice of marks

Choose a regular diamond before caustics or an expansion turning point, with $0<\epsilon<1$ fixed. In the representative $k=2g$, keep the embeddings of the tips and geometric cuts fixed, rescale each unit-frame vector by $e^{-s}$, and retain its angular labels. A constant rescaling preserves the connection and the null curves. On each face it gives
$$
 q_{AB}\mapsto e^{2s}q_{AB},\qquad
 \varrho\mapsto e^s\varrho,\qquad v=\varrho/\varrho_S\mapsto v,
 \qquad \bar q_{AB}\mapsto\bar q_{AB}.
$$
Both endpoint area-ratio conditions and the common induced metric matching at $S$ are preserved. The full nonlinear focusing exponent $\Xi_y$ of (3.26c) is unchanged on every generator, including generators with shear. Thus $u_*(y)=\varrho_S(y)\int_\epsilon^1 e^{\Xi_y(v)}dv$ scales by $e^s$. In the average (3.28) the numerator scales by $e^{2s}$ and the denominator by $e^s$. For the past and future face readings $T_p,T_q$ and corner area $\mathscr A$ the responses are therefore
$$
 dT_p(2g)=T_p,\qquad dT_q(2g)=T_q,\qquad
 d\mathscr A(2g)=2\mathscr A .
$$
Each reading is strictly positive on the regular segment. The ratios $T_p/\sqrt{\mathscr A}$ and $T_q/\sqrt{\mathscr A}$ have zero response. These identities hold regardless of differences in shear between the two faces. [v1, boundary conditions (3.18)](https://arxiv.org/html/2611.34924v1#S3.E18) · [v1, finite-cap clocks (3.27)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27)

With external marks this is a response of the **specified marked family**. If a gauge change adds $\mathcal L_Vg$ to the metric representative, it also changes an embedding $X$ by $-V\circ X$. The Lie derivatives then cancel in the variation of $X^*g$. Fixing the embedding's coordinate components a second time after a gauge change would define a different experiment. A compact metric source on the parent spacetime alone does not tell independently dynamical boundary frames how to move. [v1, Eq. (3.40)](https://arxiv.org/html/2611.34924v1#S3.E40)

A sufficient additional hypothesis gives a mixed Peierls pairing on the **bulk gauge quotient** itself. Suppose four dimensionless scalar curvature invariants $I^\alpha[g]$, invariant under constant rescaling, give a nonsingular intrinsic chart near the two tips. Specify both events by values of $I^\alpha$ on locally unique branches. Choose a future-directed unit frame by orthonormalizing fixed linear combinations of their gradients on a patch where the chosen timelike and spacelike pivots are regular. Construct the null boundaries from these tips, their angular frames and their area-ratio cuts. This marking transforms equivariantly under diffeomorphisms. The tips stay fixed under $g_s$, the normalized vectors scale by $e^{-s}$, and this construction supplies the marking used above. With this hypothesis,
$$
 \{T_p,F_f\}_g=T_p,\qquad \{T_q,F_f\}_g=T_q .
$$
The intrinsic-chart hypothesis needs to be verified for any selected background. In particular a spacetime with two independent Killing vectors cannot supply four independent scalar coordinates there. Spatially compact gravitational-wave solutions such as polarized $T^3$ Gowdy metrics admit the externally marked calculation instead. The response uses the integrable tangent $2g$ even on backgrounds with symmetries. [Khavkine, differential invariants as gravitational observables](https://arxiv.org/abs/1503.03754) · [Jurke, polarized Gowdy solutions](https://arxiv.org/abs/gr-qc/0210022)

## What would establish the finite-diamond bracket?

The smooth perturbation $Ef$ can be restricted to a null sheet, to its cuts and to the tips in the intrinsic marking above. This mixed calculation requires only the derivative of a clock along that smooth perturbation. For a **pair** of sharp geometric functionals, trying to restrict the causal Green distribution to null sheets encounters a different question. The normal covector to a null sheet is itself characteristic. Two points on one generator can therefore have conormal covectors joined by the wave propagation relation. The usual sufficient wavefront criterion for restricting the propagator does not then apply directly. A cancellation in the tensor contractions or a limit of specified smooth measurements would require its own proof. An endpoint trace already appears on the radiative null block. [Endpoint calculation](endpoint-inverse.md)

There is a useful exception for sources supported strictly inside **opposite** faces. Take the two cones of timelike separated tips inside a causally convex normal neighborhood. A characteristic connecting conormals to their interiors would follow a generator of each. Uniqueness of the geodesic would put both tips on the same null geodesic within the neighborhood, contradicting their timelike separation. Thus the retarded-minus-advanced kernel of a normally hyperbolic equation admits this cross-face restriction. A gauge-fixed metric kernel has the same characteristic relation. Gauge invariance of a proposed gravitational probe remains a separate condition. Sharp terms on the rims and the common cut can have additional conormals, so the argument by itself does not pair the two complete clock differentials. [Duistermaat and Hörmander, propagation along bicharacteristics](https://doi.org/10.1007/BF02392165)

For an explicit scalar check take the flat four-dimensional tips at $(0,0)$ and $(2R,0)$. Write $x_p=(r,r n)$, $x_q=(2R-s,s n')$, with $0<r,s<R$ and unit spatial directions $n,n'$. For the operator $\partial_t^2-\nabla^2$, average $E(x_q,x_p)$ over both unit spheres with probability measure. Its future-light-cone kernel is $\delta((2R-r-s)^2-|s n'-r n|^2)/(2\pi)$. The argument is affine in $n\cdot n'$ with derivative $2rs$. Its root lies between $-1$ and $1$ precisely when $r+s\ge R$, and the cosine is uniform with density $1/2$. Thus the angular average is $\mathbf 1_{r+s>R}/(8\pi r s)$ as a distribution on the open radial square. It gives a nonzero, unambiguous bracket for smooth radial smearings on opposite null faces even though no restriction to the same generators was used.

There is a precise extension-independence result for interior sources. In a causally compatible globally hyperbolic open subregion, the advanced and retarded Green operators of the gauge-fixed hyperbolic equation agree with the restricted ambient operators on smooth sources compactly supported in that subregion. Extension by zero followed by the ambient Green operator obeys the local inhomogeneous equation and the required causal support, so uniqueness gives the claim. A source on the boundary or spanning the parent Cauchy surface falls outside this argument. [Bär, Green-hyperbolic operators](https://arxiv.org/abs/1310.0738)

Here the cutoff-independent source probes the full surrounding Cauchy surface. On a noncompact Cauchy surface its time-slab support generally extends to spatial infinity. On a fixed-area leaf the dilation is transverse. At fixed nonzero $\Lambda$ the scaled metric generally ceases to solve the same Einstein equation. Finally $F_f$ is a linearized observable based at $g$. Treating the source $f[g]$ as one nonlinear Hamiltonian for all backgrounds would require differentiating its background dependence and proving that the dilation generates a symplectic flow. The intrinsic finite-diamond problem still requires a causal prescription or inverse on its own matched cap, sheet and boundary-frame data. The two mixed readings above give definite values against which to test a proposed relation to the ambient theory.

## Reproduce the source and propagator checks

Run `python3 -B checks/joint_scaling.py` and `make check` from the repository root. The focused script differentiates the Einstein tensor of a conformally perturbed, nonflat Kasner metric using the diagonal Bianchi I equations, integrates the torus probe with a smooth temporal switch, and integrates a narrow approximation of the light-cone delta over the relative angle of two rays. The selected radii keep the angular root away from a pole. Expected output follows. [Executable calculation](../checks/joint_scaling.py)

~~~text
Conformal Einstein source on Kasner: 12 components agree within 1e-12
Flat torus probe in units of V_0/(4 pi G): -1.000000
Opposite-face scalar kernel: 3 angular integrals agree within 1e-12
~~~
