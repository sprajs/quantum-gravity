# The spherical clock Hessian as a distributional Einstein wave

On a unit-radius flat diamond, the response to a smooth quadrupole with nonzero first-order optical shear at the cap rim has a finite jump in the metric and a Dirac measure in the canonical momentum. Both lie on a spherical wavefront. A single explicit radial integral gives the response to every compactly supported master profile of the chosen quadrupole. Its Einstein symplectic pairing reproduces both sharp-rim packet limits, including the response to a reference wave whose first five optical slope coefficients vanish. The calculation concerns the Hessian of the averaged affine clock at its flat critical point. [Chandrasekaran, arXiv:2611.34924v1, (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Vacuum preparation and Hessian](joint-flat-hessian.md) · [Opposed packets](match-packets.md)

## The physical test space and its symplectic normalization

Use the point tips at $t=0,2$, the waist disk $t=1$, the angular labels of the first tip and the matched-radius preparation. Write $s=v$ on the flat lower cone, let the cap ratio be $0<a<1$, and put $f(s)=F(2s)$. The prescribed smooth reference and test profiles $f_W,f_Z$ belong to $C_c^\infty(0,1)$. The spatial metric variation $h_F$ is generated from the regular scalar wave $\phi_F=[F(t+r)-F(t-r)]/r$ by the order-four transverse-traceless (TT) operator in the [spherical wave construction](joint-flat-hessian.md). Its fixed polarization is $S=\mathrm{diag}(-1/2,-1/2,1)$. If $B(n)$ is the trace-free projection of $S$ onto the screen perpendicular to the unit vector $n$, then $\langle B:B\rangle=3/5$. The symbol of the operator is $|k|^4 B(k/|k|)$.

Orient the Einstein form by $\Omega=D\pi^{ij}\wedge Dh_{ij}$ integrated over the disk, with $K_{ij}=\dot h_{ij}/2$ at first order. Use a single continued spacetime field and frame across the cap and null sheet. Their joined current agrees with that disk integral. The test vanishes in a collar of the waist and outside the disk on $t=1$, so the TT pairing is
$$
 \Omega(X,Z)=\frac{1}{32\pi G_N}\int_{\mathbb R^3}
       (\dot h_X:h_Z-\dot h_Z:h_X)\,d^3x .
$$
In spatial Fourier variables both scalar factors are radial. Angular integration thus replaces the product of TT symbols by $(3/5)|k|^8$. The two factors of $|k|^4$ can be applied as $\Delta^2=\partial_t^4$ on each scalar solution. For masters $U=F_X^{(4)}$, $V=F_Z^{(4)}$, write $U_\pm=U(1\pm r)$ and similarly for $V$. After radial integration the terms with unlike phases integrate to the boundary values of $U_-V_+-U_+V_-$. They vanish at the center and outside the test. The same-phase terms give the ordinary line integral $\int(U'V-V'U)\,du$. The solid angle and action supply $4\pi(3/5)/(32\pi G_N)=3/(40G_N)$. Therefore
$$
 \Omega(X,Z)=\frac{3}{20G_N}\langle F_X^{(9)},F_Z\rangle_u
       =\frac{3}{5120G_N}\langle f_X^{(9)},f_Z\rangle_s .
 \tag{1}
$$
The second equality uses $du=2ds$. This argument first applies to smooth profiles, then extends by distributional duality in the first slot. A distributional response may be cut off smoothly outside $0\leq u\leq2$ when computing (1) against these tests. The full-space equality above uses the support of the test data on this particular disk. [ADM convention in a TT polarization](joint-wave.md) · [Independent normalization and ambient extension](weak-normalization.md)

## Inverting the Hessian

Write the cut strain as $G_f=Af$ and its slope as $Lf=\partial_s(Af)$, with
$$
 A=\frac{1}{16s}\partial_s^4-\frac{1}{4s^2}\partial_s^3
          +\frac{1}{4s^3}\partial_s^2,\qquad
 b(s)=s(1-s)G'_W(s).
$$
For $D=\bar u_*-(1-a)M$, the excess over the flat radius reading, $dD_{\rm flat}=0$ and
$$
 d^2D(W,Z)=\frac{3}{20}\int_a^1 b(s)Lf_Z(s)\,ds .
$$
The restricted Hamilton equation $\Omega(X_W,Z)=d^2D(W,Z)$ is exactly
$$
 \partial_s^9 f_X=256G_N\,L^*(\mathbf1_{(a,1)} b)
     =256G_N A^*\!\left[-\partial_s(\mathbf1_{(a,1)} b)\right]
        \quad\text{in }\mathcal D'(0,1).
 \tag{2}
$$
Here the star is the formal adjoint for $ds$. The derivative differentiates the sharp lower limit as well as the interior weight. Compactness of $W$ makes $b$ vanish near the waist.

Choose the primitive that vanishes for $s<a$. For $a<s<1$ it is the ordinary integral
$$
\begin{split}
 f_X(s)=-256G_N\int_a^s b(t)\bigg[
 &\frac{(s-t)^3}{16t\,3!}
  +\frac{5(s-t)^4}{16t^2\,4!}\\
 &+\frac{3(s-t)^5}{4t^3\,5!}
  +\frac{3(s-t)^6}{4t^4\,6!}\bigg]dt .
\end{split}\tag{3}
$$
Indeed the ninth derivative of $E_9(x)=x_+^8/8!$ is $\delta_0$. Transfer $L^*$ in the convolution $E_9*L^*(\mathbf1 b)$ onto $E_9(s-t)$ as $L_t$ to obtain the four terms of (3). All solutions of (2) on this open interval differ from (3) by a polynomial of degree at most eight. These homogeneous profiles have zero pairing with every compact master test in (1). Endpoint or ambient conditions can distinguish representatives. The left integration limit in (3) fixes this freedom in the profile coordinate.

The same TT operator constructs a weak spacetime solution from $F_X(u)=f_X(u/2)$. At the spatial center the scalar formula has the distributional extension $\phi_F=2\langle F'(t+n\cdot\mathbf x)\rangle_n$, the spherical average of plane waves. Each term obeys the wave equation and the spatial operator enforces the TT constraints. Equation (2) therefore gives a distributional **metric response** in this sector. At flat space the clock itself has zero first derivative on the matched-radius preparation. The nonzero response calculated here belongs to its linearized variation along $W$.

The upper face follows from $t'=2-t$. Its transformed master is $(Pf)(s)=-f(1-s)$, as one sees by substituting $t'$ in the regular scalar wave. The upper-face Hessian is the lower-face Hessian on $(Pf_W,Pf_Z)$. Time reversal sends $\Omega(PX,PZ)$ to $-\Omega(X,Z)$ by (1). Thus, if $X[W]$ is the lower-face formula (3), the upper-face response in the original time orientation has profile $-P X[PW]$. This identifies both individual Hessian responses on the common compact test space.

## What crosses the spacelike disk

Suppose $G'_W(s)=c_m(s-a)^m+O((s-a)^{m+1})$ at the cap, with $c_m\ne0$. Only the first kernel in (3) contributes at leading order. In a neighborhood of $a$,
$$
 f_X(s)=-16G_N(1-a)c_m
       \frac{m!}{(m+4)!}(s-a)_+^{m+4}
       +O((s-a)_+^{m+5}).
 \tag{4}
$$
The expansion on the right side of the cut is smooth up to the cut. For nonzero slope, $m=0$, the fourth master derivative jumps by $J=-16G_N(1-a)G'_W(a)$ from left to right. For $a<1/2$ the singular phase on the waist disk is $u=1-r$, at $r_*=1-2a$. The highest radial derivative in $h_X$ is $-B_{ij}(n)F_X^{(4)}(1-r)/r$ there. Lower derivatives of this phase and the other phase are continuous. Since $F_X^{(4)}=f_X^{(4)}/16$, the **outward** metric jump and the singular ADM momentum density in Cartesian coordinates are
$$
 [h_{ij}]_{r_*}=-\frac{G_N(1-a)G'_W(a)}{r_*}B_{ij}(n),
 \qquad
 (\pi^{ij})_{\rm sing}
   =\frac{(1-a)G'_W(a)}{32\pi r_*} B^{ij}(n)\,\delta(r-r_*).
 \tag{5}
$$
At $a=1/3$ and unit slope these are $-2G_N B_{ij}$ and $B^{ij}\delta(r-1/3)/(16\pi)$. The shell delta in (5) is a radial delta under $d^3x=r^2dr\,d\Omega$. Its sign follows from the first-slot convention in (1).

Within this compact-test preparation the response has locally finite ordinary TT energy at the rim wavefront exactly when $G'_W(a)=0$. A nonzero jump puts a delta in the first metric derivatives. When the slope vanishes, (3) has four continuous derivatives, with locally bounded piecewise fifth derivative. Smooth continuation of the two endpoint pieces gives a compact master with finite energy in this case. Equivalently, the full-space TT energy of a compact master is $3\int |F^{(5)}|^2du/(40G_N)$, by the same angular reduction. The calibrated $m=5$ reference illustrates that a wave can have finite energy and still fail the smooth-vector test. The unmarked interior tests prescribe no separate singularities at the physical tips. A construction including nonzero vertex jets has additional source terms. [Energy and vertex calculation](weak-normalization.md)

## Testing the inverse on the two packets

For the single shrinking pulse, $f_Z^{(4)}(a)=16a$ and its lower jets tend to zero, while $G'_W(a)=1$. The leading term in $f_X^{(9)}$ is $J\delta_a^{(4)}$. Its action in (1) gives $3J(16a)/(5120G_N)=-3a(1-a)/20$, or **$-1/30$** at $a=1/3$. The lower delta derivatives and the locally bounded bulk density vanish on this shrinking test in the limit. [Unit rim-strain preparation](joint-flat-hessian.md)

For the opposed unit-mass pulses, $G'_W=(s-a)^5+O((s-a)^6)$ and each pulse is separated from $a$ by a gap. By (4), $f_X^{(9)}$ jumps by $-16G_N(1-a)5!=-1280G_N$ at $a=1/3$. The positive and negative pulses sample its right and left limits. Equation (1) gives **$-3/4$**. No delta at the rim is needed in this second response. The measured discontinuity is five derivatives higher than in the unit-slope test. Both results are Hessian pairings against smooth probes. A bracket between two sharp clocks, arbitrary angular or corner tests, and the quantum domain require additional equations. [Two-pulse calibration](match-packets.md)

## Reproduction

Run the following from the repository root. [Exact polynomial check](../checks/weak_master.py)

~~~sh
python3 -B checks/weak_master.py
make check
~~~

The focused check takes $f_W=(18/175)s^{10}$ on the integration collar. The reference has unit slope at the rim and the inverse has a nonzero ninth derivative on its smooth side. Two compact piecewise polynomial tests compare the integral (3) paired with $-f_Z^{(9)}$ to the original optical Hessian. The second test vanishes to sixth order at the rim, so it checks the interior source alone. Expected output follows.

~~~text
Unit-slope jump of fourth master derivative = -32/3 (G_N=1)
Master pairing / optical Hessian, test with x^0 = 1
Master pairing / optical Hessian, test with x^6 = 1
Single rim pulse limit = -1/30
Opposed unit-mass pulses, ninth derivative jump = -1280, limit = -3/4
~~~
