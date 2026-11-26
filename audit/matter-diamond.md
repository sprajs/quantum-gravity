# Two light-cone clocks in an exact Einstein–scalar diamond

A freely falling observer sends a spherical flash at event $p$ and receives its immediate echoes at event $q$. The events that can return a flash at precisely $q$ form a closed sphere $S$. How large is that sphere, and what does the capped affine clock read on each of its two light cones? In an expanding universe filled by a homogeneous massless scalar, the sphere is round and the optical shear vanishes. The scalar's null energy nevertheless makes both clocks exceed $(1-\epsilon)\sqrt{\mathscr A/(4\pi)}$. Their readings can differ even though both refer to the same sphere. This is a four-dimensional classical matter benchmark for any extension of Venkatesa Chandrasekaran's vacuum construction. The paper supplies the affine clock, the angular average and a *vacuum* focusing law. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Clock and average, Eqs. (3.27)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27)

## Prepare the diamond on one observer's clock

Work in units $c=1$, with zero cosmological constant, spatial slices $\mathbb R^3$, and a canonically normalized, minimally coupled scalar with zero potential. Cosmic time $t>0$ is proper time along the comoving observer at the origin. The continuum equations $3H^2=4\pi G\dot\phi^2$ and $\partial_t(a^3\dot\phi)=0$ give the expanding solution

$$
a(t)=a_0(t/t_0)^{1/3},\qquad
\phi(t)=\phi_0\pm\frac{\log(t/t_0)}{\sqrt{12\pi G}},\qquad
P=\rho=\tfrac12\dot\phi^2.
$$

The two clock events can be specified by proper times $0<t_p<t_q$ or by the corresponding readings of the monotone scalar on this same worldline. Only combinations independent of the choice of comoving length unit enter the predictions below. [Jercher and Steinhaus, continuum equations (81)–(83)](https://arxiv.org/html/2312.11639v2#A2.SS1)

Write $dt=a\,d\eta$ with $\eta=0$ at the singularity, so $a=C\sqrt{\eta}$ and $t=2a\eta/3$. The conformal metric is $ds^2=a^2(-d\eta^2+d\chi^2+\chi^2d\Omega^2)$. From the past tip the null sheet has $\chi=\eta-\eta_p$, and from the future tip it has $\chi=\eta_q-\eta$. Their intersection and its area are exact,

$$
h=\eta_S=\frac{\eta_q+\eta_p}{2},\qquad
\delta=\frac{\eta_q-\eta_p}{\eta_q+\eta_p}\in(0,1),\qquad
\chi_S=h\delta,\qquad R=a_S h\delta,\qquad \mathscr A=4\pi R^2 .
$$

Here $a_S=a(h)$. The observer's measured half-duration $L=(t_q-t_p)/2$ is the radar range for an immediate echo from $S$. Integrating $dt$ gives

$$
\frac{L}{R}
=\frac{(1+\delta)^{3/2}-(1-\delta)^{3/2}}{3\delta}
=1-\frac{\delta^2}{24}+O(\delta^4).
$$

This ratio is the average of $\sqrt{z}$ over $1-\delta\le z\le1+\delta$. Strict concavity makes $L<R$ for every nonzero width. As a check, the four-dimensional small-diamond result of Gibbons and Solodukhin gives $\mathscr A/(4\pi L^2)=1-\mathcal R(2L)^2/72+\cdots$. The spacetime Ricci scalar here is $\mathcal R=-6H^2$, and $\delta=2H_S R$, so the area correction agrees. [Gibbons and Solodukhin, Eq. (29)](https://arxiv.org/pdf/hep-th/0703098#page=6)

## Put the cap at a measured area

Orient an affine parameter $\lambda$ from each tip toward $S$. Set $b=+1$ on the future-directed rays from $p$ and $b=-1$ on the past-directed rays from $q$. On either ray write $x=\chi/\chi_S$, $d=b\delta$ and $w=\eta/h=1-d(1-x)$. Calibrate $d\Omega$ in the comoving tip frame and normalize the tangent by $|k\cdot U_{\rm tip}|=1$. Then $a^2 d\eta/d\lambda=b\,a_{\rm tip}$ by the null geodesic equation. The area distance $D=\sqrt{dA/d\Omega}$ and affine increment satisfy

$$
\frac{D(x)}{R}=x\sqrt{w},\qquad
\frac{d\lambda}{dx}=\frac{R\,w}{\sqrt{1-d}},\qquad
D'(0)=1 ,
$$

where the prime denotes an affine derivative and $\lambda=0$ at the tip. Every $0<\epsilon<1$ selects a unique cap $x_c$ by $D_c=\epsilon R$ (equivalently $A_c/\mathscr A=\epsilon^2$). Indeed $\partial_x(D/R)=[1-d+3dx/2]/\sqrt w$. Its numerator is at least $1-\delta$ on the past-tip sheet and $1-\delta/2$ on the future-tip sheet. Both are strictly positive. Each radial sky direction meets $S$ once, with positive transverse area throughout $0<x\le1$, so neither a turning point nor a generator crossing intervenes.

Set $y=\sqrt{w_c}=a_c/a_S$. The cap solves $x_c y=\epsilon$ and $y^2=1-d(1-x_c)$. Multiplying the affine cap slope by the cap-to-waist interval gives

$$
\frac{U_b}{R}=\frac{D'(\lambda_c)(\lambda_S-\lambda_c)}{R}
=\left(y+\frac{d x_c}{2y}\right)\frac{(1-x_c)(1+y^2)}{2y^2}.
$$

An affine rescaling changes the slope and interval inversely. Spherical symmetry makes the $D_S$-weighted average over the full observer sky equal to $U_b$ on each sheet. These are two possible readings of the diamond clock, one from each cap. In a proposed observation the angular aperture and proper area determine $D$. Reconstructing the cap slope and affine interval additionally requires optical measurements along the ray, such as local distances and frequency ratios from comoving observers. A single radar return determines $L$. [Angular average, Eq. (3.28)](https://arxiv.org/html/2611.34924v1#S3.E28) · [Affine reconstruction from frequency ratios](observable-optics.md)

## Isolate the matter focusing

Here $R_{kk}=8\pi G(k\cdot\nabla\phi)^2=3(d\eta/d\lambda)^2/(2\eta^2)>0$. The shear-free optical equation $D''=-R_{kk}D/2$ therefore gives

$$
U_b-(1-\epsilon)R
=\tfrac12\int_{\lambda_c}^{\lambda_S}(\lambda_S-s)D(s)R_{kk}(s)\,ds .
$$

In the increasing area coordinate $v=D/R$, the same equation reads $-\partial_v\log D'=4\pi Gv(\partial_v\phi)^2$. It specifies the matter contribution missing if the vacuum shear expression in Eq. (3.26) is applied to this solution. Eliminating $d(1-x_c)$ in the exact reading gives a strictly positive expression on either branch,

$$
\boxed{\frac{U_b-(1-\epsilon)R}{R}
=\frac{\delta^2(1-x_c)^2}{4y^3}
\left[x_c+\frac{2y^2}{(1+y)^2}\right].}
$$

At fixed $\epsilon$, the small-diamond limit gives $x_c=\epsilon+O(\delta)$ and $y=1+O(\delta)$. Hence the first matter correction is identical on both sheets. Its size depends on which flat diamond one prepares for comparison,

$$
\begin{aligned}
\frac{U_b-(1-\epsilon)R}{R}
 &=\delta^2\frac{(1-\epsilon)^2(1+2\epsilon)}{8}+O(\delta^3),\\
\frac{U_b-(1-\epsilon)L}{R}
 &=\delta^2\left[\frac{(1-\epsilon)^2(1+2\epsilon)}{8}
                 +\frac{1-\epsilon}{24}\right]+O(\delta^3).
\end{aligned}
$$

The first comparison matches the waist area, so the flat reading equals the area bound. The second matches the observer's elapsed time $2L$. Its additional term comes from the change in waist area. Both comparisons are strictly positive at finite width since $U_b>(1-\epsilon)R>(1-\epsilon)L$. Since $\delta=2H_S R$ and $H_S^2=8\pi G\rho_S/3$, the leading fractional excess scales linearly with the scalar energy density at fixed physical radius. At fixed $0<\delta<1$, shrinking the cap onto its smooth vertex gives $U_b/R\to(1-d/2)/\sqrt{1-d}$, the entire tip-to-waist affine distance in tip units. Moving the cap to the waist gives $U_b/[(1-\epsilon)R]\to1$. The endpoint $\delta=1$ puts the past tip on the big-bang singularity and falls outside this preparation.

This result tests classical backreaction in a homogeneous state. A prediction for quantum fluctuations would require a matter-coupled quantum clock and a specified joint state.

## A benchmark in exact fractions

Choose $\delta=3/4$ and $\epsilon=5/16$. This sets $\eta_q/\eta_p=7$ and $A_c/\mathscr A=25/256$ on both cones. In the table the area bound divided by $R$ is $11/16$. For a flat diamond of the same radar range the corresponding number is $(11/16)(7\sqrt7-1)/18$.

| Starting tip | $x_c$ | $a_c/a_S$ | $U_b/R$ | Excess above area bound, in units of $R$ |
|---|---:|---:|---:|---:|
| Past | $5/12$ | $3/4$ | $4025/5184$ | $461/5184$ |
| Future | $1/4$ | $5/4$ | $5781/8000$ | $281/8000$ |

From the repository root run `python3 checks/matter_diamond.py`. It checks these four clock and excess fractions exactly, differentiates the area radius against the scalar focusing equation at both caps, and locates caps independently from the measured area in the weak limit. For $\epsilon=1/2$ the reported coefficients of $\delta^2$ are `0.0625` at equal area and `0.0833333333` at equal radar range. The repository suite runs the same check with `make check`. [Executable calculation](../checks/matter_diamond.py)
