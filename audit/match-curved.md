# The full displacement charge at a curved spherical rim

At the top of the spherical cap in a vacuum plane wave, an angular displacement stretches the two principal directions unequally. Either normal displacement can also produce unequal stretches there. The compensated gravitational pulse measures their **sum** in the Einstein surface charge. Equality of the two pulled-back rim metrics sets that sum to zero, even if its angular and normal terms are individually nonzero. This calculation tests smooth relative spacetime displacements of two markings of the same metric. The angularly averaged clock retains its nonzero first variation in the same experiment. [Spherical diamond and clock measurement](joint-focal.md) · [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.50b)–(3.50c)](https://arxiv.org/html/2611.34924v1#S3.E50.2)

## Compute the charge before splitting the displacement

Use the two smooth tips, axis lengths and fractional cut of the [focal calculation](joint-focal.md). Near the incoming cone, change the original Rosen coordinates to
$$
 k_i=x_i/I_i(U),\qquad w=V-\tfrac12\sum_i k_i^2 I_i(U).
$$
The metric becomes $-2\,dU\,dw+\sum_i q_i(U)dk_i^2$, where $q_i=(A_i I_i)^2$, $P_i=q_i'/(2q_i)$, and $m=\sqrt{q_1 q_2}=F^2$. Primes denote $U$ derivatives. The cone is $w=0$, and its rim $C$ has $U=b(k)$. Its center is $b(0)=c$, with $b(k)=c-k^TEk+O(|k|^4)$ and $E$ positive definite. A smooth compactly supported incident profile $f_h$ has zero total integral and unit integral on the earlier half of its support. On the rim $f_h(b)$ converges to $M\delta^{(2)}(k)$ with $M=\pi/\sqrt{\det E}$. The coordinate chart need only cover a neighborhood of this maximum. Elsewhere on the rim the metric variation is zero before the pulse or vanishes weakly. [Optical profile and moving cut, Eqs. (1)–(4)](joint-focal.md)

Write $r_i=\delta_h q_i/q_i$ for the perturbed optical metric in these coordinates. Orient spacetime by $dU\wedge dw\wedge dk_1\wedge dk_2$ and the cut integral by $dk_1\wedge dk_2$. At a background cut take a smooth spacetime field $\xi$, held fixed while computing the metric variation. A field-dependent displacement uses the same formula with $Q_{\delta\xi}$ subtracted. Set $b_i=\partial_i b$. Substitution in the Komar two-form and Einstein metric potential gives the following cut densities, after removing the common factor $m\,d^2k/(16\pi G_N)$.
$$
\begin{aligned}
 \widehat Q_\xi
 &=\partial_w\xi^w-\partial_U\xi^U
 +\sum_i b_i\left(\partial_U\xi^i+2P_i\xi^i+q_i^{-1}\partial_i\xi^w\right),\\
 \widehat {i_\xi\theta}
 &=-\left(\xi^U-\sum_i b_i\xi^i\right)\sum_j(P_j r_j+r_j').
\end{aligned}                                                     \tag{1}
$$
Here the derivatives of $\xi$ inside the first line are spacetime partial derivatives before restriction. For example, $\Gamma^w_{ii}=q_iP_i$ and $\Gamma^i_{Ui}=P_i$. The only nonzero component of the metric potential flux is along $\partial_w$, with coefficient $\sum_j(P_j r_j+r_j')$. [Einstein potential (A.6)](https://arxiv.org/html/2611.34924v1#A1.E6) · [Noether charge identity](https://arxiv.org/abs/gr-qc/9403028v1)

In the band $|U-c|\le h$, $r_i=s_i f_h+O(1)$ with $s_1=1,s_2=-1$, and $r_i'=s_i f_h'+O(|f_h|+1)$. The trace is $r_1+r_2=4\delta F/F$. Equation (3) of the [focal calculation](joint-focal.md) gives
$$
 \sum_i(P_i r_i+r_i')=-(P_1-P_2)f_h+O(1).
$$
The band on the rim has area $O(h)$. Terms $b_i f_h(b)$ vanish weakly because $b_i=O(\sqrt h)$ there. In varying the first line of (1), the only surviving terms are therefore $\sum_i s_i\xi^i\partial_i[f_h(b)]$. Their angular derivatives transfer to the smooth weight and $\xi^i|_C$ by integration by parts. At the center $\partial_i m(b)=0$. With $k_\xi=\delta Q_\xi-Q_{\delta\xi}-i_\xi\theta$ this gives
$$
 \lim_{h\to0}\int_C k_\xi[\delta_h g]
 =-\frac{M m(c)}{16\pi G_N}
 \left[\partial_1\xi^1-\partial_2\xi^2+\xi^U(P_1-P_2)\right]_{k=0}.
                                                                    \tag{2}
$$
The derivatives inside the bracket can equivalently be taken after restriction since $db(0)=0$. Reversing the cut orientation changes the sign. In particular, changing only normal derivatives of a smooth extension of $\xi$ cannot change this limit. Formula (2) is also proportional to the difference of the two diagonal components of $\mathcal L_\xi g$ in an orthonormal screen frame.

## Impose the matching condition

Let $t_i=\partial_i+b_i\ell$ be the graph tangents, with $\ell=\partial_U$. Its other future null normal is $n=\partial_w+\sum_i (b_i/q_i)\partial_i+|db|_q^2\ell/2$, so $n\cdot\ell=-1$. At the center the eigenvalues of the two null second fundamental forms are $P_i$ and $N_i=b_{ii}/q_i=-2E_{ii}/q_i$, respectively. Decompose the **net** relative displacement, including any angular comparison map, as $\xi=Y^it_i+\alpha\ell+\gamma n$. For the same spacetime metric perturbation on the two sides the pullback difference in the two principal metric components is
$$
 \frac{(\mathcal L_\xi g)(t_i,t_i)}{2q_i}
 =\partial_i Y^i+\alpha P_i+\gamma N_i\qquad(k=0,\ \text{no sum}).
                                                                    \tag{3}
$$
The bracket in (2) is the difference of the two right-hand sides of (3). Matching both metric components therefore removes the entire focal displacement charge. Matching the local area density only sets their sum to zero and permits a nonzero difference. The off-diagonal condition further restricts the relative motion but is unnecessary for this conclusion. These necessary conditions suffice for the limiting test without having to classify all global relative displacements. [Matching the optical and cap data](joint-edges.md) · [Angular charge on a round rim](joint-angular.md)

An exact check uses the parallel null translation $\partial_w$. On $C$ it has $Y^i=-b_i/q_i$, $\gamma=1$, and $\alpha=|db|_q^2/2$. At the center the angular and transverse normal stretches cancel separately for each principal axis. Since $\partial_w$ is parallel throughout the optical family and the potential flux is along $\partial_w$, both terms of $k_{\partial_w}$ vanish identically there, at every width. Its angular term in (2) nevertheless has the finite value $-0.063558$ in the example below. A relative translation can move the tips. Its role here is to check the local charge decomposition.

The fractional cut moves in this optical chart by $\delta b(k)\partial_U$. Its displacement is bounded and tends to zero as a distribution, and so do all its angular derivatives. A collar extension constant in the two transverse coordinates near $C$ has the same property for its needed jets. Contributions against a smooth response from this embedding change then vanish by angular integration by parts. For a geometric cap tilt one concrete choice near the maximum is the spacelike collar $w=\tau[b(k)-U]$, with fixed $\tau>0$ and $2\tau>\tau^2|db|_q^2$. Its future unit normal satisfies $-T\cdot\ell=\tau/(2\tau-\tau^2|db|_q^2)^{1/2}$. The fractional change in this tilt vanishes weakly on the packet. Indeed its term from $r_i$ is multiplied by $b_i^2$, and the terms from $\delta b$ and $\partial_i\delta b$ have smooth coefficients. One can continue the collar smoothly away from the maximum, with the same prescribed background collar for the smooth family. The tip normalization of $\ell$ multiplies this inner product by a fixed angular function. On this preparation $\delta_h\mu_C=\epsilon^2\delta_h\mu_S$ also tends weakly to zero, by the regular waist-level estimate. Consequently (A.18)'s boost–area two-form contributes zero against a fixed smooth response. An independent boost mark can likewise be held fixed along the test if the phase space permits that lift. [Joint (A.18)](https://arxiv.org/html/2611.34924v1#A1.E18)

For a common smooth metric, the usual metric pairing on a spacelike ball spanning the waist tends to zero. Equations (2)–(3) also exclude repairing the finite discrepancy by a relative smooth Iyer–Wald displacement preserving the full rim metric, supplemented by the stated boost–area term on this test. The clock variation itself tends to $-0.060534$. This is a **range obstruction** for that class of geometric responses. A regulator imposing additional frame transport on the test or further independent boundary momenta requires its own reduced equations. The full finite-diamond bracket remains a **proof gap**. [Clock measurement and bulk estimate](joint-focal.md) · [Phase space (3.19)](https://arxiv.org/html/2611.34924v1#S3.E19)

## Metric currents for two smoothly varying pieces

There is a related test that permits different smooth response metrics on the two faces. Suppose the pairing is the sum of the Einstein metric currents on a spacelike cap ball $\Sigma$ with boundary $C$ and on the adjoining null segment $N$ from $C$ to $S$. Both pieces are embedded in the specified plane-wave background, or are separate copies of its restrictions. On each piece take the perturbation induced by the **same** focal packet, with the moving cuts lifted as above. Allow the responses $X_\Sigma,X_N$ to come from separate smooth linearized vacuum metrics up to the cut. Include their embedding Lie derivatives in $X_\Sigma,X_N$, so these symbols denote the changes of the metrics in the comparison charts. This hypothesis specifies the pairing being tested. Any separately retained surface field has an additional Hamilton equation.

Use $\omega(h,X)=\delta_h\theta(X)-\delta_X\theta(h)$ with $h=\delta_h g$ denoting the packet. At the axis define $H=q_1\,dk_1^2-q_2\,dk_2^2$ and $\nu=dU$. The only potentially surviving differentiated pulse in $\nabla h$ is $\nu\otimes H\,f_h'$. The tensor $H$ is trace-free and $H^{ab}\nu_b=0$. Writing the current three-form as $i_J\epsilon_g$, the derivative term of the Einstein current at this point is
$$
 16\pi G_N J^a \big|_{f_h'}
 =\left(H^{ac}X_{cd}\nu^d-\tfrac12\nu^a H^{cd}X_{cd}\right) f_h' .
                                                               \tag{4}
$$
Indeed the derivative parts of $16\pi G_N\delta_h\theta^a(X)$ and $16\pi G_N\delta_X\theta^a(h)$ are $\nu^a(H:X)f_h'/2$ and $[\nu^a(H:X)-H^{ac}X_{cd}\nu^d]f_h'$, respectively. Thus $J^U$ has zero coefficient and $16\pi G_N J^w$ has coefficient $\Delta(X)/2$, where $\Delta(X)=X_{11}/q_1-X_{22}/q_2$ at the center. [Einstein metric potential (A.6)](https://arxiv.org/html/2611.34924v1#A1.E6)

The orientations of $\Sigma$ and $N$ both use increasing $(U,k_1,k_2)$ near the joint, as for adjacent pieces of one initial surface. A spacelike cap is locally a graph $w=W(U,k)$ because $\partial_w$ is null. Since $W(b(k),k)=0$ on $C$ and $db(0)=0$, the two $k$ tangents at the center are the screen axes. Possible screen components of $J$ therefore drop out of the flux there. With $\epsilon_{Uw12}>0$, the coefficient of the pulled-back three-form on each piece is $-m(c)\Delta(X)/(32\pi G_N)$ times $f_h'$. The restriction of $U$ to the spacelike cap has no stationary point in its interior. Its maximum on the compact ball occurs at the boundary maximum $c$, so the cap occupies $U\le b(k)$ locally there. Integrating $f_h'$ in $U$ gives $+f_h(b)$ from its upper end. On $N$ the interval is $b(k)\le U\le s(k)$, and the lower end gives $-f_h(b)$. The term at $s=c$ integrates to zero in the limit since $s$ has a regular level there and the full pulse has zero integral. Terms multiplying $f_h$ in the volume, including the derivative of the smooth coefficient in (4), also vanish. On the full incoming cone the level density is smooth since $s=c$ is regular, and the pulse has zero full integral. The angular area removed at the quadratic endpoint is $O(|U-c|)$, so the integral of $|f_h|$ over that removed volume is $O(h)$.

Consequently, with $h$ in the first slot,
$$
 \lim_{h\to0}\left(\int_\Sigma \omega(h,X_\Sigma)+\int_N\omega(h,X_N)\right)
   =\frac{M m(c)}{32\pi G_N}\,[\Delta(X_N)-\Delta(X_\Sigma)].
                                                               \tag{5}
$$
For a moving pullback the packet also contains $\mathcal L_{\chi_h}g$ on each piece. Choose its extensions of $\delta b(k)\partial_U$ at $C$ and $\delta s(k)\partial_U$ at $S$ constant in transverse coordinates near the cuts. Both displacements and their first angular derivatives tend weakly to zero, using the regular waist estimate for $\delta s$. On each piece the on-shell current with $\mathcal L_{\chi_h}g$ is an exterior derivative of the surface charge against its smooth $X$. Its boundary integral tests only $\chi_h$ and its first derivatives against smooth coefficients. These moving-pullback terms thus leave (5) intact. Regular charts at the waist poles can be used for this argument. [Moving pullbacks and surface charge, Eqs. (3.40) and (3.50b)](https://arxiv.org/html/2611.34924v1#S3.E40)

Equality of the two pulled-back rim metric variations makes (5) zero. The result allows their normal derivatives and other components to differ. It extends the obstruction to this sum of piecewise metric currents with the stated test lift. Including an independently dynamical corner changes the pairing. For that problem, (5) determines the residual contribution the additional variables must supply.

## Numerical check

Run `python3 checks/match_curved.py` and `make check` from the repository root. With $G_N=L=D=1$ and $\epsilon=1/2$, the script integrates (1) directly for $\xi^U=\alpha$, $\xi^i=d_i k_i$ near the maximum. It uses the exact angular area $K(u)=2\pi D F(L-s)/[F(s)F(L)]$ above $b=u$, with $F(s)=F(u)/\epsilon$. Integrating $k_i\partial_i\mathbf1_{b>u}$ over the plane gives $\int k_i b_i\delta(b-u)d^2k=-K(u)$. These identities reduce the surface integral to a single numerical quadrature. The three tests take $(\alpha,d_1,d_2)=(0,1/2,-1/2),(1,0,0),(1,-P_1(c),-P_2(c))$. The last test imposes both diagonal matching conditions **at the critical point**. For the first test the check also integrates the spacelike cap current in (5) before taking the limit. For $X_{11}/q_1=1$, $X_{22}/q_2=-1$, its density is $-K m[(r_1+r_2)(P_1-P_2)+r_1'-r_2']/(32\pi G_N)$ in $U$. Expected output follows. [Executable calculation](../checks/match_curved.py)

~~~text
Null shear differences at the axis: 0.331719, -0.990255
Limits for unit angular strain and unit outgoing shift: -0.064183, -0.021291
Parallel translation, angular and normal parts: -0.063558, 0.063558
width 0.025000  angular -0.056214  outgoing -0.016823  matched 0.001764
width 0.012500  angular -0.060173  outgoing -0.019019  matched 0.000926
width 0.006250  angular -0.062171  outgoing -0.020146  matched 0.000474
width 0.003125  angular -0.063176  outgoing -0.020716  matched 0.000240
Cap volume and angular surface charge agree within 1e-12.
~~~
