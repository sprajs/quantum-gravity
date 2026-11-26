# What the clock measures at a cap joint

On a regular expanding generator the clock differential has a cap term proportional to the shear contracted with the change of the rim metric. Its coefficient can be obtained twice. Varying the integrated focusing equation gives it as an endpoint evaluation. Varying the initial expansion gives it as the change of the inverse metric used in a trace. These two calculations identify precisely which components of the cap Cauchy data enter. The Hamiltonian vector on the full constrained diamond still requires an inverse of the joined symplectic form. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Clock (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Fixed-area inverse test](endpoint-inverse.md)

## Two calculations of the same one-form

Let $C$ be the initial cap rim, $b=\epsilon>0$, $v=\rho/\rho_S$, $\rho_C=b\rho_S$ and $\Delta u=u_S-u_C$ for an affine generator $\ell=\partial_u$. Fix the generator labels, $b$ and the local area density at $S$. For the two polarization coordinates $z$ let $\langle\ ,\ \rangle$ and $\nabla_v$ denote the metric and connection in (4.21). Put $K(v)=\int_v^1 e^{\Xi(s)}ds$, with $\Xi(v)=\tfrac14\int_b^v s|z'(s)|^2ds$. A variation at fixed area coordinate has
$$
 D u_*=\frac{\rho_S}{2}\int_b^1 vK(v)\langle z',\nabla_v Dz\rangle\,dv.
$$
Integrating by parts gives a smooth interior density and the following lower-end contribution. Here $p_C=(\partial_u\rho)_C>0$, $\mu_C=\rho_C^2\epsilon_0$ and $Dq_{AB}$ is the variation of the metric pulled back to the marked rim.
$$
 \beta_C=-\frac{\rho_S b K(b)}{2}\langle z'_C,Dz_C\rangle
         =-\frac{\rho_C\Delta u}{2}\,\sigma_{(\ell)}^{AB}Dq_{AB}.
 \tag{1}
$$
Indeed $p_C\Delta u=\rho_S K(b)$, $(\partial_u v)_C=p_C/\rho_S$, and $\sigma_{(\ell)}^{AB}Dq_{AB}=(\partial_u v)_C\langle z'_C,Dz_C\rangle$. The endpoint at $S$ has $K(1)=0$. The product $\Delta u\,\sigma_{(\ell)}$ is invariant when the affine tangent is rescaled by a positive function constant on each generator. For the averaged clock (3.28), integrate (1) against $\rho_S\epsilon_0/\int_S\rho_S\epsilon_0$ in this fixed-density sector. In (1) the term “endpoint trace” means evaluation at $C$. Only the trace-free part of $Dq_{AB}$ enters. [Optics (3.25)](https://arxiv.org/html/2611.34924v1#S3.E25.4) · [Polarization metric (4.21)](https://arxiv.org/html/2611.34924v1#S4.E21.2)

For the second calculation write $\chi^{(\ell)}_{AB}=g(\nabla_A\ell,e_B)$ and $\theta_\ell=q^{AB}\chi^{(\ell)}_{AB}$. The starting expansion already determines $p_C=\rho_C\theta_\ell/2$. At fixed $\rho_C$ the defining clock $u_*=p_C\Delta u$ therefore obeys
$$
 Du_* =
 p_C D\Delta u
 +\frac{\rho_C\Delta u}{2}
  \big(q^{AB}D\chi^{(\ell)}_{AB}
             -\chi_{(\ell)}^{AB}Dq_{AB}\big)_C .
 \tag{2}
$$
The last summand equals (1) because $q^{AB}Dq_{AB}=0$. Outside the fixed-density sector (2) also has $(\Delta u\,\theta_\ell/2)D\rho_C$ and the metric contraction can have a trace. The split in (2) depends on the variables used to take the variation. For example, choosing $p_C=1$ throughout a family makes the two terms in parentheses cancel at fixed $\rho_C$. The whole variation then lies in $D\Delta u$ and integrating by parts in $v$ still gives (1). Treating $D\chi_{AB}^{(\ell)}$ and $Dq_{AB}$ as independently adjustable canonical sources would double count this dependence. [Initial expansion (3.25c)](https://arxiv.org/html/2611.34924v1#S3.E25.3)

The longitudinal test has $b=1/2$, $\rho_S=p_C=1$, $z^1=2\log v$, $z^2=0$ and $Y=vDz^1$. In a suitable transverse chart $q=\operatorname{diag}(v^4,1)$ and $u=v^2-1/4$. These are the optical data of a flat cylindrical wavefront on a patch, with transverse lengths proportional to $u+1/4$ and $1$. At $C$, $\Delta u=3/4$ and $\sigma_{(\ell)}^{AB}Dq_{AB}=8Y_C$. Equation (1) gives $-3Y_C/2$. The full differential is $2\int_{1/2}^1Y\,dv-3Y_C/2$. The cylindrical chart describes a local background for the calculation. [Worked differential and independent nonlinear variation](endpoint-inverse.md)

## A physical variation on a spherical diamond

The contracted shear in (1) can also be measured on a closed spherical rim in an exact vacuum spacetime. Take the two tips on one geodesic a proper time $2L$ apart in a constant-profile plane wave. Use its launch angles and write $A=q_{\rm wave} L^2$ for the small signed dimensionless tidal amplitude and $\nu=(1-n_z)/2$ for direction. With $s$ the launch-normalized affine distance, the two Jacobi lengths are $J_\pm=s[1\pm A\nu^2s^2/(6L^2)+O(A^2)]$. The polarization in the corresponding axes is $z=\log(J_+/J_-)=A\nu^2v^2/3+O(A^2)$ because $s=Lv+O(LA)$. Motion of the cap and waist changes the zeroth-order conformal metric by zero. Thus on this family of two-tip solutions varying $A$ with $b$ fixed, the spin-two cap term of the averaged *past* clock is
$$
 \int_S\frac{\rho_S\epsilon_0}{\int_S\rho_S\epsilon_0}\,\beta_C
 =-\frac{L b^4(1-b)}{45}\, A\,dA+O(LA^2\,dA).
 \tag{3}
$$
In fact $z'_C=(2/3)A\nu^2b+O(A^2)$, $Dz_C=[\nu^2b^2/3+O(A)]dA$, and $K(b)=1-b+O(A^2)$. The normalized solid-angle average of $\nu^4$ is $1/5$. The tensors can be evaluated in any regular screen frame, including across a change of polarization chart. The expression isolates an actual nonzero component of the differential in the fixed-$v$ decomposition. Variations of the area density and the distributed optical terms also enter the full derivative on this family. The physical argument only needs regular weak waves before a caustic. [Exact intersecting cones, Jacobi lengths and area-ratio cap](observable-optics.md)

## Matching the optical data to the spacelike cap

Let $T$ be the future cap normal and $s$ the unit normal to $C$ within the cap pointing in the spatial direction of $\ell$. Set $a=-T\cdot\ell>0$ and choose the transverse future null normal $n$ to satisfy $\ell\cdot n=-1$. Then
$$
 \ell=a(T+s),\qquad n=(T-s)/(2a).
$$
Use $K_{ij}=g(\nabla_iT,e_j)$ for the cap extrinsic curvature and $k_{AB}=g(\nabla_A s,e_B)$ for the second fundamental form of $C$ in the cap. Projection of $\nabla_A\ell$ onto $e_B$ and $-n$, respectively, gives
$$
 q^\Sigma_{AB}|_C=q^{\mathscr H}_{AB}|_C,\qquad
 \chi^{(\ell)}_{AB}=a(K_{AB}+k_{AB}),\qquad
 \varpi_A=D_A\log a+K_{As}.
 \tag{4}
$$
Here $D_A$ on a scalar is the angular derivative. The other optical tensor is $\chi^{(n)}_{AB}=(K_{AB}-k_{AB})/(2a)$. The derivatives of the prefactors project to zero in both optical tensors. These identities also give the necessary *linearized* matching conditions by differentiating the complete pullbacks, including the embeddings and the normals. Equal rim metrics alone leave out their normal derivatives. The cap Hamiltonian and momentum constraints and the null transport equations still apply off the cut. [Cap normal (3.12)](https://arxiv.org/html/2611.34924v1#S3.E12) · [Moving pullbacks (3.40)](https://arxiv.org/html/2611.34924v1#S3.E40)

In the momentum convention $\pi^{ij}=\sqrt h\,(K^{ij}-Kh^{ij})/(16\pi G_N)$ one can read the tensor in (1) directly from the cap. With the indices lowered using its three-metric,
$$
 \sigma^{(\ell)}_{AB}
    =a\left[\frac{16\pi G_N}{\sqrt h}(\pi_{AB})^{\mathrm{TF}}
                    +(k_{AB})^{\mathrm{TF}}\right]_C .
 \tag{5}
$$
The trace-free projection is two-dimensional. In Gaussian distance coordinates for the rim in the spacelike cap, $k_{AB}=\partial_s q_{AB}/2$. The scalar expansion uses a different component of the momentum. Since $16\pi G_N\pi_{ss}/\sqrt h=K_{ss}-K=-q^{AB}K_{AB}$, its cap value is
$$
 p_C=\frac{\rho_C a}{2}
       \left(q^{AB}k_{AB}-\frac{16\pi G_N}{\sqrt h}\pi_{ss}\right).
 \tag{6}
$$
Equations (5) and (6) specify which cap momenta and spatial metric derivatives enter the known geometric coefficients. Neither is an inversion of the symplectic form. [Cap potential (3.46)](https://arxiv.org/html/2611.34924v1#S3.E46) · [Boundary action (3.15)](https://arxiv.org/html/2611.34924v1#S3.E15.1)

## Which corner terms can detect the source?

The joint in the action yields the cap potential $-\epsilon_C(8\pi G_N)^{-1}\int_C \log a\,D\mu_C$. Its two-form annihilates any test variation fixing both $a$ and $\mu_C$, for every putative response vector. The tangential term reconstructed from (A.8) on the null sheet pairs the angular displacement with $\mu_C\varpi_A$. Its two-form likewise annihilates a test variation fixing the angular map and that momentum. The canonical boost and twist pairs in (A.14) live at $S$ and depend on the identification of its two sheets. They cannot be transferred to $C$ as freely adjustable momenta. Their action on a globally extended perturbation must be evaluated using that extension. [Null flux (A.8)–(A.9)](https://arxiv.org/html/2611.34924v1#A1.E8) · [Two-sheet form (A.14)](https://arxiv.org/html/2611.34924v1#A1.E14X) · [Cap joint (A.18)](https://arxiv.org/html/2611.34924v1#A1.E18) · [Tangential charge calculation](rim-potential.md)

Local vacuum data permit changes of the conformal metric of $C$ at fixed area, twist and chosen cap boost. The characteristic free data on two future null hypersurfaces include the conformal metric on each branch, with common cut value, and both initial expansions and the torsion on their intersection. To obtain a cap *collar*, take the auxiliary intersection a short distance to the past of $C$ on the extended outgoing sheet. In transported angular coordinates prescribe a smooth family of outgoing conformal metrics with the desired determinant-one change at $C$. Solve the focusing and normal-connection transport equations back to the auxiliary cut, starting with the desired area, positive expansion and torsion at $C$. Use the resulting initial values and compatible smooth data on the second sheet for local vacuum evolution. In double-null coordinates with outgoing sheet $U=0$, auxiliary intersection $V=-d$ and rim $V=0$, the one-sided development contains $U\ge0$, $-d<V<0$ near $C$. A short spacelike collar through $C$ enters this quadrant with $U$ increasing and $V$ decreasing. Its initial tilt can be chosen to give the prescribed $a$ in (4). Restricting the developed geometry to this collar gives data satisfying the cap constraints. This argument establishes freedom in a neighborhood of the joint for vacuum $\Lambda=0$. Completion of a ball, the second external sheet and its data at $S$ are global questions. [Luk, §2.3 and Theorems 2 and 4](https://arxiv.org/pdf/1107.0898) · [Normal-connection transport (3.57c)](https://arxiv.org/html/2611.34924v1#S3.E57.3)

There is a candidate with the correct tensor structure in the charge for *normal* motion of a cut. Smear the clock with $f\epsilon_0$ and take $\xi=\alpha\ell$ at $C$. In the orientation $\eta=du\wedge\mu$, the shear part of $-i_\xi\mathcal E$ in (A.9) is $-\alpha\mu_C\sigma_{(\ell)}^{AB}Dq_{AB}/(16\pi G_N)$. It equals the integrand of the smeared (1) if $\alpha=8\pi G_N f\Delta u/\rho_C$. This matches only one term of the surface-charge variation. Equation (3.50b) also contains $D Q_\xi-Q_{D\xi}$ and the other terms in the full potential. A displacement along a fixed null sheet changes the area by $\alpha\theta_\ell\mu_C$ at fixed labels, so at fixed waist density the displacement alone violates (3.18) wherever this product is nonzero. Also, for two pieces of a hypersurface carrying the *same* smooth fields and the same smooth spacetime displacement, the complete covariant surface-charge integrands at their shared cut have opposite orientations and cancel. Independent variations of a relative boundary frame, or compensating variations of the metric and embeddings, require their own inclusion in the pullback. A single one-sided flux coefficient establishes neither a physical normal displacement nor a solution of the full Hamilton equation. [Charge (3.50)](https://arxiv.org/html/2611.34924v1#S3.E50.2) · [Extended potential (B.21)](https://arxiv.org/html/2611.34924v1#A2.E21) · [Regulator (3.18)](https://arxiv.org/html/2611.34924v1#S3.E18)

The remaining **proof gap** is a range problem. A putative vector $X$ must obey (4) and its linearization, the cap and sheet constraints and the prescribed outer boundary data. On every allowed $Y$, including those varying the spacelike interior, its contraction with the *sum* of the cap, sheet and joint forms must equal $Du_*(Y)$. The coefficient in (5) and the value $-3/2$ are necessary checks on that equation in the worked sector. Only the complete differential has an invariant meaning under integrations by parts.

## Reproduce the longitudinal check

Run `python3 checks/joint_edges.py` from the repository root. It uses rational arithmetic on the cylindrical background, contracts the metric and optical tensors, and checks (4)–(6) with a rescaled affine tangent. A separate calculation evaluates the two Jacobi axes at weak tidal amplitude and integrates the leading angular polynomial for (3). The expected output is

```text
Optical shear contraction for unit cap trace: 8
Clock endpoint from the cap geometry: -3/2
Affine rescaling leaves the coefficient invariant: yes
Spherical half-radius rim coefficient in units of L A dA: -1/1440
```

Run `make check` for the full repository suite. [Executable check](../checks/joint_edges.py)
