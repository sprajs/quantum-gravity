# A finite null sheet derived from the metric potential

For the fixed cap ratio of Venkatesa Chandrasekaran's v1, the Einstein metric potential gives an explicit correction to the radiative part of (A.14). In a frame transported along the generators, both polarizations contribute. The coefficient is fixed by the vacuum focusing constraint. Tangential motion of either cut has a second, independently calculable charge. Even with these terms included, spacelike cap data can carry a nonzero symplectic product with all incoming sheet and rim variations zero. [Versioned manuscript](https://arxiv.org/abs/2611.34924v1) · [Boundary conditions (3.18)](https://arxiv.org/html/2611.34924v1#S3.E18) · [Reduced pullback (3.45)](https://arxiv.org/html/2611.34924v1#S3.E45)

## Direct pullback of (A.6)

Take one regular sheet in torsion-free four-dimensional vacuum gravity, with closed cuts, before a caustic or expansion turning point. A reference coordinate $x$ fixes the two ends. In a collar of the sheet use the metric
$$
g=-2\,dx\,dw+F\,dx^2+
q_{AB}(dy^A-U^A dx)(dy^B-U^B dx),\qquad F|_{w=0}=0 .
$$
The metric fields here are pulled back to the reference collar. The null generator on $w=0$ is $L=\partial_x+U^A\partial_A$ and its transverse null normal is $N=\partial_w$. Thus $L^\flat=-dw$ there and $g(L,N)=-1$. This chooses the extensions of the normal frames. Let $\mu=M\epsilon_0$ be the cut area, $\theta=\mu^{-1}(\partial_x+\mathcal L_U)\mu$ its expansion, $\kappa=\tfrac12\partial_w F$, and $\varpi_A=-N_b\nabla_A L^b$. Write $D$ for an exterior derivative on field space. The branch orientation below agrees with the integral from $1$ to $b$ in (A.14). [Metric potential (A.6)](https://arxiv.org/html/2611.34924v1#A1.E6) · [Moving pullbacks (3.40)](https://arxiv.org/html/2611.34924v1#S3.E40)

Here is a direct contraction of the metric current. For $h_{ab}=Dg_{ab}$, raise its indices with $g$. Then $h=2D\log M$, $h^{wx}=0$, $h^{wA}=DU^A$ and $h^{ww}=DF$. On the sheet, $\Gamma^w_{AB}=K_{AB}=\tfrac12(\partial_x+\mathcal L_U)q_{AB}$ and $\Gamma^w_{wA}=-\varpi_A$. With $\epsilon_{w x12}$ positive, the flux in (A.6) is consequently
$$
\nabla_e h^{we}-\nabla^w h=
 2D\kappa+\operatorname{div}_\mu DU
 + K^{AB}Dq_{AB}-2\varpi_A DU^A+L(2D\log M).
$$
Integrating the last term by parts and subtracting the field-exact $2D\int dx\,\mu\kappa$ gives the one-form
$$
16\pi G_N\Theta_{\mathscr H}
 =\int dx\int \mu\big[
 \sigma^{AB}Dq_{AB}-(2\kappa+\theta)D\log M-2\varpi_A DU^A\big]
 +2\left[\int D\mu\right]_{\rm ends}.
\tag{1}
$$
The angular divergence integrates to zero. Equation (1) also follows from (A.8)–(A.9) with $\psi=0$ and $\upsilon^a=(DU)^a$. On domains with angular sides the divergence would have its own boundary integral. Taking $D$ in this fixed reference chart includes the response of the generator direction, the cut geometry and their mixed variations. A simultaneous spacetime diffeomorphism of the metric and its embedding leaves these pulled-back fields fixed. [Null flux (A.8)–(A.9)](https://arxiv.org/html/2611.34924v1#A1.E8) · [Extended endpoint potential (B.21)](https://arxiv.org/html/2611.34924v1#A2.E21)

## Both polarizations and the area of the rim

First transport the angular labels, so $U=DU=0$. Set $x=v$, let $r=\varrho_S^2(y)$ and take $b=\epsilon$ fixed, $0<b<1$. Equation (A.11) gives $M=rv^2$. Use primes for $\partial_v$, $p=z'$ and the target metric in (4.21), with $\langle p,p\rangle=(p^1)^2+e^{2z^1}(p^2)^2$. Then
$$
\theta=2/v,\qquad
\sigma^{AB}Dq_{AB}=\langle p,Dz\rangle,\qquad
\sigma^{AB}\sigma_{AB}=\tfrac12|p|^2,\qquad
\kappa_v=\tfrac v4|p|^2 .
$$
The last equality follows from $L\theta=\kappa_v\theta-\theta^2/2-\sigma^{AB}\sigma_{AB}$, using $R_{LL}=0$. Area radius need not be affine. Suppress $(16\pi G_N)^{-1}\int_S\epsilon_0$ and define
$$
P=r\int_1^b v^2\langle p,D_v z\rangle\,dv,\qquad
E=\tfrac12\int_1^b v^3|p|^2\,dv,\qquad m=rb^2 .
$$
Here $D_v z$ varies the field at fixed $v$. The shear supplies $P$, the inaffinity supplies $-E\,Dr$, and the integrated expansion plus endpoint term supplies $(b^2-1)Dr$. The last term is exact for fixed $b$. The sheet therefore contributes $D(P-E\,Dr)$. [Intrinsic metric (A.11)](https://arxiv.org/html/2611.34924v1#A1.E11) · [Target metric (4.21)](https://arxiv.org/html/2611.34924v1#S4.E21.2) · [Vacuum inaffinity (A.23d)](https://arxiv.org/html/2611.34924v1#A1.E23.4)

For comparison call the last two terms in the square brackets of (A.14) $\omega_{\rm rad}$, including its mixed term at $S$. To verify the comparison even when $b$ varies, set $X=D_vz-vp\,Dr/(2r)$ in its integral. Metric compatibility and the torsion-free identity $\nabla_D p=\nabla_v D_vz$ give $D\langle p,D_vz\rangle=\langle\nabla_vD_vz\wedge D_vz\rangle$. Expansion of $\langle\nabla_v X\wedge X\rangle$ leaves the two cross terms. Integrating the one containing $\nabla_v(vp)$ by parts cancels the explicit mixed term at $v=1$. Keeping the upper-limit terms in $DP,DE$ gives
$$
\omega_{\rm rad}
=D(P-E\,Dr)-\tfrac b2 Dm\wedge\langle p_b,Dz_C\rangle,\qquad
z_C=z(b),\quad Dz_C=(D_vz)_b+p_bDb .
\tag{2}
$$
In particular the fixed-ratio sheet derived in (1) contributes
$$
\boxed{\ \omega_{\mathscr H}=\omega_{\rm rad}
+\tfrac{b^3}{2}Dr\wedge\langle p_b,(D_vz)_b\rangle\ },\qquad Db=0 .
\tag{3}
$$
The exterior derivative of the added term cancels the [finite-cap defect](cap-crosscheck.md), including for generic two-polarization data. The defect in (A.14) as written is thus repairable on this sector. Holding the absolute rim area density fixed removes the term in (2). Holding only the integrated area fixed leaves the local $Dr(y)$ free. [Printed two-form (A.14)](https://arxiv.org/html/2611.34924v1#A1.E14X) · [Rim area variations (A.17)](https://arxiv.org/html/2611.34924v1#A1.E17.3)

A varying cutoff provides a check of which pieces depend on the frame. Use $x\in[0,1]$ with $V(x)=b+(1-b)x$, oriented from $x=1$ to $x=0$, and $v=V(x)$. Allow $b=b(y)$ to vary. In (1), $\kappa_x=(1-b)\kappa_v$, $\theta_x=2(1-b)/v$, $D_x z=D_v z+p(1-x)Db$, and $D\log M=Dr/r+2(1-x)Db/v$. The shear and inaffinity terms proportional to $|p|^2Db$ cancel. The rest gives
$$
 \Theta_{\mathscr H}=P-E\,Dr+(b^2-1)Dr+2r(1+b)Db,\qquad
 \omega_{\mathscr H}=\omega_{\rm rad}
 +\tfrac b2 Dm\wedge\langle p_b,Dz_C\rangle+2Dr\wedge Db .
\tag{4}
$$
These formulas use the suppressed units above. The last closed term depends on the prescribed normalization. For example replacing $V$ by a smooth monotone interpolation and writing $W=\partial_x V$ gives the additional endpoint one-forms $-2\log W_C\,Dm+2\log W_S\,Dr$ alongside $(b^2-1)Dr$, modulo an exact term. This follows on setting $T=(D_x V)|_{x(V)}$, using $D_v\log W=\partial_vT-T\partial_v\log W$ and integrating once in $v$. Equation (4) uses $W_C=W_S=1-b$ and is equivalent to this expression modulo an exact one-form. A varying $b$ tests a larger family than the fixed regulator in (3.18).

## Angular motion of the cuts

Use a fixed-end coordinate $x$ and the transported angular chart as the base chart. At each $x$ pull the metric back by an angular map $F_x$, leaving $x,w$ unchanged in the collar. Its Eulerian variation is $Y=DF_x\circ F_x^{-1}$. A pure change of this identification gives $Dq=\mathcal L_Yq$, $D\log M=\operatorname{div}_\mu Y$ and $DU=-\partial_xY$ in the base chart. The last sign follows by differentiating the pullback of $L=\partial_x$. Integration by parts on the closed cut converts the first two angular terms in (1) to $\mu Y^A[\nabla_A(2\kappa+\theta)-2\nabla_B\sigma^B{}_A]$, where $\nabla_A$ is the Levi-Civita derivative of $q$. The vacuum projection $R_{LA}=0$ gives the nonaffine null Codazzi equation
$$
 \partial_x(\mu\varpi_A)
 =\mu\,[\nabla_A(\kappa+\theta/2)-\nabla_B\sigma^B{}_A] .
$$
This also follows by rescaling the affine normal in (3.57c) and projecting on the cuts. Adding the $2\mu\varpi_A\partial_xY^A$ term from $DU$ now gives a total $x$ derivative. For arbitrary variations of the transported data and angular maps the additional one-form is
$$
 16\pi G_N\Theta_{\rm ang}
 =2\left[\int \mu\,\varpi_A (DF_x\circ F_x^{-1})^A\right]_{\rm ends}.
\tag{5}
$$
In particular a displacement supported away from both ends has zero charge. A map fixed at $S$ may still move the rim. Differentiating the whole one-form includes the Lie bracket of successive angular displacements through $DY(\delta_1,\delta_2)=-[Y_1,Y_2]$ for commuting variations. The rim twist can be recovered by integrating the displayed constraint with its value at $S$. The closed two-form is $D(\Theta_{\mathscr H}+\Theta_{\rm ang})$ in these transported variables. Equation (5) reconstructs the tangential charge in this chart. Adding it directly to the printed $D\widetilde t_i\wedge Ds^i$ could count angular motion twice. Identifying independent momenta requires matching the two branches and their frames at $S$. [Normal connection and affine null constraint (3.56)–(3.57)](https://arxiv.org/html/2611.34924v1#S3.E57.3) · [Printed twist variables (A.12)](https://arxiv.org/html/2611.34924v1#A1.E12.3)

## What the cap contributes

The joint one-form in (A.18) contributes $-\epsilon_C(8\pi G_N)^{-1}\int_C D\log(-n_C\cdot\ell)\wedge D\mu_C$. Its exterior derivative vanishes. It cannot supply the derivative needed in (3). A field-exact $DB$ in a potential preserves its two-form. A spacetime-exact improvement $dY$ of the local current potential adds $D\int_{\partial\mathscr H}Y$ to a sheet two-form. Equal and oppositely oriented improvements cancel across a compatible interface. Thus closure by itself cannot fix the allocation of every closed cut term between a cap and its sheet. The shared action, normalizations and embeddings must make that allocation consistently. [Cap joint (A.18)](https://arxiv.org/html/2611.34924v1#A1.E18) · [Boundary action (3.15a)](https://arxiv.org/html/2611.34924v1#S3.E15.1)

There is a direct test of the missing spacelike interior. On a flat Minkowski initial-cap ball let $T_{ij}$ be a nonzero smooth transverse traceless tensor supported strictly inside the ball. One construction applies $(P_{ik}P_{jl}-\tfrac12P_{ij}P_{kl})$ to a compactly supported symmetric seed $S_{kl}$ in Euclidean coordinates, where $P_{ij}=\delta_{ij}\Delta-\partial_i\partial_j$. Divergence vanishes since $\partial_iP_{ij}=0$, and trace vanishes since $P_{ik}P_{ij}=\Delta P_{kj}$ and $P_{ii}=2\Delta$. A seed with nonzero transverse traceless symbol gives $T\ne0$. Use the ADM momentum density with its usual $1/(16\pi G_N)$ already included. The linearized initial variations $(Dh,D\pi)=(T,0)$ and $(0,T)$ both satisfy the vacuum Hamiltonian and momentum constraints. They vanish with all derivatives near the rim. Finite propagation in linearized vacuum theory leaves the expanding outgoing generators from that rim undisturbed, since those generators run outwards at light speed. Nevertheless the absolute value of their cap symplectic product is $\int T_{ij}T^{ij}\,d^3x>0$. The opposite sheet can receive the signal. This is a linearized interior witness on the incoming initial surface, without an assumption of nonlinear compact shielding. [Canonical cap potential (3.46)](https://arxiv.org/html/2611.34924v1#S3.E46) · [Cap and sheet data in (3.19)](https://arxiv.org/html/2611.34924v1#S3.E19)

The full reduction still requires the cap canonical fields, their matching, the corner and boost frames, and the kernel and inverse of the resulting constrained two-form. Equations (1)–(5) derive a closed sheet contribution for specified variations. The full Poisson brackets and the physical conjecture remain open.

## Reproduce the checks

Run the following from the repository root. [Executable calculation](../checks/rim_potential.py)

~~~sh
python3 checks/rim_potential.py
make check
~~~

The focused check differentiates (1) in the linear interpolation chart using complex-step derivatives and compares all six coordinate pairs $(r,b,z\text{-amplitude}_1,z\text{-amplitude}_2)$ to the Christoffel and endpoint terms of (A.14) and (4). Both backgrounds have two nonzero polarizations and shear at $S$. A separate periodic angular calculation uses $q_{AB}=rv^2\,\mathrm{diag}(e^z,e^{-z})$, $z=0.7v\cos y$, and $Y^y=(1-v)(\sin y+\sin 2y)$. It evaluates the angular part of (1) and the charge (5) independently after solving the angular constraint. This is an integral identity on a closed periodic test cut. The expected output is

~~~text
b=0.4: six two-form components agree within 2e-8
b=0.7: six two-form components agree within 2e-8
Angular flux and endpoint charge (cut average): 0.00460096
~~~

The full suite should exit successfully.
