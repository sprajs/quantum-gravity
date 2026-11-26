# What could a light beam and a clock measure?

A circular pencil of light can arrive as an ellipse even when the central pulse returns at precisely its flat-space time. In an explicit vacuum gravitational wave, the spot's ellipticity is linear in tidal curvature. The reduction of its area at fixed radar range is quadratic. Moving the receiver until the spot reaches a prescribed area then requires a longer range. This gives an operational example of the classical focusing underlying Venkatesa Chandrasekaran’s diamond clock. The same experiment has the same classical prediction in Einstein gravity. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.25)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E25) · [Harte, exact optics in plane waves](https://arxiv.org/abs/1502.03658)

## The range, the screen and the waveform

Place an emitter and an axial reflector on freely falling worldlines. At a recorded proper time the emitter launches a narrow circular cone of rays with calibrated solid angle $d\Omega$ in its own frame. At the far end a calibrated screen measures the proper transverse area $dA$ and the ellipse axes. An immediate reflection of the central ray gives a round-trip radar range $L_{\rm rad}=c(\tau_{\rm return}-\tau_{\rm launch})/2$ from the emitter’s one clock. The optical area distance is $D=\sqrt{dA/d\Omega}$. Geometric optics, infinitesimal aperture and negligible apparatus gravity are assumed. Realizing the screen and the angle calibration with finite resolution would be a separate experimental problem.

Use an exact plane wave in length coordinates $u=(ct-z)/2$, $v=ct+z$,

$$
ds^2=-2\,du\,dv+dx^2+dy^2+q(u)(x^2-y^2)\,du^2 .
$$

The transverse Laplacian of the last coefficient vanishes, so the wave is Ricci flat. Choose a profile with a positive constant plateau $q(u)=q$ for $0\le u\le L$. It can taper smoothly to zero outside the sampled interval. On the axis $x=y=0$ the metric is Minkowskian and all its first derivatives vanish. The emitter at $z=0$ and reflector at $z=-L$ are therefore exact timelike geodesics with proper time $t$. Launch at $t=0$. The central outward ray has $z=-ct$, hence $u=ct$, and the return ray has constant $u=L$. It arrives at $t=2L/c$, giving **exactly** $L_{\rm rad}=L$ for any profile. This equality between an affine length and the radar range uses the axial geometry and the emitter normalization. Other orientations and worldlines require their own light propagation calculation.

## Two measurable effects with different powers of curvature

On the outward ray, a small launch angle $\delta\theta_i$ produces a proper displacement $J_i(u)\delta\theta_i$ on the transverse screen, with $J_i(0)=0$ and $J_i'(0)=1$. The transverse geodesic equations give $J_x''=qJ_x$ and $J_y''=-qJ_y$. Thus, writing $k=\sqrt q$,

$$
J_x=\sinh(ku)/k,\qquad J_y=\sin(ku)/k,\qquad
D=\sqrt{J_xJ_y},\qquad e=\frac{J_x-J_y}{J_x+J_y}.
$$

Here $e$ is the signed ellipticity referred to the two polarization axes. Interchanging them reverses its sign. Use a short, expanding segment before any caustic. With the dimensionless tidal strength $a=qL^2$ the axis lengths in units of $L$ are $1\pm a/6+a^2/120+O(a^3)$. It follows that

$$
e=\frac a6+O(a^3),\qquad
1-\frac DL=\frac{a^2}{180}+O(a^4)=\frac{e^2}{5}+O(e^4).
$$

At small curvature the two axes stretch and contract by equal first-order amounts. Their product reveals the remaining focusing. The fractional **spot area** deficit is $1-D^2/L^2=a^2/90+O(a^4)$. For a fixed target optical distance $D_0$ instead, the required radar range becomes $L=D_0+q^2D_0^5/180+O(q^4D_0^9)$. The reflector location changes in this comparison. A stationary reflector at the original range records the same central echo time as before.

The ratio $1/5$ depends on the profile. For any weak, fixed-polarization $q(s)$ in this axial geometry, the first-order optical shear eigenvalues are $\pm b(s)$. The Jacobi equations give $(s^2 b)'=s^2q(s)$ with a regular vertex. Vacuum Raychaudhuri then gives the leading area-distance deficit,

$$
b(s)=s^{-2}\int_0^s t^2q(t)\,dt,\qquad
L-D(L)=\int_0^L(L-s)\,s\,b(s)^2\,ds+O(L\alpha^4),
\quad \alpha=L^2\sup_{[0,L]}|q|.
$$

The even remainder follows because reversing this entire profile interchanges the two axes. A final ellipse alone does not determine the shear history of a general wave. Matter on the ray adds the Ricci term $R_{ab}k^ak^b$ to the focusing equation, where $k^a$ is the affine tangent.

## The finite cap in the manuscript

Choose a cap on the expanding ray by the measured radius ratio $D(u_0)=\epsilon D(L)$, $0<\epsilon<1$. On this ray the manuscript’s cap-normalized reading is $u_*=D'(u_0)(L-u_0)$. An ideal array sampling the same outgoing cone at neighboring radar ranges can infer the cap slope $D'(u_0)$. In general the slope and interval separately depend on the affine normalization. Their product is invariant under affine rescaling. The fiducial solid angle is the emitter's calibrated solid angle here. [Clock definition (3.27)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Null data and affine derivation](03-2.md)

Twice integrating $D''=-D\sigma_{AB}\sigma^{AB}/2$ gives the excess above a shear-free cone with the same endpoint optical distance and cap fraction. On the constant plateau $b(s)=qs/3$ to first order, $\sigma_{AB}\sigma^{AB}=2b^2+O(s^{-2}(qs^2)^4)$ and $u_0=\epsilon L+O(La^2)$. Hence

$$
\begin{aligned}
u_*-(1-\epsilon)D(L)
&=\tfrac12\int_{u_0}^L(L-s)D(s)\sigma_{AB}\sigma^{AB}(s)\,ds\\
&=\frac{La^2}{180}(1-5\epsilon^4+4\epsilon^5)+O(La^4).
\end{aligned}
$$

This is a reconstructed reading on one generator. The full diamond clock in (3.28) requires a closed intersection cut, a cap prescription on each generator, and the $\varrho_S$-weighted angular average. The next calculation supplies those data. [Clock average (3.28)](https://arxiv.org/html/2611.34924v1#S3.E28)

## The full diamond from two events on one clock

Take both tips on the emitter’s geodesic, separated by proper time $2L/c$. Its outgoing light cone and the earlier light cone of the second tip intersect in a closed waist $S$ for $|a|=|q|L^2\ll1$. Operationally, a transponder at the waist receives the first tip’s flash and can send a flash that reaches the emitter at the second tip. Every point on this waist has the same round-trip radar range $L$, although the optical distance $D_S$ varies over the sky. Measuring $u_*$ off axis also requires the affine length along the ray. An ideal network can reconstruct it from infinitesimal local distances and photon frequencies. If $k=dx/ds$ has $-k\cdot U_{\rm launch}=1$ with unit four-velocities, the local spatial path length in a receiver's rest frame is $d\ell=(-k\cdot U_{\rm rec})ds=(\nu_{\rm rec}/\nu_{\rm launch})ds$. A single echo alone supplies only the round-trip range.

For a launch direction $\mathbf n$ in the emitter's frame, let $\beta=(1-n_z)/2$. The affine tangent has constant $du/ds=\beta$. The exact transverse tidal eigenvalues are $\pm q\beta^2$. For $\beta>0$ a parallel screen basis modulo the tangent is $\partial_i+(dx^i/du)\partial_v$. Its transverse metric is the identity, and contracting the curvature with the tangent twice supplies the factor $\beta^2$. The parallel direction $\beta=0$ follows by continuity. At leading order the waist affine distance is $s_S=L+O(La)$. In the quadratic single-ray excess above one can therefore set $s_S=L$ and use the zeroth-order angular weights. For a sky average $\langle\cdot\rangle=\int d\Omega\,(\cdot)/(4\pi)$, $\langle\beta^4\rangle=\int_0^1\beta^4d\beta=1/5$. With $B_\epsilon=1-5\epsilon^4+4\epsilon^5$, the manuscript's weighted average obeys

$$
\bar u_*-(1-\epsilon)\frac{\langle D_S^2\rangle}{\langle D_S\rangle}
=La^2\frac{B_\epsilon}{900}+O(La^4).
$$

The correction is even in $q$ because interchanging the transverse axes preserves these integrated scalar readings. The smooth small-diamond expansion is taken at a fixed cap fraction. Comparing directly to the area radius $\sqrt{\mathscr A/(4\pi)}=\sqrt{\langle D_S^2\rangle}$ introduces a second effect, the angular variation of the waist itself.

To calculate that variation, put $S_x(u)=\sinh(ku)/k$ and $S_y(u)=\sin(ku)/k$. The outgoing ray has transverse coordinates $x_i=n_iS_i(u)/\beta$. On each leg the null condition gives $2\,dv/du=d(\sum_i x_i\,dx_i/du)/du$. Matching the two cone solutions at the waist, with $(u,v)=(L,2L)$ at the second tip, gives

$$
4L=\frac{1}{\beta^2}\sum_{i=x,y} n_i^2
         \frac{S_i(u)S_i(L)}{S_i(L-u)}.
$$

Expanding this equation about $u=\beta L$ yields
$s_S/L=1-a(n_x^2-n_y^2)/12+O(a^2)$. Since $D_S=s_S+O(La^2)$ and $\langle(n_x^2-n_y^2)^2\rangle=4/15$, the variance of $D_S$ is $L^2a^2/540+O(L^2a^4)$. The difference $\langle D_S^2\rangle/\langle D_S\rangle-\sqrt{\langle D_S^2\rangle}$ is this variance divided by $2L$ to leading order. The **full clock excess above the manuscript’s area-radius bound** is consequently

$$
\boxed{\displaystyle
\bar u_*-(1-\epsilon)\sqrt{\mathscr A/(4\pi)}
= L(qL^2)^2\left(\frac{1-5\epsilon^4+4\epsilon^5}{900}
                  +\frac{1-\epsilon}{1080}\right)+O\big(L(qL^2)^4\big).}
$$

For a half-radius cap, the coefficient is 0.00136574. The first contribution is accumulated focusing and the second comes from the anisotropic waist. This prediction uses one explicitly specified vacuum solution, both tips, the full cut and the manuscript's averaging measure. [Manuscript’s clock and area bound](https://arxiv.org/html/2611.34924v1#S3.E28)

## Size and comparison with observations

For a weak, plus-polarized sinusoid of strain amplitude $h$ and frequency $f$, the maximum counter-propagating tidal coefficient in our normalization is $|q|=2h(2\pi f/c)^2$. To see the factor of two, write $h_{xx}^{\rm TT}=h\cos[(2\pi f/c)(ct-z)]$. In these null coordinates the linearized curvature gives $q=\tfrac12\partial_u^2h_{xx}^{\rm TT}$. At a curvature extremum, $L=4\,\mathrm{km}$ spans a wave phase of only $4\pi f L/c=0.0168$ radians for $f=100\,\mathrm{Hz}$, so the plateau is a local approximation. The example uses $h=10^{-21}$. The LIGO–Virgo discovery paper reported a peak strain of this order and a frequency sweep of 35–250 Hz for GW150914. Its detectors measured differential interferometer strain. The values below are calculated for the axial screen and the closed diamond with the same radar range. [GW150914 discovery paper](https://arxiv.org/abs/1602.03837)

| Quantity | Calculated value |
|---|---:|
| Tidal coefficient near a wave extremum, $\lvert q\rvert$ | $8.79\times10^{-33}\,\mathrm{m}^{-2}$ |
| Magnitude of spot ellipticity, $\lvert e\rvert$ | $2.34\times10^{-26}$ |
| Fractional area-distance deficit, $1-D/L$ | $1.10\times10^{-52}$ |
| Optical distance deficit, $L-D$ | $4.39\times10^{-49}\,\mathrm m$ |
| Full-diamond clock excess above its area-radius bound, $\epsilon=1/2$ | $1.08\times10^{-49}\,\mathrm m$ |
| Fixed-endpoint central round-trip time shift | Exactly zero in this geometry |

An actual astronomical measurement of image shear uses correlated galaxy shapes. The Dark Energy Survey year-three analysis used over 100 million galaxies and reported a signal-to-noise ratio of 40 using all angular scales, 27 with the fiducial cuts, and 31 with the optimized cuts. That result concerns lensing by intervening cosmic structure. Neither it nor GW150914 measures the quadratic vacuum beam-area signal in this table. [Amon et al., DES Year 3 cosmic shear](https://arxiv.org/abs/2105.13543)

A direct comparison of quantizations would need a predicted difference, such as a change in the mean or covariance of $D/L_{\rm rad}$ or $e$ for a specified preparation, beam aperture, pulse duration and detector. The ordinary GR or low-energy quantum-gravity baseline must use the same boundary conditions and readout. A shared classical focusing law, a finite-dimensionality conjecture and a regulated vacuum shear variance each leave the size and even the sign of that difference open. No sensitivity to a quantization-specific parameter follows from the table. [Semiclassical backreaction audit](06-2.md) · [Shear composite and resolution](shear-uv.md)

Run `python checks/observable_optics.py` from the repository root. The check evaluates both Jacobi axes to high precision, locates each cap by its area, and compares the resulting clock excess with the perturbative coefficient. Expect a weak-profile deficit-to-squared-ellipticity ratio of 0.200000000000, a normalized excess of 0.004513888889 for $\epsilon=1/2$, and $D/L=0.994433359$ for $qL^2=1$. A separate numerical intersection of both exact cones gives the full-diamond coefficient 0.00136574 at the half-radius cap. [Executable calculation](../checks/observable_optics.py)
