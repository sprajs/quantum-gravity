# A positive continuum clock with a fixed detector resolution

Prepare the oscillator vacuum on a round, fixed-area null cone and read the shear through a specified radial and angular response before squaring it. In the linearized radiative model below, the resulting positive operator has a dense form domain even when all modes are present. For the explicit response, a reading below 1.2 times the shear-free value has probability at least 0.6373 in the vacuum. The same clock window has infinite rank. Sufficiently weak sensitivity to high modes can therefore give a nonempty window while defeating a finite state count in this model.

Venkatesa Chandrasekaran's construction uses the local shear, a nonlinear target metric and a quantum corner density. The calculation here retains the exponential of each integrated shear prefix and the angular average, with a frozen round corner and a finite detector resolution. It addresses the proof gap in constructing the positive clock and its allowed states. Applying it to the physical gravitational projector requires a representation of those operators and of the constraints. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Eqs. (4.22)–(4.27)](https://arxiv.org/html/2611.34924v1#S4.E22) · [Eq. (5.19)](https://arxiv.org/html/2611.34924v1#S5.E19)

## A sufficient condition on the measured shear

Let $d\omega=d\Omega/(4\pi)$, $\mathscr A=4\pi b^2$, $0<\epsilon<1$ and $u_0=b(1-\epsilon)$. Use symmetric Fock space over an infinite-dimensional separable one-particle Hilbert space and its vacuum $\Omega$. Write $\Phi(f)=a(f)+a^\dagger(f)$ with $\|\Phi(f)\Omega\|^2=\|f\|^2$. At each generator and prefix $(y,v)$ take measurable one-particle kernels $f_i$ and a positive measure $d\mu(i)$, which can include a sum over shear components and an integral up to $v$. The kernels and measure may depend on $(y,v)$. Suppose the quantities
$$
 X_{yv}=\int\Phi(f_i)^2\,d\mu(i),\qquad
 V_{yv}=\int\|f_i\|^2\,d\mu(i),\qquad
 V=\mathop{\rm ess\,sup}_{y,v} V_{yv}<\tfrac12
$$
are defined by the finite-particle construction below, with a measurable family of prefixes. Set
$$
 T_R=b\int d\omega(y)\int_\epsilon^1
             e^{\min(X_{yv},R)}\,dv .
$$
Then the monotone form limit of $T_R$ defines a positive self-adjoint clock $T$ with $T\ge u_0 I$. Its vacuum mean $U=\|T^{1/2}\Omega\|^2$ satisfies
$$
 u_0\le U\le \frac{u_0}{\sqrt{1-2V}}.
$$
Every window $P_\ell=\mathbf1_{[0,\ell]}(T)$ with $\ell>U$ contains the normalized state $P_\ell\Omega/\|P_\ell\Omega\|$ and has infinite rank. Its vacuum probability is at least $(\ell-U)/(\ell-u_0)$. The area ceiling follows directly from $T\ge(1-\epsilon)\sqrt{\mathscr A/(4\pi)}\,I$. An accepted fixed-area sector thus obeys $\mathscr A\le4\pi\ell^2/(1-\epsilon)^2$. [v1, Eq. (5.21)](https://arxiv.org/html/2611.34924v1#S5.E21)

**Construction and vacuum bound.** The norm of $\Phi(f)$ on vectors supported on at most $m$ particles is at most $2\sqrt{m+1}\|f\|$. The integral of its square therefore defines a positive symmetric operator on the invariant finite-particle domain, bounded from that subspace into at most $m+2$ particles by $4(m+2)V_{yv}$. Iterating gives analytic vectors there, so its closure is self-adjoint. In the vacuum expectation of $X_{yv}^n$, each ordered product has $(2n-1)!!$ Wick pairings. Each contraction has absolute value bounded by the product of its two kernel norms, including when the covariance is complex. Since each field index occurs twice, integration bounds the moment by $(2n-1)!!\,V_{yv}^n$. Positivity and the scalar spectral series then give
$$
 \langle e^{X_{yv}}\rangle_\Omega
 \le\sum_{n\ge0}\frac{(2n-1)!!}{n!}V_{yv}^n
 =(1-2V_{yv})^{-1/2}.
$$
For a vector formed from $p$ creations on the vacuum the same absolute bound acquires the fixed external kernel norms and replaces $(2n-1)!!$ by $(2n+2p-1)!!$. This multiplies the summands by a polynomial in $n$ of fixed degree $p$ and preserves convergence. The span of these vectors is dense. The increasing bounded capped forms thus have a densely defined closed limit, including the vacuum. A single quadrature $X=c\Phi(f)^2$ with $\|f\|=1$ attains the vacuum estimate for $0\le c<1/2$, so a larger universal threshold cannot follow from $V$ alone. [Wick's contraction theorem](https://doi.org/10.1103/PhysRev.80.268) · [Nelson's analytic-vector theorem](https://doi.org/10.2307/1970331) · [v1, Appendix C.2](https://arxiv.org/html/2611.34924v1#A3.SS2)

**Number of accepted states.** Choose any orthonormal one-particle vectors $u_j$ and put $\psi_j=a^\dagger(u_j)\Omega$. At each prefix let $D_j=\int|\langle u_j,f_i\rangle|^2d\mu(i)$. The Wick pairings connecting the two external legs to each other give the vacuum moment. The remaining $2n(2n-1)!!$ terms each contribute at most $D_j V_{yv}^{n-1}$. When the external contractions reach different integration indices this uses $(\int |\langle u_j,f_i\rangle|\,\|f_i\|d\mu)^2\le D_j V_{yv}$. Summing the exponential series yields
$$
 |\langle e^{X_{yv}}\rangle_{\psi_j}
    -\langle e^{X_{yv}}\rangle_\Omega|
 \le 2D_j(1-2V)^{-3/2}.
$$
Bessel's inequality gives $\sum_j D_j\le V_{yv}$. Since $T\ge u_0P_\ell+\ell(I-P_\ell)$, summing the resulting probability bounds for any $M$ such preparations gives
$$
 \operatorname{rank}P_\ell\ \ge\ \sum_{j=1}^M\|P_\ell\psi_j\|^2
 \ \ge\ M\frac{\ell-U}{\ell-u_0}
          -\frac{2u_0 V}{(\ell-u_0)(1-2V)^{3/2}}.
$$
Taking $M$ arbitrarily large proves the rank statement. The projected one-particle states can overlap. Their total accepted probability already requires the indicated number of orthogonal dimensions. [Projector rank test](finite-kinematics.md)

## A response with both tensor polarizations and all wavelengths

Hold the round corner density, angular frame and endpoint values fixed. In the tangent plane of the target metric at the round cone let $x(r,y)=r z(r,y)$, with two real components. Choose real tensor harmonics $E_{jmp}(y)$ normalized in this plane with measure $d\omega$, where $j\ge2$, $-j\le m\le j$ and $p$ distinguishes the two polarization families. Rotational invariance and the integrated norms give $\sum_{m,p}|E_{jmp}(y)|^2=2(2j+1)$. Set $s=\mathscr A/(4G_N\hbar)$, $\kappa=2\pi/(1-\epsilon)$, and $w_k(r)=e^{ik\kappa(r-\epsilon)}-1$ for $k\ge1$. Both endpoints of $w_k$ vanish. The real and imaginary parts are the two quadratures of a pinned radial Fourier pair. At fixed corner the bulk pairing is proportional to $\int(x'g-g'x)dr$, giving pair commutators of magnitude $2/(sk)$ in the chosen normalization. [v1, Eq. (3.42)](https://arxiv.org/html/2611.34924v1#S3.E42) · [Fixed-endpoint expression, Eq. (D.42)](https://arxiv.org/html/2611.34924v1#A4.E42)

Choose real response coefficients $R_k$ radially and $A_j$ angularly. The measured $x$ field has creation kernel $E_{jmp}(y)R_k A_jw_k(r)/\sqrt{sk}$ in mode $(k,j,m,p)$ and the conjugate annihilation coefficient. The response acts on the field being measured. The canonical oscillators and their Hilbert space include every retained and attenuated mode. With $f_i$ the component kernels of $x'-x/r$, use $d\mu=dr/(4r)$ and sum over the two components. This gives exactly the positive quadratic tangent-space focusing $\tfrac14\int_\epsilon^v r|z'|^2dr$ applied to the smoothed fields. As long as the response sums below converge, the kernels in the example give a measurable field. For any prefix the identity
$$
 \int_\epsilon^v \frac{|w_k'-w_k/r|^2}{r}\,dr
 =\int_\epsilon^v\frac{|w_k'|^2}{r}\,dr
   -\frac{|w_k(v)|^2}{v^2}-\int_\epsilon^v\frac{|w_k|^2}{r^3}\,dr
 \le \kappa^2k^2\log(1/\epsilon)
$$
gives the explicit sufficient bound
$$
 V\le V_*=
 \frac{\kappa^2\log(1/\epsilon)}{4s}
 \left[2\sum_{j\ge2}(2j+1)A_j^2\right]
 \left[\sum_{k\ge1}k R_k^2\right].
$$
For power-law amplitude responses $R_k\asymp k^{-a}$ and $A_j\asymp j^{-d}$ the two sums converge for $a>1$ and $d>1$. The product must also make $V_*<1/2$. Taking both mode cutoffs to infinity at fixed response is justified directly in Fock space. Project each kernel onto successively larger mode subspaces. The restricted quadratics converge on the finite-particle core by the field norm bound and dominated convergence. Essential self-adjointness gives strong resolvent convergence on each prefix. At fixed cap the bounded continuous spectral functions and hence the averaged clocks converge strongly. The cap can then be removed by the monotone form construction. The response widths are held fixed throughout.

Writing $C=sV_*$ makes the scale dependence explicit. At fixed physical length $\ell$ and response, a sufficient area sector satisfies $s>2C$ and $\ell>(1-\epsilon)\ell_P s/\sqrt{\pi(s-2C)}$, with $\ell_P^2=G_N\hbar$. The right-hand side has its minimum at $s=4C$. Thus every $\ell>(1-\epsilon)\ell_P\sqrt{8C/\pi}$ has a model sector with positive vacuum acceptance, if area is available as a preparation parameter. The calculation constructs each fixed-area sector independently.

For a numerical example choose $\epsilon=1/4$, $s=10{,}000$, $R_k=2^{-(k-1)}$ and $A_j=2^{-(j-2)}$. The fundamental radial mode and both quadrupole families pass with unit gain. The radial sum is $16/9$ and the angular sum is $136/9$. This yields $V_* = 0.0653441251$, $U/u_0\le1.07253686$ and, at $\ell=1.2u_0$, vacuum acceptance at least $0.63731571$. At $M=100$ the rank inequality requires at least 63 orthogonal dimensions. Run the check from the repository root. It also checks the pinned-mode identity at interior cuts and the Wick bounds against oscillator moments for both parallel and noncommuting quadratures. [Verification script](../checks/clock_construction.py)

```sh
python3 -B checks/clock_construction.py
```

Expected output, rounded to eight decimals where applicable.

```text
integrated variance upper bound    0.06534413
vacuum mean / u0 upper bound       1.07253686
vacuum acceptance lower bound      0.63731572
rank lower bound at M=100          63
```

## Transfer to gravity

The estimate supplies a concrete alternative to replacing a quantum resolvent by a classical Wigner tail. To use it for v1 one would have to exhibit corresponding exponential-moment bounds on physical preparations, including the densities multiplying the exponential in (4.27), and justify the physical status of the chosen resolution. The rank conclusion would also require the orthonormal preparations to survive the physical constraints. In the example, smearing with nonzero gain at every frequency still allows high modes to pass the clock at essentially the vacuum cost. Sending the response widths to zero at fixed $s$ removes the variance control. The unsmeared point-current obstruction has a separate derivation. [Bare shear analysis](shear-uv.md) · [Fable's fixed-resolution and curved-target tests](../reviews/fable-clock-sewing.md)

The nonlinear weight $e^{2z^1}$ is already significant at finite resolution. For independent nondegenerate Gaussian multiplication coordinates $X,Y$, a prefix cost $c e^{2X}Y^2$ with $c>0$ has an infinite vacuum exponential moment. Conditioned on sufficiently large $X$, the positive exponent in $Y^2$ exceeds the Gaussian decay rate. Finite-reading vectors with bounded coordinate support still exist in that commuting example. Deciding nonemptiness for the original clock requires a domain or spectral estimate for the interacting operators and their corner weights. Neither result here refutes the four-dimensional physical conjecture. [v1, Eqs. (4.21c)–(4.22)](https://arxiv.org/html/2611.34924v1#S4.E22) · [Fable's analysis of noncommuting curved-target costs](../reviews/fable-clock-sewing.md)
