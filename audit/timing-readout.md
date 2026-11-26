# Reading two spherical clocks with one quantum meter

Two finite-width linear readings of the spherical clock can be recorded jointly in the free Minkowski graviton theory. If their classical bracket is $B_h$, a Gaussian meter with unit gain, equal added variances and zero symmetrized noise covariance can attain $\hbar |B_h|/2$ of added variance in each channel. The timing windows determine $B_h$. The state of the incident field supplies a second contribution to the observed spread. These results use the mixed derivative of Chandrasekaran's affine clock on a flat diamond and give an ideal measurement in that model. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Flat clock Hessian](joint-flat-hessian.md)

## What the meter measures

Set the waist radius to one and the cap ratio to $a=1/3$. Translate the emitter, marks and smooth reference quadrupole $W$ together through proper time $t$ on the common Minkowski continuation. Let $L_t=d^2D_{\rm flat}(W_t,\cdot)$ denote the resulting translated linear response of the matched-radius clock excess. In the radiative Fock representation, averaging this response against each of two real, smooth, rapidly decreasing unit-mass profiles of width $h>0$ gives self-adjoint Segal fields $R_1,R_2$. The same construction permits different reference quadrupoles in the two slots. Write $\kappa_h=\hbar B_h$. The two fields obey the Weyl relations with $[R_1,R_2]=i\kappa_h I$ on their finite-particle core. [Finite-duration quantum responses](timing-quantum.md) · [Two optical preparations](timing-two-clocks.md)

Take $\kappa_h\ne0$. Prepare an independent oscillator with $Q=x$, $P=-i\partial_x$, and normalized wavefunction $\psi_v(x)=(2\pi v)^{-1/4}\exp[-x^2/(4v)]$, where $v>0$. On field and oscillator together read the two pointers
$$
 M_1=R_1\otimes I+I\otimes Q,\qquad
 M_2=R_2\otimes I-I\otimes\kappa_h P .                              \tag{1}
$$
The field and oscillator Weyl phases cancel for every pair of real couplings. The pointer unitary groups therefore commute, giving a joint spectral measure $P_M$ for their two real outcomes. With $V\phi=\phi\otimes\psi_v$, the field's positive operator-valued measure (POVM) is $E(S)=V^*P_M(S)V$ for each Borel set $S\subseteq\mathbb R^2$. Compression gives positive effects, countable additivity in matrix elements and $E(\mathbb R^2)=I$. Its characteristic operator is
$$
 \int e^{ik\cdot y}E(dy)=e^{i(k_1R_1+k_2R_2)}e^{-k^TNk/2},\qquad
 N=\begin{pmatrix}v&0\\0&\kappa_h^2/(4v)\end{pmatrix}.             \tag{2}
$$
Each pointer marginal convolves its field's spectral law with a centered Gaussian of the indicated variance. A field displacement shifting $R_i$ by $c_i$ shifts the outcome law by $(c_1,c_2)$, so the meter is covariant and unbiased for states with finite first moments. For any state with finite second moments its output covariance is the symmetrized field covariance plus $N$. This statement also covers incident fields whose output law is non-Gaussian. [Holevo, Eqs. (3)–(7) and Theorem 1](https://arxiv.org/pdf/2007.02340v1#page=3)

The determinant in (2) is minimal. To see necessity, take a joint meter whose first moments are $R_i$ and whose second moments add the same real symmetric matrix $N$ in every state. In a spectral dilation with isometry $V$ and commuting pointers $M_i$, take the Gram matrix of $(I-VV^*)M_iV\phi$ for a normalized field vector $\phi$ on the common moment core. The pointer products commute, while the field products have antisymmetric part $i\kappa_h J/2$, with $J_{12}=1$, $J_{21}=-1$, $J_{11}=J_{22}=0$. Hence
$$
 N-i\kappa_h J/2\ \succeq\ 0,\qquad
 N_{11}N_{22}-N_{12}^2\ \ge\ \kappa_h^2/4.                           \tag{3}
$$
Equation (1) attains equality for every $v$. For a given variance $v$ in channel one, the least added standard deviation in channel two is $|\kappa_h|/(2\sqrt v)$. In common readout units the equal-noise choice is $v=|\kappa_h|/2$. Perfect spectral marginals for both fields would require $N=0$. When $B_h=0$, the field unitary groups commute and the joint spectral measure of the fields themselves achieves zero added noise. [Gaussian observable positivity condition, Eq. (4)](https://arxiv.org/pdf/2007.02340v1#page=3)

## Cost of shortening the exposure

For a specific calibration take $G'_W(a)=1$ with the vertex jump cancelled, as in the full optical source below. Average the same translated response with two Gaussian timing densities of standard deviation $h$ centered at $0$ and $\lambda h$. Their timing difference divided by $h$ has the normal law $X\sim\mathcal N(\lambda,2)$ in the double smearing integral. The bracket of the two exposures is $B_h=\mathbb E[B(hX)]$, where $B(0^\pm)=\pm G_N/30$. Bounded convergence gives
$$
 \lim_{h\downarrow0} B_h=\frac{G_N}{30}\operatorname{erf}(\lambda/2),\qquad
 \lim_{h\downarrow0}v_{\rm balanced}
   =\frac{\hbar G_N}{60}\left|\operatorname{erf}(\lambda/2)\right|.     \tag{4}
$$
Identical exposures ($\lambda=0$) can copy the same spectral reading into both channels. At fixed separation in units of exposure width, (4) gives a finite cost. For the two compact profiles sharing a center and variance whose ordering bias is $-1/5$, the same argument gives $B_h\to-G_N/150$ and balanced added variance $\hbar G_N/300$. For the distinct optical slopes $s^4,s^5$, even identical timing profiles select the nonzero midpoint $8126G_N/48715425$, to which (3) applies. [Optical delay bracket and compact profiles](weak-clock-contact.md) · [Synchronized distinct clocks](timing-midpoint.md)

The first finite-duration correction in (4) probes the regular optical response. Write $z=f_X^{(4)}$, $dz=v_0(s)ds+d\,\delta_a$ and $A=3/(5120G_N)$ as in the optical inversion. The calibration uses $G'_W(s)=p s^4+q s^5$ with $p,q$ fixed by the unit rim slope and vanishing vertex jump. Differentiating $B(\tau)=-A\int z(s-\tau/2)\,dz(s)$ for small positive delay pairs $dz$ with its translate with prefactor $A/2$. The two displaced atoms are separated. The density-density term tends to $\int v_0^2$ and the two atom-density terms sample the opposite traces. In this preparation the resulting regular right derivative is
$$
 b=\frac A2\left[\int v_0^2\,ds+d\big(v_0(a^-)+v_0(a^+)\big)\right]
   =\frac{535896929}{29327760}G_N .                                     \tag{5}
$$
The piecewise-polynomial response gives $B(\tau)=\operatorname{sgn}(\tau)G_N/30+b\tau+O(\tau^2)$ on either side of zero by oddness. At fixed $\lambda$, Gaussian averaging gives $B_h=(G_N/30)\operatorname{erf}(\lambda/2)+b\lambda h+O(h^2)$, with exponentially small contribution from delays outside a fixed neighborhood of zero. The coefficient $b$ depends on the full preparation. [Piecewise optical response](../checks/weak_clock_contact.py) · [Trace and delay calculation](../checks/timing_readout.py)

In the free vacuum, each of these unit-rim-slope readings gains $\hbar G_N\log 2/(30\pi)$ of **intrinsic variance** per halving of $h$ in the short-duration limit. The balanced meter adds the bounded term in (4) to each marginal. A finite limiting Weyl phase or a formal equal-time Weyl algebra specifies a multiplication law. A sharp projective readout in this representation would require self-adjoint sharp fields. The diverging one-particle norms prevent the finite-width unitaries of either individual calibrated reading from converging strongly to such a field's unitary group. For nonlinear gravity, the remaining proof gap is to derive a joint instrument from the constrained clock, with its state, coupling to the meter and regional boundary conditions. [Fock variance and Weyl limits](timing-quantum.md) · [Sharp-rim ultraviolet weight](weak-fock.md)

Run `python3 -B checks/timing_readout.py` to integrate the exact separated optical brackets over the Gaussian delay distribution in units $G_N=\hbar=1$. The script computes (5) in rational arithmetic and refines the time quadrature independently. At $h=10^{-5}$ the balanced added variances are `0.004651119` and `0.014227726` for $\lambda=0.5$ and $2$, respectively. Their limits are `0.004605440` and `0.014045013`. The last line gives `One-sided regular slope 535896929/29327760 (G_N=hbar=1)`. Run `make check` for the full suite. [Executable check](../checks/timing_readout.py)
