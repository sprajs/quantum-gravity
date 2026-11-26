# The cap momentum and metric jump for a null clock source

One physical polarization of a free graviton admits an explicit inversion of the cap and null symplectic form against smooth Cauchy tests. The linear source taken from the worked clock example produces a delta in cap-time ADM momentum **and** a jump in the metric perturbation. Smearing makes the Hamiltonian vector finite-energy, with energy growing inversely with the smearing width. This calculation specifies the cap continuation and the topology in which the sharp limit fails. [Original work by Venkatesa Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Clock differential on the fixed-area cone](endpoint-inverse.md)

## A mixed slice with physical cap data

On flat spacetime with coordinates $(t,x,y,z)$, take $(y,z)$ on a flat two-torus and let $h_{AB}=h(t,x)T_{AB}$, where $T_{AB}$ is a nonzero constant trace-free transverse polarization. Other components vanish. This field satisfies the linearized Hamiltonian and momentum constraints. Nonaffine wave profiles carry the tidal curvature $\delta R_{tAtB}=-T_{AB}h_{tt}/2$. With $K_{ij}=+\dot\gamma_{ij}/2$ in synchronous gauge, the trace-free ADM momentum is $\delta\pi^{AB}=T^{AB}h_t/(32\pi G_N)$ in the Cartesian chart. Contraction with $T_{AB}$ and integration over the torus gives $p=c h_t$, where $c=\int T_{AB}T^{AB}dy\,dz/(32\pi G_N)$. The quadratic action for this sector follows from the ADM kinetic term and the linearized vacuum equation $h_{tt}=h_{xx}$,

$$
 I^{(2)}=\frac c2\int dt\,dx\,[(h_t)^2-(h_x)^2].
$$

Use the future boundary of a spacetime region, parametrized by increasing $x$ on $t=\tau(x)$. The on-shell action variation gives $c\int(h_t+\tau'h_x)\delta h\,dx$. Choose $\tau=0$ for $x<0$, $\tau=x$ for $0\le x\le L$, and $\tau=L$ for $x>L$. The outer spacelike piece specifies the continuation past the far end of the null segment. Variations have compactly supported Cauchy data before completion. Write $(q_\pm,p_\pm)$ for the metric amplitude and ADM momentum on the two spacelike pieces, and $n(s)=h(s,s)$ on the null segment. The potential and symplectic form with these orientations are

$$
 \Theta=\int_{x<0}p_-Dq_-\,dx+
 c\int_0^L n'Dn\,ds+
 \int_{x>L}p_+Dq_+\,dx,\qquad \Omega=D\Theta .
 \tag{1}
$$

$D$ varies the fields at fixed embedding. The plus sign on the null piece follows from $h_t+h_x=n'$. Both spacelike and null pieces have the same future orientation. The divergence of the symplectic current vanishes on two solutions, so (1) equals $\int_{\mathbb R}Dp\wedge Dq\,dx$ on the flat Cauchy surface $t=0$. This sector uses the spacelike momentum of the metric itself. The torus has fixed periods and the frame and embeddings are fixed. [Cap canonical potential, Eq. (3.46)](https://arxiv.org/html/2611.34924v1#S3.E46) · [Fixed-frame radiative normalization and flux](radiative-flux.md)

For smooth solutions the common traces are $q_-(0)=n(0)$ and $q_+(L)=n(L)$. At each seam, the one-sided value of $q_\pm'+p_\pm/c$ equals the corresponding $n'$. There is a further matching condition across the entire null piece. Writing $h=A(x-t)+B(x+t)$ gives $h_x-h_t=2A'(0)$ everywhere on it. Consequently $q_-'-p_-/c$ at $0$ equals $q_+'-p_+/c$ at $L$. The higher jets of the same smooth $A,B$ also match. We take the finite-energy domain from the ordinary Cauchy data $(q,p)\in H^1(\mathbb R)\times L^2(\mathbb R)$. The field is continuous in $x$ and the momentum and first derivatives need only be square-integrable there. Pointwise derivative conditions describe smooth tests before this completion.

## Transfer the source to an ordinary Cauchy surface

Let $f$ be smooth on $[0,L]$, $M=\int_0^L f(s)ds$, and $K(s)=\int_s^L f(r)dr$. Keep the cap values free. Probe the field with the linear observable

$$
 F[h]=\int_0^L f(s)n(s)ds+\beta_0 n(0)+\beta_L n(L).
$$

Define the response by $\Omega(X_F,Y)=dF(Y)$, as in the fixed-area inverse calculation. Thus $X_Fp=\delta F/\delta q$ and $X_Fq=-\delta F/\delta p$ on the flat surface. Equivalently $X_F[G]=\{F,G\}$ for the convention $\{q(x),p(y)\}=\delta(x-y)$. D'Alembert evolution of ordinary Cauchy data gives

$$
 n(s)=\tfrac12[q(0)+q(2s)]+\frac{1}{2c}\int_0^{2s}p(x)\,dx .
$$

Substitute this expression into $F$ and exchange the integrations. With $\chi=\mathbf 1_{(0,2L)}(x)$, the unique Cauchy distributions pairing correctly with every smooth compactly supported test are

$$
\begin{aligned}
 X_Fp &=
 \left(\frac{M+\beta_L}{2}+\beta_0\right)\delta_0+
 \frac{\beta_L}{2}\delta_{2L}+
 \tfrac14\chi f(x/2),\\
 X_Fq &=-\frac{\chi}{2c}\,[K(x/2)+\beta_L].
\end{aligned}\tag{2}
$$

The two factors of $1/2$ in the bulk momentum density come from the split into left- and right-moving waves and the Jacobian $dx=2ds$. A separate check uses the retarded minus advanced solution kernel for $c(\partial_t^2-\partial_x^2)$,

$$
 E(t,x)=\frac{\operatorname{sgn}t}{2c}\,\mathbf 1_{|x|<|t|}.
$$

A source at $(s,s)$ gives $E(t-s,x-s)$. At $t=0$ and $s>0$ its field is $-\mathbf 1_{(0,2s)}/(2c)$ and its momentum $c\partial_t E$ is $(\delta_0+\delta_{2s})/2$. At $s=0$ the Cauchy data are $(0,\delta_0)$. Superposition gives both lines of (2). This weak Peierls response can be tested on smooth spacetime or Cauchy observables. Pairing two singular sources on the same null ray would require a separate restriction or smearing prescription.

The propagator also determines the two limiting values at each open-sheet point $0<s<L$. Approach $(t,x)=(s,s)$ at fixed $x=s$. For $t>s$ only earlier sources contribute in the limit. For $t<s$ only later sources contribute, with the advanced sign. The limits are

$$
 c X_F h(s+0,s)=\tfrac12\left(\beta_0+\int_0^s f\right),\qquad
 c X_F h(s-0,s)=-\tfrac12\left(\beta_L+\int_s^L f\right).
$$

The open spacelike pieces have zero field response because their points are spacelike to the source. Distinct one-sided values on the null leg preclude reading off a unique sharp null field there. For a zero-mean interior source without either marked endpoint, both limits agree.

The form on $H^1\times L^2$ is weakly symplectic. Here a **finite-energy Hamiltonian vector** means a representative of $dF$ in that very space. The $X_Fq$ jumps at $0$ and $2L$ force $M+\beta_L=0$ and $\beta_L=0$, respectively. The remaining delta in $X_Fp$ forces $\beta_0=0$. Conversely, when $M=\beta_0=\beta_L=0$, (2) is in $H^1\times L^2$. In this case its cap components vanish and its null component is $X_F n(s)=\int_0^s f(r)dr/(2c)$. It reproduces the fixed-density interior inverse and its sign in the convention of (1). In particular, canceling just the initial momentum delta for a nonzero-mean source can leave a metric jump. [Interior algebra and branch orientation](endpoint-inverse.md)

## A unit rim variation and its resolution cost

In the cone example $v\in[1/2,1]$, the fixed-area clock covector is $2\int Y(v)dv-3Y(1/2)/2$. Transport that *covector* to the wave model by $s=v-1/2$, with $L=1/2$, $f=2$, $\beta_0=-3/2$, and $\beta_L=0$. The background of the TT calculation is planar and shear-free. The original spherical clock has its own nonzero-shear background, expansion, and cap and corner variations. In the wave model, with $\chi=\mathbf 1_{(0,1)}$, equation (2) gives

$$
 X_Fp=-\delta_0+\tfrac12\chi,\qquad
 cX_Fq=-\tfrac12(1-x)\chi,\qquad
 c\partial_x X_Fq=-\tfrac12\delta_0+\tfrac12\chi .
 \tag{3}
$$

The bulk null measurement supplies $+1/2$ to the initial momentum delta, and the marked rim supplies $-3/2$. Their sum is $-1$. A smooth Cauchy variation with $Yq=1-4x$, $Yp=0$ on $[0,1]$ (continued smoothly with compact support) induces $Yn(s)=1-4s$. Its mean is zero and its rim value is one. Contracting (3) gives $-1+\frac12\int_0^1(1-4x)dx=-3/2$, the full clock test value.

Spatially smear the source by a unit-mass box of half-width $\eta$, with $0<\eta\le1/2$. Translation invariance convolves both Cauchy components of (3) by the same box $\rho_\eta$. Put $W_\eta=\chi*\rho_\eta$. The smoothed response has momentum $W_\eta/2-\rho_\eta$ and metric gradient $(W_\eta/2-\rho_\eta/2)/c$. The integrals $\int W_\eta^2=1-2\eta/3$, $\int W_\eta\rho_\eta=1/2$ and $\int \rho_\eta^2=1/(2\eta)$ give the exact ordinary wave energy

$$
 E_\eta=\frac{1}{2c}\int [(X_Fp)_\eta^2+c^2(\partial_x X_Fq)_\eta^2]dx
 =\frac1c\left(\frac{5}{16\eta}-\frac18-\frac{\eta}{6}\right).
 \tag{4}
$$

Thus the regulator gives a weak limit with a divergent response energy. The number $5/16$ uses the specified box. This is the energy of the *Hamiltonian vector of the measurement* on the linearized wave phase space. It does not give a quantum clock reading or an energy bound on the state being measured.

The model settles which Cauchy variables represent this source for one explicit continuation across the seams. A cylindrical vacuum calculation obtains its source by varying the affine reading itself. Its momentum delta has a different coefficient because the physical field and radial measure differ. Whether the spherical, moving-boundary clock differential belongs to the range of the physical two-form is a **proof gap**. Its cap and corner terms and allowed variations must be derived on the same constrained domain. No physical refutation follows from (3) or (4). [Actual affine clock in polarized cylindrical gravity](joint-peierls.md)

## Reproduce the calculation

From the repository root run the following commands. [Exact rational checks](../checks/joint_wave.py)

~~~sh
python3 checks/joint_wave.py
make check
~~~

The focused check integrates the action current for a pair of compact left- and right-moving wave packets on both slices. It gives cap flux $55/36$, null flux $-23/18$ and total $1/4$ in units of $c$. It compares three independent Cauchy tests with their null measurements, yielding $-3/2$, $1/6$ and $5/12$. Propagating (3) to either side at $s=1/4$ gives the limiting field values $-1/(2c)$ and $-1/(4c)$. Finally it checks (4) by integrating the squared smoothed response at four widths. The last output reports $\eta c E_\eta\to5/16$. The full suite should exit successfully.
