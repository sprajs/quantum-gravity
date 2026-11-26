# Angular momentum on a matched Kerr sphere

On a sphere in the exterior of Kerr, a rotation preserves the induced metric and has a one-sided angular charge equal to the black hole spin up to orientation. In a single smooth spacetime the adjacent faces measure that same momentum with opposite boundary orientations. This gives a vacuum example where measuring a charge on one side and measuring the residual charge of the joined system give different answers. It also tests which matching data the intrinsic metric supplies. [Chandrasekaran, arXiv:2611.34924v1, (3.56)–(3.57c)](https://arxiv.org/html/2611.34924v1#S3.E57.3) · [Angular endpoint potential, Eq. (5)](rim-potential.md)

## A rotation which preserves the entire rim metric

Use units with $c=1$, geometric mass $m=G_N M$, and Kerr spin parameter $a=J/M$. Fix $r>2m$, $|a|<m$, and a marked axial generator $Y=\partial_\phi$ of period $2\pi$. On the Boyer–Lindquist slice $t=0$ define
$$
 \Sigma=r^2+a^2\cos^2\theta,\qquad \Delta=r^2-2mr+a^2,\qquad
 A=(r^2+a^2)^2-a^2\Delta\sin^2\theta.
$$
The rim metric, radial metric coefficient, lapse and azimuthal shift are
$$
 q_{AB}dy^A dy^B=\Sigma\,d\theta^2+
     \frac{A\sin^2\theta}{\Sigma}\,d\phi^2,\qquad
 h_{rr}=\frac{\Sigma}{\Delta},\qquad
 N^2=\frac{\Sigma\Delta}{A},\qquad \beta^\phi=-\frac{2mar}{A}.
$$
Thus $+a$ and $-a$ give exactly the same three-metric on the slice and the same two-metric in the common marked chart. Each rim admits $Y$ as an exact Killing field. Along the Kerr family through Schwarzschild, $\partial_a q_{AB}|_{a=0}=0$ and the background rim is round. At finite spin the two induced metrics agree and are generally nonspherical. Reversing the marking by $\phi\mapsto-\phi$ also reverses the chosen axial generator, so the sign comparison uses the same $Y$ throughout. [Boyer and Lindquist, *Maximal Analytic Extension of the Kerr Metric*](https://doi.org/10.1063/1.1705193) · [Explicit Boyer–Lindquist metric](https://link.springer.com/article/10.1007/s00023-024-01472-9)

Let $T$ be the future unit normal to the slice and $s=\sqrt{\Delta/\Sigma}\,\partial_r$ its outward radial unit vector. Choose $\ell=T+s$, $n=(T-s)/2$ at the rim, and $\varpi_B=-n\cdot\nabla_B\ell=K_{Bs}$ with $K_{ij}=g(\nabla_i T,e_j)$. The outgoing orthogonal null geodesics give a vacuum sheet collar through this same sphere. Stationarity gives $K=-\mathcal L_\beta h/(2N)$ as a tensor, hence
$$
 \varpi_\phi=-\frac{q_{\phi\phi}}{2N}\sqrt{\frac{\Delta}{\Sigma}}\,
                      \partial_r\beta^\phi,\qquad \varpi_\theta=0.
 \tag{1}
$$
For small spin, $\varpi_\phi=-3G_N J\sin^2\theta/r^2+O(a^3)$ at fixed $m,r$. This is the axial dipole on the round background. It pairs pointwise to zero with $D^A P_2(\cos\theta)$, the electric quadrupole in the clock test. A change $\ell\mapsto e^b\ell$ adds $db$ to $\varpi$. Since $Y$ preserves the area form on every one of these spheres, $\int_C\mu\,Y^A D_A b=0$ for every smooth single-valued $b$. [Cap-to-sheet normal-frame identity, Eq. (4)](joint-edges.md) · [Round clock quadrupole, Eq. (3)](joint-angular.md)

Take the one-sided orientation giving $P_C[Y]=(8\pi G_N)^{-1}\int_C\mu\,\varpi_A Y^A$. With $x=\cos\theta$, $\mu=\sqrt A\sin\theta\,d\theta\,d\phi$, (1) gives
$$
 P_C[Y]=-\frac{ma}{4G_N}\int_{-1}^1
   \frac{(1-x^2)(r\partial_r A-A)}{\Sigma^2}\,dx=-\frac{ma}{G_N}=-J.
 \tag{2}
$$
For the last equality, the integrand is the $x$ derivative of $2x+(r^2+a^2)x(1-x^2)/\Sigma$, with endpoint difference $4$. This proves the finite-spin coefficient at every stated radius. The conventional positive angular momentum is $-P_C[Y]$ with the chosen $K$ and orientation. [Ashtekar, Beetle and Lewandowski, rotating isolated horizons and the Komar angular momentum](https://arxiv.org/abs/gr-qc/0103026)

## What remains after joining

Fix the other end of the sheet's angular map and let $\alpha$ be the rotation angle of this rim alone. In the one-sided endpoint potential its contribution is $-J\,d\alpha$, with two-form $-dJ\wedge d\alpha$. The momentum (2) is integrable on this family and $\partial_J$ about Schwarzschild has unit pairing with a rotation in the first slot. This example realizes a finite relative rotation preserving $q$, and a variable conjugate momentum, for independently marked boundary data. A simultaneous spacetime diffeomorphism of the metric and embedding leaves all pulled-back data fixed. A separate angular frame held at a subregion boundary is what gives the rotation parameter its meaning. [Moving pullbacks, v1 (3.40)](https://arxiv.org/html/2611.34924v1#S3.E40)

Across an ordinary internal seam, express both sectors in one angular chart and one normal frame. The tangential cap momentum gives the same $K_{As}$ as (1), and the two induced boundary orientations are opposite. A common angular displacement couples to the difference of the two momentum densities, so both its charge and its spin variation vanish for the smoothly matched Kerr geometry. Taking $+a$ data on one side and $-a$ data on the other with the identity marking gives a formal difference $-2J$ in the displayed orientation. These data violate angular momentum matching. For example, joining the two spacelike Kerr collars with that marking makes the normal flux of $K^i{}_j-\delta^i_j\operatorname{tr}K$ jump in the axial momentum constraint. A smooth vacuum gluing cannot have that jump. If one uses a comparison map reversing the axis, the generator must be transported along with the data. [Cap and sheet constraints](joint-edges.md)

The exterior restriction matters. A smooth vacuum cap ball with an axial Killing field of its entire three-metric and no inner boundary has zero axial flux through its boundary. Integrate $D_i[(K^i{}_j-\delta^i_j\operatorname{tr}K)Y^j]$ over the ball. The momentum constraint kills the divergence of the tensor, and the Killing equation kills its contraction with $D_iY_j$. A Kerr exterior annulus instead has an inner sphere with an equal, oppositely oriented flux. The Kerr calculation therefore supplies an exact counterexample to inferring a zero **one-sided** momentum from metric matching, while the regular two-tip clock experiment and the Hamiltonian on its reduced phase space require additional evidence. [Independent vacuum data in the quadrupole sector](match-independent.md)

Run `python3 -B checks/match_rotation.py` and `make check` from the repository root. The focused check differentiates the exact shift by a complex step and integrates (1) on twelve exterior spheres, including near-extremal spin and the Schwarzschild limit. Its expected line is `Kerr rim metrics agree for opposite spins and axial charges equal -J within 1e-10`. [Executable check](../checks/match_rotation.py)
