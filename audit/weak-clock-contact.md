# The short-time bracket of two translated spherical clock readings

Prepare a smooth, even quadrupole vacuum wave $W$ on the unit-radius flat diamond. Give it unit optical strain slope at the cap $a=1/3$ and choose its vertex coefficient as described below. Compare the mixed clock readings $L_0=d^2D_{\rm flat}(W,\cdot)$ and $L_\tau$ obtained by repeating the **entire** experiment a proper time $\tau$ later. Their classical bracket tends to $+G_N/30$ when the second experiment is later and to $-G_N/30$ when it is earlier. Two finite-resolution readings of this same observable, with exactly the same mean time and variance, can have limiting bracket $-G_N/150$. Identical detectors have zero mutual bracket at every width. This is a measurable ordering effect for the linearized spherical clock response on the common Minkowski continuation. At flat space the matched-radius clock itself is critical. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Clock Hessian](joint-flat-hessian.md)

## Translating the marked experiment

Write $D=\bar u_*-(1-a)M$ for the excess above the flat reading, where $M$ is the weighted waist radius. Let $U_\tau h(t,\mathbf x)=h(t+\tau,\mathbf x)$. The later observable uses tips $(\tau,\mathbf 0),(2+\tau,\mathbf 0)$ with the translated emitter, tetrad, cut prescription, radius adjustment and reference wave $U_{-\tau}W$. Minkowski time translation is an isometry and it commutes with the causal Green operators. Hence $L_\tau[h]=L_0[U_\tau h]$ and its weak first-slot Hamiltonian field is $U_{-\tau}X_0$ modulo gauge. This translates the global conserved current, including its vertex terms. Translation of the cap alone would produce a different experiment. [Conserved metric current](weak-tidal.md) · [Point-vertex terms](weak-normalization.md)

Let $f(s)=F(2s)$ denote the quadrupole master for the regular wave built from $F(t+r)-F(t-r)$. Work initially on the whole profile line. For $S=\operatorname{diag}(-1/2,-1/2,1)$ the Einstein pairing is
$$
 \Omega(f,g)=A\langle f^{(9)},g\rangle,\qquad A=\frac{3}{5120G_N}.
$$
Write $z=f_X^{(4)}$ for the sharp response. The full-line solution of $A f_X^{(9)}=L_0$ has at most affine tails. Consequently $z$ has compact support. It is piecewise smooth, and $z'$ is an ordinary bounded piecewise smooth density $v$ plus finitely many atoms $d_i\delta_{s_i}$. The rim supplies
$$
 d_a=-16G_N(1-a)G'_W(a).
$$
There may also be a vertex jump at $s=0$. It vanishes precisely when $\int_a^1(s^{-1}-1)G'_W(s)ds=0$. A lower vertex derivative still contributes to $v$. The waist has zero fourth-derivative jump because the optical weight contains $1-s$. All coefficients here refer to the dimensionless $s$ master. [Distributional rim inverse](weak-master.md) · [Full-line normalization and vertex moments](weak-normalization.md)

These formulas suffice on the radiative quadrupole sector. They also give the bracket in the ordinary decaying Minkowski radiative TT continuation. The round Hessian is rotation and reflection covariant, and the response depends linearly on the polar STF tensor $S$. At nonzero spatial Fourier wavevector $k$, each TT Cauchy tensor must therefore be a radial scalar times the screen trace-free projection $\Pi^{\rm TT}(\hat k)S$. To see this, fix $\hat k$: rotations around this axis require a map from the spin-two part of $S$ to screen spin two. Reflection in a plane containing $\hat k$ removes the map rotating that polarization by $90$ degrees in polarization space. Equivalently, terms built from $S,\hat k,\delta_{ij}$ containing a free $\hat k_i$ or a screen trace project to zero. The full real master supplies both time phases at every nonzero frequency through $F(t+r)-F(t-r)$. Thus this observable has no independent TT angular component outside the computed sector. The radiative continuation excludes spatial polynomial zero modes. Distinct regional boundary sectors would require their own pairings.

## Why the two time limits differ

In the $s$ master the later response is $z(s-\tau/2)$. Converting $\Omega(X,\cdot)=dL$ with $\Omega=\int\delta\pi\wedge\delta q$ to the usual canonical bracket introduces a minus sign. Four integrations by parts give the time-delay bracket as the distribution
$$
 B(\tau)=\{L_0,L_\tau\}
   =-A\int z'(s)z(s-\tau/2)\,ds .                                      \tag{1}
$$
One can first apply smooth time windows to both experiments. Their response profiles are smooth, so (1) follows from the ordinary Einstein pairing. Moving the smooth windows onto the delay variable gives the convolution of the bounded function $z$ with the finite measure $z'$, with the argument shown. It defines a bounded distribution in $\tau$. There is no delta distribution supported at zero delay. For sufficiently small $\tau\ne0$, none of the shifted jumps coincide with the original ones, and (1) is an ordinary integral plus unambiguous point evaluations.

The $v$ term has the same limit from either side by dominated convergence. The $i$th atom evaluates $z$ just below $s_i$ for $\tau>0$ and just above it for $\tau<0$. Its contribution to $B(0^+)-B(0^-)$ is $A d_i^2$. Skewness and exact translation covariance give $B(-\tau)=-B(\tau)$, so
$$
 B(0^+)=-B(0^-)=\frac{A}{2}\sum_i d_i^2.                               \tag{2}
$$
The sign can also be read in Fourier space. With $\widehat f(k)=\int e^{-iks}f(s)ds$, the separated bracket has sine transform $A\int_0^\infty k^9|\widehat f_X(k)|^2\sin(k\tau/2)dk/\pi$ with distributional interpretation. An isolated jump $d_i$ in $f_X^{(4)}$ gives high-frequency weight $A d_i^2/(\pi k)$. Its sine transform approaches $+A d_i^2/2$ from positive delays. Distinct-atom interference gives singularities at other delays. [Minkowski one-particle spectral weight](weak-fock.md)

For unit rim slope and vanishing vertex jump this gives $B(0^+)=3G_N(1-a)^2/40=G_N/30$ at $a=1/3$. The earlier compact unit-slope preparation proportional to $(u-2a)^5$ near $2a$ obeys the vertex condition. For an independent exact computation choose $G'_W(s)=p s^4+q s^5$ on $a\le s\le1$, taking $p,q$ so that $G'_W(a)=1$ and $\int_a^1(s^{-1}-1)G'_W(s)ds=0$. This is physical smooth vacuum data. A master equal to $(2p/1575)s^{10}+(q/1650)s^{11}$ throughout this interval, with smooth compact cutoff away from the vertex and beyond the waist, has exactly that slope. The test below includes the residual vertex second-derivative term when forming $z$. Different smooth references with the same two conditions give the same two limits.

## Timing windows with the same center and variance

Measure $\int a_h(t)L_t\,dt$ and $\int b_h(t)L_t\,dt$, where $a_h=h^{-1}a(t/h)$ and likewise for $b_h$. For any smooth compact probability profiles the cross-bracket is the average of $B(h(t'-t))$ with weights $a(t)b(t')$. At each nonzero width the timelike translates of the conserved sources have smooth causal responses. Boundedness of (1) and (2) give the limit
$$
 B(0^+)\int a(t)b(t')\operatorname{sgn}(t'-t)\,dt\,dt'.               \tag{3}
$$
Choose the first profile by mixing two peaks at $-1,1$ with equal weights. Put the second peaks at $-2,1/2$ with weights $1/5,4/5$. Center every peak on the same smooth even unit-mass bump supported in $(-1/8,1/8)$. Both profiles have zero mean and variance one plus the variance of the common bump. The second reading is later with probability $2/5$ and earlier with probability $3/5$, so (3) is $-G_N/150$. Identical profiles give zero by antisymmetry, and interchanging the two detector labels gives $+G_N/150$. All these clocks converge on every fixed smooth perturbation to the same $L_0$. This demonstrates nonuniqueness of a bracket defined by independently sharpening two detector profiles for this spherical clock Hessian. It leaves intact the algebraic one-symbol self-bracket $\{L_0,L_0\}=0$. [Weak domains for smooth and sharp probes](weak-domain.md) · [Earlier nonlinear cylindrical detector experiment](joint-resolution.md)

For two different responses, matched smooth windows select the mean of the two time-order limits. Under independent sharpening, order dependence is proportional to the sum of products of jumps at shared locations. Calibrating a common wave so this sum vanishes gives two distinct cap readings with the same nonzero limit for either order. [Two-response formula](timing-midpoint.md) · [Two-cap calculation](timing-caps.md) · [Finite-resolution measurement](timing.md)

## Reproduce the calculation

Run `python3 -B checks/weak_clock_contact.py` from the repository root and `make check` for the complete suite. The focused check constructs the whole piecewise polynomial $z$ for the second smooth reference directly from the optical source, integrates its translated pairing with exact rational arithmetic and verifies skewness before taking the limit. Its expected output is below. [Executable check](../checks/weak_clock_contact.py)

~~~text
Proper-time delay 0.0010000: spherical clock bracket 0.05155663
Proper-time delay 0.0000100: spherical clock bracket 0.03351606
Proper-time delay 0.0000001: spherical clock bracket 0.03333516
Later-time limit 1/30; equal-moment detector limit -1/150 (G_N=1)
~~~
