# Finite-cap closure of the null symplectic form

**Physical question.** Does the paper's reduced symplectic two-form (A.14) stay closed ($D\omega=0$, equivalent to the Jacobi identity) when the spacelike cap area varies in fixed proportion to the corner area as in (3.18)—and if a defect appears at the cap rim, could vacuum evolution between the past and future rims force the two rims to cancel?

**Outcome.** No on both counts. Direct differentiation of (A.14) on the variable-area, fixed-ratio cap data of (3.18) leaves a nonzero three-form localized at the cap rim: $D\omega=\tfrac{b^3}{2}Dr\wedge(Dz')|_b\wedge(Dz)|_b$. This clarifies why the primary reference (Reisenberger) is closed while (A.14) is not: Reisenberger holds the *absolute* area density fixed at each truncation surface ($Dm=0$), whereas (3.18) fixes the *ratio* $b=\epsilon$ ($Dm=\epsilon^2 Dr$). An independent exact check on local data gives $1/16=b^3/2$ at $b=1/2$, and a full one-spacetime vacuum plane-wave family—curved across the past cap rim but flat across the future cap rim—gives a strictly nonzero past-rim contribution and zero future-rim contribution, ruling out cross-diamond cancellation. The smooth-cone identity (3.42b) passes the same closure test because it is the exterior derivative of (3.42a) on $0\le v\le 1$. The obstruction applies specifically to the explicit extension (A.14) at a finite cap; the covariant symplectic current remains available for a fresh reduction with moving caps.

Source scope: equations (3.18)–(3.19) and (A.13)–(A.18). [Paper, (3.18)–(3.19)](https://arxiv.org/pdf/2611.34924v1#page=14) · [Paper, (A.13)–(A.18)](https://arxiv.org/pdf/2611.34924v1#page=56)

## Direct differentiation

Write $D$ for the field-space exterior derivative, $r=\varrho_S^2$, and a prime for $\partial_v$. Hold angular identifications fixed, and on an angular patch of the cut restrict (4.21) to a single polarization $z=z^1$ with $z^2=0$, where the target metric has $\mathsf g_{11}=1$ and its induced connection coefficient vanishes. Work on one branch, suppressing $(16\pi G_N)^{-1}\int_S\epsilon_0$ and the closed canonical corner pairs. Put $b=v_C$, $z_C=z(b)$, and $m=rb^2$ for the cap area density relative to $\epsilon_0$. Equations (A.13)–(A.14) then reduce to

$$
X=Dz-\frac{v z'}{2r}Dr,\qquad
\omega=-\frac12 Dr\wedge z'(1)Dz(1)
       +r\int_1^b v^2\partial_v X\wedge X\,dv ,
$$

with the integral orientation of (A.14). Define the one-form $P=r\int_1^b v^2 z'Dz\,dv$ and the scalar $E=\tfrac12\int_1^b v^3(z')^2\,dv$. Expanding $X$ and integrating the term with $(vz')'Dz$ by parts cancels the explicit corner term at $v=1$. Retaining the endpoint variations in $DP$ and $DE$ and using $Dz_C=(Dz)|_b+z'(b)Db$ gives the exact identity

$$
\omega=DP+Dr\wedge DE-\frac b2 Dm\wedge z'(b)Dz_C.
$$

Under the fixed-ratio condition $b=\epsilon$, we have $Dm=b^2 Dr$, and taking $D$ leaves

$$
D\omega=\frac{b^3}{2}Dr\wedge (Dz')|_b\wedge (Dz)|_b.
$$

By contrast, when the **absolute** cap area density is fixed, $Dm=0$ and the moving upper limit cancels the discrepancy completely. This explains the scope of the cited derivation: Reisenberger defines admissible variations to keep the area density fixed in the chosen chart at each truncation surface, and footnote 31 explains how that removes independent variation of the upper limit. Equation (3.18) of the audited paper instead lets $Dm=\epsilon^2 Dr$ vary, and holding only the *total* corner area fixed still allows local variations of $r(y)$. [Reisenberger, §4.1, condition 2 and §4.2, footnote 31](https://arxiv.org/pdf/1211.3880#page=24)

## Three allowed null-data variations

Around a shear-free background, pick a smooth angular amplitude $t(y)$ supported inside one polarization chart. Let the first variation rescale $r$ uniformly while both caps track (3.18)—the ordinary size variation of a family of round flat diamonds. Let the other two vary the conformal metric on one branch via $Dz=t(y)f(v)$ and $Dz=t(y)g(v)$, choosing smooth profiles supported away from the common corner $v=1$ with

$$
f(b)=0,\quad f'(b)=1,\qquad g(b)=1,\quad g'(b)=0 .
$$

These two variations change the conformal metric and its radial shear at the cap rim independently while keeping the area fixed. The free conformal profiles of §3.2 allow these jets: at a shear-free background the linearized Raychaudhuri equation has no shear source (the source is quadratic), the endpoint jets extend smoothly across the rim with compatible cap metric and extrinsic data, and because both profiles vanish near the common corner $S$, corner matching imposes no constraint between them. Unlike a simultaneous gauge diffeomorphism of fields and edge labels—which leaves dressed null data unchanged—these variations alter the dressed data. (This is a local characteristic-data check; it makes no claim about global existence for independently prescribed past and future caps.)

Per unit variation of $r$, (A.14) evaluates on this ordered triple to $b^3(32\pi G_N)^{-1}\int_S\epsilon_0 t^2>0$. As an independent exact rational check, set $b=1/2$, $f=4(v-1/2)(1-v)^2$, and $g=4(1-v)^2(4v-1)$ (both values and first derivatives vanish at $v=1$). Writing $z=af+cg$ and computing the three cyclic derivatives of the original integral with respect to $(r,a,c)$ gives, in the suppressed units, $-29/840$, $37/240$, and $-2/35$, whose sum is exactly $1/16=b^3/2$. Multiplying by a smooth cutoff equal to $1$ near the rim leaves this endpoint result unchanged.

## A vacuum family with both caps in one spacetime

Could vacuum evolution linking the past and future caps force their rim three-forms to cancel? To test this, we construct a family of exact vacuum spacetimes containing both caps.

First note that the fixed-label identity above extends directly to both polarizations, replacing $z'Dz$ with $\langle z',Dz\rangle_{\mathsf g}$ and $(z')^2$ with $\langle z',z'\rangle_{\mathsf g}$ (by the same integration by parts using metric compatibility and $\nabla_D z'=\nabla_v Dz$). On a shear-free background, the rim wedge evaluated on two profile variations $H_1,H_2$ is their Wronskian $\langle H_1',H_2\rangle-\langle H_2',H_1\rangle$ in this positive target metric.

Start with a Minkowski diamond with vertices $p=(-L,\mathbf 0)$ and $q=(L,\mathbf 0)$, and choose $0<b<1/2$. Vary its overall size and turn on two weak vacuum plane-wave profiles using the exact metrics

$$
g=-dt^2+dX^2+dY^2+dZ^2+
       [a h_1(U)+c h_2(U)](X^2-Y^2)dU^2,\qquad U=t-Z.
$$

Because the transverse Laplacian of $X^2-Y^2$ vanishes, every metric in this family is Ricci-flat. Its only independent curvature components in null coordinates are $R_{UiUj}=-[a h_1+c h_2]\,\mathrm{diag}(1,-1)_{ij}$ for $i,j=X,Y$. Along an unperturbed past generator with unit spatial direction $n$ at affine distance $s$ from $p$, we have $U+L=s(1-n_Z)$. Set $h_1=1$ and $h_2=(U+L)/L$ on an open neighborhood of $0\le U+L\le 2bL$, and taper both smoothly to zero on an open neighborhood of $2(1-b)L\le U+L\le 2L$. Since $b<1/2$, these two intervals are disjoint: the entire segment from the future vertex to the future cap rim lies in the flat collar at the background and stays flat for sufficiently small $(a,c)$. Fix past angular labels in the vertex frame, transport the common-corner labels to the future rim holding edge coordinate identifications fixed, and let the spacelike cap embeddings follow the fixed area ratio (3.18).

On each past ray, let $W(n)$ denote the first perturbation of the trace-free optical tidal tensor; the second is $s(1-n_Z)W(n)/L$. Solving the linearized Jacobi equation with $J(0)=0$, $J'(0)=1$ and taking the trace-free part of $J^\top J/s^2$ gives the linearized conformal screen metric in the fixed vertex frame:

$$
H_i(s)=-\frac{2}{s}\int_0^s (s-x)x\,\delta_i R_{AkBk}(x)\,dx .
$$

On the background, $s=Lv$, and switching from fixed $s$ to fixed $v$ adds nothing to the conformal variation because the background conformal metric is radially constant. Integrating yields

$$
H_1=-\frac{L^2 v^2}{3}W(n),\qquad
H_2=-\frac{(1-n_Z)L^2v^3}{6}W(n).
$$

At the past cap rim $v=b$, their Wronskian is $-L^4 b^4(1-n_Z)\lVert W(n)\rVert^2/18$. Because $W(n)$ is nonzero (for instance along a ray in the negative-$Z$ direction), its integral over the sphere has a strict sign. At the future cap rim, meanwhile, both $H_i'$ vanish identically: a cone emerging from a regular vertex inside a flat collar has radially constant conformal metric even after any radius-independent angular relabeling. The third variation—a uniform size change at $a=c=0$—shifts $r$ while leaving the round conformal profile untouched, so any $r$-variations along the two wave directions drop out of the three-form evaluated on this triple. Thus this exact vacuum family realizes the closure defect for an entire open interval of cap ratios $0<b<1/2$ with zero compensating contribution from the opposite rim.

## Edge terms, gluing and scope of a repair

None of the other displayed terms in Appendix A.2 cancels this defect: the boost and angular pieces $D\lambda\wedge Dr$ and $D\widetilde t_i\wedge Ds^i$ are closed on every pullback; the cap-joint potential (A.18) gives a two-form proportional to $D\log(-n_C\cdot\ell)\wedge Dm$, which is closed even if the cap normal depends on radiation; and an exact corner shift $DB_S$ leaves the two-form unchanged. Gluing duplicate data at the *same* rim with opposite orientations cancels internal flux inside the union, but an unglued external rim still requires a properly closed reduced form.

On the fixed-label, single-polarization sector, adding $(b/2)Dm\wedge z'(b)Dz_C$ restores $D\omega=0$ directly. Finding its full covariant extension—including angular displacements, cap interior data, and the resulting physical canonical brackets—requires varying the complete cap-plus-null potential with the moving cut. Alternatively, holding the cap conformal metric fixed removes these specific rim variations, and holding the corner area density fixed on every generator removes the area variation; however, the phase space declared in (3.18)–(3.19) imposes neither restriction. Finally, equation (3.42) integrates over $0\le v\le 1$ (smooth vertex), so its exactness does not supply the coupled canonical brackets at a finite outer cap.
