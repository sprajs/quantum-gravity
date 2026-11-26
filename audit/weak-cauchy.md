# The spherical clock response on an equal-time surface

On a complete Minkowski Cauchy surface the first shear-dependent response of the sharp clock has an explicit pair of distributional initial data. At unit waist time, an ingoing light front from the cap meets the slice on the sphere of radius $|2a-1|$, where $a$ is the cap fraction. If the reference wave has nonzero optical-strain slope at the cap, the response has a displacement jump and a momentum impulse there. Their coefficients depend on the direction and polarization of the incident shear. The result gives a distributional representative for the Hessian of the **clock excess** at the flat solution. The excess itself has zero first differential there. [Chandrasekaran, arXiv:2611.34924v1, (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Optical Hessian at a round flat diamond](joint-flat-hessian.md)

## Initial data for the weak bracket

Take tips $(0,0),(2,0)$, waist time $T=1$, and $0<a<1$. Use the spatial transverse-traceless (TT) gauge $h_{0\mu}=0$, $\partial_i h_{ij}=h_{ii}=0$ for radiative solutions on the full Minkowski continuation. Write $D=\bar u_*-(1-a)M$ with $M=\langle\rho_S^2\rangle/\langle\rho_S\rangle$, and $\langle\cdot\rangle=(4\pi)^{-1}\int d\Omega$. Fix any smooth incident linearized vacuum wave $W$. Write $H_W$ for its first-order conformal screen metric in the marked vertex frame. Define the linear observable $L_W(Z)=d^2D_{\rm flat}(W,Z)$ on smooth TT test data. On the matched-radius preparation this is the mixed second variation of the clock. [Preparation and Hessian](joint-flat-hessian.md)

Let $n$ denote a unit launch direction, $k=(1,n)$, and take the screen perpendicular to $n$ in the vertex frame. Use the convention $Q_{AB}[Z]=-R^{(1)}_{AkBk}[Z]$ and denote the Euclidean contraction by a colon. The regular vertex Jacobi equation gives $H'_Z(s)=2s^{-2}\int_0^s u^2 Q[Z](u,un)du$. Exchanging the order in the optical Hessian yields

$$
 L_W(Z)=\left\langle\int_0^1 J(s,n):Q[Z](s,sn)\,ds\right\rangle,
 \qquad
 J(s,n)=\frac{s^2}{2}\int_{\max(s,a)}^1
            \frac{1-v}{v}H'_W(v,n)\,dv.                                      \tag{1}
$$

The components of $J$ can be regarded as a trace-free Cartesian tensor with $J^{ij}n_j=0$. Define the compact spatial-tensor spacetime distribution $j$ by the right side of (1), applied to arbitrary smooth test spatial tensors in temporal gauge. Explicitly the operator contracted with $J$ is
$$
 2Q_{ij}[h]=D_k^2 h_{ij}+\partial_i\partial_j h_{nn}
              -D_k\partial_i h_{nj}-D_k\partial_j h_{in},\qquad
 D_k=\partial_t+n\cdot\nabla .                                                 \tag{2}
$$
Both derivatives and contractions in (2) hold $n$ fixed. Writing (1) before differentiating defines the source at the cap, the radial integration endpoints and every angular chart. In particular the optical history on $0<s<a$ contributes to $L_W$.

Let $C_\tau=\cos(\tau|\nabla|)$ and $S_\tau=\sin(\tau|\nabla|)/|\nabla|$. For $q=Z(T)$, $v=\dot Z(T)$ define two raw Cauchy distributions by duality,
$$
 \langle A,q\rangle=\langle j,C_{t-T}q\rangle,\qquad
 \langle B,v\rangle=\langle j,S_{t-T}v\rangle .                                \tag{3}
$$
Equation (3) is explicit in position space through the Kirchhoff formula
$S_\tau f(x)=\tau\langle f(x+\tau m)\rangle_m$ and $C_\tau=\partial_\tau S_\tau$.
Both raw distributions have support in the closed waist ball on $T=1$. At each spatial Fourier covector $\xi\ne0$, put $P=I-\hat\xi\hat\xi^t$ and $\Pi h=PhP-\tfrac12P\operatorname{tr}(Ph)$ for symmetric $h$. This is the orthogonal TT projector for the full Cartesian tensor contraction. The Fourier transforms of $A,B$ are smooth of polynomial growth. Multiplication by the bounded symbol $\Pi$ defines their projected tempered distributions independently of its value at the origin. This choice uses the full spatial continuation and fixes the zero-mode prescription for decaying radiative data.

With $K_{ij}=\dot h_{ij}/2$ to first order, ADM momentum is $\pi=c\dot h$ in this gauge, where $c=1/(32\pi G_N)$. Use $\Omega(X,Z)=\int (X_\pi:Z_q-X_q:Z_\pi)\,d^3x$. The unique TT initial data in the stated Fourier prescription representing $L_W$ via $\Omega(X,Z)=L_W(Z)$ are
$$
 X_q=-\Pi B/c,\qquad X_\pi=\Pi A .                                               \tag{4}
$$
Indeed $Z=C_{t-T}q+S_{t-T}v$ and $Z_\pi=cv$, so (4) reproduces (3) in both slots. Equivalently $X=(1/c)\Pi E j$, where the retarded-minus-advanced kernel for $\partial_t^2-\Delta$ is $E(T-t)=S_{T-t}$. The odd sine kernel gives $-B$ at time $T$ and its even derivative gives $A$. Distributional evolution by these same propagators gives the response at every time. This defines a bracket with smooth radiative probes on the chosen continuation. [Arnowitt, Deser and Misner, canonical gravity](https://arxiv.org/abs/gr-qc/0405109) · [First-slot convention in the cylindrical calculation](joint-peierls.md)

For example take $P_{e,f}=\int(e:q+f:\pi)\,d^3x$ with smooth compact TT tensors $e,f$. In the order $\{q,\pi\}=\Pi$ the ordinary canonical formula gives
$$
 \{L_W,P_{e,f}\}=\langle A,f\rangle-\langle B,e\rangle/c
                   =dP_{e,f}[X],\qquad
 \{P_{e,f},L_W\}=-dP_{e,f}[X].                                                   \tag{5}
$$
The opposite-order right Hamiltonian vector $\{\,\cdot\,,L_W\}$ has signs opposite to (4). These formulas also apply to compact non-TT $e,f$ after projection, by pairing the compact raw kernels with the smooth projected probes. Gauge-invariant curvature probes admit a spacetime construction using their conserved sources. The spatial TT projection uses inverse Laplacians, so spatial support before projection alone gives no support theorem for the TT representative.

## What meets the waist slice

Assume $a\ne1/2$, and set $r_0=|2a-1|$, $\sigma=\operatorname{sgn}(2a-1)$. Write $S_W(\hat x)=H'_W(a,\sigma\hat x)$ as a Cartesian screen tensor. The leading singularities near the interior sphere are
$$
 \boxed{\displaystyle
 \Pi A=-\sigma\frac{1-a}{32\pi r_0}S_W(\hat x)\,\delta(r-r_0)+A_{\rm rem},
 \qquad
 \Pi B=\frac{1-a}{32\pi r_0}S_W(\hat x)\,\mathbf1_{r>r_0}+B_{\rm rem}.}          \tag{6}
$$
Here $\delta(r-r_0)$ is a density relative to $d^3x=r^2dr\,d\Omega$. The remainders are locally lower by one normal derivative. In particular $A_{\rm rem}$ is locally integrable and $B_{\rm rem}$ is continuous near the sphere. Smooth trace-free shear of either polarization is allowed. At angular zeros of $S_W$ the leading coefficient vanishes. If $a=1/2$ the incoming front refocuses at the origin of this slice and the next section gives its separate local expansion. The exact inverse (3)–(4) applies for every cap fraction.

To obtain (6), first suppress the two derivatives in $Q$ and insert a smooth angular and piecewise-smooth radial tensor weight $J$ against the sine kernel. Vary the observation time $T$ near one while keeping the source fixed. Near the inner sphere $r=|x|$, the null-intersection equation has the single root
$$
 s=\frac{T^2-r^2}{2(T-r\mu)},\qquad \mu=\hat x\cdot n .
$$
The part meeting the cap has $s<T$. Kirchhoff's sine kernel there is $-\delta(|x-sn|^2-(T-s)^2)/(2\pi)$. Integrating $s$ and then changing the angular variable $\mu$ to $s$ gives the undifferentiated kernel
$$
 K_J(T,x)=-\frac1{8\pi r}\int_{(T-r)/2}^{(T+r)/2}
        \frac{\langle J(s,n)\rangle_\varphi}{s}\,ds .                            \tag{7}
$$
The azimuthal mean is over $n$ at the indicated $\mu$. The formula holds in a neighborhood of the inner sphere on which both integration endpoints are inside $(0,1)$. Smooth angular weights have smooth azimuthal means up to either pole. The only loss of radial differentiability in (7) occurs when an endpoint crosses $s=a$. Equation (1) gives the slope jump $[J']=-a(1-a)H'_W(a,n)/2$, with brackets denoting outer minus inner values. For $a>T/2$ the upper endpoint crosses $a$ from below. For $a<T/2$ the lower endpoint crosses $a$ from above. In both cases, integration of this kink adds the same leading term to a smooth continuation,
$$
 K_J(T,x)=K_{\rm smooth}
 +\frac{1-a}{128\pi |2a-T|}S_W(\hat x)\,(r-|2a-T|)_+^2
 +O((r-|2a-T|)_+^3) .                                                            \tag{8}
$$

The ray from the source point $(a,an)$ to the contact point $(T,(2a-T)n)$ has spatial velocity $-n$. A scalar wave depending on $t+n\cdot x$ has $D_k=2\partial_t$ at this radial characteristic covector. The spatial factors $\partial_i$ or $\partial_j$ in the other terms of (2) contract with $J$ in the screen, so their highest normal derivatives vanish. More explicitly each spatial derivative of the sine kernel in its source variable is $-\partial_{x_i}$ at the observation point. There $\partial_{x_i}$ acting on the leading front is proportional to $n_i\partial_r$. Each source time derivative is $-\partial_T$. Equations (7)–(8) also apply to the weights $J$ multiplied by components of $n$ in (2). Thus the leading normal derivatives for $B$ act as $2\partial_T^2K_J$ and those for $A$ as $-2\partial_T^3K_J$. Since $\partial_T(r-|2a-T|)=\sigma$, these give (6) before TT projection.

In local angular and normal coordinates the remaining powers in (8) are one order smoother. The spatial TT multiplier is smooth of order zero away from $\xi=0$. On the radial normal its symbol acts as identity on $S_W$. Equivalently the Fourier integral across the sphere has phases $\lambda(r-r_0)$ and the leading symbol on these phases is $\Pi(\lambda\hat x)S_W=S_W$ for either sign of $\lambda$. Derivatives of the symbol in this expansion lower the order by one. The low-frequency piece of the projected compact raw kernels is smooth. This gives the same impulse and jump for the projected representatives. The raw kernels and their projections are smooth away from the spheres $r_0$ and $1$ on the full waist slice. At the interior origin when $r_0>0$ the root formula before the change of angular variable is regular since $T-x\cdot n$ stays positive and $s$ stays on one side of $a$. This argument gives an upper bound on singular support at the outer sphere. Only the interior coefficient has been evaluated here.

## The focus at half radius

At $a=1/2$ all inward fronts reach the center at $T_0=1$. For each observation direction $\hat x$ write $\overline S(\mu)$ for the azimuthal mean of the Cartesian tensor $S(n)=H'_W(a,n)$ on the circle $\hat x\cdot n=\mu$. The leading homogeneous terms at the origin are
$$
 (\Pi B)_{-1}=\frac{\overline S(0)}{64\pi r},
 \qquad
 (\Pi A)_{-2}=\frac{\overline S'(0)}{64\pi r^2}.                                 \tag{9}
$$
Thus the field samples an equatorial mean of the shear slope, and the momentum samples its first angular derivative. An angular parity can eliminate either coefficient. Both powers in (9) are locally integrable in three spatial dimensions.

Indeed, before the azimuthal change of variables, the sine kernel in (7) reads
$K_J=-\langle J(s,n)/(T-x\cdot n)\rangle/(4\pi)$ at the null-intersection root. Set $\tau=T-1$. Near the focus,
$s-a=(\tau+x\cdot n)/2+O((|\tau|+r)^2)$ and $[J']=-S/8$.
The first homogeneous term after smooth subtraction is therefore
$$
 K_J^{(1)}=\frac1{64\pi}\left\langle S(n)(\tau+x\cdot n)_+\right\rangle .
$$
This is a superposition of plane fronts, each transverse and trace-free on its own spatial normal $n$. Equation (2) on each such front gives $2\partial_T^2$ for $B$ and $-2\partial_T^3$ for $A$. At $\tau=0$ the angular integrals of $S\delta(\tau+r\mu)$ and $S\delta'(\tau+r\mu)$ are $\overline S(0)/(2r)$ and $-\overline S'(0)/(2r^2)$, respectively. The spatial TT projection preserves each leading plane front away from zero Fourier covector. To control the expansion, put $(\tau,x)=\lambda(z,y)$ with $|y|=1$ and $|z|<1/2$. The zero of $s-a$ in $\mu$ is transverse and smooth in $(\lambda,z)$ near $\mu=-z$. Splitting the polar integral at that zero gives a smooth expansion in $\lambda$ on either side, including its required $z$ and angular derivatives. The remaining raw terms have one higher degree. For a test on the entire scaled ball, including its center, the normal coordinate $y\cdot n$ remains transverse for each fixed $n$. The positive part and its derivatives therefore admit the same expansion by duality in that coordinate, uniformly over $n$. The multiplier has order zero and preserves the leading TT terms. This distributional scaling excludes an extra point-supported delta, which would have degree $-3$ or less. For example, along the $z$ axis the polynomial vacuum wave used in the check below gives $\overline S_{xx}-\overline S_{yy}=(1-\mu)^4/6$. The two coefficients in (9) for this component difference are $1/(384\pi)$ and $-1/(96\pi)$.

## The two canonical contributions to a measured bracket

For the regular compact quadrupole of the earlier unit-rim-strain test, let $B_n$ denote the screen projection of $\operatorname{diag}(-1/2,-1/2,1)$ with its trace removed. Then $S_W=B_n$ and $\langle B_n:B_n\rangle=3/5$. Write $F(u)=a\eta^4 f((u-2a)/\eta)$, with $f^{(4)}(0)=1$, $f^{(j)}(0)=0$ for $0\le j<4$, and compactly supported $f$. On the Cauchy annulus $|r-r_0|<\eta$ the incident master field equals $\sigma F(T+\sigma r)/r$. The four spatial derivatives making the TT wave give the screen coefficient
$$
 b=\sigma\left(\frac{F^{(4)}}r-\frac{2\sigma F^{(3)}}{r^2}
          +\frac{3F''}{r^3}-\frac{3\sigma F'}{r^4}+\frac{3F}{r^5}\right).
$$
This follows by applying $\Delta^2-2r^{-1}\partial_r\Delta+r^{-2}\partial_r^2-r^{-3}\partial_r$ to the radial master and contracting the angular screen. Its time derivative gives the velocity. The other tensor components do not enter the leading contraction. At $r=r_0$ the screen coefficient is $\sigma a/r_0$. Across the exterior half-annulus, $\int_{r_0}^\infty r^2\dot b\,dr\to-ar_0$ by the fundamental theorem of calculus. The smooth and lower-order terms pair to zero in the limit, since $q$ is bounded on a shrinking shell and the velocity has bounded $L^1$ norm and zero distributional limit. Taking $f_{\rm probe}=q$ and $e_{\rm probe}=-c\dot q$ in (5), the displacement and velocity contributions each give $-3a(1-a)/40$. Their sum is $-1/30$ at $a=1/3$ as well as $a=2/3$. This verifies which terms in (4) realize the earlier optical result. [Quadrupole generator and optical calculation](joint-flat-hessian.md)

Run `python3 -B checks/weak_cauchy.py` from the repository root. The first check contracts (7) against the $zz$ component of the tide of the vacuum wave $h=(t-z)^2\operatorname{diag}(1,-1,0)$ near the contact along the $x$ axis. After subtraction of the smooth continuation, the measured quadratic coefficient divided by (8) tends to one on each side of the focusing case. The second check uses the compact quadrupole at width $1/512$ and evaluates its initial displacement, its initial velocity and the original optical Hessian independently. The last check differences the Kirchhoff kernel in scaled time at radius $10^{-5}$ to measure both focal coefficients in (9). Expected rounded output follows. Run `make check` for the complete suite. [Executable check](../checks/weak_cauchy.py)

```text
cap=0.333333  Kirchhoff coefficient ratio=0.999923  position=-0.01666667  velocity=-0.01666667  optical=-0.03333333
cap=0.666667  Kirchhoff coefficient ratio=0.999960  position=-0.01666667  velocity=-0.01666667  optical=-0.03333333
focus: sine coefficient ratio=0.999961  cosine coefficient ratio=0.999972
```

The **remaining proof gap** concerns using two singular responses in the same symplectic pairing and passing from the complete linearized continuation to a finite, independently framed diamond. The initial data above solve the inverse against smooth global probes. A nonlinear or quantum inverse would need a domain and boundary conditions for which the corresponding pairings exist.
