# A spectral obstruction for a clock with two curved-target polarizations

Can the second polarization in the null-cone clock remove the ultraviolet obstruction found for a single free polarization? The bulk classical bracket at fixed area density gives a partial answer. For every smooth radial curve in the hyperbolic target, its first polarization has the same derivative-of-delta term in its shear bracket. The second polarization changes the remaining kernel by an amount controlled by its own shear. This gives a state-independent spectral obstruction in a quantized tangent model around **any** such curve, even with both exponentials of the original clock retained. It also identifies a specific weak-commutator estimate that would give the obstruction in the interacting quantum theory. The latter estimate remains open. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Earlier single-polarization calculation](shear-uv.md)

## The contact term on a curved classical profile

Fix one angular cell, a constant positive corner density, and an interior radial interval $I=(a,b)\subset(\epsilon,1)$. The classical profile $z_0(s)=(x(s),y(s))$ can have both polarizations excited. The metric $dx^2+e^{2x}dy^2$ has orthonormal frame $E_1=\partial_x$, $E_2=e^{-x}\partial_y$. Along the profile, $\nabla_s E_1=\theta' E_2$, $\nabla_s E_2=-\theta' E_1$, with $\theta'=e^x y'$. In a parallel frame the components of $E_1$ are $u(s)=(\cos\theta(s),\sin\theta(s))$. The $11$ component of the transporter in (A.36) is therefore $u(s)\cdot u(t)$. Choose orientation and absorb the corner and angular normalization into $\kappa>0$, including $\hbar$ when comparing commutators. The resulting $11$ bulk coordinate kernel is $-\kappa\,\mathrm{sgn}(s-t)u(s)\cdot u(t)/(st)$. The separate homogeneous term $k_\partial$ depends on the cut conditions. [Target metric (4.21)](https://arxiv.org/html/2611.34924v1#S4.E21) · [Fixed-area Dirac kernel (A.34)–(A.36)](https://arxiv.org/html/2611.34924v1#A1.E36)

For the first current $J(s)=s\,\partial_s z^1(s)$, put $D_s=\partial_s-1/s$ and $B(s)=D_su(s)$. Differentiating the kernel gives the following distribution identity on the interior,

$$
D_sD_t[\mathrm{sgn}(s-t)u(s)\cdot u(t)]
=-2\delta'(s-t)+\mathrm{sgn}(s-t)B(s)\cdot B(t),
\qquad |B(s)|^2=(e^x y')^2+s^{-2}.
$$

Here $\delta'$ differentiates the first argument. The coefficients of the undifferentiated delta cancel because $u\cdot u'=0$ and $1/s=1/t$ on the diagonal. Equivalently, the first differentiation already evaluates the moving-frame dot product to one on the delta. For real test functions $f,g$ supported in $I$, Cauchy–Schwarz bounds the magnitude of the regular kernel paired with $f\otimes g$ by $\|f\|_2\|g\|_2 B_I$, where

$$B_I=\int_I[(e^x y')^2+s^{-2}]\,ds.$$

This is an exact calculation of the bulk term in the *classical* fixed-density bracket at the given profile. Any additional cut kernel with a bounded mixed derivative after the current weights contributes a finite $L^2(I)\to L^2(I)$ norm to the remainder. Whether the physical cap yields such a bound after quantization is a separate question. [Fixed and varying area treatments after (A.36)](https://arxiv.org/html/2611.34924v1#A1.E37)

## A two-polarization quantum comparison with the full clock exponential

Quantize the tangent variations at this profile. Use two real scaled parallel-frame fields $H_{1,N},H_{2,N}$ on $[\epsilon,1]$ with brackets

$$
[H_{i,N}(s),H_{j,N}(t)]=-i\kappa\delta_{ij}S_N(s-t)\,1,
\qquad S_N(d)=\frac4\pi\sum_{n=0}^{N-1}\frac{\sin((2n+1)\pi d/(1-\epsilon))}{2n+1}.
$$

These are finite collections of Schrödinger oscillator pairs. For example, take independent $[q_{in},p_{jm}]=i\delta_{ij}\delta_{nm}$ and sum $q_{in}\cos\omega_n(s-\epsilon)+p_{in}\sin\omega_n(s-\epsilon)$ with coefficients $\sqrt{4\kappa/[\pi(2n+1)]}$, $\omega_n=(2n+1)\pi/(1-\epsilon)$. The antiperiodic boundary choice realizes the bulk sign kernel in the parallel frame. It is a comparison boundary condition. The angular chart represents a single cell of positive solid angle. Define

$$
\widehat z_N^1=x+u\cdot H_N/s,\qquad
\widehat z_N^2=y+e^{-x}u_\perp\cdot H_N/s,\qquad
u_\perp=(-\sin\theta,\cos\theta).
$$

Insert both fields directly into the positive form of (4.22), with $\|e^{\widehat z^1_N}\partial_s\widehat z^2_N\psi\|^2$ for its second summand. The exponent contains the **fluctuating** first field. At each finite $N$ the sum of square norms on polynomial times Gaussian wavefunctions is densely defined and closable. To see closability, test the map into radial $L^2$ against smooth radial functions times polynomial Gaussians. The formal adjoints $\partial_s\widehat z^1_N$ and $(\partial_s\widehat z^2_N)e^{\widehat z^1_N}$ send these tests into integrable Hilbert-space vectors on the finite collar. Exponentiating a real linear quadrature sends a polynomial Gaussian to a displaced polynomial Gaussian, with bounds uniform on each compact coefficient set. The adjoint therefore has dense domain. Use the resulting closed positive focusing form for each cut, and cap its associated self-adjoint operator by spectral calculus. [Shear and clock orderings (4.22), (4.26)](https://arxiv.org/html/2611.34924v1#S4.E22) · [Cap prescription (C.11)](https://arxiv.org/html/2611.34924v1#A3.E11)

Choose a real $w\in C_c^\infty(I)$ of unit $L^2$ norm. Set $f=w\cos Ks$ and $g=w\sin Ks$. Then $\|f\|^2+\|g\|^2=1$ and $2\int f g'=K$. Let $J_N=s\partial_s\widehat z^1_N$. Its smeared commutator divided by $i$ is a scalar $c_N(f,g)$ for every $N$. At fixed $K$, $S_N\to\mathrm{sgn}$ in $L^2$ on the difference interval $(-(1-\epsilon),1-\epsilon)$. After integration by parts the test factors are $(f'+f/s)u(s)$ and $(g'+g/s)u(s)$. Thus the finite commutators converge to the contact plus regular kernel computed above, giving

$$\liminf_{N\to\infty}|c_N(f,g)|\ \ge\ \kappa(K-B_I/2).$$

On any normalized core vector the weak commutator bound gives

$$
|c_N(f,g)|\le 2\|J_N(f)\psi\|\|J_N(g)\psi\|
\le \int_I\|J_N(s)\psi\|^2\,ds
\le 4\,\Xi_N(v)[\psi],\qquad b\le v\le1.
$$

The last inequality uses $s^2\le s$ and positivity of the ordered curved-polarization square. Closure extends this lower bound to the full focusing form domain. The bound is uniform in the late cut $v$ and the state, including states that vary with $N$. First select any desired floor by taking $K$ large, then choose $N$ sufficiently large for these fixed test functions. It follows that $h_N=\inf_{b\le v\le1}\inf\sigma(\Xi_N(v))\to+\infty$. There is no exchange of high-frequency and cutoff limits in this argument.

A sharper bound gives the growth rate in this particular regulator. Write $L=1-\epsilon$, take $d=L/(4N)$, and use the finite-mode currents at $s$ and $t=s-d$. Their scalar commutator divided by $-i\kappa$ is

$$-S_N''(d)u(s)\cdot u(t)+S_N'(d)[u(s)\cdot B(t)-B(s)\cdot u(t)]+S_N(d)B(s)\cdot B(t).$$

At this separation $|S_N(d)|\le1$ by $|\sin x|\le |x|$, and $|S_N'(d)|\le4N/L$. On the fixed smooth background $B$ is bounded and $u(s)\cdot u(s-d)\to1$ uniformly on $I$. The leading term follows from a Riemann sum,

$$\frac{-S_N''(d)}{N^2}=\frac{4\pi}{L^2 N}\sum_{n=0}^{N-1}\frac{2n+1}{N}\sin\!\left(\frac{(2n+1)\pi}{4N}\right)\ \longrightarrow\ \frac{4\pi}{L^2}\int_0^1 2x\sin(\pi x/2)\,dx=\frac{32}{\pi L^2}.$$

Integrate the point-pair uncertainty inequality over $t\in(a,b-d)$. The sum of the two pointwise squared current norms integrates to at most $2\int_I\|J_N(t)\psi\|^2dt\le8\Xi_N(v)[\psi]$. For every fixed smooth two-polarization background this proves the state-independent bound

$$\boxed{\displaystyle \liminf_{N\to\infty}\frac{h_N}{N^2}\ \ge\ \frac{4\kappa |I|}{\pi(1-\epsilon)^2}.}$$

The coefficient does not depend on the chosen background. The resolution at which it is approached can depend on that background. The wave-packet argument above uses only fixed test functions and thus gives a criterion for other regulators without presupposing agreement at separations of one cutoff wavelength.

For a frozen corner let $m>0$ be the area of this cell and $a_0=\int_S\varrho_S\,d\Omega$. Other cells may have any positive focusing forms. Retaining the chosen cell and only its late cuts in (4.26) gives the **spectral floor of the clock**

$$T_{N,R}\ \ge\ (1-b)\,\frac m{a_0}\exp(\min\{h_N,R\})\,1.$$

This uses the scalar spectral floor of each individual focusing operator. Different cuts and polarizations may fail to commute. For every finite $\ell$ the projector $\mathbf 1_{[0,\ell]}(T_{N,R})$ is exactly zero once $N,R$ are sufficiently large, independently of their relative rates. The conclusion applies to the vacuum and every other state. No limit of oscillator vacuum means or identification of Hilbert spaces at different cutoffs is needed. The comparison quantizes a **frozen tangent symplectic form** while keeping the nonlinear observable. It supplies no embedding or nonlinear Dirac representation for the gravitational Hilbert space. [Finite-reading claim (5.19)](https://arxiv.org/html/2611.34924v1#S5.E19)

## A criterion for the interacting clock

On the actual regulated space set $E_{2,I}[\psi]=\int_I\|e^{\widehat z^1}\partial_s\widehat z^2\psi\|^2ds$. A sufficient hypothesis is that the weak commutator $\mathcal C_\psi(f,g)=2\,\mathrm{Im}\langle J(f)\psi,J(g)\psi\rangle$ on a common core of the bare form obeys, up to orientation,

$$
\left|\mathcal C_\psi(f,g)-2\kappa\int f g'\,\|\psi\|^2\right|
\le \|f\|\|g\|\,[\beta\|\psi\|^2+\gamma E_{2,I}[\psi]]+o_N(1)\|\psi\|^2.
$$

Here $\kappa>0$, $\beta,\gamma\ge0$ are independent of the cutoff, tests and state. The last error may depend on fixed tests but is uniform in the core vector. The classically computed remainder has precisely this energy dependence. For normalized states $E_{2,I}\le4\Xi_N(v)/a$. The same paired tests therefore imply

$$ (4+2\gamma/a)\,\Xi_N(v)[\psi]\ \ge\ \kappa K-\beta/2-o_N(1),\qquad b\le v\le1.$$

For a fluctuating corner one must also transfer a floor to the sandwich in (4.26). For example, if the bound is uniform on cells carrying $\int_{\rm good}\widehat\varrho_S^2d\Omega\ge m_0\,1$ with $m_0>0$ uniformly in the cutoff, the previous inequality for the clock holds with $m/a_0$ replaced by $m_0/\sqrt{4\pi\mathscr A}$. This follows by sandwiching each *scalar* focusing floor and using $\widehat a\le\sqrt{4\pi\mathscr A}\,1$ from (4.25). It does not require density and shear to commute. A positive solid angle alone does not guarantee the required operator mass for a fluctuating corner. [Area normalization and sandwich (4.25)–(4.26)](https://arxiv.org/html/2611.34924v1#S4.E25)

Establishing the quantum commutator estimate at fixed nonzero $G_N$, including cut contributions and local angular regulation, would decide against finite readings for this bare prescription under the stated mass hypothesis. A modified contact term, an error growing with wave number at bounded focusing energy, or a renormalized shear that no longer dominates the bare current norm would invalidate the inference. The published classical Dirac kernel and the order-by-order Weyl expansion do not decide these alternatives. This is a proof gap for the interacting vacuum and a negative result for the specified comparison model. [Coupled constraints (A.37)–(A.42)](https://arxiv.org/html/2611.34924v1#A1.E38) · [Weyl expansion (C.9)–(C.10)](https://arxiv.org/html/2611.34924v1#A3.E10)

## Numerical check

Run `python3 checks/clock_spectrum.py` or the repository suite `make check`. For $\kappa=1$, $\epsilon=0.2$, $I=(0.3,0.7)$ and $\theta'=3$, the script independently integrates the 48-mode coordinate bracket and the differentiated continuum kernel. One possible profile is $x=s$, $y=-3e^{-s}$. It uses a compactly supported $C^3$ sine-power test window, sufficient for the integration by parts. The last column in the first table is the analytic lower bound on the limiting focusing floor from that test. The second calculation integrates the finite-mode current-pair bound at separation $d$ and compares its coefficient with the analytic large-$N$ value. [Executable check](../checks/clock_spectrum.py)

```text
K    finite bracket   contact minus remainder   limit floor for Xi
 32      32.5093851               32.5093838           7.3119048
 64      64.2125573               64.2125546          15.3119048
128     128.1031805              128.1031751          31.3119048
Shifted-current floor divided by N^2; predicted limit 0.7957747
  16  0.7739199
  64  0.7897507
 256  0.7942326
1024  0.7953869
```
