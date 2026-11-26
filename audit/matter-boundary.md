# A conserved scalar charge on both capped cones

A freely propagating real massless scalar can carry one canonical pair through an entire Einstein–scalar diamond. At fixed waist area, its scalar offset can vary through all real values. Its conjugate charge can vary through an open interval on which **both** geometric clocks pass the same ceiling. Quantizing this exact homogeneous family gives infinitely many mutually orthogonal accepted states. The boundary choice is transparent matching to the same scalar outside, with its target origin available as a calibration. Chandrasekaran's four-dimensional construction specifies vacuum geometric data. Its variational principle supplies neither a scalar boundary condition nor an apparatus for reading a scalar value. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.15), (3.18)–(3.19)](https://arxiv.org/html/2611.34924v1#S3.E18)

## Which charge crosses the diamond?

Use signature $(-+++)$ and the scalar Lagrangian four-form $L_\phi=-d\phi\wedge\star d\phi/2$. For $X\phi=1$ and $Xg=0$, its on-shell shift current and symplectic potential are
$$
J=-\star d\phi,\qquad dJ=0,\qquad
\theta_\phi(\delta)=J\,\delta\phi .
$$
Use $\Omega(\delta_1,\delta_2)=\int_C[\delta_1\theta(\delta_2)-\delta_2\theta(\delta_1)]$ for commuting variations. On a fixed oriented cut $C$ this gives $\Omega(\delta,X)=\delta Q_C$ with $Q_C=\int_C J$. Variation of the Hodge star includes the metric response. The gravitational potential has zero contraction with the scalar shift and is shift invariant. These formulas use the action above with no extra scalar joint term.

Let $C_p$ consist of the initial spacelike cap and the rest of the past-tip light cone up to the waist $S$. Define $C_q$ by the analogous future cap and cone. Orient both as Cauchy cuts with the same boundary orientation at $S$. Stokes' theorem gives $Q_{C_p}=Q_{C_q}$, also equal to the charge on any intervening spacelike disk spanning $S$. Integrating over the *outward* boundary of the four-volume subtracts the two equal charges. The vanishing difference expresses conservation and permits either individual charge to be nonzero.

Across an artificial interface, identify the scalar traces and the flux three-forms $J$ in a common orientation. For a common variation of that trace the two oriented terms $\int\theta_\phi$ cancel pointwise. On a null face the flux is fixed by the generator derivative and area element. On a spacelike cap it also involves the normal derivative. The homogeneous solutions below continue smoothly through every face, cap and joint. This gives a concrete boundary variational prescription in which histories can change their scalar offset. The transparent interface transmits flux. A cap or a null segment alone generally omits part of $Q_C$. A Dirichlet datum fixed to an external scalar origin would select a different ensemble. [Chandrasekaran, geometric overlap matching, Eqs. (3.29)–(3.31)](https://arxiv.org/html/2611.34924v1#S3.E30)

## A canonical pair on complete solutions

Fix a round waist of area $4\pi R^2$ and its comoving central observer. In conformal coordinates put the waist at $\eta=0$, normalize the scale factor to one there and put the tips at $\eta=\mp R$, $\chi=0$. Write $s$ for the scalar proper-time derivative at the waist, $\kappa=\sqrt{4\pi G/3}$ and $H=\kappa s$. An exact branch of the spatially flat Einstein–scalar equations at zero cosmological constant is
$$
 ds^2=a^2(-d\eta^2+d\chi^2+\chi^2d\Omega^2),\qquad
 a^2=1+2H\eta,\qquad
 \phi=q+s\int_0^\eta\frac{d\eta'}{1+2H\eta'} .
$$
Indeed $a^2\phi'=s$ and $(a'/a^2)^2=(4\pi G/3)(\phi'/a)^2$, where prime denotes $d/d\eta$. Choosing $|2HR|<1$ keeps both vertices regular and joins expanding and contracting branches smoothly through flat space. This is one choice of branch and time orientation. The waist scalar $q$ spans $\mathbb R$. A smooth exterior can have periodic spatial coordinates of side greater than $4R$, so the same local diamond fits inside a finite-volume solution. In that example a global shift acts in the exterior too. Its total charge uses the whole torus volume. [Jercher and Steinhaus, continuum Einstein–scalar equations (81)–(83)](https://arxiv.org/html/2312.11639v2#A2.SS1) · [Exact clocks on the expanding branch](matter-diamond.md)

With spacetime orientation $d\eta\wedge d\chi\wedge d\Omega$ (positive volume factors understood), the current throughout the chart is
$$
 J=s\,\chi^2 d\chi\wedge d\Omega .
$$
The complete incoming and outgoing cuts both have increasing $\chi$ from the centre to $R$. On a cap of comoving radius $\chi_c$ the charge is $4\pi s\chi_c^3/3$. The remainder on its null sheet is $4\pi s(R^3-\chi_c^3)/3$. As $s$ varies, the two caps generally move by different amounts to maintain $dA_c=\epsilon^2 dA_S$ on each face. On each composite cut the moving-rim contributions cancel. The waist disk has a fixed embedding in the displayed coordinates, providing an independent place to evaluate the symplectic form.

Set $V=4\pi R^3/3$ and $P=Vs$. On the waist disk the scalar potential integrates to $P\,\delta q$. All gravitational fields, geometric embeddings and their joint data on this family depend only on $s$, so their shift-invariant potential restricts to a multiple of $ds$ with coefficient depending only on $s$. Its exterior derivative vanishes. The resulting pullback and its bracket are
$$
 \Omega=dP\wedge dq,\qquad \{q,P\}=1 .
$$
Thus varying the scalar offset pairs nontrivially with an allowed variation of the conserved charge. A single fixed value of $P$ would remove precisely the tangent direction used in this test. The calculation concerns the subregion form. On the entire homogeneous torus, the canonical momentum is its volume times $s$.

A geometric specification of $q$ is $\int_S \phi\,dA/\int_SdA$. A simultaneous spacetime diffeomorphism of fields and corner preserves it. A scalar shift by $b$ increases it by $b$. Operationally this observable calls for a detector whose zero is calibrated in the scalar target. A pointer coupled during readout to the smeared scalar itself distinguishes the offsets. An instrument coupled only to $d\phi$ gives the same response on every translate, as does any purely gravitational instrument. The subregion symmetry refers to translating the smooth solution, including its exterior. Shifting only the diamond against the original exterior generally violates the matching prescription. [Chandrasekaran, variation of a frame pullback, Eq. (3.40)](https://arxiv.org/html/2611.34924v1#S3.E40)

## A common window for both clocks

Define $P_0=V/(2\kappa R)$, $x=\chi/R$ and $d=+P/P_0$ on the past-tip face and $d=-P/P_0$ on the future-tip face. The scale factor on either face satisfies $a^2=w(x)=1-d(1-x)$. The cap fraction $0<\epsilon<1$ fixes $x_c\sqrt{w_c}=\epsilon$ uniquely since the area radius $Rx\sqrt{w}$ increases on $[0,1]$ for $|d|<1$. An affine parameter in units with $d\tau=w\,dx$ gives the dimensionless capped reading
$$
 \frac{U(d)}{R}=
 \left(\sqrt{w_c}+\frac{d x_c}{2\sqrt{w_c}}\right)
 \frac{(1-x_c)(1+w_c)}{2w_c}.
$$
It is continuous in $d$, and $U(0)=(1-\epsilon)R$. Consequently every ceiling $\ell>(1-\epsilon)R$ admits an open interval of charges around zero on both faces. For $s\ne0$ the positive classical null stress makes the excess strictly positive on each face. [Chandrasekaran, affine length and angular average, Eqs. (3.27)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Direct two-face calculation](matter-diamond.md)

A sufficient interval can be bounded without locating a spectral threshold. Write $f=x\sqrt w$ for the dimensionless area radius. Its affine focusing equation is $\partial_\tau^2 f=-3d^2f/(4w^4)$. Twice integrating between the cap and waist gives
$$
 \frac{U(d)}R-(1-\epsilon)=\frac{3d^2}{4}
 \int_{x_c}^1\left(\int_x^1 w(z)\,dz\right)xw(x)^{-5/2}\,dx
 \ \le\ \frac{D^2(1+D)}{8(1-D)^{5/2}},\qquad |d|\le D<1 .
$$
Here $1-D\le w\le1+D$ and $\int_0^1 x(1-x)\,dx=1/6$. For $\epsilon=1/2$, every charge with $|P|\le P_0/4$ passes a two-face ceiling of $0.521 R$. The uniform upper bound on the excess is $0.02004689R$ after rounding upward.

## Counting and reading the states

Quantize this two-dimensional solution family in the momentum representation $L^2(I,dP)$, where $I=(-P_0,P_0)$. Represent the two classical clocks by multiplication by $U(\pm P/P_0)$. Their joint spectral projector multiplies by the indicator of the common allowed set. For $\ell>(1-\epsilon)R$ take any band $[-p,p]\subset I$ of positive width inside that set. The states
$$
 \psi_n(P)=(2p)^{-1/2}\,\mathbf 1_{[-p,p]}(P)\,e^{-in\pi P/p},
 \qquad n\in\mathbb Z ,
$$
are normalized, mutually orthogonal, and have identical joint clock distributions. Each is the preceding packet translated in scalar value by $\pi\hbar/p$. The same construction can be centered in a smaller accepted interval strictly inside $P>0$. It then uses only regular expanding geometries and avoids the intersection of the two Friedmann branches at flat space. At the exact flat ceiling, the only accepted classical charge is $P=0$, a set of zero measure in this representation.

There is also a normalized covariant scalar-value measurement in this model with bounded momentum. Let $W$ extend a wave function by zero from $I$ to $\mathbb R$, and use the unitary Fourier transform $\mathcal F$ with kernel $e^{iPz/\hbar}/\sqrt{2\pi\hbar}$. For a Borel set $B$ of readout values, set
$$
 E(B)=W^*\mathcal F^*\mathbf 1_B\mathcal F W .
$$
Then $E(\mathbb R)=1$, and $e^{-ibP/\hbar}$ translates its outcome density by $b$. This defines a positive operator-valued measure without assuming a self-adjoint Weyl conjugate to a bounded momentum. Bins of width $\pi\hbar/p$ centered on the translated peaks identify each preparation with probability $0.77369501$. Smooth momentum envelopes with finite field variance give the same obstruction. [Wave packets and finite-resolution test](matter-state-count.md)

**A measurement using only geometry.** The model also gives an infinite-rank test with no scalar target calibration. On the accepted positive-momentum interval adjoining zero, the past-face clock is continuous, tends to the flat value as $P$ tends to zero, and exceeds that value at each interior point. Its range therefore contains an open interval of clock readings. Choose any $N$ disjoint open bins inside this interval. Each bin has an open, nonempty preimage within the accepted momenta. A normalized wave packet supported in each preimage registers in its intended bin with probability one and passes both ceilings. The preparations have different clock distributions, and a larger $N$ requires finer clock resolution. For the half-radius cap, the eight past-face readings at $P/P_0=j/32$, $1\le j\le8$, have minimum spacing $0.00018637638R$. Continuity allows packets of positive bandwidth about these momenta to populate eight disjoint bins. A closed interval ending at $P_0/4$ suffices by taking a one-sided packet there. This test uses the continuous multiplication spectrum in the stated quantization. A continuous range of classical readings alone does not prove a continuous quantum spectrum.

The calculation supplies a shift charge, two-face and cap matching, and an explicit readout and nonempty two-clock projector in the **quantized homogeneous family**. A corresponding full-theory result would require a physical quantum representation that admits those charged preparations or independently realizes the noncompact shift, covariant readout and nonempty invariant projector. The target calibration, transparent exterior and homogeneous quantization are choices in this example. The model leaves the four-dimensional vacuum state count open.

Run `python3 checks/matter_boundary.py` from the repository root. At $P/P_0=3/4$ and $\epsilon=5/16$, the computed cap fractions of the charge are `125/1728` and `1/64` and each complete cut gives one unit of normalized charge. The check also verifies the moving-rim derivatives, the two-clock bound at $|P/P_0|\le1/4$, and the minimum spacing of the eight geometric readouts. The same script runs under `make check`. [Executable check](../checks/matter_boundary.py)
