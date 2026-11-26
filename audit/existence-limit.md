# What resolution can a fixed-size quantum clock admit?

A necessary condition for a finite clock reading can be proved in the same round, linearized radiation model in which a detector with fixed smoothing admits the vacuum. At fixed response, both sums $\sum k|R_k|^2$ and $\sum (2j+1)|A_j|^2$ must converge, provided the detector passes at least one radial mode and one angular degree. Every state is excluded if either sum diverges. There is also a bound for the full fixed-area clock ordering. A diverging local focusing cost on three quarters of the sky, for example, excludes readings strictly below twice the shear-free round value even if the quantum corner can redistribute all its area. The first result is a model theorem. The second applies to a physical clock once its local spectral costs have been established. Existence in the full constrained four-dimensional theory remains a proof gap. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Positive focusing and clock form, (4.22)–(4.27)](https://arxiv.org/html/2611.34924v1#S4.E22) · [Claim (5.19)](https://arxiv.org/html/2611.34924v1#S5.E19)

## A necessary condition on the detector response

Fix $0<\epsilon<v_0<1$, radius $b>0$, entropy parameter $s=\mathscr A/(4G_N\hbar)>0$, $\mathscr A=4\pi b^2$, $L=1-\epsilon$ and $\kappa=2\pi/L$. In the pinned linearized radiation model let $x=rz$ be the two-component radiative strain multiplied by the area coordinate. Use the radial functions $w_k(r)=e^{ik\kappa(r-\epsilon)}-1$ and real tensor harmonics $E_{jmp}$ with $\sum_{m,p}|E_{jmp}(y)|^2=2(2j+1)$ for normalized spherical measure. Here $p$ labels the two polarizations. For independent canonical oscillators with $[a_\nu,a_\mu^\dagger]=\delta_{\nu\mu}I$ and $\nu=(k,j,m,p)$, the coefficient of $a_\nu^\dagger$ in $x$ is $E_{jmp}(y)R_k A_jw_k(r)/\sqrt{sk}$. Take its complex conjugate for $a_\nu$. The responses can include zeros and can change with each regulator. At first keep finitely many modes with a full set of harmonics at each retained degree. The clock exponent is the positive quadratic $X_y(v)=\tfrac14\int_\epsilon^v r|\partial_r z|^2dr$. Its finite-oscillator positive form is the closure from Schwartz vectors. These specifications give the same normalization and ensemble as the positive smoothed-clock construction. [Radiative symplectic form (D.42)](https://arxiv.org/html/2611.34924v1#A4.E42) · [Pinned responses and vacuum construction](clock-construction.md)

Let
$$S_{KJ}=\left(\sum_{k=1}^K k|R_k|^2\right)
             \left(2\sum_{j=2}^J(2j+1)|A_j|^2\right).$$
For every generator and every late cut $v\ge v_0$ there is a state-independent spectral bound
$$
 X_y(v)\ \ge\ H_{KJ} I,\qquad
 H_{KJ}=\frac{\epsilon\kappa^2(v_0-\epsilon)^2}{4v_0^2 Ls}\,S_{KJ}.                 \tag{1}
$$

**Localizing the radial current.** Write $I=[\epsilon,v_0]$ and $J=\partial_r x$. For each polarization component and core vector $\psi$, integration by parts and $x(\epsilon)=0$ give
$$
 \int_I r^2\|z'\psi\|^2dr
 =\int_I\|x'\psi\|^2dr-\|x(v_0)\psi\|^2/v_0
 \ \ge\ (\epsilon/v_0)\int_I\|x'\psi\|^2dr .
$$
The endpoint estimate uses $\|x(v_0)\psi\|^2\le(v_0-\epsilon)\int_I\|x'\psi\|^2dr$. Since $r\le v_0$ on $I$, the focusing therefore dominates $\epsilon/(4v_0^2)$ times the squared current norm integrated on $I$. No condition on the field at $v_0$ is needed.

Let $W=\mathbf1_I$, $\widehat W_n=L^{-1/2}\int_\epsilon^1 W(r)e^{-in\kappa(r-\epsilon)}dr$ and $B_m=L^{-1/2}\int W(r)e^{im\kappa(r-\epsilon)}J(r)dr$ for one component. On the core $B_{-m}=B_m^\dagger$ as matrix elements. Parseval gives $\int_I\|J\psi\|^2=\sum_{m\in\mathbb Z}\|B_m\psi\|^2$. For $m>0$ each opposite-frequency pair bounds its signed weak commutator $\|B_m^\dagger\psi\|^2-\|B_m\psi\|^2$ from above. The derivative of $w_k$ has a single frequency, so a mode $k$ contributes to this signed difference in proportion to $|\widehat W_{m-k}|^2-|\widehat W_{m+k}|^2$. The independent oscillator commutators eliminate all mixed-mode terms. Summing over $m$ gives the telescoping identity
$$
 \sum_{m=1}^\infty
 \left(|\widehat W_{m-k}|^2-|\widehat W_{m+k}|^2\right)
 =\sum_{n=1-k}^k|\widehat W_n|^2
 \ \ge\ |\widehat W_0|^2=(v_0-\epsilon)^2/L .
$$
The two series being subtracted are summable. Each coefficient is multiplied by $\kappa^2 k|R_k A_j|^2/s$ and the square of the relevant harmonic component. Sum the two component inequalities and the angular multiplets to get (1), extended by form closure. The Fourier localization prevents squeezing one mode against another from cancelling the bound.

**Removing the cutoffs.** Set $u_0=b(1-\epsilon)$, the round shear-free clock. The frozen round corner averages $b\exp[\min(X_y(v),c)]$ over normalized angle and over cuts. The scalar spectral floor at each late cut gives
$$
 T_{KJc}/u_0\ \ge\ 1+\frac{1-v_0}{1-\epsilon}
                    \left(e^{\min(H_{KJ},c)}-1\right).
 \tag{2}
$$
For every sequence with $S_{KJ}\to\infty$ and $c\to\infty$, the finite-threshold projector is eventually identically zero. In particular any regulator which restores unit response separately at each fixed radial and angular mode has $S_{KJ}\to\infty$, by retaining as many fixed terms of each nonnegative sum as desired. This result allows the state, the response profiles and the relative regulator speeds to vary.

For bare sharp cutoffs $S_{KJ}=K(K+1)[(J+1)^2-4]$. More quantitatively, if a fixed window $\ell/u_0>1$ contains any state and $c>h_*=\log[1+L(\ell/u_0-1)/(1-v_0)]$, (2) requires $H_{KJ}\le h_*$. At fixed cap geometry this requires $S_{KJ}/s$ to stay bounded. In particular, a simultaneous large-area limit with bare equal cutoffs $K=J$ requires $K=O(s^{1/4})$ as a necessary condition at that fixed clock ratio.

At fixed detector response $R_k\asymp k^{-a}$ and $A_j\asymp j^{-d}$, divergence occurs for $a\le1$ or $d\le1$, including the logarithmic endpoints. On the summable side the previous sufficient vacuum construction applies when $\kappa^2\log(1/\epsilon)S_{\infty\infty}/(4s)<1/2$. The estimates leave open the range of larger finite sums.

For $\epsilon=1/4$, $v_0=5/8$, $s=10^4$, $K=J=6$ and $c\ge1$, (2) gives $T/u_0\ge1.244379$. Thus the bare model already excludes the window at $1.2u_0$ with these six radial modes and angular degrees two through six. The fixed exponentially smoothed model at the same $s$ admits the vacuum there with probability at least $0.6373157$. [Exponential moments and an explicit positive probability](clock-construction.md) · [Earlier curved-background commutator test](clock-spectrum.md)

## Transferring a local obstruction through a fluctuating corner

Suppose a regulated physical fixed-area space has the positive measurable densities $\rho_y$, positive self-adjoint prefixes $\Xi_y(v)$ and capped form of v1. Write $a=\int\rho_y d\Omega$ and use $\int\rho_y^2d\Omega=\mathscr A I$ in quadratic-form sense. Assume on each ray a measurable scalar $d_y\ge1$ bounds the integrated cost,
$$
 \frac{1}{L}\int_\epsilon^1 e^{\min(\Xi_y(v),c)}dv\ \ge\ d_y I .
$$
The normalised spherical average is $\langle f\rangle_S=(4\pi)^{-1}\int f d\Omega$. The full clock then obeys
$$
 \frac{T_c}{u_0}\ \ge\
 \sqrt{\frac{\operatorname{ess\,inf}_y d_y}{\langle d_y^{-1}\rangle_S}}\,I .
 \tag{3}
$$
This holds with noncommuting densities, shear and $a$, and does not require a lower bound on the area of any specified angular patch. [Area normalization (4.25)](https://arxiv.org/html/2611.34924v1#S4.E25) · [Clock ordering (4.26)–(4.27)](https://arxiv.org/html/2611.34924v1#S4.E26)

Indeed, for a nonzero form vector $\psi$, put $h=a^{-1/2}\psi$ and $N=\int d_y\|\rho_y h\|^2d\Omega$. The clock quotient divided by $L$ is bounded below by $N/\langle h,ah\rangle$, since each scalar cost can be sandwiched between its two density factors. Weighted Cauchy–Schwarz gives
$$
 \langle h,ah\rangle\le\|h\|\int\|\rho_yh\|d\Omega
 \le\|h\|\sqrt{N\int d_y^{-1}d\Omega},\qquad
 N\ge(\operatorname{ess\,inf} d_y)\mathscr A\|h\|^2 .
$$
Their combination yields (3). The original form includes $\|\psi\|^2=\langle h,ah\rangle$ in its Rayleigh quotient.

If $\Xi_y(v)\ge H I$ for $v\ge v_0$ on a fraction $p$ of solid angle, take $d_y=D=1+(1-v_0)(e^{\min(H,c)}-1)/L$ there and one elsewhere. For $p<1$, (3) yields $T_c/u_0\ge(1-p+p/D)^{-1/2}$. For $D\to\infty$ this excludes each threshold strictly below $u_0/\sqrt{1-p}$. If the fraction tends to one and $D\to\infty$, every fixed threshold is excluded. More generally the same conclusion follows if the local costs grow without bound in solid-angle measure, since $0\le d_y^{-1}\le1$. When $p=1$ identically use (3) with $\inf d_y=D$ to recover $T_c/u_0\ge D$. These exclusions compare cutoff projections directly and do not presume norm convergence of states in different regulated Hilbert spaces.

For fixed $0<p<1$ the asymptotic threshold is sharp given only these area and cost hypotheses. With commuting scalar data let the density be proportional to $1/D$ on the patch and one on its complement, normalized to the specified area. Take integrated costs exactly $D$ and one. The quotient is $(1-p+p/D^2)^{-1/2}$ in units of $u_0$. At arbitrarily large $D$ this approaches $(1-p)^{-1/2}$, so no strictly higher asymptotic universal floor follows. This scalar two-cell example tests the inequality under its hypotheses. Realizing these profiles as solutions of the constrained gravitational problem is a separate requirement.

**Sharp finite-cost bound for two angular regions.** An independent Astra check sharpened (3) by optimizing the distribution of area. Put $g(y)=\|\rho_yh\|/(b\|h\|)$. The area identity gives $\langle g^2\rangle_S=1$ and the clock quotient satisfies $T_c[\psi]/(u_0\|\psi\|^2)\ge\langle d g^2\rangle_S/\langle g\rangle_S$, where $T_c[\psi]$ denotes the clock form. For $0<\lambda<\operatorname{ess\,inf}d$, set $J(\lambda)=\langle(d-\lambda)^{-1}\rangle_S$. Cauchy–Schwarz gives $\langle d g^2\rangle_S\ge\lambda+\langle g\rangle_S^2/J(\lambda)$. The arithmetic-geometric mean inequality then yields
$$
 T_c/u_0\ \ge\ \sup_{0<\lambda<\operatorname{ess\,inf}d}
                 2\sqrt{\lambda/J(\lambda)}\,I .                                      \tag{4}
$$
For $d=1$ and $D>1$ on respective fractions $1-p$ and $p$, with $0<p<1$, this is the exact universal lower bound allowed by the given costs and normalization. Here $J=(1-p)/(1-\lambda)+p/(D-\lambda)$. The maximum occurs at the unique root $J=\lambda J'$ in $(0,1)$, because $J-\lambda J'$ decreases from a positive value to $-\infty$. The positive density profile $\rho_y=b(d_y-\lambda)^{-1}/\sqrt{J'}$ has the required total area and saturates both inequalities for scalar local costs. At $p=3/4$ and $D=16$ the sharp floor is $1.911478396u_0$. Physical angular smoothness or coupling can impose further restrictions on these optimizing data.

**What would decide the four-dimensional claim?** For exclusion at a given $\ell$, a physical construction of the regulated corner and a scalar lower cost giving a right-hand side of (3) strictly above $\ell/u_0$ suffices at each sufficiently fine regulator. A compatible continuum clock must reproduce that exclusion, for example by strong resolvent convergence of the extended positive clocks with the same strictly positive spectral margin. Local floors could be obtained from a nonperturbative current commutator estimate with controlled cap contributions, as detailed in the curved-target analysis. For existence, a nonzero accepted physical state at the specified threshold requires control in the opposite direction. One sufficient test is a common physical normalization and continuum form with a normalized physical vector $\chi$ satisfying $\langle T\rangle_\chi<\ell$. Its probability is at least $(\ell-\langle T\rangle_\chi)/(\ell-u_0)$ for $\ell>u_0$. For the spherical preparation itself one must also establish its overlap with the accepted subspace. Equation (5.19) claims full Gaussian weight as $\ell$ increases. The signed-current calculation uses independent canonical radiation on a pinned tangent plane. The finite-$G_N$ cap, quantum corner and nonlinear Dirac reduction have yet to supply the corresponding physical spectral data. [Interacting commutator criterion](clock-spectrum.md) · [Exact meaning of (5.19)](05-1.md) · [Versioned clock filter (C.13)](https://arxiv.org/html/2611.34924v1#A3.E13)

## Reproduction

Run `python3 -B checks/existence_limit.py` from the repository root, or `make check` for the suite. The first check compares the signed Fourier sum, including its finite truncation tail, with its central coefficients. Independent quadrature of the actual one-oscillator focusing matrix gives the spectral bottom $\sqrt{\det M}$ for $M_{11}Q^2+M_{12}(QP+PQ)+M_{22}P^2$ with $[Q,P]=i$. The all-mode floors use $\epsilon=1/4$, $v_0=5/8$, $s=10^4$. A three-cell real symmetric matrix clock has noncommuting densities obeying the area identity and noncommuting local costs. Direct minimization over normalized two-cell densities checks the sharp finite-cost value against (4). The last line uses the asymptotic sharpness example at $p=3/4$ and $D=4096$. [Executable check](../checks/existence_limit.py)

```text
localized Fourier commutator: 12 identities verified
k=1  one-mode spectral bottom 0.00112825  lower bound 0.00021055
k=4  one-mode spectral bottom 0.00634899  lower bound 0.00084221
K=J= 4  bare prefix floor 0.088432
K=J= 6  clock lower bound at cap 1: 1.244379
K=J= 8  bare prefix floor 1.167298
K=J=16  bare prefix floor 16.321957
noncommuting corner: lower bound 1.632993  exact matrix minimum 7.538027
three-quarter patch at cost 16: sharp floor 1.911478396
three-quarter patch: bound 1.999268  scalar example 1.999999821  limit 2
```
