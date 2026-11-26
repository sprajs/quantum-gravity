# Two cap fractions on one spherical gravity wave

Two detectors use the same emitter, waist and incident quadrupole. One resets its affine clock when the area radius reaches one third of its waist value, the other at one half. Two smooth choices of the incident wave give equal-time Poisson brackets **$+3G_N/160$** and **$-3G_N/160$** for their mixed clock responses, with the detectors kept in this order. Each detector may choose its own smooth timing window for either preparation. The result uses a regular vacuum wave and the Einstein symplectic form on the decaying Minkowski radiative continuation. It also fixes a perturbative coefficient for the actual clock readings, subject to the fixed-resolution hypotheses below. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Matched-radius experiment](joint-flat-hessian.md)

## A formula for nested caps

Use the radius-one flat diamond with tips at observer proper times 0 and 2. Select two fractions $0<a<b<1$ of the area radius on the same outgoing generators. The waist has weighted radius $M=\langle\rho^2\rangle/\langle\rho\rangle=1$, fixed by adjusting the return tip. For cap $c$, the excess $D_c=\bar u_c-(1-c)M$ is critical at flat space. A wave $W$ with one real polar quadrupole $S=\operatorname{diag}(-1/2,-1/2,1)$ defines the linear reading $L_c=d^2D_c(W,\cdot)$. Put $p(s)=G'_W(s)$, the radial slope of the screen strain amplitude, and $w(s)=s(1-s)p(s)$. For the regular test master $f(s)=F(2s)$,
$$
 L_c[f]=\frac3{20}\int_c^1 w(s)G'_f(s)\,ds,\qquad
 \Omega(X,f)=A\langle f_X^{(9)},f\rangle,\qquad A=\frac{3}{5120G_N}.
$$
The full-line test space retains the terms from waves incident on the vertex. The angular projection onto this quadrupole exhausts the response in the usual decaying TT continuation by rotation covariance and even parity. [Normalized master and vertex jets](weak-normalization.md) · [Angular-sector argument and sign convention](weak-clock-contact.md)

Write $z_c=f_{X_c}^{(4)}$ for the first-slot Einstein response, $\Omega(X_c,f)=L_c[f]$. Define two moments at a dimensionless radius $x>0$,
$$
 I(x)=\int_x^1\frac{w(t)}{t^2}\,dt,\qquad K(x)=\int_x^1\frac{w(t)}{t^4}\,dt .
$$
The complete profile vanishes outside $[0,1]$. For $0<s<1$ and $s\ne c$ it is
$$
 \frac{z_c(s)}{G_N}
 =96s^2K(\max(c,s))-16I(\max(c,s))-16\,\mathbf1_{s>c}\,\frac{w(s)}s . \tag{1}
$$
To check the weak equation, pair (1) with $-Af^{(5)}$. Interchanging the two integrals replaces the $I$ term's inner integral by $f^{(4)}(t)-f^{(4)}(0)$. For the $K$ term it gives $t^2f^{(4)}(t)-2tf'''(t)+2f''(t)-2f''(0)$. With the last local term these reproduce the vertex-normalized optical slope
$$
 G'_f(t)=\frac{f^{(5)}(t)}{16t}
 -\frac{5f^{(4)}(t)+f^{(4)}(0)}{16t^2}
 +\frac{3f'''(t)}{4t^3}-\frac{3[f''(t)-f''(0)]}{4t^4}.
$$
The full-line representative has zero left tail. Equation (1) reaches zero continuously at the waist. Its jumps at the vertex and rim are $-16G_N I(c)$ and $d_c=-16G_N(1-c)p(c)$, respectively. It also obeys $\int s z_c(s)\,ds=0$. Indeed a compact master equal to $s^6$ in a neighborhood of $[0,1]$ has zero optical slope, and its fifth derivative there is $720s$.

Write $e_c=-16G_N I(c)$ for the vertex jump. Translating the second complete experiment by proper time $\tau$ pairs $-A\int z_b(s-\tau/2)\,dz_a(s)$. Its ordinary integral converges from both sides by dominated convergence. At each atom the sign of the delay selects a trace. The two rims are distinct, so the vertex is the only possible common jump. With $B_+$ denoting a later outer reading and $B_-$ an earlier one, the trace difference gives $B_+-B_-=A e_a e_b$. [Two-sided delay calculation](weak-clock-contact.md)

For the midpoint $M_{ab}=(B_++B_-)/2$, denote the mean trace at a jump by $z_c^*$. Compact support and integration by parts give $M_{ab}/A=-\int z_b^*\,dz_a=\int z_a^*\,dz_b$ and $\int z_b^*\,dz_b=0$. Subtract the latter integral. The profiles agree above $b$. On $0<s<b$ the measure is $dz_b=192G_NK(b)s\,ds$, so $\int s(z_a-z_b)\,ds=0$ eliminates this ordinary integral. At $b$ the inner clock samples $z_a(b)=z_b(b+)$, differing from the outer midpoint by $d_b/2$. At zero the difference of the two midpoint traces is $(e_a-e_b)/2$. Thus $M_{ab}=A[d_b^2-e_b^2+e_a e_b]/2$ and
$$
 B_- = \frac A2(d_b^2-e_b^2),\qquad
 B_+ = \frac A2(d_b^2-e_b^2+2e_a e_b).                              \tag{2a}
$$
A pair of independently shrinking smooth timing windows with limiting probability $P$ that the outer reading comes later selects $(1-P)B_-+PB_+$. The limits agree exactly when $e_a e_b=0$. For example, the untuned slope $p(s)=s^4$ at $a=1/3$, $b=1/2$ gives $B_-/G_N=-207/4096000$ and $B_+/G_N=15949/66355200$. The order of the two observables throughout is inner then outer, with the canonical sign $\{q,\pi\}=1$.

When the **outer** vertex moment vanishes, $e_b=0$, (2a) simplifies for every inner fraction $0<a<b$ to
$$
 \boxed{\lim_{\tau\to0}\{L_a,L_{b,\tau}\}
   =\frac{A}{2}d_b^2
   =\frac{3G_N}{40}(1-b)^2 p(b)^2 .} \tag{2}
$$
When the **inner** vertex moment vanishes, $e_a=0$, the common limit is $A(d_b^2-e_b^2)/2$. It can have either sign. In both preparations the trace at each atom in the cross-bracket is unambiguous.

## Two smooth vacuum preparations

For $a=1/3$ and $b=1/2$, take
$$
 p(s)=\frac{152}{3}s^4\left(1-\frac{26}{19}s\right)
$$
on $[a,1]$. The ratio $26/19$ is the quotient of $\int_b^1(1/s-1)s^4ds$ by $\int_b^1(1/s-1)s^5ds$. Thus $I(b)=0$ and $p(b)=1$. To prepare the wave, use the regular radial scalar $[F(t+r)-F(t-r)]/r$ and the transverse-traceless spatial operator for $S$. Choose $F(2s)$ equal to $(152/3)[2s^{10}/1575-(26/19)s^{11}/1650]$ throughout a neighborhood of $[a,1]$ and cut it off smoothly away from that neighborhood and the vertex. The optical slope above then follows by differentiation. Its two response jump sets and amplitudes are
$$
 \begin{array}{c|cc}
 & [z_c]_0/G_N & [z_c]_c/G_N \\ \hline
 c=1/3 & -15616/6561 & -7936/2187 \\
 c=1/2 & 0 & -8
 \end{array}
$$
Equation (2) gives $+3G_N/160$. The wave with the overall factor $152/3$ omitted gives $+27G_N/3696640$, since the bracket coefficient is quadratic in the reference amplitude. [Vacuum master construction](joint-flat-hessian.md)

Keep both cap fractions and the ordering fixed. For a second vacuum wave choose $p(s)=48s(1-s)(2s-1)$ on the same collar. It is realized by the master $F(2s)=-16s^7/7+48s^8/35-8s^9/27$ there, cut off as above. Direct integration gives $I(s)=24(s-1/3)(1-s)^3$. Thus $e_a=d_b=0$, $d_a=1024G_N/27$, and $e_b=-8G_N$. The two nonzero jumps are at the inner rim and the vertex, respectively. Both delay limits are now **$-3G_N/160$** by (2a). Changing the sign of the whole wave would preserve the bracket, since both covectors depend linearly on it. This sign reversal instead changes the radial dependence of its strain.

## The actual clocks on one perturbed spacetime

Let $D_{c,t}$ denote the nonlinear excess with starting proper time $t$ along one marked observer and return event adjusted to keep $M=1$. Average it with a smooth compact probability density $\rho_{c,h}(t)$ supported in a shrinking neighborhood of zero to form $D_{c,h}$. The two densities and their shrinking rates may differ. For each fixed positive resolution, assume the following.

* The experiments share a regular, noncaustic family of vacuum solutions $g_\lambda$ with $g_0=\eta$, $\dot g_0=W$. The observer, frames, tip-time origin and integrations are calibrated in relational labels and carried by the gauge action.
* The averaged readings belong to a common reduced Poisson domain. In a smooth identification of its tangent spaces their first covectors are differentiable along this family in a topology in which the paired Poisson bivector varies continuously. At the flat point that bivector gives the radiative Einstein pairing above, including the response of the prescribed marks.

Because $dD_{c,h}|_\eta=0$, the fixed-width first derivative on the family is $dD_{c,h}|_{g_\lambda}=\lambda d^2D_{c,h}|_\eta(W,\cdot)+o_h(\lambda)$. The bracket therefore starts at order $\lambda^2$ with coefficient the flat pairing of the two averaged Hessians. Quadratic corrections to the common metric, and variation of the bivector, drop out of this coefficient.

The wave in these two derivatives is fixed in spacetime. At time $t$ the recentered tangent is $U_tW$, where $(U_tW)(x^0,\mathbf x)=W(x^0+t,\mathbf x)$, so the actual Hessian is the translation of $L_c[U_tW]$ back to its measured time. For $s\in[c,1]$ the recentered slope differs from $p(s)$ by $O(|t|)$ in $C^1$. This follows from the smooth master and the full optical formula, including its vertex jets. By (1) the corresponding $z$ difference has supremum and total variation $O(|t|)$ on its fixed pieces, including the changes of all jumps. Translation preserves those bounds. The pairing $\int z_2\,dz_1$ away from coincident jumps is bounded by $\|z_2\|_\infty |dz_1|(\mathbb R)$, so freezing both reference waves at the central $W$ changes the averaged coefficient by a term tending to zero. The exceptional diagonal of equal sampling times has zero product measure. At finite width the shift integral smooths the flat master response across each moving jump. For the two preparations, (2a) now gives the sequential statement
$$
 \lim_{h\to0}\lim_{\lambda\to0}
  \frac{\{D_{a,h},D_{b,h}\}(g_\lambda)}{\lambda^2}
 =\begin{cases}+3G_N/160 & \text{for the first wave},\\ -3G_N/160 & \text{for the second wave}.\end{cases} \tag{3}
$$
For every sufficiently small fixed width the conditional coefficient has the displayed sign, and the actual bracket then has that sign for sufficiently small nonzero amplitude depending on the width. At fixed nonzero amplitude, convergence as the detectors sharpen would require uniform estimates on the nonlinear covectors and the Poisson pairing. The existence of that limit, and the corresponding intrinsic finite-diamond algebra with independent rim data, remain proof gaps. The ambient linear result (2) needs neither hypothesis. [Calibrated curved currents and their Ward identity](weak-curved.md)

## Reproduce the calculation

Run `python3 -B checks/timing_caps.py` from the repository root and `make check` for the full suite. The focused check pairs the exact polynomial response with the independent optical source on eighteen monomials for each cap, checks four different inner caps, computes the integral with the reversed order, and evaluates both sides at three nonzero delays. It verifies the second wave’s moments and independently integrates a higher-degree polynomial preparation with the same three coefficients $e_a,e_b,d_b$. Its expected output is below. [Executable check](../checks/timing_caps.py)

~~~text
Common wave slope (152/3) s^4 (1 + q s), q = -26/19; outer rim slope = 1
Cap 1/3 jumps: -15616/6561, -7936/2187 (vertex, rim)
Cap 1/2 jumps: 0, -8 (vertex, rim)
Equal-time bracket / G_N = 3/160 (0.01875)
At delay -/+0.0010000: 0.01752080762, 0.01997862724
At delay -/+0.0000100: 0.01873767851, 0.01876232143
At delay -/+0.0000001: 0.01874987678, 0.01875012322
Untuned s^4, earlier/later limits / G_N: -207/4096000, 15949/66355200
Inner vertex and outer rim canceled, both delay limits / G_N: -3/160
~~~
