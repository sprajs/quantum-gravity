# A gravitational probe with a nonzero bracket against the cap clock

A curvature measurement can select a launch slice, and its normal can select the freely falling emitter of a light flash. In a smooth vacuum Kasner universe with toroidal spatial sections, choose the return time of the flash to match a measured waist size. The angularly averaged incoming clock of Venkatesa Chandrasekaran then has a **nonzero classical Peierls bracket** with an explicitly normalized gravitational probe. The probe compares the shape of the spatial torus at nearby times. Its causal response is an exact tangent to a family of four-dimensional vacuum solutions. This calculation includes the moving cap and the intersection with the opposite null cone. It uses a preparation and a probe in the surrounding spacetime. An inverse for the isolated capped-diamond phase space with its own cap and corner conditions remains a separate proof gap. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Clock and average, (3.27)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Fewster and Hunt, linearized vacuum gravity, §§3–4](https://arxiv.org/pdf/1203.0261#page=15)

## Differentiating the light experiment

Consider a region inside a convex normal neighborhood. Assume that the two light cones meet transversely, that the Jacobi map is nonsingular from the vertex to the intersection apart from the vertex itself, and that the optical radius increases strictly at the cap. The observer, emission and return events, and sky measure must be specified covariantly. Fix the affine scale by $-k\cdot V=1$ at launch for the unit emitter velocity $V$. On one ray let $S$ be the affine distance to the waist, $C$ the cap distance, and $D(s)=\sqrt{\det J(s)}$ the area radius per unit physical launch solid angle. Choose an oriented parallel screen, with the Jacobi map satisfying $J(0)=0$, $J'(0)=I$ and $J''=QJ$, where $Q_{AB}=-R_{AkBk}$ in the geodesic-deviation convention. Put $D(C)=\epsilon D(S)$ and $U=D'(C)(S-C)$. The tangent $k$, the screen and the observer all belong to this experiment. [Exact optical propagation in plane waves](https://arxiv.org/abs/1502.03658) · [Two-tip plane-wave example](observable-optics.md)

For a smooth metric perturbation $h$, a dot denotes variation at fixed affine value with launch direction identified in the emitter's orthonormal sky. If $B(s,t)$ solves the Jacobi equation with $B(t,t)=0$, $\partial_sB(t,t)=I$, then
$$
 \dot J(s)=\int_0^s B(s,t)\,\dot Q(t)J(t)\,dt,\qquad
 \dot D(s)=\tfrac12D(s)\,\mathrm{tr}(J^{-1}\dot J)(s).
$$
Here $\dot Q$ differentiates the full contraction of curvature along the varied geodesic and parallel screen, including their displacements. It can be evaluated by varying the geodesic and transport equations with the prescribed launch data. A ray displacement $Z$ at fixed affine parameter obeys the forced geodesic-deviation equation with connection force $-\delta\Gamma^a{}_{bc}k^bk^c$, where $\delta\Gamma$ is the metric connection variation. Its initial position and tangent follow by differentiating the launch prescription, including $-k\cdot V=1$.

Write $\sigma(z_+,x)$ for half the squared geodesic interval from the future tip to the outgoing ray. Let $Z_+$ be the varied future tip and $x=x(S)$. With $y(\lambda)$ the returning null connector, affinely parametrized on $[0,1]$, stationarity of its geodesic action gives
$$
 \delta S=-\frac{\sigma_{;z_+}\cdot Z_+
     +\sigma_{;x}\cdot Z(S)+\frac12\int_0^1 h(\partial_\lambda y,\partial_\lambda y)\,d\lambda}
      {\sigma_{;x}\cdot k}.
$$
Transversality makes the denominator nonzero. The first variation of the cut equation and that of the measured slope now give
$$
 \begin{aligned}
 \delta D_S&=\dot D(S)+D'(S)\delta S,\\
 \delta C&=[\epsilon\,\delta D_S-\dot D(C)]/D'(C),\\
 \delta U&=(S-C)[\dot D'(C)+D''(C)\delta C]+D'(C)(\delta S-\delta C),\\
 \delta\bar U
 &=\frac{\langle D_S\,\delta U+(U-\bar U)\delta D_S\rangle}{\langle D_S\rangle}.
 \end{aligned}
$$
Angle brackets use the normalized launch sky. The product defining $U$ is invariant under affine rescaling on each ray. Holding the coordinate cap time, the outgoing affine distance, or the return connector fixed would generally change this differential.

These variations act on smooth perturbations by integrals along rays, cut evaluations and the derivatives required by the observer prescription. Smooth finite-time ODE dependence and the nonzero implicit-function denominators give continuous linear functionals of a finite number of metric derivatives on the sampled compact region. Spatial and angular averages retain this property. A smooth compactly supported conserved gravitational source $f$ has a smooth causal response $E f$ on a globally hyperbolic vacuum background, modulo linearized diffeomorphisms. The mixed Peierls bracket with our covariantly prepared clock is $d\bar U[E f]$, with $E=E_{\rm ret}-E_{\rm adv}$ for the Einstein–Hilbert Hessian. Covariance annihilates the pure-gauge ambiguity. This mixed pairing uses one smooth argument. Bracketing two sharply localized clocks would require additional control of their singularities. [Fewster and Hunt, Theorems 3.9 and 4.8–4.10](https://arxiv.org/pdf/1203.0261#page=22) · [The cap trace in the isolated radiative block](endpoint-inverse.md)

## An intrinsic preparation in vacuum gravity

Use units $c=1$, coordinates of period one on a three-torus, and the exact metric
$$
 ds^2=-dt^2+\sum_{i=1}^3 a_i(t)^2(dx^i)^2,\qquad
 a_i(t)=A_i(t/T)^{p_i},\qquad
 (p_1,p_2,p_3)=\frac{(-b,1+b,b(1+b))}{1+b+b^2}.
$$
Here $T>0$ is fixed, $t>0$ and $b$ is near 2. The identities $\sum p_i=\sum p_i^2=1$ solve the vacuum equations. Take $(A_1,A_2,A_3)=(6a/5,11a/10,a)$, $a>0$, and diamonds short compared with $T$ and $a$. The spacetime is globally hyperbolic on $t>0$. Every measurement stays a positive time away from its past singularity.

For $K=R_{abcd}R^{abcd}$ define the scalar $\tau=4K/\sqrt{-\nabla_aK\nabla^aK}$. Here $K=-16p_1p_2p_3/t^4>0$ and $\tau=t$. In a neighborhood of these backgrounds use the connected launch slice $\tau=T$ with timelike gradient. From each point launch a freely falling observer normal to this slice, emit at launch, and return to the observer after proper time $2L$. Each emission and return pair defines one closed waist. Vary $L$ until
$$
 M=\frac{\langle D_S^2\rangle}{\langle D_S\rangle}=R
$$
for a prescribed length $R$. For sufficiently small $L$, $M=L+O(L^3/T^2)$ and $\partial_L M=1+O(L^2/T^2)$. This selects a unique nearby return time. In the preceding variation its shift obeys $\delta L=-\delta_g M/(\partial_LM)$, where $\delta_g$ holds $L$ fixed. At a fixed launch point read $\bar U=\langle D_S U\rangle/\langle D_S\rangle$. Define the spacetime observable $\mathcal U_\epsilon$ by averaging these readings over launch points with the normalized proper volume measure of the slice. Spatial translations make all individual readings identical in every member of this Kasner family. The position average defines the experiment even for perturbations that break homogeneity. This ensemble fixes a weighted optical waist size. Its physical choices include the reference sky and the adjustment of the return time. [Covariant observables on metric-dependent domains](https://arxiv.org/abs/1503.03754)

## A smooth geometric probe and its retarded and advanced fields

On each slice $\tau=s$ in a narrow band about $T$, take the Hodge representatives $\omega_i$ of the three primitive integral $H^1(T^3;\mathbb Z)$ classes, up to sign, with the three smallest distinct mean squared norms
$$
 H_i=V_s^{-1}\int_{\tau=s} |\omega_i|^2\,dV_s .
$$
Order these norms increasingly. On the rectangular background they are $a_i^{-2}$, represented by $dx^i$. The chosen side lengths give a strict gap to every further class as well as gaps between the three listed norms. These gaps persist on a sufficiently narrow time band and for nearby metrics. Harmonic representatives depend smoothly on the positive spatial metric there. Choosing the classes by their norms removes the need to mark the torus cycles.

Let $p'_i=dp_i/db$ at $b=2$ and $V_T=A_1 A_2 A_3$. Use a smooth weight $w$ supported in the band with $\int w\,ds=1$ and $\int w\log(s/T)\,ds=0$. One choice is $w(s)=\eta(\log(s/T))/s$, where $\eta$ is even, normalized and compactly supported. Define the scalar probe
$$
 P=\frac{V_T}{16\pi G_N T}\int w(s)\sum_i p'_i\log(a^2H_i(s))\,ds .
$$
The displayed prefactor uses the fixed preparation constants. At the background $\sum p'_i=\sum p_i p'_i=0$. Varying a harmonic representative within its fixed class adds an exact form orthogonal to the original harmonic form. Each background norm density is constant in space, so the variation of the volume weight cancels its normalization. A local displacement of the slice contributes $-2p_i\,\delta t/s$ to the change of log norm after spatial averaging, which cancels in the sum. Consequently for **arbitrary** smooth off-shell $h$ the differential is
$$
 dP[h]=-\frac{V_T}{16\pi G_N T}\int w(s)\sum_i p'_i
              \left\langle h_{ii}/a_i^2\right\rangle_{T^3}ds .
$$
Its source is smooth and spacetime compact. Gauge invariance also follows directly here from the integrated spatial divergences and $\sum p_i p'_i=0$.

To construct its response, put $h_{ii}=2a_i^2 p'_i\psi(t)$ with all other components zero. Direct variation of the Ricci tensor gives $\delta G^i{}_i=p'_i(\psi''+\psi'/t)$ without summing on $i$. The $00$, shift, off-diagonal and trace equations vanish identically by the two Kasner tangent identities above. Since $V(t)=V_T t/T$ and the Einstein–Hilbert variation with respect to $g_{ab}$ is $-G^{ab}dV/(16\pi G_N)$, its Hessian acting on this field equals $dP$ precisely when
$$
 (t\psi')'=w(t).
$$
The retarded solution is $\int_0^t w(s)\log(t/s)ds$ and the advanced solution is $\int_t^\infty w(s)\log(s/t)ds$. Their difference is $\log(t/T)$. Thus $E\,dP=\partial_b g|_{b=2}$ modulo gauge. This verifies the normalization and sign in the full spacetime equations. The tangent is integrable to exact vacuum metrics and changes $K$ on a fixed $\tau$ slice.

## Size and sign of the full-clock bracket

Write $B_\epsilon=1-5\epsilon^4+4\epsilon^5$. To leading order about the vertex the optical deformation matrix is $J'J^{-1}=I/s+sQ(0)/3+O(s^2/T^3)$, with trace-free $Q(0)$ in vacuum. Integrating $D''=-D\,\mathrm{tr}(\sigma^2)/2$ from the cap gives
$$
 U-(1-\epsilon)D_S
 =\frac12\int_C^S (S-s)D(s)\,\mathrm{tr}(\sigma^2)(s)\,ds
 =\frac{B_\epsilon L^5}{360}\,\mathrm{tr}(Q(0)^2)+O(L^6/T^5).
$$
Here $S=L+O(L^3/T^2)$ in the locally inertial emitter frame, and $C=\epsilon L+O(L^3/T^2)$. The weighted sky average and replacement of $L$ by $R$ preserve this coefficient. The fixed $M$ removes the entire variation of the term $(1-\epsilon)M$, including the anisotropy of the waist.

In the comoving Kasner frame the Weyl tensor is purely electric, with eigenvalues $E_i=p_i(1-p_i)/T^2$ for $E_{ij}=C_{i0j0}$. For launch direction $n$ let $P_n=I-nn^T$. The screen tidal matrix equals $2P_n E P_n-\mathrm{tr}(P_n E P_n)P_n$ up to an overall sign. Using $\langle n_i n_j\rangle=\delta_{ij}/3$ and the isotropic fourth moment gives
$$
 \langle\mathrm{tr}(Q^2)\rangle
 =\left\langle 4\,\mathrm{tr}(E^2)-8n^TE^2n+2(n^TEn)^2\right\rangle
 =\tfrac85\,\mathrm{tr}(E^2).
$$
Therefore $\mathcal U_\epsilon=(1-\epsilon)R+B_\epsilon R^5\mathrm{tr}(E^2)/225+O(R^6/T^5)$. The optical ODEs and implicit roots are smooth jointly in the Kasner parameter and small size (the cone matching uses distances scaled by $L$ at the vertex). The Taylor remainder can be differentiated once in $b$ on a compact neighborhood of 2. Since $T^4\mathrm{tr}(E^2)=-2p_1p_2p_3$ has derivative $-240/2401$ at $b=2$,
$$
 \boxed{\displaystyle
 \{\mathcal U_\epsilon,P\}
 =-\frac{16B_\epsilon}{36015}\frac{R^5}{T^4}
  +O(R^6/T^5).}
$$
The coefficient is strictly negative for every fixed $0<\epsilon<1$, hence the bracket is nonzero for all sufficiently small positive $R/T$ at that cap fraction. The sign uses the stated order and retarded-minus-advanced convention. The smooth probe includes an inverse gravitational coupling in its normalization and samples the whole torus. This example tests classical response in a specified surrounding vacuum spacetime. Whether a comparable probe belongs to an intrinsic diamond algebra, and whether the sharp quantum clock exists on its physical Hilbert space, remain open.

## The Hamiltonian perturbation of this spatially averaged clock

The spatial average in this preparation gives enough symmetry to determine the reverse response as well. Write $u(b)=\mathcal U_\epsilon[g_b]$ at fixed $T$, $R$ and $\epsilon$. At the Kasner background the differential of the clock is invariant under translations and the three coordinate reflections. Evaluating it on a smooth linearized solution therefore gives the same result as evaluating it on its group average. This leaves a spatially homogeneous diagonal solution. In proper-time gauge put $H_i=\dot a_i/a_i$ just for the following evolution equations. The spatial vacuum equations give $\partial_t(V H_i)=0$, so $V$ is linear in time, and the Hamiltonian constraint gives the Kasner exponents. The diagonal tangents are thus variations of the $A_i$, the single exponent parameter $b$, and the time origin. The relational preparation eliminates the time origin. Before any torus image is sampled the diamonds with different $A_i$ are locally isometric, and their normalized position averages agree. Hence $d\mathcal U_\epsilon=u'(2)\,db$ on these tangents.

One can give $db$ a smooth spacetime source representative on the entire linearized solution space. Set $F(b)=-16p_1p_2p_3$ and apply its local inverse at $2$ to $\int w(s)\langle s^4 K\rangle_{\tau=s}\,ds$, with normalized slice volume. On Kasner the resulting spacetime observable $B$ is exactly $b$. The time smearing converts the slice integrals into an integral of smooth finite-order metric data on a compact spacetime band by the coarea formula. Its differential at the smooth background is a smooth compact source after integration by parts. It has the same translation and reflection symmetries as the clock. Thus $d\mathcal U_\epsilon=u'(2)dB$ on *all* smooth on-shell perturbations at this background.

For an explicit Hamiltonian vector let $Y$ change only the torus moduli,
$$
 Y\log A_i=\frac{8\pi G_N T}{V_T}\,
              \frac{p'_i}{\sum_j(p'_j)^2},\qquad Yp_i=0 .
$$
Adopt $\Omega=\int\delta q_{ij}\wedge\delta\pi^{ij}$ with $\pi^{ij}=\sqrt{q}(K^{ij}-q^{ij}K)/(16\pi G_N)$ and $K_{ij}=\dot q_{ij}/2$. At $t=T$, $q_{ii}=A_i^2$ and $\pi^{ii}=V_T(p_i-1)/(16\pi G_N T A_i^2)$. Since $\partial_bq_{ii}=0$, direct contraction gives $\Omega(Y,\partial_b g)=1$. Against every independent side-length variation the contraction vanishes by $\sum p'_i=\sum p_i p'_i=0$. Spatial symmetry and gauge degeneracy extend the identity to $\Omega(Y,h)=dB[h]$ for every smooth on-shell $h$. In this ambient problem the clock's Hamiltonian tangent is therefore $u'(2)Y$, modulo diffeomorphisms. The opposite bracket is $dP[u'(2)Y]=-u'(2)$ as required.

This response is locally a spatial coordinate rescaling. A periodic diffeomorphism cannot implement it globally when the shortest torus norms change. A gauge-invariant smooth probe supported inside a single contractible spacetime patch pairs to zero with this response, since the local generating vector can be extended with a cutoff equal to one on its support. The torus probe detects the global modulus. Both the position average and the surrounding spatial topology enter this conclusion.

## Direct numerical check

The check absorbs the constants $A_i$ into local Cartesian coordinates and integrates the homogeneous null geodesics for arbitrary launch directions with their three conserved spatial momenta. It solves three matching equations for the waist time and the two components of the return direction. Transverse derivatives of the outgoing ray give the proper screen area and its affine slope. It locates the fixed-ratio cap, adjusts the future tip to enforce $M=R$ for each perturbed geometry, and differences the original weighted clock. It uses four Gauss nodes in polar cosine and eight azimuths, which integrate the leading fourth sky moment exactly. The finite-size differences retain higher-order terms. [Executable calculation](../checks/joint_jacobi.py)

Run `python3 -B checks/joint_jacobi.py` from the repository root. Expected rounded output at $T=1$, $\epsilon=1/2$ and centered parameter step $0.02$ follows.

```text
predicted normalized bracket -0.00036096
R/T=0.06 normalized bracket -0.00029215
R/T=0.03 normalized bracket -0.00032415
linear extrapolation          -0.00035616
```
