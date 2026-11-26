# Equal rim metrics can carry different angular momenta

Consider a spacelike cap and a finite null sheet prepared as **independent** vacuum solutions. Identifying their induced two-metrics by a comparison map leaves their normal connections free. Even matching both null second fundamental forms at the rim can leave a quadrupole in the connection. A single diamond in Venkatesa Chandrasekaran’s construction has one smooth tetrad and its torsion-free connection on the two faces, which imposes additional compatibility conditions. [Chandrasekaran, arXiv:2611.34924v1, Eq. (3.19)](https://arxiv.org/html/2611.34924v1#S3.E19) · [Cap projections, Eq. (4)](joint-edges.md)

## A comparison independent of the choice of boost

Take future null normals with $\ell\cdot n=-1$, and fix which null line is outgoing. On an expanding round rim of radius $r$, write $\theta_\ell$ for the expansion and $\varpi_A=-n\cdot\nabla_A\ell$ for the normal connection. The one-form
$$
 j=\varpi-d\log(r\theta_\ell/2)
$$
is the connection evaluated with the null normal for which the initial area-radius slope is one. Indeed $\partial_\ell\rho=r\theta_\ell/2$ at this cut with unit-sphere reference measure. Under $\ell\mapsto e^\beta\ell$, the connection gains $d\beta$ and the expansion gains the factor $e^\beta$. Hence $j$ is independent of any smooth local boost. If the two faces come from the same smooth cut, a comparison map $F$ must give $j_\Sigma=F^*j_{\mathscr H}$. This follows by eliminating the relative boost between expansion matching and connection matching. It holds for any $F$ compatible with the other data. [Expansion and clock normalization, Eqs. (3.25)–(3.27)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Normal-frame matching, Eq. (3.62)](https://arxiv.org/html/2611.34924v1#S3.E62)

## A sheet with the same optical tensors as the flat cap

Use a Euclidean round ball on a constant-time slice of Minkowski space as the cap. With $T$ its future unit normal and $s$ the outward spatial unit normal, choose $\ell=T+s$, $n=(T-s)/2$. At its rim $C$, the metric is $r^2\gamma$, the two shears vanish, the expansions are $2/r,-1/r$, and $\varpi=j=0$. Here $\gamma$ is the unit sphere metric.

For the independently prepared sheet, prescribe smooth characteristic data on two intersecting truncated null hypersurfaces. Choose the same round metric and expansions at their intersection, and constant round conformal classes along both hypersurfaces. Prescribe the corner one-form as $\varpi_C=k\,dQ$ in the same normalized null frame, where $Q=P_2(\cos\theta)$ and $k$ is real. This is free initial data. Luk’s initial-data definition allows a smooth one-form on the intersecting sphere independently of its metric, expansions and the two conformal classes. His vacuum existence theorem applies on a regular neighborhood to the future of the initial surfaces. The sign of his torsion variable can be absorbed in the freely chosen $k$. [Luk, §2.3, Definitions 1–2](https://arxiv.org/pdf/1107.0898#page=7) · [Luk, Theorem 1](https://arxiv.org/pdf/1107.0898#page=2)

On the outgoing hypersurface let $u$ be affine with $\rho=u$ and $C$ at $u=r$. The metric is $u^2\gamma$, the shear is zero and $\theta_\ell=2/u$. Raychaudhuri holds identically. The angular vacuum constraint becomes $\partial_u(u^2\varpi_A)=0$, so
$$
 \varpi_A(u)=k\,\frac{r^2}{u^2}D_AQ.
$$
The other transverse fields evolve by their own constraints. Prescribing flat values for both optical tensors **at $C$** leaves their transverse derivatives free to differ from the flat values. The construction uses a truncated sheet. Extending this same shear-free solution back to $u=0$ with a regular vertex would force $k=0$. [Angular and cross-focusing equations, (3.57)](https://arxiv.org/html/2611.34924v1#S3.E57.3)

For every $k$ the identity compares the two rim metrics and both second fundamental forms exactly. For $k\ne0$ the sheet has $j_C=k\,dQ$, while the cap has $j_C=0$. No diffeomorphism pulls a nonzero one-form back to zero. A boost can remove $\varpi_C$ alone, but that boost changes the angular dependence of $\theta_\ell$. Matching the two equal positive expansions already fixes the relative boost to zero. The curvature $d\varpi$ vanishes on both sides. The allowed magnetic-parity datum $k\,{*}_\gamma dQ$ gives $d\varpi=-6kQ\,d\Omega$ and has zero contraction with $\operatorname{grad}_\gamma Q$. The electric test therefore measures information that the normal curvature alone misses.

There is a direct tidal measurement on this shear-free cut. Let $c=\theta_\ell/2>0$ and use $R(X,Y)Z=[\nabla_X,\nabla_Y]Z-\nabla_{[X,Y]}Z$. The tangential and normal components give $\nabla_A\ell=c\,e_A+\varpi_A\ell$. Antisymmetrizing its derivative and tracing over two tangent indices yields
$$
 q^{AC}g(R(e_A,e_B)\ell,e_C)=-D_Bc+c\,\varpi_B=c\,j_B.
$$
The left side is a component of Weyl curvature in vacuum. Dividing by $c$ makes it independent of the null scale. The scalar $(4\pi)^{-1}\int_C |j|_q^2\,\mu$ consequently distinguishes the sides without choosing an angular marking. It is zero on the flat cap and $6k^2/5$ on the sheet.

The one-sided coefficient can be compared directly with the clock experiment. At $k=0$ take a test $Z$ with $\delta_Z k=1/2$, holding both markings and the radii fixed. Use the angular-variation matrix element with displacement $V=G_N\operatorname{grad}_\gamma Q$ in the response slot, and choose the sheet orientation for which $\Theta_C=+(8\pi G_N)^{-1}\int_C\mu\varpi_A\,\delta F^A$ at the identity. The matrix element at $r=1/3$ then equals
$$
 -\frac{1}{8\pi G_N}\int_C\mu\,V^A\delta_Z\varpi_A
 =-\frac{r^2}{4}\langle|DQ|^2\rangle=-\frac{1}{30},
 \qquad \langle |DQ|^2\rangle=\frac65 .
$$
Along this particular torsion variation the shear-free capped clock at fixed radii is constant. Thus an independent angular term adjusted to the narrowing-pulse experiment would also respond to a direction in which the clock differential is zero. Any Hamiltonian construction using these independent data would have to account for that equation as well. This one-sided matrix element leaves tangency and the other terms of the reduced symplectic form open. [Pulse and orientation](joint-angular.md) · [Clock, Eq. (3.27)](https://arxiv.org/html/2611.34924v1#S3.E27)

## An exact vacuum cap with variable momentum

The freedom is also visible when the sheet stays flat and only a complete spacelike ball varies. Use the axisymmetric Kasner metric
$$
 g=-dt^2+\sum_{i=1}^3(1+\lambda t)^{2p_i}(dx^i)^2,\qquad
 (p_1,p_2,p_3)=(2/3,2/3,-1/3).
$$
On $1+\lambda t>0$ this is vacuum since $\sum p_i=\sum p_i^2=1$. For example the directional expansion rates are $H_i=\lambda p_i/(1+\lambda t)$ and give $R_{tt}=-\sum_i(\dot H_i+H_i^2)=0$, $R_{ii}/g_{ii}=\dot H_i+H_i\sum_jH_j=0$. At $t=0$ take the ball $|x|\le r$. Its metric is Euclidean for every $\lambda$, and its extrinsic curvature in the convention $K_{ij}=g(\nabla_iT,e_j)$ is $\lambda\,\mathrm{diag}(p_i)$. With radial unit vector $\nu$ and $P=\sum p_i\nu_i^2=1/3-2Q/3$, projection in the cap frame gives
$$
 \varpi=K_{A\nu}\,dy^A=\frac{\lambda r}{2}\,dP,\qquad
 \theta_\ell=\frac2r+\lambda(1-P).
$$
Indeed the rim tangent is $e_A=r\,\partial_A\nu$, and tracing $K$ over the tangent plane subtracts $\lambda P$ from $\lambda\sum p_i$. For sufficiently small $|\lambda|r$ the expansion stays positive everywhere. At the round sphere,
$$
 j=\left(\frac{\lambda r}{2}+
 \frac{\lambda}{2/r+\lambda(1-P)}\right)dP,\qquad
 \left.\partial_\lambda j\right|_0=-\frac{2r}{3}\,dQ.
$$
Consequently a flat independent cone can have exactly the same rim metric through this family while its calibrated connection stays zero. Here the cap’s outgoing shear changes as well. The Kasner curvature is of order $\lambda^2$ near flat space. Its first-order effect records the extrinsic geometry of the chosen cut. The characteristic example isolates the connection mismatch even when the shear agrees and detects it in the linearized Weyl curvature.

One can also join the Kasner cap to **its own** outgoing null hypersurface generated by $\ell=T+\nu$ at $C$. Before the first caustic this gives a smooth vacuum collar. Take $\lambda=-3t_0/(2r)$, so in this cap-adapted affine frame $\varpi_C=t_0\,dQ/2$ exactly. Mark the cap by a family $F_\tau$ generated at the rim by $G_N\operatorname{grad}_\gamma Q$ while using the original marks on the sheet. The cap marking extends smoothly into a collar and can be cut off before the center. Pulling back every cap tensor by $F_\tau$ gives $q_{\rm cap}=F_\tau^*q_{\rm sheet}$ and $\varpi_{\rm cap}=F_\tau^*\varpi_{\rm sheet}$ as well as equality of the pulled-back optical tensors, with zero relative boost. This realizes the two-parameter marked-rim data on constrained vacuum fields. With the relative cotangent potential $+(8\pi G_N)^{-1}\int_C \mu_{\rm sheet}\varpi_{\rm sheet}(\delta F_\tau\circ F_\tau^{-1})$, its exterior derivative on $(\partial_\tau,\partial_{t_0})$ at the origin is $-1/30$ for $r=1/3$. If $F_\tau$ only expresses the same physical seam in changing coordinates, the common-displacement charge cancels. Interpreting the marks as independent observables requires a prescription for measuring them and the full reduced two-form. This collar construction imposes no two-tip boundary condition.

Both calculations rule out inferring angular-charge cancellation from equality of induced metrics alone. A smooth common seam instead requires the cap and sheet projections of the same ambient connection in compatible frames. The mismatched data give a counterexample to the weaker gluing rule. A separate analysis on a complete two-tip diamond excludes a smooth clock repair for an explicit class of marked frames. [Full-diamond test](rim-matching.md)

## Reproduce the numerical coefficient

From the repository root, the first command prints the squared-gradient mean and the one-sided charge. Its expected output is shown below. The second command runs the repository suite and should exit successfully.

~~~sh
python3 -c 'from fractions import Fraction as F; r=F(1,3); norm=9*(F(1,3)-F(1,5)); print(norm, -r*r*norm/4)'
make check
~~~

~~~text
6/5 -1/30
~~~
