# How much radial shear can a finite clock reading admit?

The exponential in Venkatesa Chandrasekaran's incoming clock bounds a weighted integral of the quantum shear squares. The weight falls as the square root of the remaining radial distance to the corner. The quadratic expansion of the clock gives a weight falling linearly there. This difference yields a finite radial interval for the symplectic mode count, even though the unweighted shear energy can diverge along a sequence of allowed classical profiles. The new estimate gives a direct route to a radial rank bound in a fixed-polarization comparison. The angular, corner and representation problems still enter the four-dimensional conjecture. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Focusing squares, Eq. (4.22)](https://arxiv.org/html/2611.34924v1#S4.E22) · [Earlier endpoint examples](D3.md)

## An inequality for the full exponential

Let $d=1-\epsilon$, $0<\epsilon<1$, and $w(v)=\sqrt{(1-v)/d}$. Suppose the positive focusing forms $\Xi_y(v)$ are the integrals from $\epsilon$ to $v$ of the shear squares in (4.22), and suppose the uncapped clock form (4.27) exists on the vector being tested. Fix a unit vector $\psi$ of finite clock form and set

$$
\xi_y=\widehat\varrho_S(y)\widehat{\mathsf a}^{-1/2}\psi,\qquad
M=\int_S\|\xi_y\|^2\,\boldsymbol\epsilon_0(y),\qquad
T[\psi]=\int_S\!\boldsymbol\epsilon_0(y)\int_\epsilon^1
\langle\xi_y,e^{\Xi_y(v)}\xi_y\rangle\,dv .
$$

Assume $M>0$. At positive fixed area $\mathscr A$, $M=\mathscr A\|\widehat{\mathsf a}^{-1/2}\psi\|^2$, and $dM\le T[\psi]$. A fixed round density of radius $R$ gives $M=R$. These expressions preserve the manuscript's operator ordering when the density fluctuates. Define the dimensionless weighted focusing

$$
E=\frac{1}{M}\int_S\!\boldsymbol\epsilon_0(y)\int_\epsilon^1
w(v)\,d\langle\xi_y,\Xi_y(v)\xi_y\rangle.
$$

Then

$$
\frac{T[\psi]}{dM}\ \ge\ \Phi(E),\qquad
\Phi(E)=\begin{cases}1+E^2,&0\le E\le1,\\[2pt]2e^{E-1},&E\ge1.\end{cases} \tag{1}
$$

In particular $2dME\le T[\psi]$. Every vector in the clock projection at $\ell$ satisfies (1) with $\ell$ on its left in place of $T[\psi]$. The hypotheses permit finite positive-square regulators and any continuum realization retaining these forms. Applying a finite ceiling to $\Xi$ inside the exponential changes the left side and does not justify the bound on the uncapped shear. [Clock ordering and form, Eqs. (4.26)–(4.27)](https://arxiv.org/html/2611.34924v1#S4.E27) · [Uncapped form limit, Appendix C.2](https://arxiv.org/html/2611.34924v1#A3.E13)

**Proof.** Write $r=w(v)$, so $dv/d=-2r\,dr$. Tonelli's theorem applied to the positive accumulated shear gives $ME=\int_S\boldsymbol\epsilon_0\int_0^1\langle\xi_y,\Xi_y(1-dr^2)\xi_y\rangle dr$. For $a>0$ and $x\ge0$, the tangent to $e^x$ at $x=\log(a/r)$ gives

$$
e^x\ge(a/r)x+(a/r)[1-\log(a/r)]\quad (r<a).
$$

For $r\ge a$, use $e^x\ge 1+(a/r)x$. Apply each inequality by spectral calculus to the **single** operator $\Xi_y(1-dr^2)$ at that cut. Integrating with $2r\,dr$ and the vectors $\xi_y$ gives

$$
\frac{T[\psi]}{dM}\ge
\begin{cases}2aE+1-a^2,&0<a\le1,\\2aE-2a\log a,&a\ge1.\end{cases}
$$

For $0<E\le1$ take $a=E$, with $a\downarrow0$ at $E=0$. For $E\ge1$ take $a=e^{E-1}$. This proves (1), including finiteness of $E$ on every tested vector (use $a=1$ first). Only positivity and spectral calculus at each cut enter the argument. Operators at different radii or angles may fail to commute.

The constants are sharp for scalar positive focusing. Take $\Xi(v)=\max(0,\log[a/w(v)])$. For $a\le1$, the integrals give $E=a$ and $T/(dM)=1+a^2$. For $a\ge1$ they give $E=1+\log a$ and $T/(dM)=2a$. Truncate the logarithm near the corner and interpolate from zero in a shrinking neighborhood of $\epsilon$ if $a>1$. Smooth monotone approximations give the same limiting integrals, since the omitted logarithm in $dr$ and its exponential in $2r\,dr$ are integrable. These are scalar comparisons for (1). Realizing such a profile in a physical quantum state would require a preparation. At the junction $E=1$, the smooth profiles $\Xi=\tfrac12\log[(1+\eta)/(w^2+\eta)]$ approach equality in $2dME\le T$ as $\eta\downarrow0$.

## What a reading near the minimum requires

At fixed positive total area let $b=\sqrt{\mathscr A/(4\pi)}$ and $u_0=db$. The angular variance about a round density, measured on the original vector, is
$$
D=\frac{1}{4\pi}\int_S\|(\widehat\varrho_S(y)/b-I)\psi\|^2\,\boldsymbol\epsilon_0
=2\left(1-\frac{\langle\psi,\widehat{\mathsf a}\psi\rangle}{4\pi b}\right).
$$
The identity uses $\int_S\widehat\varrho_S(y)^2\boldsymbol\epsilon_0=\mathscr A I$. Since $\|\psi\|=1$, Cauchy–Schwarz for $\widehat{\mathsf a}^{1/2}\psi$ and $\widehat{\mathsf a}^{-1/2}\psi$ gives $M/b\ge(1-D/2)^{-1}$. Thus $T[\psi]/u_0\ge\Phi(E)/(1-D/2)$. Every unit state admitted at $\ell=u_0(1+\delta)$ with $0\le\delta\le1$ obeys the joint budget
$$
E^2+\tfrac12(1+\delta)D\le\delta. \tag{2}
$$
At precisely $u_0$ the threshold eigenspace consists of the common round, shear-free vectors. Equality forces $D=0$, so $\widehat\varrho_S(y)\psi=b\psi$ almost everywhere and each $\xi_y$ is the same scalar multiple of $\psi$. Equality also forces $E=0$, so positivity gives $\Xi_y(v)\psi=0$ almost everywhere. Conversely these two conditions evaluate the clock form to its minimum, hence imply membership in the threshold eigenspace. Existence of such a common vector depends on the representation. Equation (2) applies above threshold even with noncommuting area and shear operators. [Area normalization and ordering, Eqs. (4.25)–(4.27)](https://arxiv.org/html/2611.34924v1#S4.E25)

## The radial oscillator comparison

Fix a round density of radius $R$ and pin the radiative profile at both ends, $h(\epsilon)=h(1)=0$. Retain one linear polarization and $m<\infty$ independent angular profiles orthonormal in $d\Omega/(4\pi)$, with the pairing in (D.42a). The comparison allows the induced normal connection to vary at the ends. Pinning it at both ends as well would impose $\int_\epsilon^1 v^2 h'(v)dv=0$ in the nonzero spin-two harmonics by (D.39), changing the space on which the modes below are diagonal. For $z^1=\sum_jf_j(y)h_j(v)$, $z^2=0$, the squared shear in (4.22) gives

$$
Q=\sum_{j=1}^m\int_\epsilon^1 w(v)v|h_j'(v)|^2dv,\qquad ME=RQ/4 .
$$

The same identity holds in expectation when these linear fields and their positive squares are realized on a common domain. Thus $T\ge dRQ/2$ there. The full nonlinearity in the exponential supplied this quadratic comparison. On the classical profiles define $x=vh$ and $t=\int_\epsilon^v du/w(u)=2d(1-w(v))$, an interval of length $L=2d$. For one channel set

$$
B[x]=\int_0^L|x_t|^2dt=\int_\epsilon^1 w(v)|(vh)'|^2dv .
$$

Since $h(\epsilon)=0$, Cauchy–Schwarz gives $\sup|h|^2\le (2d/\epsilon)\int wv|h'|^2dv$. Using $|(vh)'|^2\le2v^2|h'|^2+2|h|^2$ and $\int w\,dv=2d/3$ gives $\sum_j B[x_j]\le C_\epsilon Q$ with $C_\epsilon=2+8d^2/(3\epsilon)$. These Hilbert-space norm inequalities also apply to fields acting on a fixed common-domain vector. In contrast, the quadratic Taylor term of $T$ alone gives weight $1-v$ after exchanging its radial integrals, and $\int^1dv/(1-v)$ diverges. [Radial pairing and fixed endpoints, Eqs. (D.42a)–(D.44)](https://arxiv.org/html/2611.34924v1#A4.E44)

Choose the sign of the symplectic orientation so that its coefficient $\kappa$ is positive. In each channel the pairing becomes

$$
\Omega(x,y)=\kappa\int_0^L(x_t y-y_t x)dt,\qquad x(0)=x(L)=0.
$$

The derivative maps the completion in the $B$ norm isometrically onto mean-zero $L^2(0,L)$. Integrating its sine and cosine basis gives pairs $\sqrt{2/L}(1-\cos kt)/k,\ \sqrt{2/L}\sin(kt)/k$, $k=2\pi n/L$. These are orthonormal for $B$. Their symplectic pairing is $2\kappa/k$, and all cross-pair entries vanish. The comparison Hamiltonian $H_c=\tfrac12\sum_j B[x_j]$ therefore has oscillator level spacings $\nu_n=\pi\hbar n/(\kappa L)$, with $m$ copies. The calculation diagonalizes the comparison Hamiltonian on its specified completed phase space.

Additional closed homogeneous linear endpoint constraints can only raise the ordered positive oscillator frequencies of this quadratic comparison. If $A$ represents $\Omega$ in the $B$ inner product and $W$ is the allowed closed subspace, the operator there is $P_WA|_W$. Compressing each rank-$k$ approximation to $A$ gives a rank-at-most-$k$ approximation on $W$ with at most the original error. Its ordered singular values are consequently at most those of $A$. After removing the kernel of the restricted pairing, excitation energies are inversely proportional to these singular values. This argument allows the comparison bound to survive a linear constraint such as the fixed endpoint connection. The constrained oscillator eigenfunctions themselves may change.

Suppose the full Hilbert space for this restricted model is the $m$-channel Fock space just described, with each joint occupation vector occurring once. If it realizes the corresponding normally ordered Fock energy $H_{\rm exc}=\sum_{j,n}\nu_n N_{jn}$ and satisfies $H_{\rm exc}\le C_\epsilon T/(dR)$ in quadratic forms, the min–max principle gives

$$
\operatorname{rank}P_\ell\le
\#\left\{(N_{jn}):\sum_{j,n} nN_{jn}
\le\frac{C_\epsilon\kappa L\ell}{\pi\hbar dR}\right\}<\infty .
$$

The right side counts partitions with $m$ possible labels for each part and includes the vacuum. The comparison counts it even if the physical clock rejects it. If the stronger form comparison $H_{\rm exc}\le C_\epsilon Q/2$ survives quantization, (1) replaces the energy ceiling $C_\epsilon\ell/(dR)$ by $2C_\epsilon\Phi^{-1}(\ell/(dR))$ for $\ell\ge dR$. In particular, when $\ell=dR(1+\delta)$ with $0\le\delta\le1$ and $2C_\epsilon\sqrt\delta<\nu_1$, there is room for at most **one** accepted state in this model. Its existence is a separate spectral question.

In a finite radial quantization the bare positive oscillator energy contains in addition $m\sum_{n\le K}\nu_n/2$. A growing zero-point term can empty a clock window. To infer a nonempty continuum count requires an actual clock realization and a justified comparison to its excitation energy after vacuum subtraction. [Continuum clock obstruction in a specified regulator](clock-spectrum.md)

In the full four-dimensional problem (1) controls a radial shear form on the vectors $\xi_y$. It supplies no angular derivative, no lower bound on the physical cost of arbitrarily high angular momentum, and no count of corner states. In particular, allowing infinitely many angular channels in the comparison leaves the first radial frequency infinitely degenerate. A completion of this proof route would need a growing angular and corner energy on the same physical clock subspace, as well as a nonzero accepted preparation. The absence of these estimates is a proof gap.

Run `python3 checks/rank_energy_test.py` from the repository root. The scalar examples give $(E,T/(dM))=(0.25,1.0625),(0.8,1.64),(1,2),(1+\log2,4)$. A smooth endpoint regulator reaches $E/[T/(dM)]=0.499971$. A two-cell matrix example with noncommuting positive operators has minimum sampled margin $T/(dM)-\Phi(E)=0.386852$. Reducing both focusing forms tenfold gives minimum sampled slack $0.032451$ in the joint budget (2). The check also integrates all symplectic matrix entries of eight radial pairs. The repository suite includes this check via `make check`. [Executable check](../checks/rank_energy_test.py)
