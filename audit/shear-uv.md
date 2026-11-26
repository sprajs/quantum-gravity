# The bare shear square and the finite-reading probability

**Physical question.** Can the paper's bare quadratic shear operator (4.22) be constructed in the continuum so that the gravitational clock assigns nonzero—or unit—probability to finite readings, as claimed in (5.19)?

**Outcome.** Conditional on the corner area-density operator, the angular denominator $a^{-1/2}$ is well controlled at positive fixed area, and the square ordering of (4.22) produces a positive quadratic form at any finite mode cutoff. In the continuum, however, two explicit checks expose a missing ultraviolet construction in the step from (4.22) to (5.19). First, the paper's own linearized shear commutator from Appendix D.2 already rules out a literal radial integral of squared point-field norms on *any* nonzero vector over an open interval. Second, in a regulated one-polarization radial comparison model with the paper's short-wave symplectic scaling, the capped clock's spectral floor grows as $\exp(\min(C_N,R))$ with $C_N\propto N(N+1)$, forcing every finite-reading projection $\mathbf 1_{[0,\ell]}(T_{N,R})$ to vanish identically once cutoffs are large—even with a constant, perfectly regular angular denominator. Because the full gravitational clock involves nonlinear reconstruction, both polarizations, and quantum corner data, these linearized and reduced models do not settle its exact value; its continuum definition and finite-reading probability remain open. [Shear (4.22)](https://arxiv.org/html/2611.34924v1#S4.E22) · [Clock (4.26)–(4.27)](https://arxiv.org/html/2611.34924v1#S4.E26) · [Claim (5.19)](https://arxiv.org/html/2611.34924v1#S5.E19)

## An obstruction in the paper’s linearized shear algebra

Pick a real transverse polarization and transverse smearing for which the linearized flat-null-plane shear current $J(u)$ has nonzero two-point normalization. Equation (D.19) and the discussion following it yield the derivative-of-delta commutator; absorbing normalization and orientation into a real constant $c\ne 0$, real radial smearings in the corresponding regular free-field representation satisfy

$$
[J(f),J(g)]=ic\int f(u)g'(u)\,du\,I .
$$

Keeping the frequency damping $\tau>0$ of (D.19) at coincident affine coordinates yields the vacuum expectation $c_\perp\int_0^\infty\omega e^{-\tau\omega}\,d\omega=c_\perp/\tau^2$, so smearing the bare coincident square against any fixed positive weight still diverges in the vacuum. Although an infinite expectation in one state would not by itself forbid a dense form domain, the commutator enforces a far stronger obstruction. [Linearized kernel and commutator](https://arxiv.org/html/2611.34924v1#A4.SS2.p2.7)

Suppose some vector $\psi$ admitted an $L^2(I;\mathcal H)$ representative $u\mapsto J(u)\psi$ on an open interval $I$, giving a finite bare shear form $E_I[\psi]=\int_I\|J(u)\psi\|^2\,du<\infty$. Then $\|J(f)\psi\|\le \|f\|_2 E_I[\psi]^{1/2}$ for every real $f\in C_c^\infty(I)$. Differentiating the Weyl relation as a quadratic form on the common domain of the smeared generators—which requires only a single smeared generator on each side of the inner product—gives the weak commutator bound

$$
|c|\left|\int f g'\right|\,\|\psi\|^2
\le 2\|J(f)\psi\|\|J(g)\psi\|
\le (\|f\|_2^2+\|g\|_2^2)E_I[\psi].
$$

Now pick any nonzero real test function $w\in C_c^\infty(I)$ and set $f=w\cos(Ku)$, $g=w\sin(Ku)$ for $K>0$. Then $\|f\|_2^2+\|g\|_2^2=\|w\|_2^2$, while integration by parts gives $2\int f g'=\int(fg'-gf')=K\|w\|_2^2$. Substituting these into the inequality yields

$$
E_I[\psi]\ \ge\ \tfrac12|c|K\,\|\psi\|^2
\quad\text{for every } K>0 .
$$

Sending $K\to\infty$ forces $\psi=0$: no nonzero state can have a finite bare point-field shear integral on any open radial interval. Multiplying by a positive radial weight bounded below on an interior subinterval leaves the obstruction unchanged, and in the linear theory a positive local square integrated over angle would dominate an angularly smeared component by Cauchy–Schwarz. Because this proof relies on the free-field commutator down to arbitrarily short scales (derived in Appendix D at linearized order), deciding whether the nonlinear reconstructed field at finite $G_N$ escapes it requires nonperturbative information.

Appendix D itself avoids the bare square by subtracting the vacuum singularity before coincidence, obtaining a lower bound with the negative derivative term $-c_f\|g'\|_2^2/2$ for the smeared Wick square. While subtracting a ground energy preserves positivity for a global oscillator Hamiltonian, subtracting a vacuum variance does *not* preserve positivity for a local quadrature square—a squeezed state with variance below the vacuum gives a negative expectation. Connecting Appendix D's subtracted observable back to the strictly positive operator invoked in (4.22) therefore requires an explicit continuum prescription that establishes both positivity and a domain. [One-loop subtraction](https://arxiv.org/html/2611.34924v1#A4.SS2.p3.1) · [Smeared Wick square (D.28)](https://arxiv.org/html/2611.34924v1#A4.E28)

## A regulated clock with vanishing finite-reading probability

A second check keeps the mode cutoff $N$ and focusing cap $R$ finite throughout, testing what happens as they are removed. Consider a radial comparison model with frozen spherical corner density $\rho_S=b$, a single polarization $z^1(v,y)=Y(y)x(v)/v$, and $z^2=0$, where $Y$ is a fixed smooth real angular profile supported in a polarization chart and nonzero on an open patch. Fix $0<\epsilon<1$, $d=(1-\epsilon)/2$, $v_0=\epsilon+d$, and $\omega_k=2\pi k/d$, and expand on the full radial interval $[\epsilon,1]$ in the $2N$-mode family

$$
x_N(v)=\sum_{k=1}^N\big[Q_k\sin\big(\omega_k(v-\epsilon)\big)
             +B_k\big(1-\cos\big(\omega_k(v-\epsilon)\big)\big)\big].
$$

Every basis function vanishes at $\epsilon$, $v_0$, and $1$ (with possibly nonzero derivatives). The change of variables $x=vh$ converts the radial symplectic pairing in (D.42a) into a constant multiple of $\int(x'\widetilde x-\widetilde x' x)\,dv$. Integrating over $[\epsilon,1]$ gives pairing magnitude $2d\,\omega_k$ within each $(Q_k,B_k)$ pair and zero between distinct pairs. Choosing orientation and angular normalization fixes the canonical commutators $[Q_k,B_j]=i\kappa\delta_{kj}/k$ ($\kappa>0$); isotropic Gaussians then have variances $\kappa/(2k)$, matching the $1/k$ scaling in (4.32), though the spectral bound below holds in *every* state of these oscillators. [Radial symplectic form](https://arxiv.org/html/2611.34924v1#A4.SS3.p4.1) · [Example Gaussian](https://arxiv.org/html/2611.34924v1#S4.SS4.p8.1)

Set $h=x_N/v$. For every $v\ge v_0$, the bare focusing integral includes the early subinterval $I=[\epsilon,v_0]$. Using $r\le 1$, the boundary-vanishing identity $r^2(h')^2=(x_N')^2-\partial_r(x_N^2/r)$ (which holds including symmetrized cross terms for noncommuting quadratures), orthogonality of sines and cosines on $I$, and the uncertainty bound $Q_k^2+B_k^2\ge\kappa/k$ from $(Q_k+iB_k)^\dagger(Q_k+iB_k)\ge 0$, the quadratic form obeys

$$
\begin{aligned}
\Xi_{N,y}(v)
 &\ge \frac{Y(y)^2}{4}\int_I r^2(h')^2\,dr
  = \frac{Y(y)^2}{4}\int_I(x_N')^2\,dr\\
 &= \frac{dY(y)^2}{8}\sum_{k=1}^N\omega_k^2(Q_k^2+B_k^2)
 \ \ge\ \frac{\pi^2\kappa\,Y(y)^2}{4d}N(N+1)\,I_{\mathcal H}.
\end{aligned}
$$

This bound holds on the Schwartz core and extends to the nonnegative self-adjoint oscillator quadratic forms.

To avoid assuming any domain for the uncapped exponential, impose the exact same focusing cap $R$ used in §5.1. Pick a patch $P$ of solid angle $|P|>0$ where $|Y|\ge y_0>0$, and set $C_N=\pi^2\kappa y_0^2 N(N+1)/(4d)$. With the frozen spherical density giving $a=4\pi b I$, retaining only $P\times[v_0,1]$ in the capped clock (4.26) produces the operator lower bound

$$
T_{N,R}\ \ge\ \frac{b\,|P|(1-v_0)}{4\pi}
                \exp\!\big(\min(C_N,R)\big) I .
$$

Only the scalar spectral floor of each individual $\Xi_{N,y}(v)$ enters this step. For any fixed finite clock limit $\ell$, the spectral projection $\mathbf 1_{[0,\ell]}(T_{N,R})$ becomes identically zero once both $N$ and $R$ are sufficiently large—regardless of the relative rate at which the two cutoffs are sent to infinity. In particular, the Gaussian probability of an allowed finite clock reading drops to zero even while the angular denominator $a=4\pi b I$ stays completely constant and regular.

**Scope of this model.** Because this construction quantizes an explicitly restricted one-polarization radial family (and restricting a classical phase space before quantizing does not imply a reducing subspace of the full quantum operator), it does not prove that the full gravitational clock collapses. Instead, it refutes the general inference that finite-cutoff positivity, short-wave gravitational symplectic scaling, and a smooth classical center automatically guarantee a nonzero finite-reading projection; the full theory must specify the nonlinear canonical coupling, corner operators, high-frequency behavior of $\widehat z^\alpha$, and continuum composite prescription.

## What survives for the gravitational denominator

By contrast, the *angular* corner denominator works cleanly under its stated inputs. Assuming (4.24)–(4.25) define a positive measurable density with $\int\rho_y^2\,d\Omega=\mathscr A I$ at fixed $\mathscr A>0$, Cauchy–Schwarz yields $a^2\le 4\pi\mathscr A I$ for $a=\int\rho_y\,d\Omega$. Positivity forces $\ker a=\{0\}$ (if $a\psi=0$, then $\rho_y^{1/2}\psi=0$ almost everywhere and normalization forces $\psi=0$), so $a^{-1/2}$ is densely defined even if its spectrum is unbounded. Equations (C.11) and (C.16a) therefore control the angular denominator's contribution to (5.16), conditional on the density and cutoff focusing operators. [Area normalization](https://arxiv.org/html/2611.34924v1#S4.SS3.p4.1) · [Capped clock](https://arxiv.org/html/2611.34924v1#A3.SS2.p3.1) · [Angular resolvent bound](https://arxiv.org/html/2611.34924v1#A3.SS2.p7.2)

The *conditional-probability* denominator in (5.3), however, is $\|P_\ell\Omega\|^2$ for the incoming Gaussian $\Omega$. By the monotone cutoff-form theorem in (C.13), $L(L+T)^{-1}P_M\to P_M$ as $L\to\infty$, where $M$ is the closure of the uncapped form domain; achieving unit probability in (5.19) thus requires $\Omega\in M$. Because the compactness estimate (C.16d) works strictly at fixed mode resolution—and footnote 18 explicitly labels replacing the quantum resolvent difference by a classical Wigner tail heuristic—proving (5.19) for gravity requires both a defined continuum shear composite and control of the exact spectral weight as the focusing cap and mode cutoffs are removed. As the radial model above demonstrates, that probability can collapse to zero even when the angular denominator $a$ is a constant multiple of the identity. [Section 5.1 and footnote 18](https://arxiv.org/html/2611.34924v1#S5.SS1.p13.1) · [Fixed-resolution compactness](https://arxiv.org/html/2611.34924v1#A3.SS2.p8.3) · [Behrndt et al., Theorem 4.2](https://www.numerik.math.tu-graz.ac.at/~behrndt/BehrndtHassiSnooWietsma09.pdf)
