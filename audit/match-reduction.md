# What survives angular and boost matching at the rim

A change of the comparison map between two marked spheres can carry angular momentum after the common frame has been removed. Metric matching then decides which changes of that map are available. For the round quadrupole one can express the angular pairing entirely in terms of the discrepancy between the two metric variations in their marked charts. This calculation concerns the angular and normal-frame part of the potential. The cap Cauchy data and the sheet flux also enter the gravitational two-form. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [One-sided angular charge](joint-angular.md)

## The two marked frames

Let the angular maps $s_\pm$ take a common reference sphere to the two rims $C_\pm$. In a trivialization of the oriented, time-oriented normal frame bundle, a change of frame acts on a point and its rapidity by

$$
 \Phi(x,t)=(Y(x),t+b(x)),\qquad
 \Phi_- = \Phi\circ\Phi_+,\qquad Y=s_-\circ s_+^{-1}.
$$

Here $b$ lives on $C_+$. Use $D$ for the exterior derivative on field space and $d$ on a rim. The Eulerian displacement $(D\Phi)\circ\Phi^{-1}$ is $(v,(Db)\circ Y^{-1})$, with $v=DY\circ Y^{-1}$. For a generator $(u,c)$ on $C_+$, the pushforward by $\Phi$ is $(Y_*u,(c+db(u))\circ Y^{-1})$. Both identities follow by differentiating the displayed map. The common displacement $(u,c)=(D\Phi_+)\circ\Phi_+^{-1}$ consequently enters the minus-side displacement through this pushforward.

Write $J_\pm$ for signed covector densities and $K_\pm$ for signed boost densities on their own rims. Pair them with the Eulerian displacements to form the two cotangent potentials. Composition gives their sum exactly,

$$
\begin{aligned}
 \Theta_{\rm edge}={}&
 \int_{C_+}\big[(J_++Y^*J_-+(Y^*K_-)\,db)(u)
                       +(K_++Y^*K_-)c\big] \\
 &+\int_{C_-}J_-(v)+\int_{C_+}(Y^*K_-)\,Db . \tag{1}
\end{aligned}
$$

Pullback on a density includes the Jacobian. The two coefficients in the first integral are the common-frame moment maps in this chart. On their joint zero set the first line drops out, and the second line is independent of the common frame. In particular the gradient of an angle-dependent boost enters angular momentum matching. For one concrete choice of orientation put $k_\pm=\mu_\pm/(8\pi G_N)$, $K_+=-k_+$, $K_-=k_-$, $J_+=-k_+\varpi_+$, $J_-=k_-\varpi_-$, and $b=\gamma$. Indeed $\ell_+=e^\gamma Y^*\ell_-$ gives the same normal vector rapidity $t$ in the plus frame and $t+\gamma$ in the minus frame. The moment equations give $k_+=Y^*k_-$ and $\varpi_+=Y^*\varpi_-+d\gamma$. At fixed $Y$ the surviving boost one-form is $\int k_+D\gamma$. This is the cotangent calculation for tangential displacements and boosts, with the minus angular orientation chosen as in the one-sided sheet test. V1 writes its shared-cut formulas at $S$. Their use here at the cap rim $C$ tests a proposed pair of endpoint frames. [V1, Eqs. (3.61)–(3.66)](https://arxiv.org/html/2611.34924v1#S3.E61) · [Sheet endpoint potential, Eq. (5)](rim-potential.md)

With the coordinate vector-field bracket $[v_1,v_2]^A=v_1^B\partial_Bv_2^A-v_2^B\partial_Bv_1^A$, commuting variations obey $Dv(1,2)=-[v_1,v_2]$. Indeed, differentiating $v_2= D_2Y\circ Y^{-1}$ at fixed target point gives the inverse-map contribution $-v_1^B\partial_Bv_2^A$. The mixed second derivatives cancel on antisymmetrizing. For the source displacement $w=(dY)^{-1}DY$ the sign reverses, $Dw(1,2)=[w_1,w_2]$. The differential of the second line of (1) is therefore

$$
\begin{aligned}
 \Omega_{\rm rel}(1,2)={}&\int_{C_-}\big[(D_1J_-)(v_2)-(D_2J_-)(v_1)-J_-([v_1,v_2])\big]\\
 &+\int_{C_+}\big[D_1(Y^*K_-)D_2b-D_2(Y^*K_-)D_1b\big]. \tag{2}
\end{aligned}
$$

Here $D_i(Y^*K_-)=Y^*(D_iK_-+\mathcal L_{v_i}K_-)$. Omitting that transport differentiates the boost density at the wrong point.

At a cap, take the plus frame adapted to the spacelike face with $\ell_+=T+s$ and the minus frame adapted to the sheet with $\ell_-=e^\rho(T+s)$ in a common chart. Then $\gamma=-\rho$ and $\varpi_+=K_{As}\,dy^A$. The common angular coefficient in (1) becomes $k(\varpi_--K_{As}\,dy^A-d\rho)$. At fixed angular map the boost term $-\int k\,D\rho$ equals $\int\rho\,Dk$ modulo a field-exact one-form. With the opposite cap orientation this is precisely the area–angle term in (A.18). Counting the latter again on top of that same boost potential would duplicate it. [Cap joint (A.18)](https://arxiv.org/html/2611.34924v1#A1.E18) · [Cap normal geometry](joint-edges.md)

## Restricting the comparison to isometries

Let $q_+=Y^*q_-$, $w=(dY)^{-1}DY$ on $C_+$, and $h_\pm=Dq_\pm$ in the fixed side charts. Differentiating the matching equation gives

$$
 h_+-Y^*h_-=\mathcal L_wq_+. \tag{3}
$$

On any smooth family of isometric pairs, the two metric variations determine $w$ up to a Killing field. A prescribed mismatch must lie in the range of the full symmetrized gradient. A nonzero mismatch can therefore induce a nonzero one-form $\int J_-(Y_*w)$ on the metric data. If the same geometric variation has equal marked traces at the background identification, (3) allows only Killing fields. At a fixed pair of metrics the choices of $Y$ differ by an isometry, so the remaining angular covector sees only momenta integrated against infinitesimal isometries. Full matching can restrict this freedom further. For example, matching the two second fundamental forms and the normal connection restricts a rotation which is an isometry of the two-metric alone. On a round rim with vanishing background connection and matched connection variations, linearized boost matching gives $dD\gamma=0$. A retained constant boost pairs with the total area. [V1, Eqs. (3.62a–d)](https://arxiv.org/html/2611.34924v1#S3.E62.4)

An internal seam with a single prescribed identification and normal frame admits a common marked chart with $Y=\mathrm{id}$ and $b=0$ along the smooth family. Its relative edge form pulls back to zero there. The angle between a cap-adapted frame and a separately prescribed null generator can still enter the geometric joint potential (A.18). In separately varying charts the same physical seam can have a varying coordinate description $Y$. Establishing a physical charge then requires the pullback of the *whole* potential, including the transformations of the bulk fields. With two independently anchored frames the relative transformation can instead encode a measurement. Diagonal reduction alone yields (2) in both descriptions and cannot decide which boundary data the experiment retains. [V1, Eq. (3.40)](https://arxiv.org/html/2611.34924v1#S3.E40) · [Eq. (3.66)](https://arxiv.org/html/2611.34924v1#S3.E66) · [Eq. (A.18)](https://arxiv.org/html/2611.34924v1#A1.E18) · [Donnelly and Freidel](https://arxiv.org/abs/1601.04744v2)

## A quadrupole measures the trace discrepancy

Identify the background rims by $Y=\mathrm{id}$ on $q=r_c^2\gamma_{S^2}$. Let $Q=P_2(\cos\theta)$, $B_{AB}=\tfrac12(D_AD_BQ)^{\rm TF}$ and now use $D_A$ for the unit-sphere derivative. Since $D^BB_{AB}=-D_AQ$, the angular pairing on the pulse $Z$ with $v_Z=0$, background $\varpi_-=0$ and limiting $D_Z\varpi_-=dQ/2$ obeys

$$
\begin{aligned}
 \lim\Omega_{\rm ang}(X,Z)
 &=-\frac{r_c^2}{16\pi G_N}\int_{S^2} w_X^A D_AQ\,d\Omega \\
 &=-\frac{r_c^2}{32\pi G_N}\int_{S^2}B^{AB}
    \frac{(h_{+,X}-h_{-,X})_{AB}}{r_c^2}\,d\Omega . \tag{4}
\end{aligned}
$$

The second equality uses (3) and integration by parts. If independent normal displacements are kept outside $h_\pm$, their contributions to the induced metrics are pure trace at this umbilic background and also drop out of the contraction with $B$. Equation (4) thus gives zero for equal trace-free variations in the common marked chart, including the conformal Killing ambiguity allowed by such normal motion. It concerns the angular term on this chosen lift of the test. A retained rotation with $v_Z\ne0$ has the additional first term in (2).

For comparison the kinematic family $q_-=r_c^2\gamma_{S^2}$, $q_+=Y_s^*q_-$ with $Y_s$ generated by $G_N\operatorname{grad}Q$ satisfies exact metric matching. Choose $\varpi_-=t\,dQ/2$, $\gamma=0$ and $\varpi_+=Y_s^*\varpi_-$. At $s=t=0$, the two-form on $(\partial_s,\partial_t)$ equals $-r_c^2\langle |DQ|^2\rangle/4=-1/30$ at $r_c=1/3$ in the units $R=1$. A Kasner cap joined to its own null sheet realizes these marked data on a smooth vacuum collar. Whether the two marks are independent physical readings is an extra boundary choice. A Hamiltonian for the clock would have to agree with all the radial quadrupole variations, including ones invisible to this angular pair. [Vacuum collar](match-independent.md) · [Two-packet and rank tests](match-packets.md) [Original quadrupole and clock normalization](joint-angular.md) · [Cap Cauchy matching](joint-edges.md)

## Reproduce the calculation

Run `python3 -B checks/match_reduction.py` and `make check` from the repository root. The focused check varies an explicit pair of smooth axisymmetric frame maps, computes the Eulerian displacements by inverting the angular map, and integrates both expressions in (4) by exact polynomial quadrature. Its expected output is

```text
Composed angular and boost frame potentials agree
Eulerian displacement satisfies Dv(1,2) = -[v1,v2]
Angular charge from the marked metric discrepancy: -1/30
```

[Executable check](../checks/match_reduction.py)
