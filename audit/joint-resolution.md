# Does a finite-resolution cap clock have a unique sharp bracket?

Two detectors read the cap-normalized affine distance on the **same** outgoing null face. They have the same mean waist time, the same mean cap-to-waist radius ratio and the same waist area. In a polarized cylindrical vacuum solution, their readings and their responses to every smooth perturbation converge to those of the same geometric clock. Their mutual bracket can nevertheless tend to zero, $G/648$, or $25G/324$ at the flat background. The two nonzero values use the same pair of timing profiles and differ only in how quickly their cap and timing widths shrink. These are cross-brackets of two different finite-resolution observables. An observable always has zero bracket with itself. [Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Cap clock and area weighting, (3.27)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27)

## A waist and a cap specified by geometry

Take the polarized Einstein–Rosen metric
$$
ds^2=e^{2(\gamma-\psi)}(-dt^2+dr^2)+e^{2\psi}dz^2+r^2e^{-2\psi}d\phi^2 .
$$
Give $z$ period $Z$ and $\phi$ period $2\pi$, fixing the normalizations of the Killing fields. The orbit has area $2\pi Zr$. Its area radius in the normalization $\int\epsilon_0=4\pi$ is $\rho=\sqrt{br}$ with $b=Z/2$. The harmonic conjugate of $r$ on the oriented Lorentzian orbit space fixes the Einstein–Rosen time $t$ up to an additive constant. Fix its origin by a common reference event. The waist is the orbit $r=R,t=T$. An outgoing ray ends there along $t=T+r-R$ and starts at $r=a=v_c^2 R$, giving $\rho_c/\rho_S=v_c$. Each reading uses its own cap and waist. At finite timing width the device samples neighboring waists of exactly the same area. These symmetry orbits are tori. The calculation uses a smooth continuation of the metric through the observational cuts. [Kuchař's canonical reduction](https://doi.org/10.1103/PhysRevD.4.955)

Along the ray $du/dr$ is proportional to $e^{2(\gamma-\psi)}$ for affine $u$. Hence the v1 observable $U=\rho'_c(u_S-u_c)$, where prime denotes an affine derivative, is
$$
 U(T,a)=\frac{\sqrt b}{2\sqrt a}\int_a^R
   e^{2[(\gamma-\psi)(T+r-R,r)-(\gamma-\psi)(T+a-R,a)]}\,dr .
$$
On the flat cylindrical solution $\psi=\gamma=0$. The vacuum constraints $\gamma_r=r(\psi_t^2+\psi_r^2)$, $\gamma_t=2r\psi_t\psi_r$ make $D\gamma$ constant there, so its difference drops out. For a perturbation $Y=D\psi$ write $Y_T(r)=Y(T+r-R,r)$. Then
$$
 DU(T,a)[Y]=\frac{\sqrt b}{\sqrt a}
 \left[(R-a)Y_T(a)-\int_a^R Y_T(r)\,dr\right].
 \tag{1}
$$
The first term measures the variation of the cap normalization. Positive averages of the nonlinear readings still satisfy $U_{\rm av}\ge(1-\epsilon)\sqrt{bR}$ for a cap response of mean $v_c=\epsilon$. This follows by applying the vacuum focusing bound to each reading at the common waist area. The flat cylindrical congruence already has shear.

The normalization of the bracket follows from the gravitational action. On $t=\mathrm{const}$ the ADM potential $(16\pi G)^{-1}\int \sqrt h(K^{ij}-Kh^{ij})Dh_{ij}$ in these coordinates gives $C\int r\psi_t D\psi\,dr$ with $C=Z/(2G)$. In fact the mixed curvature eigenvalues are $(\gamma_t-\psi_t,\psi_t,-\psi_t)/N$, the lapse is $N=e^{\gamma-\psi}$ and $\sqrt h/N=r$. Their contraction with the three logarithmic spatial metric variations leaves $4r\psi_t D\psi$. Use the convention $\{\psi(t,r),Cr'\psi_t(t,r')\}=\delta(r-r')$. The remaining wave equation is $\psi_{tt}=\psi_{rr}+r^{-1}\psi_r$. Both the cap trace and the bulk term in (1) are thus propagated by the gravitationally normalized cylindrical wave equation.

## The jump on a common characteristic

Average $v_c$ with a fixed bounded, compactly supported, nonnegative unit-mass density, rescaled to width $h$ and centered at $\epsilon\in(0,1)$. Let $W_h(r)dr$ be the signed radial measure in (1) after this average, including $\sqrt b$. It has a bounded total variation uniformly in $h$ and a density of size $O(1/h)$ at fixed $R,\epsilon,b$. The singular part of the sharp source at $a=\epsilon^2R$ has coefficient $\sqrt{b/a}(R-a)$. Two useful weighted masses are
$$
 M=\lim_{h\to0}\int\frac{W_h(r)}{\sqrt r}dr
   =\sqrt b\frac{(\sqrt R-\sqrt a)^2}{a},
 \qquad A=\sqrt b\frac{R-a}{a}.
$$
Here $A$ is the cap atom after the same division by $\sqrt r$.

Give the second waist a small time delay $d>0$ relative to the first. At source radii $r,s$, the time separation is $d+s-r$. Before the front that travels via the axis, the bracket vanishes for $s<r-d/2$. For $s>r-d/2$ its value is
$$
 \{\psi(T+r-R,r),\psi(T+d+s-R,s)\}
  =\frac{K(m)}{\pi C\sqrt{rs}},\qquad
 m=\frac{d[2(s-r)+d]}{4rs},
 \qquad K(m)=\int_0^{\pi/2}\frac{dx}{\sqrt{1-m\sin^2x}} .
$$
Indeed the planar retarded fundamental solution at distance $D$ and positive time $t$ is $\mathbf1_{t>D}/(2\pi\sqrt{t^2-D^2})$. Integrate it over relative polar angle with $D^2=(s-r)^2+4rs\sin^2(\phi/2)$ and divide by $C$. This normalization gives the stated equal-time bracket with the momentum. The condition $a>0$ keeps the entire measurement away from the front $|t|=r+s$ for sufficiently small $d,h$. The jump as $d\downarrow0$ is $1/(2C\sqrt{rs})$ on the triangular region $s>r$. For $d<0$ interchange the two clocks by antisymmetry.

Now let the individual waist times fluctuate independently with fixed, bounded, compactly supported normalized response densities, scaled to width $\eta$. Set $p=\Pr(T_2>T_1)$, assuming the two sampling times coincide with probability zero. The temporal averaging in each *observable* produces this product measure when taking the bracket. For $h,\eta>0$, the linearized source is a bounded compactly supported spacetime density, including the edge at $r=R$. It generates a finite-energy wave from the Cauchy propagator.

* If $\eta/(hR)\to0$, the triangular region contains half the product of the identical radial signed densities in the limit from positive delay. The strip $|r-s|\le |d|$ contributes at most a constant times $|d|/(hR)$ by the $L^1$ and $L^\infty$ bounds. The elliptic kernel tends uniformly to its jump on its timelike support. Averaging over the two timing responses yields
$$
 \lim\{U_1,U_2\}=\frac{2p-1}{4C}M^2
  =(2p-1)\frac{G}{4}\left(\frac{1-\epsilon}{\epsilon}\right)^4 .
 \tag{2}
$$

* If $hR/\eta\to0$, the product of the two cap atoms contributes in full for positive delay. For each fixed nonzero scaled delay, the whole cap-cap support has $|r-s|<|d|/2$ eventually. The smooth-bulk pair samples half of its square, while the two cap-bulk orderings together sample one full copy of their product. Thus the positive-delay coefficient changes to $(M^2+A^2)/(4C)$. Bounded total variation and a uniformly bounded kernel on the collar justify dominated convergence over the time profiles. The general answer is
$$
 \lim\{U_1,U_2\}=\frac{2p-1}{4C}(M^2+A^2).
 \tag{3}
$$

For example use an even timing density supported in $(-1/4,1/4)$ in units of $\eta$ for the first detector. For the second use the same bump centered at $+1$ with weight $3/4$ and at $-3$ with weight $1/4$. Both detectors are centered on $T=0$, yet $p=3/4$. With $\epsilon=3/4$, (2) gives $G/648$ and (3) gives $25G/324$. For two identical detectors the bracket is exactly zero at every resolution. A finite resolution or a rule correlating how observables are regularized can select a prescription. Arbitrarily chosen normalized, centered approximations to the same sharp reading do not define a continuous extension of the bracket in this sector. The two faces of a diamond are distinct observables. The calculation here uses one face twice.

## Pairing a sharp clock with a smooth probe

There is also a conditional statement for the spherical topology of v1, without cylindrical symmetry. Fix a smooth noncaustic family of relational waists and cap ratios near the reference values, with strictly positive expansion on the compact truncated faces. Suppose the gauge-reduced response $X_F$ to a probe $F$ exists and is smooth there, including its prescribed variations of the boundary frames and embeddings. Assume the dressed family and its first variation depend smoothly on these parameters and that the response weights are fixed in the relational labels. Then the bracket with a positive, normalized collar average of the clock converges to the sharp reading's directional derivative $D\bar u_*[X_F]$, for the order $\{F,\bar u_*\}$. This requires a generator for the probe and control of the clock readings along its variation.

To see convergence, pull each optical integral to its area-ratio coordinate and fixed angular labels. Variation of $u_*=\rho_S\int_{v_c}^1e^\Xi dv$ gives the variations of $\rho_S$ and $\Xi$ there. At fixed relational $v_c$, its coordinate variation is zero. In the average (3.28), one also differentiates both weights involving $\rho_S$. All integrands and their variations are continuous on a compact set under the hypotheses, and the denominator is bounded away from zero. The resulting directional derivative is continuous in the cap and waist labels, so every shrinking normalized average has the same limit. Bounded first parameter derivatives give an error bounded by the parameter widths times those derivative bounds. In the cylinder, $Y=t$ on the measurement region gives $DU=-\sqrt b(R-a)^2/(2\sqrt a)$ directly from (1). It can be realized with smooth Cauchy data equal to those of $t$ in the local domain of dependence.

The positive result leaves the existence of a smooth $X_F$ for a given physical probe as a separate test. The cylindrical counterexample shows how smooth-probe convergence can coexist with a prescription-dependent bracket when both probes sharpen. It uses a regular-axis exterior and symmetry-reduced vacuum perturbations of a toroidal waist. Establishing a joint sharp-clock algebra for v1 still requires the symplectic domain and a justified product prescription on its spherical cuts. This is a proof gap for the unrestricted theory. [Unresolved endpoint source on the single radiative block](endpoint-inverse.md)

## Reproduce the collar limits

Run `python3 checks/joint_resolution.py` from the repository root. In units $R=1$, the script integrates the retarded kernel with a centered polynomial cap density. It splits the integral at the characteristic before comparing the two orders of taking the limit. It also varies the clock on the smooth probe independently. The repository suite runs these checks with `make check`. [Executable calculation](../checks/joint_resolution.py)

```text
Later clock, broad cap collar: 0.00308809; limit 0.00308642
Later clock, narrow cap collar: 0.15392645; limit 0.15432099
Centered skew timing, limiting brackets / G: 1/648 and 25/324
Smooth-probe variation: -0.12760543; limit -0.12760417
```
