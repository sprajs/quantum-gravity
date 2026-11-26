# What can a relative boost tell us about the area spectrum?

Venkatesa Chandrasekaran’s null-cone proposal identifies the generator of a relative boost at a corner with its area. This gives a test of candidate area spectra. A particular evenly spaced spectrum would restore the initial shear correlation at rapidity two. The local graviton vacuum instead retains about 42% of the initial correlation. A second finite spectrum constructed below follows the vacuum curve to within 0.046% over the entire rapidity interval from $-3$ to $3$. The distinction depends on which areas participate and how the shear couples to them. The manuscript gives neither a list of levels nor their transition strengths. [Chandrasekaran, arXiv:2611.34924v1, §§5.1–5.2](https://arxiv.org/html/2611.34924v1#S5.SS2)

## What is boosted and what is measured?

Hold the left boundary frame and its shear insertion fixed. Change the right frame by rapidity $\eta$, using the same right packet in that frame at every setting. In units $c=1$, let $\ell_P^2=G_N\hbar$ and $s=\mathscr A/(4\ell_P^2)$. The right boost is $U_\eta=\exp(i\eta\hat s/(2\pi))$. Suppose the state on the boosted leg is supported in a common clock-selected sector preserved by this unitary, and the readout and preparation are fixed as $\eta$ varies. Any one fixed expectation in that experiment then has the form

$$
C(\eta)=\sum_{a,b}c_{ab}\exp[i\eta(s_a-s_b)/(2\pi)]
$$

when there are finitely many distinct supported areas. This follows by inserting the area spectral projections on both sides of the observable. The coefficients combine all states with the same two areas. Degeneracies change the coefficients, and selection rules can make some coefficients vanish. The bound applies to the spectrum during the boost. Projecting only at the start and end of an operation that leaves the sector during the boost would require a new derivation. The paper’s paired-cut state in (D.22) and its transformation in (D.23) provide the relevant placement of the boost. One can take the bounded two-source sine readout in (5.33) or its mixed derivative at zero sources, if the smeared second moments exist. Below $C$ is the full symmetrized two-point function with zero semiclassical one-point means and $R=C(\eta)/C(0)$, with $C(0)\ne0$. [Boost and preparation](https://arxiv.org/html/2611.34924v1#S5.E22) · [Sine readout](https://arxiv.org/html/2611.34924v1#S5.E33) · [Paired state](https://arxiv.org/html/2611.34924v1#A4.E22)

Use the paper’s freely falling, shear-free local vacuum, with reflection-matched transverse polarizations. Let the absolute affine distances from the corner be $da,db'$ with $a=1+wx$, $b'=1+wy$, where $d>0$, $w=\Delta u/d<1$, and $x,y$ are independently integrated with the same normalized even test function $p$ on $(-1,1)$. Take $p(x)\propto\exp[-1/(1-x^2)]$ there, extended smoothly by zero. The two packets have disjoint supports. Boosting the right shear multiplies it by $e^\eta$ and takes its argument to $e^\eta db'$. Thus, with $z=e^\eta$,

$$
K_w(\eta)=4z\iint\frac{p(x)p(y)}{(a+zb')^2}\,dx\,dy,\qquad
C_{\rm vac}(\eta)=-\frac{c_\perp}{4d^2}K_w(\eta),\qquad
R_w(\eta)=\frac{K_w(\eta)}{K_w(0)} .
$$

Reflection makes $R_w$ even. The zero-width limit is $R_0(\eta)=4z/(1+z)^2=\operatorname{sech}^2(\eta/2)$. For the window $|\eta|\le H$, the shortest right packet has half-width $e^{-H}\Delta u$ and the most distant point is $e^H(d+\Delta u)$. The smooth-background comparison requires $\ell_P\ll e^{-H}\Delta u$, $\Delta u\ll d$, and $e^H(d+\Delta u)\ll b\ll R_c$, where $b$ is the corner radius and $R_c$ the curvature radius. For example, $w=0.01$, $d=10^{-5}b$, $b=10^{12}\ell_P$, and $R_c=10^3b$ leave a minimum half-width of about $4{,}979\,\ell_P$ and a maximum distance of $0.000203b$ at $H=3$. These ratios allow the leading calculation. Bounds on the actual state-dependent and higher-order errors are a separate input to any exclusion. [Hierarchy and boosted kernel, (5.26)–(5.29)](https://arxiv.org/html/2611.34924v1#S5.E26) · [Local normalization and bounded response](https://arxiv.org/html/2611.34924v1#A4.E19)

## Two spectra the samples can exclude

**An evenly spaced set of active areas.** If all occupied $s_a$ belong to $s_0+\Delta s\,\mathbb Z$, every boost phase agrees at $\eta_{\rm rec}=4\pi^2/\Delta s$. All fixed readouts return to their initial expectation there. For example, $\Delta s=2\pi^2$, corresponding to area steps $8\pi^2\ell_P^2$, gives $\eta_{\rm rec}=2$. The integral above at $w=0.01$ gives $R_w(2)=0.419980119$. A measurement agreeing with this prediction and with total absolute uncertainty smaller than the $0.580019881$ separation would exclude this exact lattice under the stated protocol. The spacing is chosen for the example. An incommensurate set generally has only approximate returns. Its return scale depends on the levels and the required tolerance. Even an exactly periodic lattice can have its first guaranteed return beyond the local geometric window.

**Any spectrum containing at most two distinct active areas.** Such a system has at most three distinct signed difference frequencies, including zero. Form the four-by-four matrix $T_{jk}=R(j-k)$ for $0\le j,k\le3$. Each exponential in $R$ contributes a rank-one matrix. Thus $T$ has rank at most three for arbitrary amplitudes, with no positivity or lattice assumption. The smooth packets above give

| $\lvert\eta\rvert$ | 0 | 1 | 2 | 3 |
| --- | ---: | ---: | ---: | ---: |
| $R_w(\eta)$ | 1 | 0.786451716 | 0.419980119 | 0.180710150 |

The reference $T$ has smallest eigenvalue $0.04099069$. If every nonzero-lag sample differs by at most $\delta$, the error matrix has operator norm at most $3\delta$, since its diagonal vanishes and its row and column sums of absolute errors are at most $3\delta$. A singular matrix must therefore differ from the reference by at least $0.01366356$ at some measured lag. Measurements at both signs allow a candidate with asymmetric response. An independently established reflection symmetry reduces the required settings to four. The error budget includes normalization error, experimental error, and the accuracy of the benchmark if it supplies the data. This witness would establish at least three distinct active areas. Arbitrary multiplicity at a single area cannot imitate the missing frequencies.

## How closely a larger finite spectrum can fit

Fourier transformation of the point kernel gives $R_0(\eta)=\int_0^\infty q(\nu)\cos(\nu\eta)\,d\nu$ with $q(\nu)=4\nu/\sinh(\pi\nu)$. For the reflected packets one can rewrite the integrand of $K_w$ as $R_0(\eta+\log(b'/a))/(ab')$. Consequently the normalized positive density for $R_w$ is

$$
q_w(\nu)=\frac{q(\nu)}{K_w(0)}
  \left|\int p(x)(1+wx)^{-1+i\nu}\,dx\right|^2 .
$$

This positivity uses the matched profiles and the freely falling vacuum. A general two-sided cross-correlation can have signed or complex coefficients. [Fourier transform of the same affine kernel](05-4.md)

Place nodes at $\nu_k=0.02k$ for $0\le k\le250$. On each cell divide the probability mass between its two adjacent nodes using linear interpolation weights. Assign the tail above $\nu=5$ to node zero. The resulting positive weights give a sum of 251 cosines. It can be realized by a finite boost generator with $s_k=s_0+2\pi\nu_k$, provided the allowed area band contains these levels (width $10\pi$). For example, take a reflected pair $\sum_k t_k|k,k^*\rangle$ with normalized, positive real $t_k$. For the same real symmetric matrix $X$ on both sides, the pair correlation gives a cosine weight $2t_0t_k |X_{0k}|^2$ for $k>0$ and a constant $t_0^2 |X_{00}|^2$ when the other entries vanish. Choose those matrix elements to obtain the prescribed weights. Overall rescaling makes $X$ bounded by one while preserving the normalized ratio. This constructs a spectral fit to this one measurement. A gravitational model must also derive the matrix elements and satisfy the other constraints.

Linear interpolation of $\cos(\eta\nu)$ on a cell of width $h$ incurs at most $\eta^2 h^2/8$. Moving the tail costs at most twice its probability. Since $K_w(0)\ge1$ by convexity and the squared packet factor is at most $(1-w)^{-2}$, that probability for $\nu>L$ is bounded by

$$
\frac{8e^{-\pi L}(L/\pi+1/\pi^2)}
     {(1-w)^2(1-e^{-2\pi L})}.
$$

At $L=5$ the uniform error on $|\eta|\le3$ is below $0.000455$. The model has an exact return at $\eta=2\pi/0.02\simeq314.16$. The required factor $e^{314.16}$ in affine scale lies far beyond the example’s window. The analytic bound uses the integral-defined weights. The script evaluates them by numerical quadrature. More generally, for a positive measure on a compact frequency band, $m$ exact real cosine samples form a point of the convex hull of $\nu\mapsto(\cos(\eta_1\nu),\ldots,\cos(\eta_m\nu))$. At most $m+1$ atoms suffice to give those same samples, by the finite-dimensional convex hull theorem. Finite samples can constrain a specified band or number of levels. They cannot distinguish *every* such continuous measure from *every* unrestricted finite atomic one. The semiclassical density extends to infinite frequency; the explicit tail bound quantifies the truncation needed in the example.

## An inequality and a measurement limit

For a bounded readout $O$ on the paired state, centering the boost at the mean area and using $|e^{it}-1|\le|t|$ gives $|\langle O\rangle_\eta-\langle O\rangle_0|\le\|O\|\,|\eta|\operatorname{sd}(s)/\pi$. A measured **absolute** change bounds the area spread from below, for continuous and discrete spectra alike. A normalized shear ratio alone gives no such lower bound on the spread without a readout norm or additional information on the transition weights. [Equation (5.32)](https://arxiv.org/html/2611.34924v1#S5.E32)

The normalized contrast also differs from the signal size in a single preparation. In the ideal linearized vacuum the variance of either affine-smeared shear is $V=c_\perp I_p/\Delta u^2$, with $I_p=\int_0^\infty k|\widehat p(k)|^2dk$ and $\widehat p(k)=\int p(x)e^{ikx}dx$. Since $p$ is nonnegative, even and supported on $[-1,1]$, $\widehat p(k)\ge\cos k$ for $0\le k\le\pi/2$, so $I_p\ge\pi^2/16-1/4$. Also $K_w(0)\le(1-w)^{-2}$. Hence at $w=0.01$ the absolute single-pair correlation coefficient $|C(0)|/V$ is at most $6.96\times10^{-5}$. Even estimating the difference of the two covariances as the difference of sample means of shear products, from $N$ independent Gaussian pairs **per setting**, has variance at least $2V^2/N$ by Wick contraction. A signal-to-noise ratio of one for the example’s $0.58002|C(0)|$ change needs over $1.2\times10^9$ ideal pairs per setting by this bound alone. This estimates one simple protocol with no readout noise. It gives no sensitivity limit for other protocols. No apparatus, repeatable preparation, noise floor or derived area spacing in v1 establishes a feasible experiment. [Vacuum shear spectral measure](https://arxiv.org/html/2611.34924v1#A4.E19)

Run `python3 checks/boost_observable.py` from the repository root. It checks the smeared ratios, the smallest-eigenvalue bound, positivity of the finite weights, and their agreement with the reference at 61 nonnegative rapidities. Expected outputs include the two-area discrepancy bound `0.013663563`, the 251-area sampled maximum error `0.00005810`, and the uniform analytic bound `0.000454165`. [Executable check](../checks/boost_observable.py)
