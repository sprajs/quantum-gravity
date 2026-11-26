# A clock bracket across a spacelike cap and a shearing null sheet

A polarized vacuum Einstein solution realizes the endpoint example of the fixed-density bracket test. A smooth gravitational perturbation with nonzero curvature changes the affine clock by $-3/2$ entirely through its rim term. For this clock, the retarded-minus-advanced gravitational response vanishes in the open spacelike cap and has a nonzero limit at the rim when approached from inside the region along the null sheet. Its initial momentum contains a delta distribution on the rim. A smooth matched tangent cannot represent the clock differential in this sector. Brackets with smooth probes still exist. The calculation uses a cylindrical light front with compactified axial direction, fixed embeddings in areal coordinates and a globally specified vacuum continuation. The cuts are tori. The result gives a junction test for the spherical problem with freely moving boundary frames. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.18)–(3.19)](https://arxiv.org/html/2611.34924v1#S3.E18) · [Earlier fixed-density endpoint calculation](endpoint-inverse.md)

## A graviton whose clock variation comes entirely from the rim

Use the polarized Einstein–Rosen metric, with $\varphi$ periodic of period $2\pi$ and $z$ periodic of length $L$. Select dimensionless coordinate units and take $L=2$ when normalizing the reference cut measure $d\varphi\,dz$ to $4\pi$. The vacuum equations in areal radius $r$ read
$$
 ds^2=e^{2(\gamma-\psi)}(-dt^2+dr^2)+r^2e^{-2\psi}d\varphi^2+e^{2\psi}dz^2,
 \qquad
 \psi_{tt}=\psi_{rr}+r^{-1}\psi_r,\quad
 \gamma_r=r(\psi_t^2+\psi_r^2),\quad \gamma_t=2r\psi_t\psi_r .
$$
Regularity fixes $\gamma(t,0)=0$. The field $\psi$ varies the norm of the axial Killing vector with its period fixed. It is a physical polarization. On the flat background $\psi=\gamma=0$ we have $\delta\gamma=0$. The induced metrics and their normalizations below follow directly from this four-dimensional metric. [Kuchař, canonical reduction of cylindrical gravitational waves](https://doi.org/10.1103/PhysRevD.4.955)

Take the cap $t=0$, $r\le a$ and the outgoing sheet $t=r-a$, $a\le r\le b$, with $0<a<b$. A second radial null sheet can return from the waist to $r=a$ at $t=2(b-a)$. Both sheets stay regular up to their finite rims. The cut density is $r$, so $\varrho=\sqrt r$, $v=\sqrt{r/b}$ and $\epsilon=\sqrt{a/b}$ on the first sheet for every $\psi$. Its conformal metric is diagonal with $z^1=\log r-2\psi$, $z^2=0$, in the dyad ordered $(\varphi,z)$. Even the flat background shears because the circumference expands while the axial length is constant. The characteristic from the axis has a line of origins. A regular point vertex imposes different global data.

Fix the affine parameter by $\partial_u\sqrt r=1$ at the rim. The radial null geodesic equation gives $du/dr\propto e^{2(\gamma-\psi)}$ along the sheet. Thus the angularly constant clock and its differential at flat space are
$$
 U=\frac{1}{2\sqrt a}\int_a^b
 e^{2[(\gamma-\psi)(s-a,s)-(\gamma-\psi)(0,a)]}\,ds,
 \qquad
 dU[h]=\frac{b-a}{\sqrt a}\,h(0,a)
 -\frac1{\sqrt a}\int_a^b h(s-a,s)\,ds ,
 \tag{1}
$$
where $h=\delta\psi$. The same formula follows by inserting the intrinsic conformal metric into the focusing integral. The $\psi(0,a)$ term in (1) is produced by the affine normalization at the spacelike cap. At $a=1/4$, $b=1$ the background has $z^1=2\log v$, $U=3/4$. With the transported variation $Y=v\delta z^1=-2v h$, (1) is $2\int_{1/2}^1Y\,dv-3Y(1/2)/2$. [v1, Eqs. (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27)

For an explicit physical preparation put $k=1/[b(b-a)]$ and
$$
 P(t,r)=-1+k(r^2-a^2+2t^2),\qquad
 \psi=\lambda P,\qquad
 \gamma=\lambda^2 k^2(r^4+8t^2r^2).
$$
These functions solve the vacuum equations above. One may smoothly cut off $P(0,r)$ outside a neighborhood of $[0,2b-a]$ and evolve its data with $P_t(0,r)=0$. Finite propagation preserves the displayed solution on the cap and first sheet. At linear order $\delta R_{tztz}=-4k$ in the flat background convention $R^a{}_{bcd}=\partial_c\Gamma^a_{db}-\partial_d\Gamma^a_{cb}+\cdots$. On the sheet, $P(0,a)=-1$ and $\int_a^bP(s-a,s)ds=0$. Equation (1) therefore gives $dU[P]=-3/2$ at the stated radii. In the usual convention $\{\psi,\pi_\psi\}=1$, this is $\{U,\int g\pi_\psi\,dr\}$ evaluated at flat space, with $g$ the initial profile of the compactly supported preparation. This probe straddles the rim on the continued spacelike Cauchy surface.

## A smooth cap cannot absorb the endpoint term

Set $H=\sqrt r\,h$ and $C=L/(2G_N)$. On the complete $t=0$ surface the reduced Einstein symplectic form in the convention $\Omega(X,Y)=dF(Y)$ for the response $X$ is
$$
 \Omega(X,Y)=C\int_0^\infty (X_tY-Y_tX)dr ,
$$
where $X,Y$ denote variations of $\sqrt r\,\psi$. Indeed the linear ADM variation has $\delta h_{zz}=2\delta\psi$ and $\delta\pi^{zz}=2r\delta\psi_t/(16\pi G_N)$, while both diagonal transverse momentum variations vanish. Integrating over both Killing coordinates fixes $C$. Conservation of this current gives its pullback to the incoming cap and sheet,
$$
 \Omega_{\mathrm{in}}(X,Y)
 =C\int_0^a(X_tY-Y_tX)dr+C\int_a^b(X'Y-Y'X)ds .
 \tag{2}
$$
A prime here differentiates along the sheet. The measure is fixed by the areal gauge. The area–boost two-form vanishes on these variations. The cap and sheet restrictions of any smooth spacetime variation have the same value at their common rim. The clock source now takes the form
$$
 dU[Y]=\alpha Y_C+\int_a^b f(s)Y(s-a,s)ds,\qquad
 \alpha=\frac{b-a}{a},\qquad f(s)=-\frac{1}{\sqrt{as}} .
 \tag{3}
$$

Suppose a smooth solution $X$ represents (3) through (2). Independent smooth position and velocity data supported strictly inside the cap have zero sheet field by finite propagation. They force $X=X_t=0$ on the open cap. Smooth matching then requires $X_C=0$. Interior sheet tests give $2CX'=f$, and integration by parts leaves $CX_CY_C-CX_SY_S$. Independent waist tests require $X_S=0$ and a test with nonzero rim strain requires $CX_C=\alpha$, in contradiction with matching.

The tests in this argument can be actual wave solutions. With zero initial position and arbitrary velocity $w=H_t(0,r)$ supported outside the cap, the retarded solution on the sheet is an integral of $w(r')$ between $a$ and $2s-a$. Its kernel is smooth on this triangle and has value $1/2$ at its upper edge, as derived below. Differentiation gives a Volterra equation of the second kind with leading term $w(2s-a)$. It determines a smooth velocity for each smooth sheet test vanishing near $a$, including tests with a freely chosen waist value. Smooth extension and cutoff beyond $2b-a$ preserve its restriction. The preparation $P$ then supplies a nonzero rim value. This argument rules out a smooth Hamiltonian vector in the matched, fixed-embedding polarization sector without assigning any trace to a singular response.

## The distributional response and the cap momentum

On the regular global continuation the linear wave operator for $H$ is $D=\partial_t^2-\partial_r^2-1/(4r^2)$, with the axis condition inherited from smooth $h$. Let $E=G_{\rm ret}-G_{\rm adv}$ for $D$. With (2)'s sign convention the global response is
$$
 CX(t,r)=\alpha E(t,r;0,a)+\int_a^b f(s)E(t,r;s-a,s)ds .
 \tag{4}
$$
Green's identity on a complete Cauchy surface pairs (4) with any smooth spacelike-compact solution $Y$ to give (3). In particular it gives the bracket with the smooth momentum probe above. This distribution can also be obtained by duality from smooth spacetime smearings approaching (3).

The one-sided values follow directly from the retarded kernel of the flat two-dimensional spatial wave equation. Write $\tau=t-t'$, $d=\tau^2-(r-s)^2$. For $\tau>0$ and $0<d<4rs$, integration of $[2\pi\sqrt{\tau^2-|\boldsymbol x-\boldsymbol x'|^2}]^{-1}$ over the causally accessible angles and conjugation by $\sqrt r$ give
$$
 G_{\rm ret}=\pi^{-1}K\!\left(\frac{d}{4rs}\right),
 \qquad K(m)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-m\sin^2\theta}} .
$$
The kernel vanishes before the direct front and has value $1/2$ immediately inside it. For any fixed $s,r>0$ along the same outgoing generator there is a neighborhood of this front before the return from the axis. Thus, for $a<r<b$, the one-sided limits of (4) on the null face are
$$
 CX_+(r)=\tfrac12\left[\alpha+\int_a^r f(s)ds\right],\qquad
 CX_-(r)=-\tfrac12\int_r^b f(s)ds .
 \tag{5}
$$
The $+$ side has $t>r-a$ inside the capped region. The limits differ by $(\alpha+\int_a^b f)/2$, constant along the generator. At the worked radii this jump equals $1/2$ in units of $CX$. As $r\downarrow a$ the inside trace tends to $\alpha/(2C)=3/(2C)$. At every point strictly inside the $t=0$ cap the source is spacelike separated, so the response and its time derivative vanish there. These are distinct one-sided limits of a distribution. Simply inserting either limiting function in the smooth formula (2) loses singular terms.

For example, on the **complete** initial spacelike surface the singular part of the canonical momentum response $CX_t(0,r)$ is
$$
 \left(\alpha+\tfrac12\int_a^b f(s)ds\right)\delta(r-a).
 \tag{6}
$$
The initial velocity of $E(t,r;0,a)$ is $\delta(r-a)$. For each later source the advanced contribution near its incoming support boundary at the initial rim is $-\tfrac12\mathbf1_{r>a+t}$ times a smooth factor equal to one on the front. Differentiating gives the other delta in (6). The second front at $r=2s-a$ integrates to an ordinary density as $s$ varies. At the worked radii the coefficient in (6) is $2$. Allocating a delta on a boundary to one face by fiat can change an attempted inverse. The complete Cauchy bracket (4) and its one-sided predictions require no such allocation.

The calculation establishes a physical, weak clock bracket once a global continuation and a smooth test probe are supplied. It leaves open a regional Poisson algebra for operators with coincident singular supports, the role of variable cap embeddings and the two-polarization problem on spherical light cones. In particular continuity of smooth matched gravitational data cannot justify identifying the one-sided traces (5) of the sharp-clock response. [Finite-rim Einstein potential](rim-potential.md) · [v1, Eq. (A.36)](https://arxiv.org/html/2611.34924v1#A1.E36)

## Reproduce the calculation

Run `python3 checks/joint_peierls.py` from the repository root. The check differentiates the exact nonlinear affine clock, evaluates the causal kernel on both sides of the sheet at $r=0.64$, checks its open-cap support and approaches the rim from inside. Two further integrations recover the momentum impulse in a collar of half-width $10^{-4}$ and pair the complete initial momentum with $\sqrt r P(0,r)$. The second calculation reproduces the nonlinear clock derivative within $5\times10^{-6}$. The repository-wide command is `make check`. [Executable calculation](../checks/joint_peierls.py)

```text
Affine clock variation on curved perturbation: -1.500000
One-sided values of C times the response: 0.90000, 0.40000
Open cap response: 0; sheet-side rim limit: 1.50000
Initial momentum in shrinking rim collar: 1.99988
Complete initial-surface pairing: -1.50000
```
