# A spherical clock test with unchanged cap and waist data

Two smooth vacuum quadrupoles can pass on opposite sides of the rim while leaving every local measurement at the rim unchanged to first order. The sharp clock includes only the outer packet. Their total symplectic product with every fixed smooth metric variation tends to zero, while the mixed variation of the clock tends to **$-3/4$** in the normalization below. This extends the single-packet test to smooth matched caps with local angular, boost and normal-displacement charges. The conclusion concerns a continuously differentiable assignment of smooth Hamiltonian vectors through flat space. It leaves distributional responses and the quantum conjecture open. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Single-packet preparation](joint-flat-hessian.md)

## The waves and their calibration

Use a four-dimensional Minkowski diamond with point tips at $(0,\mathbf 0)$ and $(2,\mathbf 0)$. The initial rim $C$ is at the area fraction $a=1/3$ on the outgoing cone. On the background the vertex-normalized affine parameter $s$, the radius $r$, and the normalized area coordinate $v$ coincide on that cone. Use the tip frame for its angular labels. In the matched-radius preparation the later tip is adjusted to hold $M=\langle\rho_S^2\rangle/\langle\rho_S\rangle=1$ with $\rho_S$ the waist area radius per solid angle. The clock excess $D=\bar u_*-(1-a)M$ is critical at flat space, including along variations changing the embeddings in the specified preparation. This follows from the quadratic dependence of focusing on shear. The raw clock and excess differ by a constant on the matched-radius preparation. [v1, (3.18)](https://arxiv.org/html/2611.34924v1#S3.E18) · [v1, (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27)

Take the smooth transverse-traceless vacuum family from the single-packet test. A compactly supported function $F(u)$ in $(0,2)$ generates the radial wave $[F(t+r)-F(t-r)]/r$. Apply $(P_{ik}P_{jl}-P_{ij}P_{kl}/2)S_{kl}$, where $P_{ij}=\delta_{ij}\Delta-\partial_i\partial_j$ and $S=\operatorname{diag}(-1/2,-1/2,1)$, to obtain the spatial metric perturbation. Its time components vanish. Let $B$ be the trace-free projection of $S$ onto the screen perpendicular to the outgoing direction $n$, with $\langle B:B\rangle=3/5$. The first variation of the conformal screen metric is $G_F(s)B$, where
$$
G_F(s)=\frac{F^{(4)}(2s)}s-\frac{2F^{(3)}(2s)}{s^2}+\frac{F''(2s)}{s^3}.
\tag{1}
$$
Each packet is a smooth linearized vacuum solution and a tangent to nearby exact vacuum data on the ball under the construction in the earlier calculation. The allowed nonlinear amplitude can depend on the packet width. [Vacuum extension and optical derivation](joint-flat-hessian.md)

Choose a smooth nonnegative bell $b$ of unit integral supported in $(-1,1)$, and put $b_\eta(x)=b(x/\eta)/\eta$. Define the test $Z_\eta$ by
$$
 F_\eta(2s)=b_\eta(s-a-2\eta)-b_\eta(s-a+2\eta).
\tag{2}
$$
Each unsigned packet has unit integral in **$s$**. All derivatives of $F_\eta$ vanish in an open interval about $2a$, of width proportional to $\eta$. For the fixed wave $W$ choose
$$
 F_W(u)=\frac{a}{384\cdot 5040}(u-2a)^{10}
\tag{3}
$$
in a neighborhood of $2a$ and multiply by a smooth compact cutoff equal to one there. Since $10!/6!=5040$, (1) gives $G_W(s)=(s-a)^6/6+O((s-a)^7)$. In particular $W$ has zero rim strain and zero rim strain slope. The nonzero response in this test therefore cannot be computed from the earlier $-1/30$ angular coefficient. [One-sided angular charge](joint-angular.md)

## The rim stays fixed even in a transported frame

Where $F(2s)$ vanishes on an interval of the lower cone, the spacetime perturbation vanishes on a collar of its cuts. Equation (1) gives zero optical strain there, and linearized vacuum focusing from the regular, fixed-frame vertex gives zero first area variation at fixed $s$. Consequently the full intrinsic metric of the affine cuts is unchanged there. This also fixes their embedding in the original flat coordinates. To see this, resolve the spatial displacement into radial displacement $d$ and angular vector $V$. The intrinsic metric variation where the ambient perturbation vanishes is $2sd\,\gamma_{AB}+2s^2D_{(A}V_{B)}$. Its trace-free part puts $V$ in the conformal Killing space of the unit sphere, whose vector harmonics have degree one. The source has pure degree two and propagation from the fixed vertex is rotation covariant, so $V=0$. The trace now gives $d=0$. This holds throughout the interval, so the spatial affine tangent also has zero variation. Null orthogonality to the angular vectors gives $D_A\delta t=0$ on each cut. The time displacement is a scalar of degree two, hence zero. The ray and tangent thus return exactly to their background values there **at linear order**, even if the ray has crossed one packet.

The angular normal connection also returns to its background value. In the vertex frame its first variation is
$$
 \delta\varpi_A=\left(-G_F/2+I_F/s^2\right) D^B B_{AB},\qquad
 I_F(s)=\int_0^s tG_F(t)\,dt
       =F^{(3)}(2s)/2-F''(2s)/s .
\tag{4}
$$
The last equality follows by differentiation and compact support away from the vertex. Even a tetrad parallel transported along the ray has no residual shift. Write $e_A=\partial_A X$ for the Jacobi screen vectors and $E_A=e_A/s$ for their rescaling. To first order, $\nabla_\ell E_A=(G_F'/2) B_A{}^B E_B+(\delta\varpi_A/s)\ell$ in a unit-sphere frame along the ray. The two coefficients have primitives $G_F B_A{}^B/2$ and $-I_F D^B B_{AB}/(2s^2)$, respectively. These vanish on every cut in the gap. A complete transported null tetrad is determined by the affine tangent, its two transported spacelike screen vectors and their normalized transverse null normal. [v1, optical transport (3.56)–(3.57)](https://arxiv.org/html/2611.34924v1#S3.E57.3)

The upper cone has the same calculation in the time coordinate $2-t$ with master profile $-F(2-u)$. For $\eta$ sufficiently small the initial rim, the final rim and the waist all lie in collars where the relevant profiles vanish. Both tips and their frames can be fixed. If an observer transports a frame along the central geodesic, its linearized spatial transport in this time gauge depends at the endpoints on the difference of $h_{ij}/2$, which vanishes there. The waist adjustment that holds $M$ fixed is zero to first order. The cut selected by (3.18) stays fixed because both its density and the waist density are unchanged. One may choose the cap to agree to first order with its original spacelike embedding and keep each independent angular marking and boost fixed on these tests. On the common collars both induced metrics, both optical tensors, the twist, the cap extrinsic curvature there, and their local derivatives have zero variation. Each test is compatible with ordinary smooth matching and with an independently chosen common comparison map fixed on that test. [v1, moving pullbacks (3.40)](https://arxiv.org/html/2611.34924v1#S3.E40) · [Cap and sheet compatibility](joint-edges.md)

## The clock and the joined Einstein current

The mixed derivative in this sector is
$$
 d^2D(W,Z_\eta)=\frac3{20}\int_a^1 s(1-s)G'_W(s)G'_{F_\eta}(s)\,ds .
\tag{5}
$$
Only the outer packet occurs in (5). Put $T=-[s(1-s)G_W']'$. Integrating once by parts and then moving the derivatives in (1) onto $T$ gives
$$
 d^2D(W,Z_\eta)=\frac3{20}\int_a^1 F_\eta(2s)
 \left[\frac1{16}(T/s)^{(4)}+\frac14(T/s^2)^{(3)}
                                 +\frac14(T/s^3)''\right]ds .
\tag{6}
$$
All boundary terms vanish for each $\eta$. Each derivative of $F(2s)$ in (1) incurs a factor of $1/2$ when expressed as an $s$ derivative. At $s=a$, $T=-5a(1-a)(s-a)^4+O((s-a)^5)$. The bracket in (6) therefore has value $-5!(1-a)/16=-5$, and unit outer mass gives
$$
 \lim_{\eta\to0}d^2D(W,Z_\eta)=-3/4 .
\tag{7}
$$
The value depends on the normalizations (2) and (3). Its origin is the sharp restriction of the radial integral, even with a gap between the two physical pulses on every member of the sequence.

On the spacelike waist disk $t=1$, both packets lie in an interior annulus near $r=1-2a=1/3$. The signed sum in (2) tends to zero as a distribution because its two terms converge to the same Dirac measure with opposite signs. Differentiation preserves this convergence. The regular radial weights on this annulus, including $1/r$, preserve it as well. The metric Cauchy data are finite sums of these derivatives, so their symplectic pairing with every fixed smooth metric tangent goes to zero. The current can be taken to the incoming joined cap and sheet by conservation. For every fixed $\eta$ all fields are smooth, and the perturbation has zero local data on the seam and waist.

The same argument includes independent local corner marks under the following hypotheses. The metric variations on the two faces are restrictions of one smooth spacetime tangent. The interior current is the Einstein current, and any additional terms from displacement, frame and joint variations are local on the cuts, as for the improved potential with (B.21). The assigned angular and normal marks on the test can be held fixed on the unchanged collars. Moving a smooth embedding in the interior of a face contributes only the boundary diffeomorphism charge on shell. In vacuum at $\Lambda=0$ the on-shell Lagrangian vanishes, and Cartan's identity applied to the pulled-back potential leaves the ordinary metric current plus local boundary terms. On $Z_\eta$ all local terms in the added two-form vanish when paired with **any** admissible smooth response. This includes responses with arbitrary comparison-map velocities, cap tilts, affine shifts and variations of the waist charges. The argument tests a necessary Hamilton equation by choosing one allowed family of variations. It does not require an independent choice of canonical momentum for the angular map. [v1, surface charge (3.50b)](https://arxiv.org/html/2611.34924v1#S3.E50.2) · [Cap boost term (A.18)](https://arxiv.org/html/2611.34924v1#A1.E18) · [Extended potential (B.21)](https://arxiv.org/html/2611.34924v1#A2.E21)

Here the Hamiltonian vector is defined in the first slot, $\Omega(X_D,\cdot)=dD$. The varying-area calculation uses v1’s second-slot convention, which reverses the vector and leaves the vanishing-pairing test invariant. On a regular phase-space reduction the Hamiltonian field of $D$ at its critical point is zero. A $C^1$ assignment of smooth Hamiltonian fields would therefore imply $d^2D(W,Z_\eta)=\Omega_{\rm flat}((d_W X_D)_{\rm flat},Z_\eta)$. The right side tends to zero under these hypotheses, contradicting (7). The obstruction applies to the raw clock on the matched-radius preparation, or to the excess when $M$ varies. The probe energies need not stay bounded as $\eta\to0$. Each individual probe is an admissible smooth tangent; the weak convergence suffices to rule out a smooth response. The result does not establish a pointwise obstruction for every curved solution or decide the operator domain of a quantum clock.

## A rank test for frames determined by cap data

For example, define a rim mark by parallel transporting the timelike vector $\partial_t$ along a spacelike radius of the initial cap $t=a$ from the center to $r=a$. Its outward component at the rim has variation $-\int_0^a\partial_t h_{rr}\,dr/2$ in the synchronous coordinates above. With $Q=S_{ij}n^i n^j$ the TT radial component on this path is $h_{rr}=6Q[F''(a+r)/r^3-3F'(a+r)/r^4+3F(a+r)/r^5]$. The other radial phase has support disjoint from the path. After differentiating in $t$ and integrating by parts, the component is
$$
 -45Q\int_0^a F(a+r)r^{-6}\,dr .
$$
The inner packet alone contributes. Although the local spacetime fields are unchanged in a collar of the rim, this particular transported mark detects the pulse. Such a mark differs from the independent cap marks held fixed above and from the vertex frame transported along the null rays.

A second pulse profile cancels the radial cap frame and position moments exactly, while retaining a nonzero calibrated Hessian. [Spacelike probe and filtered pulse](match-packet-frames.md)

There is a separate obstruction for any extension with the following property. Fix a small interval $I$ about $a$, let $f(s)=F(2s)$ run over *all* smooth compactly supported functions on $I$, and use the vacuum quadrupoles above as tests $Z_f$. Choose one differentiable lift of these waves to the marked preparation. Assume the extra two-form on $(X,Z_f)$ factors through a fixed finite-dimensional vector of linear responses $L(Z_f)$ for all smooth $X$ at flat space. A finite list of finite-order tensor data on the marked spheres has this property if their variations from $Z_f$ are rotation equivariant at the round solution. For each choice of $f$ the five angular polarizations of the wave transform in the degree-two representation. A tensor field of fixed rank on the round sphere has only finitely many angular components in that representation. Integration in radius to determine a mark can change each of the scalar functionals in $L$ without increasing their number. Independent marks can be held fixed on this test family. A reference geometry breaking spherical symmetry needs a check of the finite-rank hypothesis.

For $n=0,1,\ldots$ take smooth reference waves $W_n$ with $G'_{W_n}(s)=(s-a)^{n+5}+O((s-a)^{n+6})$. Equation (1) realizes these using cutoffs of $(u-2a)^{n+10}$ with a nonzero normalization. Integrate (5) by parts for a general $f$, which may be nonzero at the cap. The factor $s(1-s)G'_{W_n}$ and its first four derivatives vanish there, so every surface term vanishes also for these tests. On $I$ the resulting Hessian acts by integrating $f$ against the density
$$
 \mathbf1_{s>a}\left[c_n(s-a)^n+O((s-a)^{n+1})\right],\qquad
 c_n=-\frac{3}{20}\frac{1-a}{16}\frac{(n+5)!}{n!}\ne0 .
 \tag{8}
$$
Here the expression on the right of the cut is smooth up to $s=a$. Only the fourth derivative of $T/s$ in (6) contributes at the order shown. The densities (8) are linearly independent modulo smooth densities on $I$. In any nonzero finite combination, take the smallest index with a nonzero coefficient. The derivative of that order jumps at $a$.

For a fixed smooth spacetime tangent $X$ the ordinary waist-disk pairing with $Z_f$ is integration of $f$ against a smooth density on $I$. Integrating the finitely many spacetime derivatives of $F$ by parts on the interior annulus proves this statement. Thus, modulo smooth densities, all possible pairings of $Z_f$ with smooth responses lie in the finite span of the components of $L$. Equation (8) gives an infinite independent set in this same quotient. A $C^1$ family would have to represent every one of them, by differentiating its Hamilton equation in the directions $W_n$. This is impossible. The argument assumes smooth bulk tangents joined across the rim and a common marked family admitting these reference and test variations. It does not require the individual edge functionals to have kernels that are smooth functions of radius. A boundary field with additional independent radial data or a restriction excluding these tangents would require its own range analysis.

## Reproduce the coefficient

Run `python3 -B checks/match_packets.py` from the repository root. The check integrates the original product of optical slopes (5), using a normalized polynomial bell proportional to $(1-x^2)^{12}$ inside $(-1,1)$, extended by zero. This bell has eleven continuous derivatives, sufficient for the check. A smooth bell gives the same analytic limit. The signed first moment against $s$ equals $4\eta$ at every width. The final numerical clock Hessian is approximately `-0.74969107`. The next two lines estimate the first and second right-hand coefficients in (8) and print their exact limits `-9/2` and `-63/4`. The check ends with `Limiting clock Hessian: -3/4`. Run `make check` for the complete suite. [Executable check](../checks/match_packets.py)
