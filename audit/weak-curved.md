# The weak generator of a spherical clock on a curved vacuum diamond

The first variation of a two-tip clock defines a compact metric distribution. On a symmetric vacuum plane wave a single emitter can be calibrated by a local tidal measurement so that this distribution is conserved at the background. Its retarded-minus-advanced Einstein field exists by duality in a specified globally hyperbolic spacetime. A sequence of smooth compact conserved probes gives nonzero brackets with the angular mean at one emitter. The same limit holds at fixed proper duration, fixed weighted waist radius, or fixed total waist area in three separate preparations. The wave packets cross the cap where its affine calibration is reset. The construction uses the surrounding spacetime to propagate the field. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Forward variation of the two cones](joint-jacobi.md) · [Cap pulse on the same spherical diamond](joint-focal.md)

## The metric source, including the return signal

Use one freely falling emitter, a physical orthonormal launch sky and a return event on the emitter worldline at proper duration $\ell$. Let $x(s)$ denote the outgoing affinely parametrized null geodesic with $-k\cdot V=1$ at launch. Let its transverse Jacobi matrix obey $J''=QJ$, $Q_{AB}=-R_{AkBk}$, $J(0)=0$, $J'(0)=I$ in a parallel screen. Write $D=\sqrt{\det J}$, $S$ for the affine parameter at the intersection with the other cone and $C$ for the inner rim. Assume smooth cones with no cut or conjugate points up to the waist, transverse intersection there, and $D'(C)>0$. We use the smooth local root of $D(C)=\epsilon D(S)$, $0<\epsilon<1$. The reading and its normalized average over the launch sky are
$$
 P=D'(C),\qquad U=P(S-C),\qquad
 \bar U=\frac{\langle D(S)U\rangle}{\langle D(S)\rangle}.
$$
All derivatives below are at the reference metric. A dot on $D$ varies the optical solution at fixed affine argument. The shift $\delta S$ includes the motion of both cones. Let
$$
 W=\frac{D(S)}{\langle D(S)\rangle},\quad
 V_0=\frac{U-\bar U}{\langle D(S)\rangle},\quad
 G=(S-C)D''(C)/P-1,\qquad
 (A,B,H,T)=\big(W(S-C),-WG,\epsilon WG+V_0,WP+H D'(S)\big),
$$
where $H$ in the final entry is the third coefficient. Direct differentiation gives the distribution $j=d\bar U$ as
$$
 j[h]=\left\langle
 A\dot D'(C)+B\dot D(C)+H\dot D(S)+T\,\delta S
 \right\rangle .                                                     \tag{1}
$$
Indeed $P\delta C=\epsilon[\dot D(S)+D'(S)\delta S]-\dot D(C)$. Uniform sky measure stays fixed in emitter-frame coordinates. If instead $\ell$ is adjusted to keep $M=\langle D(S)^2\rangle/\langle D(S)\rangle$ fixed, assume $\partial_\ell M\ne0$. Use (1) at fixed $\ell$, with $V_0$ replaced by $V_0-(\partial_\ell\bar U/\partial_\ell M)(2D(S)-M)/\langle D(S)\rangle$. For fixed total area $\mathscr A=4\pi\langle D(S)^2\rangle$ with $\partial_\ell\mathscr A\ne0$, the corresponding replacement is $V_0-8\pi D(S)\,\partial_\ell\bar U/\partial_\ell\mathscr A$. Each formula includes the change of return time and the varying sky weight.

There is a backward kernel for evaluating (1) on any smooth off-shell metric variation $h$. Put $N(r)=D(r)J(r)^{-T}/2$, with the Frobenius matrix pairing. Let $B_J(r,t)$ solve the background Jacobi equation in $r$ with $B_J(t,t)=0$, $\partial_r B_J(t,t)=I$. Set
$$
 \begin{aligned}
 L(t)={}&\mathbf1_{t<C}\big\{
 B_J(C,t)^T[B N(C)+A N'(C)]+
            A\partial_C B_J(C,t)^T N(C)\big\}\\
 &+\mathbf1_{t<S} H B_J(S,t)^T N(S),\qquad
 K(t)=L(t)J(t)^T .                                                    \tag{2}
 \end{aligned}
$$
Here $\partial_C$ differentiates the first argument alone. The three fixed-argument optical terms in (1) equal $\int_0^S K:\dot Q\,dt$. This follows from the zero-initial-data variation $\dot J(r)=\int_0^r B_J(r,t)\dot Q(t)J(t)\,dt$. In particular the coefficient of $\dot J'(C)$ is retained across the rim. Changing the direction-dependent screen dyad conjugates the corresponding contractions.

The derivative of the ray and its screen has a second adjoint. In any coordinate patch let $z=(x,k,e_1,e_2)$ and $z'=f_g(z)=(k,-\Gamma kk,-\Gamma k e_1,-\Gamma k e_2)$. Write $b_h=\partial_g f_g[h]$, formed with $\delta\Gamma$ at fixed $z$, and $q_h=\partial_g Q[h]$ at fixed $z$, formed with the variation of the all-lower Riemann tensor. Thus $\dot Q=q_h+(\partial_z Q)\delta z$ also accounts for the displaced ray, tangent and screen. The future tip is $q$. Parameterize its geodesic connector to $x(S)$ by $y(0)=q$, $y(1)=x(S)$, and set $a=\sigma_{;x}$, $d=\sigma_{;q}$ for the world function of that branch. Its stationary geodesic action gives
$$
 \delta S=-\frac{a\cdot\delta x(S)+d\cdot\delta q+
                   \frac12\int_0^1 h(\dot y,\dot y)d\lambda}{a\cdot k(S)}.
                                                                    \tag{3}
$$
The displacement $\delta x(S)$ here is at fixed affine parameter. Put $m=-T/[a\cdot k(S)]$. Starting with $\lambda_z(S)=(m a,0,0,0)$, solve backward
$$
 -\lambda_z'=(\partial_z f_g)^T\lambda_z+(\partial_z Q)^T K .
$$
The transpose means contraction against all matrix entries in the second term. Equations (1)–(3) now read
$$
 j[h]=\left\langle \lambda_z(0)\cdot\delta z(0)
 +\int_0^S (\lambda_z\cdot b_h+K:q_h)\,dt
 + m\left(d\cdot\delta q+\tfrac12\int_0^1 h(\dot y,\dot y)d\lambda\right)
 \right\rangle .                                                     \tag{4}
$$
The same adjoint for the timelike geodesic computes the term $\langle md\rangle\cdot\delta q$. Use $z_o=(x_o,V_o)$, $f_o=(V_o,-\Gamma V_o V_o)$, terminal data $(\langle md\rangle,0)$ at $\ell$ and zero running term in the adjoint. Its contribution is $\lambda_o(0)\cdot\delta z_o(0)+\int_0^\ell\lambda_o\cdot\partial_g f_o[h]dt$. The initial variations in both terms follow from the same launch preparation. In particular $k(0)=V+\sum_i n^i E_i$ in the varied orthonormal tetrad. A local orthonormal sky dyad gives the initial screen. Differentiating these algebraic equations and the preparation below fixes all initial data. Two sky charts suffice and (4) agrees on overlaps.

Formula (4) specifies a spacetime distribution by its action on an arbitrary test metric, including perturbations outside vacuum. Its support lies on the two swept cone portions, the observer segment and the preparation support. The coefficients are smooth on each compact regular piece up to the jumps in (2). Compact sky integration gives a finite seminorm bound involving metric derivatives through order two for the point preparation below. The Jacobi solution is regular at the vertex, and $J^{-1}$ is evaluated only at the two positive radii. This construction supplies a source before choosing a gravitational Green operator.

## A single emitter with a conserved source

Use the symmetric plane wave in Rosen coordinates,
$$
 ds^2=-2\,du\,dv+\cosh^2(\kappa u)\,dx_1^2+
                  \cos^2(\kappa u)\,dx_2^2,\qquad \kappa>0.
$$
Select an auxiliary point and a pair of trial vectors there. By orthonormalizing them obtain a future unit timelike $v_0$ and a unit spacelike $n_0$ orthogonal to it. Boost to $V=v_0\cosh\chi+n_0\sinh\chi$ until the measured Weyl superenergy
$$
 \mathcal W(V)=E_{ij}(V)E^{ij}(V)+B_{ij}(V)B^{ij}(V)=w_*
                                                                    \tag{5}
$$
takes its specified value. Here $E,B$ are the electric and magnetic parts of the Weyl tensor in the observer's rest frame. Choose a local branch with $\partial_\chi\mathcal W\ne0$. For any metric test at fixed marks the rapidity varies by $\delta\chi=-\delta_g\mathcal W/\partial_\chi\mathcal W$, where $\delta_g$ includes the preliminary orthonormalization and holds $\chi$ fixed. Complete the tetrad by any smooth orthonormal spatial frame. A spatial rotation changes only the integration coordinates of the sky.

The measured quantity on this background is $4\kappa^4(V^u)^4$. To see this, the Brinkmann transverse tidal matrix is $\operatorname{diag}(-\kappa^2,\kappa^2)$ for the components $R_{iuju}$. In a frame with zero transverse velocity the two transverse electric eigenvalues are $\mp\kappa^2(V^u)^2$ and the longitudinal eigenvalue vanishes. The magnetic tensor has the same squared norm by the transverse dual rotation. The result extends to every velocity by the following isometries. In Brinkmann coordinates the metric has profile $X^T H_b X\,du^2$, $H_b=\operatorname{diag}(\kappa^2,-\kappa^2)$. Translations in $u,v$ and the maps
$$
 X\mapsto X+b(u),\qquad
 v\mapsto v+b'(u)\cdot X+\tfrac12 b'(u)\cdot b(u),\qquad b''=H_b b
$$
preserve it by substitution. The values of $b,b'$ at an event are independent. These isometries can take any event and unit future velocity to any other such pair with the same $V^u$. The unit timelike normalization fixes the remaining velocity component once the transverse components and $V^u$ are fixed.

Consequently all nearby choices of auxiliary marks at *this background*, after (5), give identical readings at fixed $\ell$. A choice of the auxiliary marks remains necessary to define the single-emitter functional on perturbed metrics. Naturality gives
$$
 F(\phi^*g;m_0)=F(g;\phi_*m_0),\qquad
 j[\mathcal L_\xi g]=d_mF[\mathcal L_{\rm flow}m_0]=0 .
                                                                    \tag{6}
$$
The right-hand side differentiates the point and trial vectors pushed by the flow. Equality to zero follows from their calibrated equivalence at the reference solution. Thus $\nabla_a j^{ab}=0$ distributionally there, with the volume density understood. This is a linearized gauge-invariant source. At a general background one must supply a covariant metric preparation, or retain the variations of physical reference fields in its Ward identity. In particular a fixed coordinate emitter with a freely specified boost has an uncancelled mark term in general. [Metric-dependent observables, Khavkine](https://arxiv.org/abs/1503.03754)

## A compact probe with a nonzero bracket

Take $\kappa=1$, $p=(0,0,0,0)$, $q=(1,1,0,0)$, $v_0=(\partial_u+\partial_v)/\sqrt2$, $n_0=(\partial_u-\partial_v)/\sqrt2$, $w_*=1$, $\ell=\sqrt2$ and $\epsilon=1/2$. Equation (5) has $\chi=0$ and $\partial_\chi\mathcal W=4$. Work on $u\in(u_-,u_+)$ with $-\pi/2<u_-<0<1<u_+<\pi/2$, $v\in\mathbb R$, and the two $x_i$ periodic with sufficiently large periods. The compact diamond and its small variations avoid all transverse images. The local isometries used to differentiate (6) need only cover these experiments. For example, $t=v+F(u)$ with $F$ strictly increasing from $-\infty$ to $+\infty$ and $F'>0$ is a Cauchy time. Both $u,v$ are nondecreasing on future causal curves. A bounded $t$ toward a future endpoint bounds both coordinates and keeps $u$ away from $u_+$. The causal inequality bounds the transverse travel on that segment by a constant times $\sqrt{\Delta u\Delta v}$. A curve then has an endpoint. The past argument is identical. This proves global hyperbolicity for the chosen surrounding spacetime.

Write the Rosen scale factors as $A_{1,2}=R e^{\pm H_r/2}$. The vacuum equation is $R''=-R(H_r')^2/4$. Take the compensated smooth variation $\delta H_r=f_d$ of width $d$ crossing $u=c$, where $\sqrt{\sinh c\sin c}=\epsilon\sqrt{\sinh 1\sin 1}$. Its profile is $f_d(u)=d^{-1}f((u-c)/d)$, with compact smooth $f$, $\int f=0$ and $\int_{-1}^0 f=1$. The metric variation vanishes near launch. The central coordinate observer stays an affinely parametrized timelike geodesic, so the calibration and both tips retain their unperturbed values in this variation. The waist and fractional rim still move. The exact spherical calculation gives a limiting first variation
$$
 \lim_{d\downarrow0}j[h_d]=
 -\frac{\pi F_0(1)(1-c)F_0(c) Z'(c)}
 {2\mathcal D\sqrt{\det E_c}}\simeq-0.060534,                         \tag{7}
$$
where $F_0(u)=\sqrt{\sinh u\sin u}$, $Z'=\coth u-\cot u$, $\mathcal D$ is the denominator of the sky integral in stereographic coordinates, and $E_c$ is the positive quadratic form describing $u=c-k^TE_c k+O(|k|^4)$ on the cap. At the smooth maximum, the sky samples one half of the compensated profile. The exact formula includes the return-cone intersection and the moving cap in (1). [Full derivation, Eqs. (1)–(5), and numerical values at finite widths](joint-focal.md)

To realize each $h_d$ as the field of a compact smooth probe, append two smooth variations of $H_r$ with support strictly after $u=1$. They can cancel the first variations of both scale factors and their derivatives beyond a compact interval. At first order put $w=\delta R/R$, $m=R^2 H_r'$, $I'=R^{-2}$. For arbitrary smooth compact profile $g=\delta H_r$ the forced equation is $(R^2w')'=-m g'/2$. Fix $\nu$ after all three supports. With zero past data, integration by parts gives
$$
 2R(\nu)^2w'(\nu)=\int m'g\,du,\qquad
 2w(\nu)=\int [m'(I(\nu)-I)-H_r'] g\,du .                            \tag{8}
$$
Here $m'=2\kappa^2 R^2>0$. The ratio $I(\nu)-I-H_r'/m'$ of the two kernels is analytic on the strip with derivative $-2$ at zero. It is nonconstant on every post-tip open subinterval. Thus two sufficiently localized smooth bumps there give independent moment columns and can cancel the two original moments exactly. The corrections are also $O(d)$ for the compensated pulse. After them $w=w'=0$, and the entire linearized metric has compact support in $u$ inside the strip. Large transverse periods leave (7) unchanged. On each $t$ slice this gives compact Cauchy support, including the periodic transverse directions.

Let $\mathcal H$ be the ungauged Einstein–Hilbert Hessian with respect to the covariant metric, including its $1/(16\pi G_N)$ action normalization. Choose a smooth time switch $\theta(t)$ equal to zero in the past and one in the future of a compact time band. The probe has linear smearing
$$
 f_d^{\rm grav}=\mathcal H(\theta h_d).
$$
It is smooth and supported in a compact spacetime set because $\mathcal H h_d=0$ and (8) makes the support spatially compact across the band. The linearized Bianchi identity gives its conservation. The retarded and advanced solutions are $\theta h_d$ and $(\theta-1)h_d$ modulo gauge. For each field $b$ solve the vector wave equation $\Box \xi=-\nabla\cdot\bar b$ with the corresponding retarded or advanced support. Adding $\mathcal L_\xi g$ puts $b$ in de Donder gauge, and uniqueness identifies the Green solution. Compactness of $\operatorname{supp}j$ extends (6) to either correcting vector by a cutoff. For $E=G_{\rm ret}-G_{\rm adv}$ in Einstein–Hilbert normalization, $E f_d^{\rm grav}=h_d$ modulo gauge. Consequently the right hand side of (7) is a limit of actual mixed brackets $\{\bar U,F_d^{\rm grav}\}=j[E f_d^{\rm grav}]$ for one calibrated emitter. Each sufficiently narrow smooth probe already gives a nonzero bracket. The limiting family has no fixed amplitude or norm assumption. [Fewster and Hunt, Lemma 3.10 and time-slice Eq. (4.28)](https://arxiv.org/pdf/1203.0261#page=18)

## Changing the ensemble at the same diamond

The return time may instead be determined by the weighted waist radius $M$, or by the total waist area $\mathscr A=4\pi\langle D(S)^2\rangle$. In each case vary $L$ in $q=(L,L,0,0)$, so $\ell=\sqrt2 L$. To check that $M$ is a regular control even at $L=1$, work in the stereographic tip labels $k$ of the focal calculation. Put $u=u(k)$ at the waist, $I_i(u)=\int_0^u A_i^{-2}$ and $T_i=I_i(L)$. The intersection solves $\sum k_i^2 m_i(u,L)=2L$, with $m_i=I_i T_i/(T_i-I_i)$. Each $m_i$ decreases in $L$ at fixed $u$ and increases in $u$. Thus $u$ and the waist radius $\rho=F_0(u)/a(k)$ increase strictly with $L$ away from the stereographic poles, where $a(k)=\sqrt2/(1+|k|^2/2)$. Smooth physical sky coordinates control both poles.

At $L=1$, put $j_1(u)=\sinh u$, $j_2(u)=\sin u$. The identity $m_i=j_i(u)j_i(1)/j_i(1-u)$ gives $m_i=\beta_i u/(1-u)$ with $\sin^2 1\le\beta_i\le\sinh^2 1$ by the monotonicity of $j_i(u)/u$. With $t_k=|k|^2/2$ and $\beta=\sum k_i^2\beta_i/|k|^2$, it follows that
$$
 \rho=\frac{F_0(u)}{u\sqrt2}\frac{1+t_k}{1+\beta t_k},\qquad
 \frac{\max\rho}{\min\rho}\le
 \frac{6}{\sqrt{35}}\left(\frac{\sinh 1}{\sin 1}\right)^2<2 .
$$
Indeed $F_0(u)/u\le1$ follows from optical concavity with unit initial slope, while $(\sinh u/u)(\sin u/u)\ge(1+u^2/6)(1-u^2/6)\ge35/36$. Since $M$ is a weighted mean of $\rho$, one has $2\rho-M>0$ throughout the sky. Then $\partial_L M=\langle(2\rho-M)\partial_L\rho\rangle/\langle\rho\rangle>0$. Monotonicity also gives $\partial_L\mathscr A>0$.

The focal packet has $\delta M,\delta\mathscr A=O(d)$ at fixed $L$. The waist perturbations in the regular $|u-c|\le d$ belt are bounded and its sky area is $O(d)$. Elsewhere the fixed-argument optical perturbations and the waist displacement have $O(d)$ tails, with the integrable polar estimates derived for the spherical cones. Equivalently, the two required angular integrals in the $k$ chart are proportional to $\int F_0(u)^2d^2k$ and $\int a(k) F_0(u)d^2k$. Enforcing either one scalar control by its implicit $L$ adjustment changes the clock differential by $O(d)$. Thus (7) holds with $M$ fixed at its background value, and also when just $\mathscr A$ is fixed there. These are separate one-constraint experiments. The distributional Ward identity holds for each since calibrated observer isometries also preserve its waist constraint. [Waist perturbation estimates and finite-area comparison](joint-focal.md)

## Distributional response and scope

For a formally self-adjoint hyperbolic gauge fixing of the vacuum Einstein Hessian (with the appropriate trace reversal), define the distributional field by $\langle E j,h\rangle=-j[E h]$ for smooth compact tests $h$. The conserved source (6) propagates to a homogeneous linearized Einstein field modulo gauge because the divergence identity for the de Donder operator extends by duality. Its support lies in $J(\operatorname{supp}j)$. With the first-slot convention $\Omega=\int\delta\pi\wedge\delta q$, $\Omega(X_F,h)=dF[h]$, the weak Hamiltonian field is $X_F=-E j$. For any smooth compact conserved probe $f$ the mixed bracket is $j[E f]=-\langle E j,f\rangle$. Distributional Green operators require global propagation and the chosen background. Equations (4), (6) and (7) specify respectively the source, its gauge constraint and a nonzero measurement of its field. [Bär, §4 on Green operators for distributional sections](https://arxiv.org/pdf/1310.0738) · [Fewster and Hunt, divergence transport (3.14) and smooth pairing (4.23)](https://arxiv.org/pdf/1203.0261#page=17) · [Tensor Green kernel on this Rosen strip](weak-rosen-green.md)

The field $X_F$ has **no globally smooth representative**, even after a distributional gauge transformation. In spacetime $h_d\to0$ distributionally. The leading profile has zero full moment in the smooth coordinate $u$. The variation $w$ is bounded inside its shrinking packet and $O(d)$ outside, including the smooth post-tip controls. Applying the fixed differential operator to $\theta h_d$ then gives $f_d^{\rm grav}\to0$ distributionally. These sources have a common compact support by (8) and the fixed time band. A smooth representative would pair to zero in the limit. Every distributional gauge term pairs to zero for each $d$ by conservation of $f_d^{\rm grav}$. Equation (7) contradicts the smooth limit in each preparation.

### Where the singularity travels

Every global representative has a singular point on each transverse torus $u=c$, $t=t_0$. If it were smooth near such a compact torus, choose the time switch in a sufficiently narrow band about $t_0$. On a common compact support outside that neighborhood the sources converge to zero in $C^\infty$. The original pulse vanishes there for small $d$, the residual scale-factor data are $O(d)$ with all derivatives by homogeneous propagation, and the two post-tip profiles have $O(d)$ coefficients. A cutoff within the smooth neighborhood pairs to zero by distributional convergence. The complementary cutoff pairs to zero against any distribution. This contradicts (7).

One can quantify the regularity detected by this test. The identity $f_d^{\rm grav}=[\mathcal H,\theta]h_d$ leaves at most one derivative of the metric. Its transverse components in $h_d$ are smooth coefficients times the profile $f_d$, the scale variation $w$, and the two smooth corrections. The profile has bounded $L^1$ norm, zero integral and shrinking support. It therefore tends to zero against continuous tests, and its first derivative tends to zero against $C^1$ tests. The compactly supported $w$ tends to zero in $L^2$ by its collar and tail bounds. Consequently a $C^1$ representative on a neighborhood of the entire torus is also excluded. For the isotropic local spacetime Sobolev norm the critical estimate, in the single profile coordinate, is
$$
 \|\partial_u f_d\|_{H^{-3/2}(\mathbb R)}^2
 \le {1\over 2\pi}\int_\mathbb R
             |\widehat f(\eta)|^2\,{d\eta\over|\eta|}<\infty .
$$
It follows by inserting $i\xi e^{-ic\xi}\widehat f(d\xi)$ and using the zero mean at $\eta=0$. A smooth compact cutoff in the other coordinates preserves this uniform bound in spacetime, as does multiplication by fixed smooth coefficients. The derivatives of the $w$ terms are bounded in $H^{-1}$ on the compact set. Density of smooth tests and the common compact support now give weak convergence to zero in $H^{-3/2}$. The same contradiction excludes a representative of local class $H^{3/2}$ on a neighborhood of the entire torus. The estimate allows singularities milder than a jump in the metric.

For the causal de Donder representative $X_F=-E j$, the null direction and the transverse position can both be specified. Formula (4) integrates smooth finite-order metric jets over the two regular null faces and the observer segment, with smooth weights on either side of the cap. Locally split at the cap, use regular interior charts on each face, and include the integration boundaries. The wavefront of this source is contained in the union of the conormals of these smooth pieces and their edges, by pushforward and differentiation. At $u=c$, the coordinate $u$ changes along the generators of each regular face. Its exceptional constant-$u$ axial generators have $u=0$ and $u=1$. The restriction to the waist has a regular level and the timelike observer has $V^u>0$. The only place where a nonzero multiple of $du$ can be conormal is the cap maximum, at $k=0$, $x_1=x_2=v=0$. For the causal Green kernel the output wavefront is contained in the null geodesic flow of the input wavefront. Since $du$ is parallel and its metric dual is $-\partial_v$, the only possible propagation of this covector at $u=c$ is the axial line $x_1=x_2=0$, including its torus identifications. Smooth interior tails of the tensor kernel respect this wavefront bound. [Duistermaat and Hörmander, propagation of singularities](https://doi.org/10.1007/BF02392165) · [Vector bundle causal kernel, Brunetti and Moro, §4](https://arxiv.org/pdf/2210.15062#page=17)

To see that this direction actually occurs, multiply any representative by the smooth tensor coefficients of $[\mathcal H,\theta]h_d$, with a compact cutoff equal to one on the common source support. Each resulting term pairs a distribution pushed to the $u$ coordinate with a smooth one-dimensional profile from the finite list $f_d,\partial_u f_d,w,\partial_u w$ and the post-tip corrections. The coefficients are fixed in $d$, with the small correction amplitudes included in the profiles. Suppose a representative had no wavefront parallel to $du$ over $u=c$, $t=t_0$. Compactness of this torus and closedness of the wavefront set permit a switch supported in derivative sufficiently near $t_0$ and a collar of $u=c$ where the pushforward theorem gives smooth projected distributions. Each profile tends weakly to zero there. Off the collar convergence in $C^\infty$ handles the rest, as above. Equation (7) contradicts this supposition. Reality supplies both signs of the covector. In particular, for this causal de Donder representative,
$$
 \big((u,v,x_1,x_2)=(c,v,0,0),\,\alpha\,du\big)\in\mathrm{WF}(X_F)
 \quad\text{for every }v\in\mathbb R,\quad\alpha\ne0.                  \tag{9}
$$
This identifies the two covector directions over the axial line. Other directions of the wavefront are possible. In an arbitrary distributional gauge the marginal argument forces such directions somewhere on every transverse torus, without fixing the transverse point. [Pushforward theorem, Brouder, Dang and Hélein, Theorem 6.3](https://arxiv.org/pdf/1409.7662#page=21)

For two sharp clocks a sufficient condition for evaluating one on the field of the other is the Hörmander product criterion. Over common base points $\mathrm{WF}(j_1)$ must avoid $-\mathrm{WF}(E j_2)$. In this particular example the axial directions in (9) require an input wavefront at the cap pole in both signs, since it is the only possible input for this ray. Hence the criterion fails for the clock paired with its own field there. A contraction, an antisymmetry convention or a specified regularization may still yield a value. The result establishes a mixed bracket with smooth probes. The independently marked cap, the reduction of its corner variables and the quantum domain remain proof gaps for the proposed finite-diamond construction. [Wavefront product, Brouder, Dang and Hélein, Theorem 13](https://arxiv.org/abs/1404.1778) · [Smooth-vector obstruction in this focal experiment](joint-focal.md)

## Numerical checks

Run `python3 -B checks/weak_curved.py` and `make check` from the repository root. The focused script varies $\kappa$ with an uncalibrated fixed coordinate emitter in the symmetric wave. Forty fixed emitter-sky directions are used in both calculations. The first calculation integrates (2) and (3), including the metric insertion on the returning geodesic. The second differences the exact two-cone root, cap and averaged clock. This comparison tests the differential for that finite angular quadrature. With the superenergy fixed by a boost $\chi=-\log\kappa$, the amplitude rescaling becomes an isometry of the local experiment and the response vanishes. A separate integration of the forced scale-factor equation checks the compact completion (8) after the two post-tip controls. [Adjoint and control check](../checks/weak_curved.py)

~~~text
Fixed emitter, adjoint derivative 0.00512673
Fixed emitter, direct derivative  0.00512673
Calibrated curvature-scale derivative below 1e-10: True
Post-tip control residual below 1e-8: True
~~~

Run `python3 -B checks/joint_focal.py` for the smooth pulse amplitudes in (7). Its narrowest tested width $0.003125$ gives $-0.059993$ and its analytic limiting prediction is $-0.060534$. The finite-width number uses the fixed proper duration. [Focal check](../checks/joint_focal.py)
