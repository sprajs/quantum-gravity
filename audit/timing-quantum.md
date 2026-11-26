# Two finite-duration readings of a spherical quantum clock

In the free Minkowski graviton vacuum the variance of a calibrated spherical clock response increases by $\hbar G_N\log 2/(30\pi)$ per halving of the detector duration in the short-duration limit. Two detectors centered on the same proper time can retain a finite variance in their difference and a finite commutator, even when their timing variances agree. These statements concern the linear observable $L_t=d^2 D_{\mathrm{flat}}(W,\cdot)$ for a specified reference wave and ambient radiative representation. The matched-radius excess $D$ itself has vanishing first variation on the flat preparation. Its nonlinear quantum operator in an isolated diamond remains a separate construction. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Spherical Hessian](joint-flat-hessian.md)

## The proper-time average in Fock space

Use the unit-waist diamond, cap ratio $a=1/3$, the even quadrupole $S=\mathrm{diag}(-1/2,-1/2,1)$, unit rim slope $G'_W(a)=1$, and $\int_a^1(s^{-1}-1)G'_W(s)\,ds=0$. Translate the entire marked experiment, including the reference, by the emitter's proper time $t$. Its first-slot response master translates by $t/2$. In the full-line master coordinate $s$ let $z=f_X^{(4)}$, where $X$ represents $L_0$ distributionally. The compact, piecewise smooth $z$ has a single jump $d=-16G_N(1-a)$ at $a$. Its derivative $m=z'$ is a finite measure with zero total mass. The residual vertex and waist contributions are included in its piecewise smooth density. With $A=3/(5120G_N)$ and master wavenumber $k>0$ set
$$
 S(k)=\frac{A}{\pi}|\widehat m(k)|^2,\qquad C=\frac{Ad^2}{\pi}=\frac{G_N}{15\pi}.
$$
Here $\widehat m(k)=\int e^{-iks}\,dm(s)$. Compact support and zero total mass give $S(k)=O(k^2)$ near zero. Integration by parts on the smooth pieces gives $\widehat m(k)=d e^{-ika}+O(1/k)$ and $S(k)=C+O(1/k)$ at high frequency. This use of $z'$ removes the affine tails allowed for $f_X$. [Einstein normalization and vertex data](weak-normalization.md) · [Minkowski norm](weak-fock.md) · [Translated response and chosen reference](weak-clock-contact.md)

Let $w$ be a real Schwartz timing profile of integral one, with $w_h(t)=h^{-1}w(t/h)$ for $h>0$. Nonnegative profiles describe detector weights. Write $X_{w,h}$ for the response to $\int w_h(t)L_t\,dt$. The translation law supplies the multiplier $\widehat w(u)$ at $u=hk/2$. For profiles $p,q$ at this common scale the ordered **vacuum two-point function** of the centered linear fields is
$$
 \langle \widehat L_{p,h}\widehat L_{q,h}\rangle_0
   =\frac{\hbar}{2}\int_0^\infty S(k)\,
       \widehat p(hk/2)\overline{\widehat q(hk/2)}\,\frac{dk}{k}.       \tag{1}
$$
Its real part is the symmetric covariance. If $B_h=\{L_{p,h},L_{q,h}\}$, its imaginary part is $\hbar B_h/2$. The order of the Fourier factors gives a positive sine for a later second reading. The integral converges at both ends for every $h>0$. In this regular Fock representation the fields are Segal fields on their common finite-particle core. Their exponentials $U_{w,h}(\lambda)=\exp(i\lambda\widehat L_{w,h})$ are bounded unitaries and satisfy the Weyl relation. [Bracket convention](weak-clock-contact.md) · [Chandrasekaran, Eq. (4.20)](https://arxiv.org/html/2611.34924v1#S4.E20)

Write $\mu(X_{w,h})=2\operatorname{Var}_0(\widehat L_{w,h})/\hbar$. For a fixed positive master reference frequency $\kappa$,
$$
 \mu(X_{w,h})=C\log\frac{2}{\kappa h}+O(1),\qquad
 \lim_{h\downarrow0}\big[\mu(X_{w,h/2})-\mu(X_{w,h})\big]= C\log 2 .     \tag{2}
$$
For the logarithm split $S=C+(S-C)$ above $\kappa$. The second term is integrable in $dk/k$, and the first acquires its fixed lower limit $\kappa h/2$ after rescaling. For the increment, $[|\widehat w(u/2)|^2-|\widehat w(u)|^2]/u$ is integrable. Its integral is $\log 2$ by cancellation of the two rescaled integrals, using $\widehat w(0)=1$. Boundedness of $S$ permits dominated convergence. The vacuum standard deviation consequently grows as $\sqrt{(\hbar C/2)\log(2/(\kappa h))}$.

Equation (1) also defines a stationary two-point distribution in the relative proper time $\tau$ on the whole line. Its unsmeared kernel at distinct sufficiently close times is the Abel boundary value of $(\hbar/2)\int_0^\infty S(k)e^{ik\tau/2}\,dk/k$. Split off $C(1-e^{-k/\kappa})$ from $S$. The difference divided by $k$ is integrable, with a continuous Fourier transform real at zero. For a damping factor $e^{-\varepsilon k}$ the part split off integrates to $C\log[(\varepsilon+1/\kappa-i\tau/2)/(\varepsilon-i\tau/2)]$ before multiplication by $\hbar/2$. Thus, for a real constant $K_\kappa$,
$$
 \langle\widehat L_0\widehat L_\tau\rangle_0
 =\frac{\hbar C}{2}\left(\log\frac{2}{\kappa|\tau|}
           +\frac{i\pi}{2}\operatorname{sgn}\tau\right)+K_\kappa+o(1).
$$
This equation describes a kernel acting on timing tests. Its real logarithm and imaginary step are locally integrable.

## Difference, commutator and ordered product

Taking the real variance of the difference and the imaginary part of the ordered product in (1) gives
$$
 \begin{aligned}
 D_{pq}&=\lim_{h\downarrow0}\mu(X_{p,h}-X_{q,h})
       =C\int_0^\infty |\widehat p(u)-\widehat q(u)|^2\frac{du}{u},\\
 B_*&=\lim_{h\downarrow0} B_h
       =C\int_0^\infty\operatorname{Im}\!\left[\widehat p(u)\overline{\widehat q(u)}\right]\frac{du}{u}.
 \end{aligned}                                                        \tag{3}
$$
The difference vanishes at zero frequency, and the imaginary part vanishes there as well. Both weights are integrable in $du/u$, so (3) follows by rescaling and dominated convergence. Distinct profiles give $D_{pq}>0$. The variance of the observable difference is $\hbar D_{pq}/2$ in the limit. The sine integral also gives $B_*=(\pi C/2)\int p(t)q(t')\operatorname{sgn}(t'-t)\,dt\,dt'$. To see this, insert $e^{-\varepsilon u}$ before interchanging integrals, then use $\arctan[(t'-t)/\varepsilon]$ and bounded convergence. The compact equal-moment profiles of the classical experiment have ordering bias $-1/5$, giving $B_*=-G_N/150$. For identical profiles the difference and the bracket vanish at every width. [Compact timing profiles](weak-clock-contact.md)

The durations can differ as well. For centered Gaussian detectors of rms durations $h$ and $rh$ with fixed $r>0$, both multipliers are real, so $B_h=0$ at every width. The limiting difference norm is $C\log[(1+r^2)/(2r)]$, obtained from (3) by integrating $(e^{-u^2/2}-e^{-r^2u^2/2})^2/u$. For example, doubling the duration leaves $C\log(5/4)$ even though both detectors approach the same time.

One can read off the phase from four bounded operators at finite width,
$$
 U_{p,h}(\lambda)U_{q,h}(\nu)U_{p,h}(-\lambda)U_{q,h}(-\nu)
       =e^{-i\hbar\lambda\nu B_h}I .
$$
For the compact profiles this converges in operator norm to $e^{+i\hbar\lambda\nu G_N/150}I$. The phase depends on the order of the two source operations. To observe this scalar phase interferometrically requires a coherent reference branch against which to compare the loop. A single fixed profile has zero commutator with itself.

Each individual $U_{w,h}(\lambda)$ for $\lambda\ne0$ converges weakly to zero as $h\downarrow0$. Indeed its vacuum expectation is $\exp[-\hbar\lambda^2\mu(X_{w,h})/4]$. A matrix element between two fixed coherent states has the same Gaussian modulus with a fixed displacement added to $\lambda X_{w,h}$. This shifted norm still diverges. Coherent vectors span a dense subspace and the operators have norm one, proving weak convergence. Since each operator preserves vector norms, the family has no strong limit. In particular these smearings cannot converge in strong resolvent sense to a self-adjoint sharp reading, which would entail strong convergence of its unitary group at each fixed coupling.

For two readings with opposite couplings the common divergence cancels. The Weyl product has the weak operator limit
$$
 U_{p,h}(\lambda)U_{q,h}(-\lambda)
  \ \rightharpoonup\
  \exp\!\left(\frac{i\hbar\lambda^2 B_*}{2}
             -\frac{\hbar\lambda^2 D_{pq}}{4}\right) I.                   \tag{4}
$$
In fact $X_{p,h}-X_{q,h}$ tends weakly to zero in one-particle space. Its norm tends to $\sqrt{D_{pq}}$, and its norm restricted to each bounded frequency interval tends to zero. Approximation by bounded-frequency vectors proves the weak assertion. Evaluating the Weyl relation between fixed coherent vectors now gives (4). For $p\ne q$ and $\lambda\ne0$ the limiting modulus is strictly below one, so this two-operator product also has no strong limit. Formula (4) describes the vacuum representation and fixed detector shapes sharpened at a common rate. A sharp operator in another representation, or convergence of a nonlinear gravitational clock with extra degrees of freedom, would require a new argument.

## An equal-variance pair with analytic coefficients

For an independent frequency-space test, let $g(t)=e^{-t^2/2}/\sqrt{2\pi}$, $H_3=t^3-3t$ and
$$
 p_\pm(t)=\frac35 g(t)\big(1\pm H_3(t)/3\big)^2 .
$$
These nonnegative Schwartz profiles both have unit mass, zero mean and variance $17/5$, so their physical standard duration is $h\sqrt{17/5}$. The Gaussian moments or Hermite orthogonality give these three values. Their Fourier transforms are
$$
 \widehat p_\pm(u)=\tfrac35 e^{-u^2/2}
  \left[1+\tfrac19(6-18u^2+9u^4-u^6)\ \pm\tfrac{2i}3u^3\right].
$$
Substitution into (3) gives $D_{+-}/C=16/25$ and $B_*/C=23\sqrt\pi/200$ for the order $(+,-)$. The opposite order reverses the phase. This example uses integrable detector tails and the whole Minkowski continuation. The compact example above yields the same qualitative distinction using finite supports.

Run `python3 -B checks/timing_quantum.py` from the repository root. The check constructs the full piecewise response from the optical Hessian, Fourier-transforms its derivative by the polynomial endpoint formula, checks the moments and ordering bias separately in the time domain, and integrates the three frequency weights numerically with $G_N=1$. At $h=10^{-9}$ expect `one-particle octave 0.014709040, relative norm squared 0.013581222, bracket 0.004325453`. It repeats the final quadrature at twice the density. Run `make check` for the full suite. [Executable check](../checks/timing_quantum.py)
