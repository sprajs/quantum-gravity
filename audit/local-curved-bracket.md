# The timing singularity of two cap clocks calibrated at one launch event

Two different spherical affine clocks on the same curved diamond can have a divergent equal-time bracket as their individual time windows narrow. The example uses one emitter, one physical calibration at launch and a common return event. The measurement that causes the leading divergence is the emitter's point measurement of the Weyl curvature. At fixed nonzero curvature its contribution grows as the inverse sixth power of the timing width for suitable smooth windows, even when their timing distributions have identical first four moments. The result applies to the classical bracket of the actual nonlinear readings at a symmetric vacuum plane wave. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Single-emitter clock differential](weak-curved.md)

## One emitter and two cap fractions

Use the Rosen metric $-2\,du\,dv+\cosh^2(\kappa u)dx_1^2+\cos^2(\kappa u)dx_2^2$, with $\kappa>0$. At the central launch event $p$, orthonormalize timelike and longitudinal trial vectors. Choose the rapidity $\chi$ along their boost plane so that $\mathcal W=E_{ij}E^{ij}+B_{ij}B^{ij}$ takes its prescribed value $w>0$. Here $E,B$ are the electric and magnetic Weyl tensors in the emitter frame. On this solution $\mathcal W=4\kappa^4(V^u)^4$. For the trial pair aligned with the wave axis, $V^u=e^\chi/\sqrt2$ and $\partial_\chi\mathcal W=4w$. This gives a regular local calibration branch. Follow the geodesic observer until the two-tip diamond has weighted waist radius $M=\langle D(S)^2\rangle/\langle D(S)\rangle=R$, where $D(s)$ is the area radius per unit launch solid angle along an affinely parametrized ray and $S$ is its affine waist coordinate. Both clocks use this same condition. For each cap fraction $a$ use $D(C_a)=a D(S)$ and measure
$$
 F_a=\frac{\langle D(S)D'(C_a)(S-C_a)\rangle}{\langle D(S)\rangle}.
$$
Assume $0<a<b<1$, a transverse waist and positive optical slope. Take a sufficiently small diamond at fixed wave and boost, or sufficiently weak curvature at fixed $R$.

Use the global Einstein causal propagator $E_{\rm EH}$ on the surrounding Rosen strip, with large transverse periods. Choose the whole swept region inside a convex normal patch with a causally compatible neighborhood and no contributing winding images. Such patches exist for sufficiently short diamonds. Work with all smooth vacuum perturbations of that continuation, differentiating the launch, caps, observer and return condition together. At this background the marked sources are conserved because of the local isometries relating the calibrated marks. Sweep the entire preparation along the central observer by its timelike Brinkmann Killing translation $\Phi_t$. This is proper time on that observer. On the causal hull under consideration the kernel shares this translation symmetry. These hypotheses fix how the gravitational field propagates beyond the measured cuts. [Ward identity and matched-radius variation](weak-curved.md) · [Timing sweep and its domain](timing-curved.md) · [Einstein normalization and Rosen propagation](weak-rosen-green.md)

## The curvature measured at launch

Write $F_a(g,\chi)$ temporarily for the clock with the boost held at its trial value and with the radius constraint still imposed. The chain rule for calibration inserts into the metric differential the term
$$
 c_a\,\delta_g\mathcal W(p),\qquad
 c_a=-\frac{\partial_\chi F_a}{\partial_\chi \mathcal W}.
 \tag{1}
$$
The metric derivative here includes preliminary orthonormalization at fixed $\chi$. Its principal term evaluates second derivatives of the metric at $p$.

The coefficient can be found from exact plane-wave optics. Put $q_n=\kappa^4(k^u)^4$ for a launch ray with $-V\cdot k=1$. Its two optical Jacobi axes have lengths $\sinh(\omega s)/\omega$ and $\sin(\omega s)/\omega$, where $\omega=\kappa k^u$. Thus $D(s)=s-q_n s^5/180+O(q_n^2 s^9)$, including the continuous limit along the parallel ray. Solving the fractional cut before taking the difference gives
$$
 D'(C_a)(S-C_a)-(1-a)D(S)
 =\frac{q_nS^5}{180}(1-5a^4+4a^5)+O(q_n^2 S^9).
$$
Let $I_a=\int_a^1 v^3(1-v)\,dv$. At zero curvature $S=R$ in every direction. In the emitter sky $k^u=V^u(1+\mu)$ with $\mu$ uniform on $[-1,1]$, so $\langle q_n\rangle=4w/5$. For small $wR^4$ this gives
$$
 F_a=(1-a)R+\frac4{45}wR^5 I_a+o(wR^5),
 \qquad c_a=-\frac4{45}R^5 I_a+o(R^5).
 \tag{2}
$$
The differentiated expansion follows from analytic dependence on the small parameter $\kappa^2(V^u)^2 R^2$ of the exact regular geodesic, waist and cap equations and of the implicit return time. The isometries and a rescaling of lengths make $F_a/R$ a function of that parameter alone for each fixed fraction. Its series begins with the constant and the displayed quadratic term. Every fixed pair of fractions therefore has $c_a c_b>0$ for sufficiently weak nonzero curvature. At $a=1/3$, $b=1/2$ the limiting coefficients in units $R^5$ are $-232/54675$ and $-13/3600$.

For later use, the full differential in local coordinates can be written as a sum of integrals of metric jets of orders at most two against finite, compactly supported signed measures. Its **only order-two point mass** is the principal part of (1). Indeed the unintegrated Jacobi variation integrates the tidal variation with bounded weights in affine parameter and launch direction, split at $C_a$. Interior points on each regular ray have zero mass under its affine integration, as do the collapsed vertex and the endpoints. The integrals against the connection vary at most one metric derivative. The direct metric insertion on the return ray has order zero. The timelike geodesic and the orthonormal initial frame use at most one derivative except for (1). The linear combination imposing fixed $M$ has all these same properties. This representation keeps the two curvature derivatives on the test metric, which makes counting atomic masses independent of chartwise integrations by parts. [Optical and observer adjoints, Eqs. (1)–(5)](weak-curved.md)

## What survives at short timing resolution

Use independent smooth compact probability windows $h^{-1}f(t/h)$ and $h^{-1}g(t/h)$. For the delay of the second reading relative to the first let $\eta(s)=\int f(t)g(t+s)dt$ and $\eta_h(s)=h^{-1}\eta(s/h)$. Denote the Einstein bracket of the windowed readings by $B_h$ in the order $a,b$. Each is a differentiable measurement with respect to smooth perturbations and its reduced causal pairing exists at positive $h$. At fixed nonzero curvature the result is
$$
 \boxed{\displaystyle
 \lim_{h\downarrow0}h^6 B_h
 =\frac{32}{5}G_N w\,c_a c_b\,\eta^{(5)}(0).}
 \tag{3}
$$

Here is an estimate excluding cancellation by the other parts of the two clocks. Smooth the causal kernel in its second argument along $\Phi_s$ with density $\eta_h$, transporting its tensor indices. For derivatives of total order $m\le4$ at the two ends, on the common compact set one has
$$
 |\partial^m E_h(x,y)|\le C_m h^{-m-2},\qquad
 \partial^m E_h(x,y)=O_{x,y}(h^{-m-1})\quad(x\ne y).
 \tag{4}
$$
For the second estimate, away from the diagonal the direct Hadamard term is a delta on a smooth null front. At a crossing its defining function has a nonzero derivative along the timelike sweep. Each derivative raises its possible delta order by one. The smooth interior coefficient times the step across the front has lower order. These estimates are uniform on compact subsets away from the diagonal. The causal propagator includes both time directions. [Rosen direct front and tail](weak-rosen-green.md)

For the first bound it suffices to work near the diagonal in a short spacelike Cauchy chart. On the two null-frequency branches the local wave kernel is a sum of oscillatory integrals in three spatial frequencies with amplitudes of order $-1$, modulo a smooth kernel. In the Cauchy evolution the two eikonal branches have order-zero transport and the initial velocity jump divides by their frequency separation of order $|\xi|$; tensor parallel transport is order zero. Each endpoint derivative adds at most one frequency power. Along $\Phi_s$ the phase derivative has magnitude at least $c|\xi|$, since its endpoint covector is null and the sweep is uniformly timelike. Integrate by parts in $s/h$ at high frequency. For any sufficiently large $N$ the absolute bound is a constant times
$$
 1+\int_1^\infty r^{m+1}(1+hr)^{-N}dr=O(h^{-m-2}).
$$
The low-frequency part is bounded. This is a local parametrix estimate, made uniform by a finite cover; it applies to the wave operator on tensors because the principal symbol is scalar. [Duistermaat and Hörmander, Fourier integral operators II](https://doi.org/10.1007/BF02392165) · [Capoferri, Dappiaggi and Drago, wave parametrices](https://arxiv.org/abs/2001.04164v4)

Multiply (4) by $h^6$ and integrate against the product measures in the two sources. Orders $m<4$ tend uniformly to zero. For $m=4$, distinct spacetime points give zero in the limit even when null related. The product of two finite measures charges their common diagonal only through shared atoms. Bounded convergence leaves just (1) at the common launch point. This argument includes both cone faces, both fractional cuts, the waist and the constraints on the emitter. It does not assume that two unsmeared currents have a defined pointwise product.

At this remaining point the leading symbol is the flat massless graviton kernel in an orthonormal emitter frame. In the same local representation, rescale spatial frequency by $1/h$ and set the delay to $hs$ at equal base points. The homogeneous phase equals its frozen Minkowski linearization to error $O(h)$ at fixed rescaled frequency, and only the principal amplitude and the four differentiated phases survive. The preceding rapid-frequency bound permits the limit after the smooth $s$ integration, with a separate arbitrarily small low-frequency ball. The principal symbol of the Weyl variation kills pure gauge modes. Equivalently the trace-reversed Einstein tensor contraction on null conserved symbols is the sum over the two unit-norm transverse traceless (TT) polarizations. For a direction $n$ write $\Pi_n$ for TT projection and $J_n$ for the unit quarter-turn of the two transverse polarizations induced by the spatial dual on one index. A mode of angular frequency $k$ has $\delta E=k^2 h^{\rm TT}/2$ and $\delta B=\pm J_n\delta E$. Consequently the squared contraction of $\delta\mathcal W=2(E:\delta E+B:\delta B)$ has angular average
$$
 k^4\left\langle|\Pi_n E\pm J_n^T\Pi_n B|^2\right\rangle
 =\frac25 k^4(E:E+B:B)=\frac25 k^4 w .
$$
The interference integrates to zero under $n\mapsto-n$. The average TT projector is $2/5$ of the identity on the five-dimensional space of symmetric trace-free tensors, by rotational invariance and its rank two. With the later observable in the second slot the scalar kernel has the positive sine sign. Including the $32\pi G_N$ Einstein normalization, the leading distribution in delay is
$$
 32\pi G_N\frac{4\pi}{(2\pi)^3}\frac{2w}{5}
    \int_0^\infty k^5\sin(k s)dk
 =-\frac{32}{5}G_N w\,\delta^{(5)}(s).
$$
Indeed the fifth derivative of $\int_0^\infty\cos(ks)dk=\pi\delta(s)$ has integrand $-k^5\sin(ks)$. Testing the derivative of delta and multiplying by $c_a c_b$ gives (3). [Einstein–Hilbert propagator convention](weak-rosen-green.md) · [Fewster and Hunt, gravitational observables and test tensors](https://arxiv.org/abs/1203.0261v4)

## Identical timestamps with unequal responses

For an explicit choice of window shapes, take an even smooth probability bump $d$ supported in $[-1,1]$ and an even smooth probability density $f_0$ supported in $(-2,2)$ that is a positive constant on $[-1,1]$. Put $f=(f_0+d)/2$ and $g=f+\varepsilon d^{(5)}$. For sufficiently small $|\varepsilon|$ both are nonnegative. Integration by parts shows that their moments of orders zero through four agree, including their zero means and identical variances. The correlation of $f$ with itself is even and $f_0$ is constant on the support of $d$, so
$$
 \eta^{(5)}(0)=\varepsilon\int f d^{(10)}dt
 =-\frac{\varepsilon}{2}\int (d^{(5)})^2dt .
$$
Either sign occurs while both windows have the same support, moments through order four and nominal proper time. Thus these clocks have no finite equal-time limit independent of their individual timing windows. At caps $1/3$ and $1/2$ the leading weak-curvature value of the multiplier in (3), divided by $G_N w R^{10}$, is $6032/61509375$. Even delay densities eliminate this leading term. For identical filters a mixed point and optical contribution still forces divergence at each sufficiently weak fixed curvature. Its weak-wave coefficient scales as $h^{-3}$. [Identical filters at fixed strength](fixed-strength-contact.md) · [Weak-wave coefficient](synchronized-contact.md)

The same estimate tests a change to the apparatus. Average the launch superenergy with a fixed smooth unit-mass weight along a short proper-time segment of the trial observer's geodesic ending at launch, then solve the boost condition. Include that segment in the swept causal neighborhood. On the symmetric wave the observer is parallel along its geodesic and the measured $\mathcal W=4\kappa^4(V^u)^4$ is constant on it. Thus both the background calibration and its regular boost derivative are preserved. The order-two curvature insertion in its differential now integrates along proper time. The varied geodesic and tangent involve at most one metric derivative and the finite segment has no order-two point mass. The isometry argument for conservation still applies to the entire marked preparation. Equation (4) therefore gives $h^6 B_h\to0$ at fixed calibration duration for every pair of timing windows in this modified experiment. It leaves possible lower-order contacts to be calculated. The inverse sixth-power obstruction diagnoses the pointwise preparation. The superenergy measurement is an extra choice of emitter preparation beyond the optical clock specified in v1. An intrinsic isolated-diamond phase space or quantum entropy claim requires separate evidence.

Run `python3 -B checks/local_curved_bracket.py` and `make check` from the repository root. The focused check differences exact two-cone readings at nearby wave strengths after rescaling to common weighted radius, integrates both TT polarizations over the emitter sky, and checks the rational weak-wave coefficient. Its optical derivatives use finite angular quadrature. An independent sign check integrates the sine transform for a centered Gaussian mixture at two timing widths and compares with the fifth derivative of its delay density. Equation (4) supplies the analytic limit for the rest of the distribution. [Executable check](../checks/local_curved_bracket.py)

~~~text
Weak-wave launch coefficients at caps 1/3 and 1/2: -232/54675 -13/3600
Direct matched-radius derivatives, kappa=0.35: -0.004242823, -0.003610947
Direct matched-radius derivatives, kappa=0.20: -0.004243210, -0.003611094
Angular TT norm / superenergy: 0.40000000
Gaussian delay test, scaled fifth derivative: -0.19630477
Weak h^(-6) coefficient / (G W R^10 eta^(5)(0)): 6032/61509375
~~~
