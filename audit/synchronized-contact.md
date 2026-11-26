# Synchronized timing windows for two cap clocks on the same weak plane wave

Two distinct caps on one curvature-calibrated Rosen diamond have a negative classical bracket in order of increasing cap fraction when both use the same sufficiently narrow timing window and the wave is sufficiently weak for that width. In the expansion in wave curvature, the first nonzero coefficient grows as the inverse cube of the width. Its sign holds for every ordered pair of interior cap fractions and every smooth compact probability window, including asymmetric shapes. The order of limits is part of the result. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27)

## Common preparation and the weak-wave coefficient

Use the symmetric Rosen plane wave with scale factors $\cosh(\kappa u),\cos(\kappa u)$, a convex causally compatible observation patch and the ambient Einstein causal propagator with no contributing winding images. Both clocks use the same emitter, orthonormal trial pair, rapidity calibration $\mathcal W=E:E+B:B=w$ at launch, geodesic observer and return condition $M=\langle D(S)^2\rangle/\langle D(S)\rangle=R$. Here $E,B$ are the electric and magnetic parts of the Weyl curvature, $D$ is the optical area radius, and $S$ is the outgoing affine coordinate of the waist. For fraction $a$ the cut obeys $D(C_a)=aD(S)$. Read the average of $D'(C_a)(S-C_a)$ weighted by $D(S)$. Sweep the entire calibration and both clocks by proper time along the timelike Killing flow on the central observer. Denote the Einstein bracket in cap order $a,b$ by $B_{ab}(\lambda,h)$, for an identical window $h^{-1}f(t/h)$ on both. The profile $f$ is smooth, compactly supported, nonnegative and has integral one. Set $\eta(s)=\int f(t)f(t+s)dt$. [Calibration and ambient domain](local-curved-bracket.md) · [Plane-wave metric propagator](weak-rosen-green.md)

To vary the strength, put $\kappa^2=\lambda\kappa_0^2$ and set $w_\lambda=\lambda^2 w_0$, with $w_0>0$, so that the background emitter rapidity stays fixed. At each positive strength, hold the given $w_\lambda$ fixed when differentiating the observations with respect to the gravitational perturbation. Write $W$ for the constant Weyl tensor of the tangent wave in the limiting inertial frame, $w_0=E_W:E_W+B_W:B_W$. For each $h>0$ small enough to stay inside the patch, define $B^{(2)}_{ab}(h)=\lim_{\lambda\downarrow0} B_{ab}(\lambda,h)/\lambda^2$. Put
$$
 c_a=-\frac{R^5}{225}(1-5a^4+4a^5),\qquad u_a=\frac{R^2}{6}(1-a)^2 .
$$
Then
$$
 \boxed{\lim_{h\downarrow0} h^3 B^{(2)}_{ab}(h)
    =\frac{16}{5}G_N w_0(c_a u_b-c_b u_a)\,\eta''(0).}                  \tag{1}
$$
In particular the multiplier of $G_Nw_0 R^7\eta''(0)$ is $238/820125$ at $a=1/3,b=1/2$. For all $0<a<b<1$, factor $1-5a^4+4a^5=(1-a)^2(1+2a+3a^2+4a^3)$. The last factor is strictly increasing, so $c_a u_b-c_b u_a>0$. Integration by parts gives $\eta''(0)=-\int (f')^2<0$. Reversing the caps reverses the bracket.

## Optical and point curvature sources

For an outgoing ray of tangent $l=(1,n)$ in the limiting emitter frame let $Q_{AB}=-C_{AlBl}$ in a parallel orthonormal screen. The vacuum focusing equation for the area radius and trace-free optical deformation matrix $\sigma$ is $D''=-D\,\sigma:\sigma/2$. Twice integrating from the cap gives the exact vacuum identity
$$
 D'(C_a)(S-C_a)-(1-a)D(S)
  =\frac12\int_{C_a}^S(S-v)D(v)\,\sigma(v):\sigma(v)\,dv .
$$
The averaged left side gives the clock excess over the constant $(1-a)R$. In this form its optical and return weights have zero first variation contribution at flat space. In particular, the waist and cap are allowed to move. The off-shell Raychaudhuri expression contains an additional Ricci integral. Its derivative on vacuum backgrounds vanishes on all linearized vacuum solutions. The shear expression gives the same on-shell differential and reduced causal pairing. [Matched-radius Hessian](joint-flat-hessian.md) · [Linearized Einstein observables](https://arxiv.org/abs/1203.0261v4)

The linear shear equation $(t^2\sigma)'=t^2 Q$ gives $\sigma_W(v)=v Q_W/3$ for the reference wave. Vary the shear of the other slot by a linear vacuum perturbation $Z$, use the flat values $C_a=aR$, $S=R$, and exchange the two affine integrals. The fixed-rapidity optical contribution to the limit of the differential divided by $\lambda$ is
$$
 O_a[Z]=\left\langle\int_0^R K_a(t)Q_W(n):Q_Z(t,tn)\,dt\right\rangle,
 \qquad K_a(t)=\frac{t^2}{6}\big[R-\max(aR,t)\big]^2 .                  \tag{2}
$$
The launch calibration contributes $c_a P[Z]$, where $P[Z]=2(E_W:E_Z+B_W:B_Z)$ at the launch point. Indeed the exact multiplier is $-\partial_\chi F_a/\partial_\chi\mathcal W$, where $F_a$ is the matched-radius clock before its boost is solved. At fixed $R$, the exact clock depends on the boost only through $w$ on this background. Its expansion is $(1-a)R-c_a w+o(wR^5)$ with a differentiated expansion, so the ratio tends to $c_a$. The derivative of the measured curvature at fixed boost equals $\lambda P[Z]+O(\lambda^2)$, including orthonormalization. The calibration branch is used at each positive $\lambda$. [Exact optical boost derivative](local-curved-bracket.md)

At fixed timing width the causal pairing of the two limiting sources $c_a P+O_a$ and $c_b P+O_b$ computes $B^{(2)}_{ab}(h)$. Here is why this perturbative coefficient transfers to the actual clocks. Use the on-shell-equivalent shear expression as an off-shell extension, taking the trace-free part of the full optical matrix. The geodesic, screen, Jacobi and two-tip cut equations depend smoothly on $\lambda$ on compact affine and angular domains, split at the cap. The shear vanishes at $\lambda=0$. At fixed trial rapidity its metric variation and the differentiated frame and optical weights have smooth parameter kernels up to this limit, using the regular Jacobi initial data at the vertex. The curvature multiplier above has a removable limit. These facts give the rescaled source on fixed parameter domains through finitely many metric jets, with bounded coefficients converging to (2) and the point term on shell. The time correlation at fixed $h$ smooths the Einstein kernel in both spatial arguments. Near the diagonal its two null-frequency phases have derivative in the timelike sweep bounded below in magnitude by a constant times frequency, uniformly for small $\lambda$. Integration by parts against the smooth window gives arbitrary inverse powers, also after endpoint differentiation. The local eikonal phases and transports for short time depend smoothly on $\lambda$. Off the diagonal the direct wavefront crosses the timelike sweep transversally; its coefficient and the tail have the same smooth parameter dependence. Thus the smoothed kernels converge with all the finitely many required endpoint derivatives. Inserting the limiting sources can equivalently use the flat on-shell transverse traceless modes. The exact point against point pairing vanishes at every positive width and strength because the two slots contain multiples of the same swept local measurement. [Timelike smoothing estimate (4)](local-curved-bracket.md) · [Harte, tensor Green function on a plane wave, §IV](https://arxiv.org/abs/1309.5020v2)

## A delay density at the launch point

A flat unit-norm transverse traceless plane mode of frequency $k$ and propagation direction $m$ has electric amplitude $k^2 H/2$ and magnetic amplitude given by the same norm in the dual polarization. On the ray $(t,tn)$ its phase advances by $kqt$, $q=1-n\cdot m$. In a screen vector $e$ the plane-wave curvature uses the spatial vector $q e+(m\cdot e)n$ in the contraction with $H$. After projection perpendicular to $m$, these two transformed screen axes are orthogonal with length $q$. Thus $|Q_Z(n)|^2=k^4q^4/4$ for each unit polarization.

The sky integral and the mode-direction integral are rotation invariant. Their contraction can therefore average the orientation of the fixed type-N tensor $W$. Each of $E_W,B_W$ has squared norm $w_0/2$ and their inner product vanishes. The rotation-averaged second moment on the two copies of the five-dimensional space of trace-free symmetric spatial tensors is $(w_0/10)\mathrm{Id}$ with zero cross term. Writing $L_n W=Q_W(n)$, it follows that the averaged product of $P[Z]$ and $Q_W(n):Q_Z(n)$ is $(w_0/5)|L_n Z|^2$. Summing both polarizations gives $w_0 k^4 q^4/10$. The remaining angular measure is $dq/2$ on $0<q<2$.

For the optical source in the second slot define the geometric delay $y=qt$. Its weighted density, omitting the factor $w_0 k^4/10$, is
$$
 \rho_a(y)=\frac{y^4}{2}\int_{y/2}^R K_a(t)t^{-5}dt,\qquad 0<y<2R.
$$
For $0<y<2aR$ the affine kernel below $aR$ is $u_a t^2$. Thus $\rho_a(y)=u_a y^2+v_a y^4$ there for a finite constant $v_a$. With the later observable in the second slot, the causal mode factor has the positive sine sign and radial normalization $(16G_N/\pi) k\,dk$. Let $\eta_h(y)=h^{-1}\eta(y/h)$. Fourier inversion gives $\int_0^\infty k^5|\widehat f(hk)|^2\sin(ky)\,dk=-\pi\eta_h^{(5)}(y)$. At sufficiently small width the support of this derivative lies within the polynomial region on the positive axis, so
$$
 -\int_0^{2R}\rho_a(y)\eta_h^{(5)}(y)dy
   =2u_a\eta_h''(0)+24v_a\eta_h(0).
$$
Antisymmetry subtracts the term with the cap labels exchanged. This produces the even contact in (1), proportional to the second derivative of the timing density at zero. [Einstein normalization and retarded sign](weak-rosen-green.md)

The two optical integrals have smaller joint growth. Extend $K_a$ by zero outside $[0,R]$. It is continuous and its second distributional derivative is a finite measure. Its Fourier transform is bounded by a constant times $(1+kq)^{-2}$. The unit-mode tidal insertion is bounded by a constant times $k^2q^2$ at every angle. Equation (2) therefore has uniformly bounded amplitude on each mode, at all frequencies. Their joint radial pairing against $k|\widehat f(hk)|^2$ is $O(h^{-2})$, which vanishes after scaling by $h^3$.

For every sufficiently narrow common window, (1) gives a negative coefficient and hence a strictly negative bracket of the actual readings for all sufficiently small nonzero strengths at that width. Equivalently no bound $|B_{ab}(\lambda,h)|\le Cw_\lambda$ holds throughout a joint neighborhood of zero width and strength. A separate analysis of the causal kernel establishes divergence in magnitude for each sufficiently weak fixed nonzero curvature. The sign and leading power at fixed strength remain open. [Fixed-strength proof](fixed-strength-contact.md) The result concerns the ambient classical bracket; an isolated-diamond reduction and a quantum clock would require their own domains.

## Reproduction

Run `python3 -B checks/synchronized_contact.py` from the repository root, then `make check` for the suite. The check directly rotates plane-wave electric and magnetic tensors, contracts both screen curvatures, evaluates the rational coefficient, and integrates the affine and angular variables with identical Gaussian windows. The Gaussian has exponentially small tails in this numerical cross-check. [Executable](../checks/synchronized_contact.py)

~~~text
Direct two-polarization contractions: w0 q^4/10
Common-window h^(-3) contact / (G w0 R^7 eta''(0)): 238/820125
Gaussian mixed term / leading contact, h=0.020: 1.01722803
Gaussian mixed term / leading contact, h=0.010: 1.00430701
Gaussian mixed term / leading contact, h=0.005: 1.00107676
~~~
