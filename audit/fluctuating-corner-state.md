# A finite clock reading with a fluctuating area density

Prepare a Gaussian logarithmic area shape and the oscillator vacuum for both shear polarizations on a marked sphere. Measure the linearized current at the fixed radial and angular resolution specified below. At total area $\mathscr A/(4G_N\hbar)=10^4$ the probability of a reading at most $1.2$ times the round shear-free length exceeds $0.4780$. The accepted space has infinite rank, even though this preparation has infinite mean clock reading. Restoring unit detector response eventually excludes the entire finite window. These results use a single continuum Hilbert space with every nonconstant shape harmonic and every radiative mode. This extends the fixed-density example to a model in which the corner controls both the normalization of the clock and the local strength of the radiation. [Fixed-density calculation](clock-construction.md) · [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Ordered clock, Eqs. (4.22)–(4.27)](https://arxiv.org/html/2611.34924v1#S4.E22)

## The preparation and its canonical coordinates

Let $d\Omega$ be solid angle on the unit sphere, $d\omega=d\Omega/(4\pi)$ and $\langle g\rangle=\int g\,d\omega$. Use real scalar harmonics $Y_{jm}$ orthonormal in **$L^2(d\Omega)$** for the Gaussian law $\gamma$. With independent real standard normals $\xi_{jm}$, set
$$
 f=\sum_{j\ge1,m}\frac{\xi_{jm}Y_{jm}}{[1+j(j+1)]^2},\qquad
 w=\frac{e^f}{\langle e^f\rangle},\quad
 r_0=\sqrt{\mathscr A/(4\pi)},\quad
 \rho_f=r_0\sqrt w,\quad a_f=\int\rho_f\,d\Omega .
$$
This is the centered Gaussian with covariance $(1-\Delta_{S^2})^{-4}$ on the spatially mean-zero subspace. The local area density is $\rho_f^2$ per unit solid angle and its integral is exactly $\mathscr A$ in every realization, implementing the commuting logarithmic density parametrization of Eqs. (4.23)–(4.25). [Area density in v1](https://arxiv.org/html/2611.34924v1#S4.E23)

Each strictly positive smooth density $b$ of this area occurs in the support: its inverse coordinate is $\log(b/r_0^2)-\langle\log(b/r_0^2)\rangle$. Finite harmonic sums approximate this coordinate uniformly. Every neighborhood of a finite sum has positive probability by independence, positive finite-dimensional Gaussian densities and the vanishing tail estimate below. Individual prescribed shapes have probability zero.

The law has continuous realizations. More precisely its mean squared $H^t$ norm is $\sum_{j\ge1}(2j+1)[1+j(j+1)]^{t-4}<\infty$ for $t<3$. Sobolev embedding gives $C^{1,\alpha}$ realizations for every $0<\alpha<1$. At $t=3$ the mean contributions of successive shells have divergent sum, whereas their independent centered fluctuations have summable variances $2(2j+1)/[1+j(j+1)]^2$. Thus the squared $H^3$ norm diverges almost surely. Smooth shapes belong to the support in the uniform topology. The Gaussian assigns the set of smooth shapes measure zero.

Take $\mathcal H=L^2(\gamma;\mathcal F)$ with $\mathcal F$ the fixed symmetric Fock space of pinned, two-polarization radiation. The normalized product preparation is the constant vector $\Psi(f)=\Omega$, the radiative vacuum. In each scalar harmonic coordinate $f_{jm}$ of variance $c_j=[1+j(j+1)]^{-4}$, the canonical momentum is $-i\hbar(\partial_{f_{jm}}-f_{jm}/(2c_j))$ on Gaussian-weighted polynomial cylinders. Its unitary group translates the coordinate with the Gaussian Radon–Nikodym factor. Thus multiplications by shape commute with this particular clock while shape translations are present in the same representation. [Gaussian preparation, Eq. (4.7)](https://arxiv.org/html/2611.34924v1#S4.E7) · [Bounded area moments and canonical charts](corner-commutant.md)

At fixed shape the linearized radiative symplectic form in a transported angular frame has a local coefficient proportional to $\rho_f^2$. A current with local unsmoothed angular bracket proportional to $\delta(y,y')$ at round density consequently acquires the factor $r_0^2/\rho_f(y)^2$ in its bracket. Realize this scale on the common oscillators by multiplying the round current on each ray by $h_f(y)=r_0/\rho_f(y)$. For our detector, **first** smooth the canonically normalized round current with the round detector kernel, **then** multiply the measured current by $h_f(y)$. Its covariance between two measured rays acquires $h_f(y)h_f(y')$. Angular smoothing and multiplication by a varying $h_f$ need not commute. This order specifies the detector; it does not derive it from the gravitational constraints. [Fixed-corner pairing, Eq. (D.42)](https://arxiv.org/html/2611.34924v1#A4.E42) · [Varying-area reduction, Eqs. (A.37)–(A.42)](https://arxiv.org/html/2611.34924v1#A1.E37)

## The clock and its domain

Take $\epsilon=1/4$, $L=1-\epsilon$ and $u_0=Lr_0$. In the pinned tangent-plane model write $x=rz$, and let $J_0=x'-x/r$ after applying amplitude responses $R_k=2^{-(k-1)}$ to radial pairs $k\ge1$ and $A_j=2^{-(j-2)}$ to both tensor-harmonic families $j\ge2$. The round prefix $X_0(y,v)$ sums both components of $\int_\epsilon^v J_0^2\,dr/(4r)$. It is positive and self-adjoint. For $J_f=h_f J_0$ the prefix is $qX_0$ with $q=h_f^2=1/w$. Define the capped clock fiber by the density sandwich of Eq. (4.26),
$$
 \frac{T_R(f)}{u_0}
  =K_f\left\langle w\,\frac1L\int_\epsilon^1
             \exp\!\big[\min(qX_0(y,v),R)\big]dv\right\rangle,
 \qquad K_f=\frac{\mathscr A}{r_0a_f}=\frac1{\langle\sqrt w\rangle}\ge1 .
$$
Indeed the sandwich factors on each side are $\rho_f/\sqrt{a_f}$, and the original integration uses $d\Omega$. Even without shear a nonround shape has clock $K_fu_0$. A finite cap gives a measurable bounded operator on each fiber with bounds $K_fu_0 I\le T_R(f)\le e^RK_fu_0 I$. Measurability follows from the measurable round prefixes and scalar functional calculus. The direct integral can be unbounded because $K_f$ can grow with the shape. [Round prefix construction and core](clock-construction.md) · [Area ordering, Eqs. (4.25)–(4.26)](https://arxiv.org/html/2611.34924v1#S4.E25)

Define $B$ by the decreasing strong limit of the positive contractions $u_0(u_0+T_R)^{-1}$. The resolvents act fiberwise and dominated convergence gives their fiberwise limit. We use the finite-reading projector
$$
 P_\ell=\mathbf1_{[u_0/(u_0+\ell),1]}(B).
$$
On any subspace where the limiting increasing form has dense domain this is the spectral projection of its ordinary self-adjoint clock. A nullspace of $B$ contributes zero to every finite window. This definition leaves room for a nondense exponential form on the complementary shapes. A failed sufficient Wick bound there would by itself prove no divergence. [Resolvent prescription, Eq. (C.13)](https://arxiv.org/html/2611.34924v1#A3.E13)

## A uniform probability on a set of shapes

For the chosen area and responses the round Wick estimate uses $V_*=(2\pi/L)^2\log(1/\epsilon)(136/9)(16/9)/(4\cdot10^4)=0.0653441251\ldots$. At any prefix the ordered vacuum moments of $X_0$ are bounded by $(2n-1)!!V_*^n$, by bounding every contraction by the product of its kernel norms. Hence the conditional vacuum expectation of $\exp(qX_0)$ is at most $F(q)=(1-2V_*q)^{-1/2}$ for $2V_*q<1$. This step allows noncommuting radiative quadratures. With finitely many external creation operators the moment bound gains only a fixed polynomial in $n$, so a uniform strict margin gives a dense finite-form domain on the selected shape subspace. Bounded scalar wavefunctions supported there times finite products of creation operators span a dense set. [Wick counting and finite-particle estimates](clock-construction.md)

Take $G=\{\|f\|_\infty\le\delta\}$ with $\delta=1/2$. Spatial mean zero, Jensen's inequality, and the secant bound on $e^f$ imply $1\le\langle e^f\rangle\le\cosh\delta$. Thus
$$
 q_- = e^{-\delta}\le q\le e^\delta\cosh\delta=q_+,
 \qquad 2V_*q_+<1.
$$
For $g=e^{f/2}\in[m,M]=[e^{-\delta/2},e^{\delta/2}]$, the inequality $g^2\le(M+m)g-mM$ gives $K_f=\sqrt{\langle g^2\rangle}/\langle g\rangle\le(M+m)/(2\sqrt{mM})=K_*=\cosh(\delta/2)$, by maximizing over $\langle g\rangle$. The normalized corner weight obeys $\langle wq\rangle=1$. Since $F$ is convex, its chord between $q_-$ and $q_+$ bounds $F$ above, giving
$$
 \langle wF(q)\rangle\le
 D=\frac{(q_+-1)F(q_-)+(1-q_-)F(q_+)}{q_+-q_-}.
$$
Thus $K_fu_0\le \langle T(f)\rangle_\Omega\le K_f D u_0$. For $t=\ell/u_0=1.2$ the weight above $\ell$ costs at least $\ell-K_fu_0$ in excess of the floor. Since $D\ge1$ and $K_*<t$ this yields
$$
 \|P_\ell(f)\Omega\|^2\ge 1-\frac{K_f(D-1)}{t-K_f}
 \ge \frac{t-K_*D}{t-K_*}=0.53613194\ldots
 \qquad(f\in G).
$$

The Gaussian probability of $G$ also admits an explicit bound. By the spherical harmonic addition identity the supremum of the $j$th shell is bounded by $\sqrt{(2j+1)/(4\pi)}\,\|\xi_j\|_2/[1+j(j+1)]^2$. The triangle inequality in probabilistic $L^2$ therefore yields
$$
 \big(\mathbb E_\gamma\|f\|_\infty^2\big)^{1/2}
 \le \frac1{\sqrt{4\pi}}
 \sum_{j\ge1}\frac{2j+1}{[1+j(j+1)]^2}
 \le \frac{7}{12\sqrt{4\pi}} .
$$
The first term is $1/3$ and for $j\ge2$ the summand is bounded by $j^{-2}-(j+1)^{-2}$. This argument also bounds any harmonic tail. Markov's inequality gives $\gamma(G)\ge1-[7/(12\sqrt{4\pi}\delta)]^2=0.89168621\ldots$. Integrating the fiber probability gives the full preparation's acceptance,
$$
 \|P_{1.2u_0}\Psi\|^2\ge
 \gamma(G)\frac{t-K_*D}{t-K_*}\ge0.47806146 .
$$
In particular $P_\ell(\mathbf1_G\Psi)/\|P_\ell(\mathbf1_G\Psi)\|$ is a normalized state supported in the finite window. Some shapes are excluded even in the absence of radiation. On the smooth dipole $f=b\cos\theta$ one has $K_f^2=(b/2)\coth(b/2)$. This tends to infinity with $b$. Continuity of $K_f$ in the uniform norm and full shape support give a positive probability of rejection from the floor alone at every fixed finite threshold.

The Gaussian restricted to $G$ is nonatomic. For example, the measure of any level set of the first scalar harmonic coefficient remains zero on restriction, so its restricted continuous distribution can divide $G$ into infinitely many disjoint sets of positive probability. Multiplying the preparation by the indicator of each set and projecting gives mutually orthogonal nonzero vectors, because the clock acts fiberwise. The rank is therefore infinite already from the local area degree of freedom. This argument requires that the marked shapes remain distinguishable by the clock's commuting multiplication operators. Physical frame constraints or a clock that differentiates in the shape variables could remove that conclusion. [Marked-corner rank criterion](corner-commutant.md)

## The full vacuum has infinite mean

At any finite cap the product vacuum belongs to the operator domain. Indeed $K_f^2\le\langle e^f\rangle$ by $\langle e^{f/2}\rangle\ge1$, and $\mathbb E_\gamma\langle e^f\rangle=\exp(\operatorname{Var}_\gamma(f(y))/2)<\infty$ by rotational invariance. The uncapped global mean nonetheless diverges. At every $y$ and every $v>\epsilon$ the conditional round mean $\mu=\langle\Omega,X_0(y,v)\Omega\rangle$ is strictly positive: the transmitted radial fundamental has nonzero derivative at the initial cut, and the quadrupole addition identity gives a positive sum of squared amplitudes on each ray. Spectral Jensen, valid with infinite expectation, gives
$$
 w\,\langle\Omega,e^{qX_0(y,v)}\Omega\rangle\ \ge\ e^{\mu q}/q.
$$
Here $q=\langle e^f\rangle e^{-f(y)}\ge e^{-f(y)}$. The function $e^{\mu q}/q$ increases for $q>1/\mu$. At each fixed $y$, $-f(y)$ is a centered Gaussian with positive variance $\sigma^2$. On its sufficiently large positive tail, the expectation is bounded below by a constant times $\int^\infty\exp(\mu e^x-x-x^2/(2\sigma^2))\,dx=\infty$. Since $K_f\ge1$, Tonelli's theorem and monotone convergence give $\sup_R\langle\Psi,T_R\Psi\rangle=\infty$. The same state has the finite-window probability proved above. Its mean cannot certify that overlap. The conditional preparation $\mathbf1_G\Psi/\sqrt{\gamma(G)}$ does have finite mean.

## Restoring unit response excludes every shape

Refining mode cutoffs with the detector held fixed constructs the continuum model above. Restoring unit response on every mode is a different limit for which one can prove the opposite outcome on the same shape space. Suppose the round regulated prefix has a scalar spectral floor $X_0(y,v)\ge H I$ on all rays and all cuts $v\ge v_0$, with $\alpha=(1-v_0)/L>0$ fixed. In the pinned model $H\to\infty$ when the product of the radial and angular response sums diverges. For example this happens for every sequence tending to unit gain on each fixed mode. [State-independent prefix bound, Eq. (1)](existence-limit.md)

On a given shape the cap-$R$ clock now has a lower bound in units of $u_0$ given by $N/\langle\sqrt w\rangle$, with
$$
 d(y)=1+\alpha\big(e^{\min(H/w(y),R)}-1\big),\qquad N=\langle w d\rangle\ge1 .
$$
Cauchy–Schwarz gives $\langle\sqrt w\rangle^2\le N\langle 1/d\rangle$. Wherever $H/w\ge R$, $d=D_R=1+\alpha(e^R-1)$. Elsewhere $d\ge\alpha e^{H/w}\ge\alpha e H/w$, since $e^x\ge e x$ for $x\ge0$. Averaging the reciprocals and using $\langle w\rangle=1$ gives
$$
 \frac{T_R(f)}{u_0}\ \ge
 \left[D_R^{-1}+(\alpha e H)^{-1}\right]^{-1/2} I \qquad (H>0).
$$
This floor diverges uniformly in the shape whenever $H,R\to\infty$, irrespective of relative speeds. Even a regulator-dependent preparation concentrating its area in a shrinking angular patch eventually has zero probability in every fixed finite clock window. This result concerns the same linearized current rescaling. The required scalar floor in constrained gravity remains an independent question.

## What this establishes for the existence question

The model gives positive overlap at one specified finite length with nonlinear area normalization, local area-dependent radiation and an explicit normalized Gaussian preparation. The physical proof gap at Eq. (5.19) includes the choice of representation for nonlinear fields after Dirac reduction, the ordered curved-target focusing term, the cap, and control of the local current as the measurement resolution is removed. The logarithmic shape covariance, post-smoothing multiplication order and commuting corner/shear coordinates specify the present comparison. The calculation neither identifies the spherical physical preparation with this vector nor proves that an interacting projector has the same rank. A physical representation with convergent clock resolvents and the corresponding bounded conditional exponential moments on a positive-probability sector would make this existence argument applicable there. [Physical existence statement (5.19)](https://arxiv.org/html/2611.34924v1#S5.E19) · [Curved-target domain test](clock-domain-jump.md) · [Fable's clock review](../reviews/fable-clock-sewing.md)

## Reproduction

Run `python3 -B checks/fluctuating_corner_state.py` from the repository root, or `make check` for the suite. The script checks the sandwich and convex bounds on nonround weighted shapes, the telescoping shell estimate and the uniform floor when the response is removed. The displayed numbers are rounded to the nearest last digit. [Executable check](../checks/fluctuating_corner_state.py)

```text
largest conditional prefix variance  0.12148394
corner normalization upper bound     1.03141310
conditional mean / u0 upper bound    1.10961518
conditional acceptance lower bound   0.53613195
shape event probability lower bound  0.89168622
full vacuum acceptance lower bound   0.47806147
```
