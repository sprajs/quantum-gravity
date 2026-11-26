# Graviton pair correlator on one incoming null cone

**Physical question.** Does the paper's graviton-pair amplitude on a single incoming null cone really converge at every positive Newton constant while its small-$G_N$ expansion breaks down logarithmically at third order—and what physical assumptions generate that logarithm?

**Outcome.** Every algebraic step of (4.32)–(4.34) reproduces exactly for the paper's Gaussian state and source, and direct numerical evaluation confirms both the exact dilogarithm sum and its analytic tail bounds (within $2.50\times 10^{-12}$ at $x=0.1$ and $N=100{,}000$). The claimed imaginary $i x^3\log x$ singularity—along with a real one-sided $-\pi x^3/2$ term that finite-cutoff expansion also misses—genuinely reflects the failure to interchange the ultraviolet mode-cutoff limit $N\to\infty$ with the weak-coupling expansion $x\downarrow 0$. Crucially, however, this example projects onto a single angular harmonic and polarization in a free Gaussian state whose source displacement shrinks proportionally to $G_N$; it tests the short-distance response of a chosen boundary source rather than bulk interacting graviton scattering. [Paper, §4.4, pp. 33–34](https://arxiv.org/pdf/2611.34924v1#page=33)

## Contraction and exact result

At fixed corner area $\mathscr A$, define the dimensionless coupling $x=1/s=4G_N\hbar/\mathscr A$ and mode variances $v_k=(\Delta q_k)^2=x/(2k)$. With zero means, equation (4.9) writes $q_k=\sqrt{v_k}(a_k+a_k^\dagger)$, so acting twice on the product Gaussian vacuum $\Omega$ yields

$$
q_k^2|\Omega\rangle=v_k|\Omega\rangle+\sqrt{2}\,v_k|2_k\rangle .
$$

Passing to the connected correlator subtracts the vacuum expectation $v_k|\Omega\rangle$. Because two-particle states in distinct modes are orthogonal and the unitary $U_N$ in (4.32) acts on $|2_k\rangle$ with phase $e^{-2ikx}$, the centered source $O_N=\sum_{k=1}^N(q_k^2-v_k)$ produces

$$
A_N(x)=\langle O_N\Omega|U_N|O_N\Omega\rangle
=2\sum_{k=1}^N v_k^2e^{-2ikx}
=\frac{x^2}{2}\sum_{k=1}^N\frac{e^{-2ikx}}{k^2}.
$$

Recognizing the dilogarithm series gives the exact continuum limit $A(x)=\frac{x^2}{2}\operatorname{Li}_2(e^{-2ix})$, with the radial limit $\operatorname{Li}_2(1)=\pi^2/6$ at coincident phases. Notice the role of centering: the squared norm of the centered vector $O_N\Omega$ converges to $\pi^2 x^2/12$, whereas the uncentered vacuum expectation grows logarithmically as $xH_N/2$, so subtracting the disconnected mean is essential before sending $N\to\infty$.

Comparing the tail with the integral of $k^{-2}$ gives the universal bound $|A-A_N|\le x^2/(2N)$, which guarantees absolute convergence even at zero source displacement. Away from $x\in\pi\mathbb Z$, summation by parts together with the geometric-series bound $|\sum_{j=m}^{n} e^{-2ijx}|\le 1/|\sin x|$ improves this to the sharper oscillatory bound $x^2/[2|\sin x|(N+1)^2]$.

## What goes wrong when the phase is expanded first

Expanding the exponential in $x$ while holding the mode cutoff $N$ fixed yields

$$
A_N(x)=\frac{x^2}{2}\sum_{k=1}^{N}k^{-2}-ix^3 H_N+O_N(x^4),
\qquad H_N=\log N+\gamma+O(N^{-1}),
$$

reproducing (4.34). The amplitude itself vanishes in both iterated limits ($N\to\infty$ then $x\downarrow 0$, or vice versa); the non-interchange strikes at the cubic Taylor coefficient because high modes with $kx\sim 1$ oscillate by $O(1)$ radians and block a uniform small-$x$ expansion as $N$ grows.

To extract the true small-$x$ asymptotics independently of the series, differentiate $\operatorname{Li}_2(e^{-i\theta})$ via its radial limit from inside the unit disk. For $0<\theta<2\pi$,

$$
\frac{d}{d\theta}\operatorname{Li}_2(e^{-i\theta})
=i\log(1-e^{-i\theta})
=-\frac{\pi-\theta}{2}+i\log\bigl(2\sin(\theta/2)\bigr).
$$

Integrating from $\theta=0$ gives the exact real part $\pi^2/6-\pi\theta/2+\theta^2/4$, while expanding $\log(2\sin(\theta/2))=\log\theta-\theta^2/24+O(\theta^4)$ and setting $\theta=2x$ yields, as $x\downarrow 0$,

$$
A(x)=\frac{\pi^2 x^2}{12}-\frac{\pi x^3}{2}+\frac{x^4}{2}
     +i x^3[\log(2x)-1]-\frac{i x^5}{18}+O(x^7).
$$

In terms of $s=1/x$, the leading imaginary nonanalyticity is $ix^3\log x=-i\log s/s^3$, and $\operatorname{Im}(d^3A/dx^3)=6\log(2x)+5+O(x^2)\to-\infty$ as $x\downarrow 0$ (derivatives with respect to $G_N$ pick up the constant factor $(4\hbar/\mathscr A)^3$ at third order). Expanding before removing the cutoff also misses the one-sided **real** cubic term $-\pi x^3/2$: at any finite $N$, the real part is even in $x$ and has identically zero cubic Taylor coefficient.

## Numerical reproduction

Run `python checks/pair.py` from the repository root using Python 3 ([checks/pair.py](../checks/pair.py)). The script checks the oscillator matrix element, evaluates the direct partial sum $A_N(x)$, and compares it against the exact real part and a numerical quadrature for the imaginary part (with the $\log\theta$ endpoint singularity subtracted out so the integrand is smooth). Representative results at $N=100{,}000$ match inside the tighter of the two analytic tail bounds:

| $x$ | $\Re A$ | $\Im A$ | $\lvert A_N-A\rvert$ | Tail bound |
|---:|---:|---:|---:|---:|
| 0.01 | 0.00008068091 | −0.000004912029 | $2.50\times10^{-13}$ | $5.00\times10^{-13}$ |
| 0.1 | 0.006703874 | −0.002609994 | $2.50\times10^{-12}$ | $5.01\times10^{-12}$ |
| 1 | −0.2483293 | −0.3635730 | $2.97\times10^{-11}$ | $5.94\times10^{-11}$ |
| $\pi$ | 8.117424 | 0 | $4.93478\times10^{-5}$ | $4.93481\times10^{-5}$ |

At $x=\pi$, the phases $e^{-2ik\pi}=1$ align constructively, leaving the larger $O(1/N)$ tail. The harmonic cutoff coefficients $H_N$ at $N=10,100,1000,10000$ are $2.928968$, $5.187378$, $7.485471$, and $9.787606$. For the continuum sum, the scaled imaginary residual $[\Im A/x^3-\log(2x)+1]/x^2$ moves from $-0.05562520$ at $x=0.25$ to $-0.05555567$ at $x=0.01$, converging cleanly to the analytic coefficient $-1/18$.

## Physical scope

Equation (4.32) specifies both the Gaussian mode variances $x/(2k)$ and the coupling-dependent affine displacement $x/\omega_1$. Holding an independent displacement fixed instead would make the entire correlator exactly proportional to $G_N^2$ at fixed area. The cubic logarithm therefore measures the short-distance response of this chosen family of boundary sources as their separation shrinks with $G_N$, while the $k^{-2}$ falloff of Gaussian pair amplitudes already secures absolute convergence at zero displacement. Connecting this boundary calculation to an interacting bulk graviton scattering amplitude—summing over all transverse modes and tracking gravitational counterterms—would require separate calculations; the manuscript introduces the two-loop scattering divergence as motivation for the example rather than computing it here. [Paper, §4.4, pp. 33–34 and footnote 17](https://arxiv.org/pdf/2611.34924v1#page=33)
