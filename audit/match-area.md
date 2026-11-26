# The sharp clock when the waist area varies

On a finite capped diamond whose outer waist carries the uniform boost of Venkatesa Chandrasekaran’s v1, the two-packet test obstructs a continuously differentiable assignment of smooth Hamiltonian vectors for a **single averaged clock**. Both the total area and its angular distribution may vary. The proof needs only the total-area generator. It uses a smooth flat vacuum diamond, cap fraction $a=1/3$, the Einstein symplectic current, and a regular reduction admitting the packet variations described below. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Two-packet derivation](match-packets.md)

## A boost of the exterior waist

Let $S$ bound the incoming Cauchy hypersurface consisting of the cap joined to its null sheet. The cap rim is internal to this hypersurface. Take a smooth, transverse waist before any caustic, with $0<a<1$. The spacetime metric is torsion free. Let $\ell,n$ be future null normals at $S$ with $\ell\cdot n=-1$, and set $E^a{}_b=n^a\ell_b-\ell^a n_b$. Then $E$ acts on $\ell,n$ by $+1,-1$ and kills tangent vectors to $S$. A unit boost of an independently marked boundary frame fixes the points of $S$ and has first derivative $E$ in the normal plane. Equivalently, it adds rapidity to the corner frame relative to the bulk metric. The uniformly shifted frame can be chosen smoothly on nearby marked solutions. [Boundary phase space (3.18)–(3.19)](https://arxiv.org/html/2611.34924v1#S3.E19) · [Corner frame (3.41)](https://arxiv.org/html/2611.34924v1#S3.E41)

For the embedding description choose coordinates $(x^+,x^-,y^A)$ near $S$, with the two sheets on the coordinate axes in each normal plane, and $\partial_+,\partial_-$ on the two null normal lines at $S$. With a smooth cutoff $c=1$ near $S$ and zero near the caps, a representative of the required value and derivative is
$$
 \xi=c(x)\bigl(x^+\partial_+-x^-\partial_-\bigr).
 \tag{1}
$$
The field preserves the two sheet images and fixes the waist pointwise. Such charts follow by extending coordinates on each intersecting sheet along its generators. Local extensions can be summed with a partition of unity because their values and derivatives agree on $S$. Choose the cutoffs on fixed reference collars when varying the solution. On the exterior-frame interpretation, (1) extends the change of frame for evaluating its gravitational charge. The metric and the two cap-normalized null congruences can be kept fixed while the external frame is boosted. Their cuts and the area-ratio conditions then hold throughout the boost. A common change of bulk fields and embedding together has vanishing dressed variation by (3.40). [Moving pullbacks (3.40)](https://arxiv.org/html/2611.34924v1#S3.E40) · [Extended potential (B.21)](https://arxiv.org/html/2611.34924v1#A2.E21)

For a varying waist use a comoving chart, obtainable locally by a simultaneous gauge transformation, so all cut tensors below are pulled back to the same reference $S$. With the outer orientation of (3.51), the Komar form is $Q_\xi=\mu/(8\pi G_N)$. Since $\xi|_S=0$, the term $i_\xi\theta$ vanishes. In varying $\xi$, the contraction giving $Q_{\delta\xi}$ is proportional to $\operatorname{tr}(E\,\delta E)$. It is zero since $\operatorname{tr}(E^2)=2$ for every metric and cut. No cap term arises from (1). Thus, for the tangent $B$ to the exterior frame boost, in v1’s second-slot convention,
$$
 \Omega(\delta,B)=\frac{\delta\mathscr A}{8\pi G_N},\qquad
 G=\sqrt{\mathscr A/(4\pi)},\qquad
 X_G=\frac{G_N}{G}\,B,\qquad \Omega(\delta,X_G)=\delta G .
 \tag{2}
$$
Here $G>0$ and $G_N$ is Newton’s constant. The smooth factor follows directly from $\mathscr A=4\pi G^2$. Varying the half-separation $R$ of flat round tips at fixed $a$ gives $\delta\mathscr A=8\pi R\,\delta R$, so this exterior motion has a nonzero pairing on the allowed family. Equation (2) is integrable on the framed phase space and is independent of the continuation of (1) off the cut. The calculation uses the charge variation at a finite cap, without extending a zero-cap null potential to positive $a$. [Surface-charge variation (3.50b)](https://arxiv.org/html/2611.34924v1#S3.E50.2) · [Unit boost (3.51)](https://arxiv.org/html/2611.34924v1#S3.E51)

**Which affine parameter changes?** For an insertion launched at $S$ with tangent $k=\ell$ fixed in the external frame and with signed affine argument $u$ measured from $S$, the boosted event at that argument is $\exp_S(e^\eta u k)$. Its velocity at zero rapidity is $u\dot\gamma(u)$ along the original geodesic. This satisfies the homogeneous Jacobi equation with initial data $(0,k)$ at fixed metric. The other null eigenline has the opposite sign. This determines the physical orbit of a source as long as its support stays inside the chart and the selected region. The cutoff in (1) serves only in the local charge calculation. The clock uses the cap calibration and the same geometric rays between the same two cuts. Its reading $p_{a,y}(u_S-u_C)$ is invariant even under a constant affine recalibration along each ray. [Clock (3.27)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Geodesic dressing (3.58)](https://arxiv.org/html/2611.34924v1#S3.E58) · [Relative-boost action (5.22)–(5.24)](https://arxiv.org/html/2611.34924v1#S5.E22)

This distinction matters if the corner frame is required to be the affine frame transported from a fixed cap. At fixed metric a tangential Jacobi displacement $f(u)\dot\gamma$ on a generator obeys $f''=0$. Fixing the cap event and affine tangent gives $f(u_C)=f'(u_C)=0$, hence $f=0$. A cut-off dilation in this one fixed affine chart cannot be an allowed nonzero boost. Likewise, gluing two exterior waists cancels the charges of a **common** boost by opposite orientations. When independently marked frames survive the matching, v1 gives the relative angle and its area momentum in (3.64). A reduction which removes the marking altogether needs a separate source of a smooth Hamiltonian for $G$ to use (2). [Unit charge (3.51)](https://arxiv.org/html/2611.34924v1#S3.E51) · [Matched boost charges (3.63)–(3.64)](https://arxiv.org/html/2611.34924v1#S3.E64)

## Removing the varying radius from the sharp clock

Let $\langle\cdot\rangle$ denote the round reference solid-angle average, $\rho=\varrho_S>0$, and $m=\langle\rho\rangle$. In the same marked angular chart the optical excess uses $M=\langle\rho^2\rangle/m$, whereas the uniform boost supplies $G=\sqrt{\langle\rho^2\rangle}$. They obey the exact identity
$$
 M-G=\frac{G}{m(G+m)}\left\langle(\rho-m)^2\right\rangle .
 \tag{3}
$$
At a round waist $\rho=R$ the first derivative of the right side vanishes on every tangent. Its mixed second derivative on tangents $W,Z$ is
$$
 d^2(M-G)(W,Z)=
 \frac{\langle\delta_W\rho\,\delta_Z\rho\rangle
       -\langle\delta_W\rho\rangle\langle\delta_Z\rho\rangle}{R}.
 \tag{4}
$$
Only first variations of the waist density enter. For instance $\rho=R+tP_2(\cos\theta)$ gives $M=R+t^2/(5R)$ and $G^2=R^2+t^2/5$, which reproduce (4). [v1 area and averaged clock (3.28)](https://arxiv.org/html/2611.34924v1#S3.E28)

Set $U=\bar u_*$, $D=U-(1-a)M$ and $E_U=U-(1-a)G$. The shear-squared focusing exponent makes $dD=0$ at the round flat diamond, so $dE_U=0$ there by (3). At $a=1/3$, take the smooth quadrupole $W$ and the signed pair $Z_\eta$ from the two-packet calculation with $R=1$. The latter has **pointwise** $\delta_{Z_\eta}\rho=0$ in the vertex chart. Both cones and their transported frames return to their unperturbed data on collars of the waist, and the same tangent can be used with the later tip fixed. Equation (4) therefore gives
$$
 d^2E_U(W,Z_\eta)=d^2D(W,Z_\eta)\longrightarrow-\frac34.
 \tag{5}
$$
No second-order fixing of the waist area or angular density is needed. Fixing just $\delta_{Z_\eta}\mathscr A=0$ would generally leave a covariance in (4). [Optical Hessian and unchanged waist](match-packets.md)

Assume a regular reduction carrying (2), with the packet tangents admitted, the ordinary Einstein symplectic current for smooth matched bulk data, and local surface terms evaluated on the marked cuts as in (B.21). The two packets cancel distributionally against every fixed smooth tangent on the waist disk. Their cap and waist metric, embedding and frame variations vanish in collars on the chosen lift, so the local surface terms also vanish on these tests. Consequently $\Omega_{\rm flat}(Z_\eta,V)\to0$ for every fixed smooth tangent $V$. [Cauchy and edge pairings](match-packets.md)

If $X_U$ were a $C^1$ assignment of smooth Hamiltonian vectors, $X_{E_U}=X_U-(1-a)X_G$ would have the same regularity. Its value at the critical flat solution would be zero after reduction. Differentiating its Hamilton equation at that solution would give
$$
 d^2E_U(W,Z_\eta)=
 \Omega_{\rm flat}\bigl(Z_\eta,(d_W X_{E_U})_{\rm flat}\bigr)\longrightarrow0 ,
$$
contrary to (5). This establishes the obstruction on the varying-area, exterior-frame interpretation of v1. At the flat solution itself $(1-a)X_G$ solves the clock equation. The contradiction concerns a $C^1$ continuation through it. If a different reduction removes the area boost, the critical excess $D$ still has its packet obstruction under the same current and tangency assumptions. Weak responses, smeared clocks and quantum operator domains remain separate questions. [Flat solution and regularity of the inverse](joint-flat-hessian.md) · [A weak clock bracket](joint-peierls.md)

Run `python3 -B checks/match_packets.py` from the repository root. The final line reads `Limiting clock Hessian: -3/4`. Equations (3)–(4) transfer that coefficient to the varying-area test analytically. Run `make check` to verify the full suite. [Executable optical test](../checks/match_packets.py)
