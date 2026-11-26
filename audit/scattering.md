# Does the graviton-pair calculation test two-loop graviton scattering?

**Physical question.** Section 4.4 introduces the celebrated two-loop Goroff–Sagnotti ultraviolet divergence of four-dimensional Einstein gravity as motivation for its convergent graviton-pair correlator (4.32)–(4.34). Does that single-cone boundary calculation actually test two-loop graviton scattering?

**Outcome.** No—not yet. The pair overlap in §4.4 is an exact calculation for independent free Gaussian oscillators on a single incoming null cone; no Einstein interaction vertex, bulk propagation between incoming and outgoing cones, or four-graviton collision kinematics enters it. Its $G_N^3\log G_N$ behavior arises because the source's affine displacement is chosen to shrink proportionally to $G_N$, probing affine frequencies of order $R/\ell_P^2$ rather than Planck-scale four-momenta. The actual Goroff–Sagnotti / Bern et al. benchmark is a six-derivative, all-plus four-graviton amplitude with a specific kinematic structure $K$, dimensional-regularization pole residue $209/24$, and scale-logarithm coefficient $-1/4$ (verified below). The manuscript itself introduces the two-loop divergence as motivation and explicitly switches to a single-cone two-point function; testing its proposed nonlinear bulk dynamics against flat-space scattering remains an open challenge. [Manuscript, §4.4, Eqs. (4.32)–(4.34) and footnote 17](https://arxiv.org/pdf/2611.34924v1#page=33)

## Where the logarithm comes from

To separate the role of Newton's constant from the role of the source displacement, keep them distinct. At fixed corner area $\mathscr A$, write $x=4G_N\hbar/\mathscr A$ and give the affine displacement $\delta u$ its own dimensionless parameter $\tau=\omega_1\delta u$ (the manuscript sets $\tau=x$). With the stipulated Gaussian variances $v_k=x/(2k)$, the centered quadratic source acting on the product vacuum $\Omega$ creates the pair vector

$$
\Psi_N=\sum_{k\leq N}(q_k^2-v_k)\Omega
=\frac{x}{\sqrt 2}\sum_{k\leq N}\frac{|2_k\rangle}{k}.
$$

The diagonal rotation generator $D=\sum_{k\ge1}k a_k^\dagger a_k$ acts simply by $D|2_k\rangle=2k|2_k\rangle$, so both the spectral weights and the exact overlap are elementary:

$$
C_N(x,\tau)=\langle\Psi_N|e^{-i\tau D}|\Psi_N\rangle
=\frac{x^2}{2}\sum_{k=1}^N\frac{e^{-2ik\tau}}{k^2},
\qquad
C(x,\tau)=\frac{x^2}{2}\operatorname{Li}_2(e^{-2i\tau}).
$$

Even at $\tau=0$, the pair vector has finite norm $\|\Psi\|^2=\pi^2 x^2/12$. Its first spectral moment, however, diverges logarithmically as $\langle\Psi_N|D|\Psi_N\rangle=x^2 H_N$ ($H_N=\sum_{k\le N}1/k$), giving $\partial_\tau C_N(x,0)=-ix^2 H_N$. Setting $\tau=x$ turns that cutoff derivative into the cubic coefficient $-iH_N$, whereas summing to $N=\infty$ first gives $\operatorname{Im}C(x,x)=x^3[\log(2x)-1]+O(x^5)$ as $x\downarrow 0$. The singular derivative sits directly in the free spectral measure. [Full derivation, error bounds and numerical check](04-pair.md)

Holding $\tau$ fixed instead makes the entire correlator strictly proportional to $G_N^2$; setting $\tau=cx$ multiplies the cutoff logarithm by the arbitrary constant $c$ (the manuscript picks $c=1$ using a clock estimate). Because the rotation is quadratic and diagonal, there is no propagation from an incoming cone to an outgoing cone, and the connected four-point cumulant of *linear* oscillator coordinates vanishes identically by Wick's theorem (only quadratic sources produce the nonzero connected pair overlap above). Although the broader framework includes nonlinear bulk dynamics elsewhere, neither the reduced gravitational Hamiltonian nor any two-loop interaction enters (4.33). [Manuscript, §4.4](https://arxiv.org/html/2611.34924v1#S4.SS4) · [§6.1](https://arxiv.org/html/2611.34924v1#S6.SS1)

The breakdown scale of the small-$x$ phase expansion also has a distinct geometric meaning. On a round cone of macroscopic radius $R$, area $4\pi R^2$, and fundamental affine frequency $\omega_1\sim 1/R$ (with $\ell_P^2=G_N\hbar$ in $c=1$ units), the crossover $kx\sim 1$ occurs at an affine frequency $k\omega_1\sim R/\ell_P^2$—a factor $R/\ell_P$ above the Planck frequency. By contrast, the Planck frequency $k\omega_1\sim 1/\ell_P$ sits at $k\sim R/\ell_P$, where $kx\sim\ell_P/R\ll 1$. Identifying the radial mode index $k$ with a flat-space loop four-momentum would therefore require a separate derivation. [Manuscript, discussion preceding Eq. (4.32) and footnote 17](https://arxiv.org/pdf/2611.34924v1#page=33)

## What the scattering calculation measures

Goroff and Sagnotti computed the genuine on-shell two-loop ultraviolet divergence of four-dimensional pure Einstein gravity, identifying a local curvature-cubed operator that survives on Ricci-flat backgrounds (where Riemann and Weyl tensors coincide). Van de Ven independently confirmed this result in position space using background-field methods, and Bern and collaborators directly computed the corresponding four-graviton all-plus helicity amplitude (using the all-outgoing momentum convention). [Goroff and Sagnotti 1985](https://doi.org/10.1016/0370-2693(85)91470-4), [detailed 1986 paper](https://www.sciencedirect.com/science/article/pii/0550321386901938), [van de Ven 1992](https://www-library.desy.de/preparch/desy/postpr/1991/desy91-115.pdf), [Bern et al. 2015, Eqs. (7)–(10)](https://arxiv.org/pdf/1507.06118#page=3)

In units $\hbar=c=1$ with $g_{\mu\nu}=\eta_{\mu\nu}+\kappa h_{\mu\nu}$, $\kappa^2=32\pi G_N$, and dimensional regularization $D_{\rm reg}=4-2\epsilon$, Bern et al.'s sign convention gives the *divergent effective Lagrangian* density

$$
\mathcal L^{\rm div}_{R^3}=
-\frac{209}{1440}\frac{(\kappa/2)^2}{(4\pi)^4\epsilon}\sqrt{-g}\,
R^{\alpha\beta}{}_{\gamma\delta}
R^{\gamma\delta}{}_{\rho\sigma}
R^{\rho\sigma}{}_{\alpha\beta}.
$$

Fixing the regulator, coupling normalization, and sign avoids confusion between the divergence and its canceling counterterm. The four-graviton matrix element scales as $\kappa^6 p^6$, carrying six derivatives and a rigid helicity and momentum structure. In terms of Mandelstam invariants $s=(p_1+p_2)^2$, $t=(p_2+p_3)^2$, and $u=(p_1+p_3)^2$ (with $p_i^2=0$ and $s+t+u=0$) and spinor-helicity brackets encoding external polarizations, define

$$
K=\frac{i(\kappa/2)^6}{(4\pi)^4}\,s t u
\left(\frac{[12][34]}{\langle12\rangle\langle34\rangle}\right)^2 .
$$

After isolating universal soft infrared singularities and subtracting one-loop subdivergences, the all-plus amplitude carries the pole $K\,209/(24\epsilon)$ in this scheme, which the local $R^3$ counterterm cancels. At fixed renormalized coupling, the explicit renormalization-scale logarithm in pure gravity is $(-K/4)\log(\mu^2/\mu_0^2)$ (with $\mu_0$ an arbitrary reference scale compensated in physical observables by the running of the local $R^3$ coupling). [Bern et al. 2015, Tables I–III](https://arxiv.org/pdf/1507.06118#page=3), [Bern et al. 2017, Eqs. (4), (8) and (11)](https://arxiv.org/pdf/1701.02422#page=5)

The distinction between the $209/24$ pole and the $-1/4$ logarithm coefficient checks directly from the published components in units of $K$: the bare two-loop graph, single Gauss–Bonnet insertion, and double Gauss–Bonnet insertion carry pole residues $a=-3431/5400$, $b=689/675$, and $c=24(53/90)^2$, weighted by $(\mu^2)^{2\epsilon}$, $(\mu^2)^\epsilon$, and $1$, respectively. Direct arithmetic confirms both $a+b+c=209/24$ and $2a+b=-1/4$. Because an evanescent operator (whose on-shell matrix element vanishes in strictly four dimensions) enters through the subdivergences, comparing pole residues across regulators requires matching conventions, whereas the $-K/4$ scale logarithm survives the evanescent scheme changes analyzed in these papers. [Bern et al. 2015, Table II](https://arxiv.org/pdf/1507.06118#page=4), [Bern et al. 2017, §II](https://arxiv.org/pdf/1701.02422#page=7)

## A comparison the proposed theory could pass or fail

To genuinely test the null-cone quantization against perturbative and UV-completed graviton scattering, one would need to carry out three steps:

1. **Asymptotic wave packets.** Construct two incoming and two outgoing graviton wave packets in large, nearly Minkowski diamonds with $\Lambda=0$, deriving their helicity, one-particle normalization, and physical four-momenta from the boundary radiative data. Hold the packets and collision kinematics fixed as $G_N$ varies, take the large-diamond limit, and specify the treatment of soft gravitons.
2. **Bulk transition amplitude.** Evaluate the connected transition matrix element using the proposed bulk evolution between the incoming and outgoing cuts, obtaining the on-shell amplitude directly or via leg amputation. A basic first check is recovering the nonzero Einstein tree amplitude in the $--++$ channel (the all-plus tree amplitude vanishes, so that channel isolates loop-level dynamics).
3. **Two-loop extraction and matching.** Extract the $\kappa^6$ all-plus contribution at external momenta well below the Planck scale, summing over all physical internal modes and channels, removing universal infrared divergences, and accounting for subdivergences. Test the kinematic factor $K$ and its $-1/4$ scale-logarithm coefficient across scattering angles (matching to the dimensional scheme above would also test the $209/24$ pole). A genuine ultraviolet completion would further predict the finite renormalized $R^3$ coupling at a reference scale—a datum left unfixed by two-loop effective field theory alone. [Bern et al. 2015](https://arxiv.org/abs/1507.06118), [complete four-graviton amplitudes](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.211601), [correction to the finite remainders](https://journals.aps.org/prl/pdf/10.1103/811n-z924)

Both calculations produce a factor of $G_N^3$, but from entirely different physics: in the single-cone overlap it combines two powers of the Gaussian variance with one power of the chosen affine displacement, whereas in four-graviton scattering it multiplies a six-derivative interacting on-shell amplitude. The pair calculation demonstrates a genuine nonuniform expansion of a finite boundary observable, yet leaves both the scattering kinematics and the curvature-cubed coupling untouched.
