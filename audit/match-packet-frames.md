# Transporting a probe through the two gravitational pulses

The null generators of the marked diamond recover their affine position, tangent and entire transported tetrad after either complete pulse. A different experiment transports a frame along a radius of the spacelike cap. It can register a finite boost. A second choice of pulse removes that signal exactly while preserving a nonzero clock Hessian. The calculations below are first variations of smooth vacuum solutions about Minkowski space, with the waist radius as the unit of length. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Pulse preparation and clock](match-packets.md)

## Which null probes recover their frames?

Write the flat ray as $t=T+s$, $\mathbf x=\mathbf x_0+s n$, $|n|=1$. Put $d=n\cdot\mathbf x_0$, $\mathbf b=\mathbf x_0-dn$, $\tau=T-d$, $u=t+r$ and $z=u-\tau$. Then $s+d=(z^2-|\mathbf b|^2)/(2z)$ and $ds/r=du/z$. Consider a segment whose endpoints miss the pulse, on which the advanced profile $F(t+r)$ traverses its entire support and the retarded profile vanishes. On the background generators each lobe in the two-pulse test meets these conditions separately on the appropriate segment. They persist on an open set of translated rays and nearby null directions for every fixed pulse width. For the master field $\phi=F(t+r)/r$ the two transfer integrals are
$$
 L_0=\int\phi\,ds=\int \frac{F(u)}z\,du,\qquad
 L_1=\int s\phi\,ds=\frac12\int F(u)\left(1-\frac{|\mathbf b|^2}{z^2}\right)du-d L_0 .
 \tag{1}
$$
All integrations use the same affine interval for nearby rays. The endpoints stay outside the support. Hence the spatial differential operator generating the transverse-traceless (TT) metric $h$ commutes with both integrals, acting on $\mathbf x_0$ at fixed $T,n$.

The operator $P_{ij}=\delta_{ij}\Delta-\partial_i\partial_j$ acts on $L_0(\tau)$ as $(\delta_{ij}-n_i n_j)\partial_\tau^2$. Thus the TT integral $\int h_{in}\,ds$ vanishes for every $i$. Also $\int s h_{nn}\,ds=0$. In fact the $nn$ component of $(P_{ik}P_{jl}-P_{ij}P_{kl}/2)S_{kl}$ contains at least three transverse derivatives in every term except
$$
 S_{AB}\,\partial_n^2(\partial_A\partial_B-\delta_{AB}\Delta_\perp/2).
$$
This trace-free Hessian annihilates the isotropic transverse quadratic in $L_1$. The other terms kill it by degree. Here $A,B$ run over the two screen directions.

For $k=(1,n)$, the integral of $\delta\Gamma^\mu_{kk}=\partial_k h^\mu{}_k-\partial^\mu h_{kk}/2$ and its first affine moment now vanish. The geodesic equation gives zero displacement and tangent perturbation after the crossing. In the symmetric tetrad the linear spin connection along the ray is $\delta\omega_{k\mu\nu}=(\partial_\nu h_{k\mu}-\partial_\mu h_{k\nu})/2$ up to convention for the frame indices. Its integral vanishes by the same $L_0$ identity, also for components involving the time axis. The calculation applies in reverse along the very same ray and on the other cone after $F(u)\mapsto -F(2-u)$. Thus frames propagated along the sheet from the waist $S$ or the relevant tip have their original values in the rim collar at first order. Variation of the null launch directions within this open family gives the same identities. [V1, geodesic displacement (3.58)](https://arxiv.org/html/2611.34924v1#S3.E58)

In particular the vertex angular marking, area per solid angle and affine area slope recover their original values. In the pulse-free spacetime collars the TT metric itself, its connection in the inertial tetrad and all local derivatives are unchanged. Both normal second fundamental forms and the normal connection of the physical cuts are then fixed. For nearby exact small-amplitude geometries, a spacelike cap through the actual cut $C_g(n)$ can be chosen in the same inertial coordinate chart by
$$
 E_g(r,n)=(a,rn)+\chi(r)\,[C_g(n)-(a,an)],\qquad 0\le r\le a .
 \tag{2}
$$
Take $\chi=1$ near $a$ and zero near the origin. The graph is a smooth spacelike ball for sufficiently small amplitudes, separately for each pulse width. It enters the interior side of the cone by transversality at its boundary. Its data satisfy the cap constraints by restriction. Since the first variation of $C_g$ under the pulse is identically zero, (2) gives zero variation of the cap embedding and of its physical unit normal on the rim. The spacetime fields in the cap interior still vary. On an overlap, a prescribed source geodesic and its transported polarization agree between the two restrictions of the same solution. A source placed *inside* a pulse can measure it. [V1, matching on the overlap (3.60)](https://arxiv.org/html/2611.34924v1#S3.E60)

## Changing the direction of a physical probe

Changing from null to timelike or spacelike transport can be measured. Let $Q=S_{ij}n^in^j$, $E_A=(S n)_A$ in an orthonormal screen, and write $h_{nn}=Q A$, $h_{nA}=E_A B$ for the incoming radial master. Direct radial differentiation gives, at $u=t+r$,
$$
 \begin{aligned}
 A&=6F''/r^3-18F'/r^4+18F/r^5,\\
 B&=2F'''/r^2-6F''/r^3+12F'/r^4-12F/r^5 .
 \end{aligned} \tag{3}
$$
Start a radial probe at $S$ and follow the background line $r=s$, $t=1+m(s-1)$ toward $s=a$, keeping the spatial component of the affine launch vector fixed. The null direction has $m=1$. Write $\alpha=1+m$. For each fixed width, $m$ in a neighborhood of one keeps the outer lobe wholly inside the segment, the inner one outside and the retarded phase away from both. Integrating (3) by parts on $a<s<1$ gives
$$
 \int_a^1\partial_t B\,ds
 =\frac{-60(\alpha-2)(\alpha^2-2\alpha+2)}{\alpha^4}
        \int_a^1 \frac{F(1-m+\alpha s)}{s^6}\,ds . \tag{4}
$$
One endpoint transverse boost of the transported frame is this expression times $E_A/2$, up to orientation. It vanishes on the null ray. Its derivative with respect to $m$ there has coefficient $-15/2$ before the factor $E_A/2$, and the remaining integral tends to $a^{-6}$ for the original unit-mass outer lobe. The frame *value* on the generator and its derivatives along families of null launches are compatible with a finite response when the probe direction changes causal character. Such a derivative involves the connection integrated along the path. It supplies a distinct measurement from the local metric jets on the cut.

The scalar boost obtained from the normal-plane curl of the *displacement* gives a different answer. Denote the fixed-affine-parameter displacement of the launched geodesic by $\chi$. The two radial Christoffel components on the unperturbed line are $\delta\Gamma^t_{kk}=Q\partial_t A/2$ and $\delta\Gamma^r_{kk}=Q(d_s A+m\partial_t A)/2$. Integrating the displacement equation from $S$ to an endpoint $s$ in the rim collar gives
$$
 \chi^r-m\chi^t=\frac Q2\int_s^1 A\,dr,\qquad
 \int_s^1 A\,dr=\frac{18(\alpha-2)^2}{\alpha^2}
                      \int_s^1 F(1-m+\alpha r)r^{-5}\,dr .
$$
Both displacements vanish on the null family there. Their $m$ derivatives at one are equal, while $t-r=(m-1)(s-1)$ at the endpoint. Consequently the first-order normal derivative of the lowered normal-plane displacement has the form $c\,d(t-r)\otimes d(t-r)$. Its antisymmetric part vanishes, so this particular off-sheet lift also has zero scalar Komar boost on the flat cut. Additional source jets depending on the traversed path require their own measurement or the finite-rank test. [Komar normal derivative on a joint](match-action.md) · [Finite-rank test](match-packets.md)

## A spacelike cap radius and a pulse which cancels its response

On the cap $t=a$ let $r$ run from the center to $a$. Only the inner lobe crosses this radius. The other master phase $a-r$ lies in $[0,a]$, outside the support for $a=1/3$ and sufficiently small widths. Define $M_p=\int_0^a F(a+r)r^{-p}dr$. The timelike vector initially equal to $\partial_t$, parallel transported along this radius, acquires radial component $-45 Q M_6$ and screen components $-30E_A M_6$. These follow from integrating $-\partial_t h_{ni}/2$. A correction to the path contributes zero to first-order parallel transport in the inertial background frame. If the probe follows the spacetime spacelike geodesic shot from the center with the original radial unit speed, its endpoint position also probes $M_5$. For example, $\delta\Gamma^n_{nn}=Q\partial_r A/2$ at fixed $t$ and $\int A\,dr=18M_5$, so $\delta r(a)=-9Q M_5$. All connection components of this transport have radial weight $r^{-6}$ after transferring derivatives. Their first moments and the first moments in the geodesic equation have weights in the span of $r^{-5}$ and $r^{-6}$. This follows from the common total order five in each $F^{(j)}/r^{5-j}$ term of the metric and one extra derivative for the connection.

Write $b_\eta(x)=b(x/\eta)/\eta$, with $b$ smooth of unit integral supported in $(-1,1)$, and $B_\eta(v)=b_\eta(v-a-2\eta)-b_\eta(v-a+2\eta)$. Replace the master by
$$
 F_\eta(2v)=P(v)B_\eta''(v),\qquad P(v)=\left(\frac{2v-a}{a}\right)^6 . \tag{5}
$$
Both lobes are smooth and have the same supports as before. Along the cap radius $r=2v-a$, $dr=2dv$. For $p=5,6$ the weight $P(v)(2v-a)^{-p}=a^{-6}(2v-a)^{6-p}$ is affine or constant. Two integrations by parts give $M_5=M_6=0$ for each fully traversed lobe separately. This includes the spacelike launch measurement just specified. It makes no assertion of cancellation for a different probe weight, such as (4).

For the fixed smooth reference choose $F_W(u)=a\,7!(u-2a)^{12}/(12!\,2^8)$ near $2a$, cut off away from there. Its conformal strain slope has leading term $G'_W(v)=(v-a)^7+O((v-a)^8)$. The radial density $K$ in the clock Hessian after integration by parts against $F_\eta(2v)$ starts on the outer side as
$$
 K(v)=-\frac3{20}\frac{1-a}{16}\frac{7!}{2!}(v-a)^2+O((v-a)^3).
$$
Since $P(a)=1$, the outer lobe tests $(P K)''(a^+)$, giving $-63/2$ at $a=1/3$. On the full waist disk the signed masters still tend to zero distributionally, since derivatives and smooth weights preserve distributional convergence. This calibrated Hessian uses the normalized radius $v$ and the specified wave amplitudes. [Clock Hessian and its radial density](match-packets.md)

The interior sheet and cap need not have separate zero symplectic products. For the original two unit-mass lobes take a smooth reference $X$ with $G_X(v)=(v-a)^5+O((v-a)^6)$ by giving $F_X$ a ninth-order zero with suitable nonzero coefficient. Stripping the fixed angular and action factors, the sheet radiation has Wronskian $\int_a^1 v^2(G_XG'_Z-G_ZG'_X)dv$. After one integration by parts its coefficient of $G_Z$ starts as $-10a^2(v-a)^4$. Transferring the four derivatives in $G_Z$ gives the outer-lobe limit $-15a=-5$. The cap contributes the opposite limit to the ordinary Einstein current by conservation on the joined surface and the distributional cancellation on the waist disk. This uses a response which extends smoothly across the seam. [Joined Einstein current](match-packets.md) · [V1, radiative symplectic form (3.42b–c)](https://arxiv.org/html/2611.34924v1#S3.E42.2)

Run `python3 -B checks/match_packet_frames.py`. It checks the exact full-lobe transport coefficients, the two cap moment cancellations and the one-sided radial Wronskian. Direct integration of the original optical slopes with (5) gives the final line `Filtered clock Hessian = -31.508652, analytic limit = -63/2` at width $2^{-19}$. The numerical bell proportional to $(1-x^2)^{12}$ inside $|x|<1$ has the required eight derivatives. Run `make check` for the full suite. [Executable check](../checks/match_packet_frames.py)
