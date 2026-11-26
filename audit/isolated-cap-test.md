# Which boundary responses can change a one-observer bracket?

Two tidal measurements test what an isolated cap would have to reproduce in the round flat diamond. Suppose its gravitational response agrees with the joined Einstein Hamilton equation on all compact radial quadrupole tests, and the change of boundary prescription adds a regular response at the endpoints. Under the marking and timing hypotheses below, the change in any pair of linear clock brackets then depends on just two moments of each reading. One explicit wave gives a nonzero bracket, $+3G_N/160$, for every prescription in this class. Another measures its one undetermined coefficient. Deriving the hypotheses from the isolated-cap action is a **proof gap**. [Chandrasekaran, arXiv:2611.34924v1, affine reading (3.27)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Moving boundary potential (B.21)](https://arxiv.org/html/2611.34924v1#A2.E21)

## A criterion for matching the bracket

Use waist radius one, the same inertial observer, marked tetrad, lower tip at $t=0$ and return tip at $t=2$. Keep the sky-weighted waist radius $M=1$. For cap ratio $0<c<1$, $D_c=\bar u_c-(1-c)M$ is critical at flat space. The measured *linear* observable is $L_c[f]=d^2D_c(W,f)$, the change in clock response to a fixed reference vacuum wave $W$. Take one real, even quadrupole with polarization $S=\operatorname{diag}(-1/2,-1/2,1)$. Write $f(s)=F(2s)$ for the radial master of its transverse-traceless (TT) metric and $G'_f$ for its optical strain slope with the regular vertex calibration. For the reference slope $p=G'_W$,
$$
 L_c[f]=\frac3{20}\int_c^1 s(1-s)p(s)G'_f(s)\,ds .
$$
Source and sign conventions are those of the full Minkowski calculation, with $\{q,\pi\}=1$. [Optical source and master equation](weak-master.md) · [Vertex calibration](weak-normalization.md) · [Two cap fractions](timing-caps.md)

Compare two putative linear response rules for a common vector space of these readings, one of which may be the radiative Minkowski rule. The following are sufficient tests of their difference.

1. Each rule gives an antisymmetric equal-time bracket on this space, with the same timing prescription. Project the metric response onto the measured quadrupole. For **every** compact master test $g\in C_c^\infty(0,1)$, both Hamilton equations for a reading $L$ reduce to $A\langle \partial_s^9 f_{X_L},g\rangle=L[g]$, $A=3/(5120G_N)$. This includes waves crossing either rim. Equality of the equations on tests supported away from the rims is weaker.
2. The difference $P_L$ of these projected masters extends regularly with its interior jets to the closed sampling interval. The full timing-prescribed difference when paired with any second reading $K$ is $K[P_L]$. This requires common vertex and waist calibration and excludes additional contractions of independently varying marks or distributions supported only at the endpoints. For a limit of two smooth detectors it suffices that the extra response converge smoothly on a fixed neighborhood of the entire closed sampled interval, including both rims and that any separate mark term tend to zero.

Test 1 implies $\partial_s^9P_L=0$ on the open interval. Hence $P_L$ is a single polynomial of degree at most eight, including across the two rims. With the same regular vertex used in both readings, all powers through degree six have zero linearized optical slope. Indeed, their radial scalar $[F(t+r)-F(t-r)]/r$ has degree at most five, so its four spatial TT derivatives have zero curvature. For $n=7,8$, the powers $s^n$ have slope $n(n-1)(n-3)(n-5)(n-6)s^{n-6}/16$, giving $21s$ and $105s^2$. Smoothly cut off these masters outside a neighborhood of $[0,1]$ to prepare regular vacuum waves. The optical moments in this basis are
$$
 m(L_c)=(L_c[s^7],L_c[s^8])
 =\frac3{20}\left(21\int_c^1s^2(1-s)p\,ds,\;105\int_c^1s^3(1-s)p\,ds\right).
 \tag{1}
$$

If $m(K)=0$, then $K[P_L]=0$ for every $L$. Antisymmetry forces the bracket difference to vanish when the moment vector in the first slot vanishes as well. It thus descends to an alternating form on the image of $m$ in $\mathbb R^2$. Every such form has the form
$$
 \Delta\{L,K\}=\kappa\,\det\!\begin{pmatrix}m(L)\\m(K)\end{pmatrix}.
 \tag{2}
$$
The same coefficient $\kappa$ applies to every pair on this space. This argument also admits image dimension zero or one, when the change vanishes. The compact equations alone cannot determine $\kappa$. For example, as a linear response model, supplement the radiative system with a separate pair of amplitudes $x,y$ with constant bracket $\{x,y\}=\kappa$. Read the total master as $f+x s^7+y s^8$ on the closed interval. The new brackets differ by precisely (2), and the added masters satisfy the homogeneous compact equation. This product construction illustrates the freedom in the tests. A physical independent cap would need its own derivation of the amplitudes and their symplectic form.

## A wave for which the bracket is fixed

Take $a=1/3$, $b=1/2$. In the four-dimensional space of slopes spanned by $s^4,s^5,s^6,s^7$, prepare the unique polynomial $p$ satisfying
$$
 p(b)=1,\qquad \int_b^1 (s^{-1}-1)p(s)\,ds=0,\qquad
 \int_a^b s^j(1-s)p(s)\,ds=0\quad (j=2,3).
 \tag{3}
$$
The executable check solves the four rational equations by elimination with four nonzero pivots. Each monomial $s^j$ is realized by a nonzero multiple of the smooth vacuum master $s^{j+6}$ on the measurement collar, cut off away from that collar and the vertex. The last two conditions give $m(L_a)=m(L_b)$. The second removes the outer clock's vertex jump. Its rim jump is $d_b=-16G_N(1-b)p(b)=-8G_N$. The ambient nested-cap bracket is $A d_b^2/2=3G_N/160$ for either time order, also verified by direct integration of the two response profiles. Equation (2) preserves this number for the common antisymmetric prescription of the matching test. This yields a one-observer check even when the boundary coefficient is unknown. [Ambient jump and timing integral](timing-caps.md)

For a second shot use $p=(152s^4-208s^5)/3$. Its outer clock has the same calibration and ambient bracket. Now the determinant in (2) equals $-4454779/188956800$. Comparing the two shots isolates the coefficient in (2). A different result for the first shot would require a failure of at least one matching hypothesis. For example, a rim current acting on metric tests across the cut changes test 1; an independently observed boundary frame can change test 2. Whether the action permits either effect depends on the chosen reduction. [Independent frames and current](rim-matching.md) · [Joined current on the closed diamond](weak-boundary.md)

## Measuring the two tidal modes on the waist disk

The two modes in (1) also have an explicit gravitational symplectic product. Keep only their amplitudes $x,y$ for this separate calculation and take the finite ball $t=1$, $r\le1$ in the background chart. Fix the embeddings in the disk integral and use the Cartesian TT metric representatives above. The linear ADM momentum is $\dot h^{ij}/(32\pi G_N)$. Write $h_n$ for the metric of master $s^n$ and take $\Omega=\int\delta\pi^{ij}\wedge\delta h_{ij}$. Angular averaging gives the radial integrand, including the $r^2$ Jacobian,
$$
 \frac{r^2}{8G_N}\left\langle
 \dot h_7:h_8-h_7:\dot h_8\right\rangle
 =-\frac{1}{G_N}\left(\frac{3969}{64}r^2+\frac{8127}{320}r^6\right).
$$
The check obtains each Cartesian contraction from the radial, mixed and trace-free screen components of the TT fields. Integration gives $\Omega_B(\partial_x,\partial_y)=-243/(10G_N)$. Thus the fixed-chart two-mode plane is symplectic. For the reference $W$ with master $s^7$, use $p=21s$ in (1). The determinant is $146461/76800$ and the bracket on this plane is
$$
 \{L_a,L_b\}_{\rm plane}
 =-\frac{\det(m(L_a),m(L_b))}{\Omega_B(\partial_x,\partial_y)}
 =\frac{146461}{1866240}G_N .
$$
This value comes from restricting the metric variations **before** inverting the two-form. The plane omits the compact radial test functions in hypothesis 1, so its inverse cannot set $\kappa$ in an isolated-cap theory. The separate pullback confirms that the homogeneous optical responses can carry gravitational symplectic weight in a finite region. Establishing their status after imposing the boundary and gauge constraints, a bracket for nonlinear sharp clocks at finite amplitude, and existence of a fixed-size quantum state remain open. [TT normalization and finite-ball convention](weak-normalization.md) · [Geometric cap and sheet data](joint-clock.md)

Run `python3 -B checks/isolated_cap_test.py` from the repository root. The expected output in units $G_N=1$ is below. Run `make check` for the suite. [Executable calculation](../checks/isolated_cap_test.py)

~~~text
Equal tidal moments at both caps; earlier and later brackets = 3/160
Control wave tidal determinant = -4454779/188956800
Waist ADM product = -243/10; restricted two-mode bracket = 146461/1866240
~~~
