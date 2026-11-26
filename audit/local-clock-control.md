# One emitter with two launch-time controls

Two spherical clocks can sample the same rays at one emitter and have a nonzero mixed bracket when both detectors use the same timing window. On a curved Kasner torus the answer is negative if the first launch is selected by curvature age and the second by the measured length of a torus cycle. For two concentric diamonds of different sizes one can also compare two individually well-defined sharp pair brackets. Their difference has a definite sign under independent sharpening. Each optical reading averages Chandrasekaran's cap clock over the sky of one emitter. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.27)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27)

## How to prepare one emitter

Use the vacuum Kasner torus with unit coordinate periods, scale factors $A_i(t/T)^{p_i}$ and exponents $p=(-b,1+b,b(1+b))/(1+b+b^2)$. Work at $b=2$ with $(A_1,A_2,A_3)=(6a/5,11a/10,a)$, well before any torus image can affect the experiment. Set $V_T=A_1A_2A_3$ and $c_G=8\pi G_NT/V_T$. The scalar age $\tau=4K/\sqrt{-\nabla K\cdot\nabla K}$, $K=C_{abcd}C^{abcd}$, equals $t$ on this family. Use a comoving timelike curve through a specified spatial mark to find the point on each launch slice. At launch take the unit future normal to the age level and then follow a geodesic. Adjust the proper duration $2L$ to match the weighted waist radius $M=\langle D_S^2\rangle/\langle D_S\rangle=R$. Set the cap by $D(C)=\epsilon D_S$ and read $\langle D_S D'(C)(S-C)\rangle/\langle D_S\rangle$ on this one sky. Use short, convex, transverse diamonds with $D'(C)>0$ and $\partial_L M\ne0$. [Kasner sky and moving-waist calculation](joint-jacobi.md)

For the age control $A_s$, launch at $\tau=T+s$. For the length control $B_s$, launch at $\tau=t_*+s$, where the harmonic length $\ell$ of the torus selects $\ell(t_*)=6a/5$. Here $\ell$ is the reciprocal square root of the smallest mean squared norm among the harmonic one-forms in primitive integral classes. In the background $\ell(t)=A_1(t/T)^{p_1}$, the minimizing class is gapped up to sign, and $t_*=T$. Thus $A_s$ and $B_s$ have the same tips, directions and fractional cut in the unperturbed spacetime. The length controller requires a measurement over the spatial slice. [Harmonic length, regular root and smooth probe](timing-kasner.md)

The mark specifies which observer is perturbed. The value of the background clock is spatially constant on each age level. Consequently every variation of the spatial position of the marked intersection within that level gives zero at first order. Under a metric gauge transformation, any discrepancy between transporting the curve and keeping its coordinates fixed changes the point only within the selected level after accounting for the level motion. The normal, geodesic and sky prescription are covariant. This proves the Ward identity for each unaveraged differential at this background. Under a nonsymmetric physical wave different spatial marks can give different readings. The construction concerns the ambient linearization with a specified mark. Fixing $R$ holds the weighted waist radius fixed. The total waist area is $4\pi\langle D_S^2\rangle$. [Spatial marks and the linearized Ward identity](weak-schwarzschild.md)

## The contribution from switching the controller

Write $u_\epsilon(b,t;R)$ for a homogeneous reading with *launch* age $t$. Before images arrive it is independent of the scale constants $A_i$ at fixed age and shape, since rescaling the three local coordinates takes one metric to the other. Let $J_s=dA_s$, $H_s=dB_s$ and $\eta=dt_*$. By differentiating the common optical experiment in its epoch,
$$
 H_s=J_s+u_{\epsilon,t}(b,T+s;R)\,\eta.                                      \tag{1}
$$
This identity holds on arbitrary smooth perturbations. The coefficient multiplying $\eta$ differentiates the **background** scalar in the time parameter. All remaining variations, including the movement of the measured waist and the perturbation of the launch normal, are the same in both readings.

The epoch differential is spatially translation and reflection invariant. At this background its spacetime source is a spatially homogeneous spacetime tensor distribution with time support at the selected age, so its nonzero wavefront covectors are timelike. Its Einstein causal response is smooth modulo gauge. One can also use its smooth compact source representative on solutions constructed by time-smearing the torus norms. In an invariant hyperbolic gauge the smooth causal response is homogeneous and diagonal, hence a Kasner tangent modulo gauge. Evaluating the localized $J_s$ on this response varies the age-controlled clock only through $b$. Thus, in the convention $\{A,B\}=dA[E\,dB]$, $E=G_{\rm ret}-G_{\rm adv}$,
$$
 J_s[E\eta]=u_{\epsilon,b}(b,T+s;R)\{b,t_*\},\qquad
 \{b,t_*\}=c_G T\frac{p'_1}{p_1\sum_i(p'_i)^2}=-\frac{21}{4}c_G T.             \tag{2}
$$
For the sign, the conjugate variation to $db$ has $Y_b\log A_i=c_Gp_i'/\sum_j(p'_j)^2$ and $Y_b b=0$. Differentiating the length condition gives $\{b,t_*\}=-Y_b t_*$. Equations (1)–(2) use the full causal pairing. Spatial symmetry applies to the response of $\eta$ alone. Inhomogeneous modes of each optical current are present. [ADM normalization of the epoch bracket](timing-kasner.md) · [Einstein causal response](https://arxiv.org/abs/1203.0261)

Let $v,w$ be smooth compactly supported probability densities of $s$ near zero, and denote averaging by subscripts $v,w$. For small $R/T$ these are legitimate finite-time measurements. In the rescaled diamond write each of the two faces, the cap, the waist and the observer as a family of fixed parameter domains, including their ends. The launch-age sweep is future timelike on each stratum. In comoving coordinates $t=T+s+O(R)$, $x=x_0+O(R)$, and the age derivatives tend uniformly to $(1,0,0,0)$ as $R\to0$. Smooth rescaled geodesic and cut matching gives the same bound at the edges. The cone tips themselves follow the observer. A parameter pushforward with a smooth weight can carry only covectors orthogonal to this timelike sweep velocity. Applying finite-order metric derivatives preserves the resulting wavefront bound. Thus $EJ_v$ is smooth and the finite-window brackets exist. [Timelike sweep and wavefront criterion](weak-domain.md) · [Pushforward of distributions](https://arxiv.org/abs/1409.7662v2)

For identical optics, (1) gives the exact finite-window relations
$$
 \begin{aligned}
 \{A_v,B_w\}-\{A_v,A_w\}
  &=\{b,t_*\}\left(\int v(s)u_{\epsilon,b}(s)\,ds\right)
                   \left(\int w(s)u_{\epsilon,t}(s)\,ds\right),\\
 \{A_w,B_w\}
  &=\{b,t_*\}\left(\int w(s)u_{\epsilon,b}(s)\,ds\right)
                   \left(\int w(s)u_{\epsilon,t}(s)\,ds\right).
 \end{aligned}                                                                \tag{3}
$$
The second line uses skewness of the entire age-controlled measurement with itself. The first line has an independent-window sharp limit for the *difference*. The second line has a sharp limit for the mixed bracket itself under any common shrinking window, including asymmetric windows. It need not describe the uncorrected pair with independently chosen timing profiles.

Set $F=\sum_i p_i^2(1-p_i)^2$ and $\alpha_\epsilon=(1-5\epsilon^4+4\epsilon^5)/225$. The short-clock expansion at fixed launch age is $u_\epsilon=(1-\epsilon)R+F\alpha_\epsilon R^5/t^4+O(R^6/t^5)$, with differentiable remainder. This follows by integrating the square of the leading shear from cap to waist and taking the sky mean. At $b=2$, $F=72/343$ and $F'=-240/2401$. At $\epsilon=1/2$, $\alpha_{1/2}=13/3600$. Hence
$$
 \lim_{w\to\delta_0}\{A_w,B_w\}
 =c_G\left[-\frac{169}{29412250}\frac{R^{10}}{T^8}
                     +O(R^{11}/T^9)\right].                                    \tag{4}
$$
The sign is strict for all sufficiently short positive radii. Reversing the controller labels reverses the sign. [Fixed-launch short-clock expansion](joint-jacobi.md)

## Unequal radii with independent timing windows

The time control can also be switched in a geometry where *both* uncorrected sharp pairs exist. Set $R_1=R,\epsilon_1=1/3$ and $R_2=R/5,\epsilon_2=1/2$. On the background precompute each launch age $t_i$ so that its matched diamond has proper midpoint $T$ on the same emitter. This is the smooth small-radius root of $t_i+L_i(b,t_i;R_i)=T$. Store these two numbers. In perturbed metrics the large instrument $A^{(1)}$ launches at age $t_1$ and the small instrument $A^{(2)}$ at $t_2$. The alternate small instrument $B^{(2)}$ launches at $t_2+t_*-T$. No instrument consults local metric jets at the midpoint. A shared point prescription could introduce an additional null singularity there.

For the two age-controlled inputs the sharp product exists. In the rescaled flat limit all characteristic conormals of the large clock lie on null lines through its launch, its return or its reflected cap center, at midpoint offsets $-R,R,-R/3$. The observer interior has only spacelike conormals, and the launch calibration jets lie at the launch tip. The whole small diamond $|t-T|+|\mathbf x-\mathbf x_0|\le R/5$ misses these lines by a margin at least $2R/15$ in this inequality. To transfer the test to Kasner, use physical coordinates at $T$ and rescale by $R$. On a bounded time band in these coordinates the metric tends smoothly to Minkowski as $R/T\to0$, the cut slope stays positive and the two compact skies converge with their first derivatives. Normalized null directions have a compact section. A sequence of connecting characteristic rays would have a limiting flat characteristic intersection by the geodesic equation, including a possible zero-length limit. Monotonicity of time and the coordinate speed bounds keep connecting causal segments inside the patch. The maximum speed on each axis is bounded by the reciprocal of its minimum scale factor in the band. Thus the large response is smooth throughout a neighborhood of the small source, including at small independent timing offsets. Switching the small control adds only the smooth response of $\eta$ in (1). Both sharp values therefore agree with the limits from arbitrary independent timing windows. [Characteristic separation for nested diamonds](timing-curved.md)

The exact difference of the two values is $u_{1,b}(b,t_1;R_1)\,u_{2,t}(b,t_2;R_2)\{b,t_*\}$. Each derivative holds the stored age or radius fixed as appropriate. Since $t_i=T+O(R)$ and $\alpha_{1/3}=232/54675$,
$$
 \{A^{(1)},B^{(2)}\}-\{A^{(1)},A^{(2)}\}
 =c_G\left[-\frac{24128}{11167463671875}\frac{R^{10}}{T^8}
                   +O(R^{11}/T^9)\right].                                     \tag{5}
$$
Thus at least one of these two specified, single-emitter sharp pairs is nonzero, with magnitude at least half the absolute difference. More generally program the small clock to launch at $t_2+\lambda(t_*-T)$, with fixed dimensionless gain $\lambda$. Equation (1) gives its sharp pair bracket exactly as $L(R)+\lambda\Delta(R)$, where $L(R)=\{A^{(1)},A^{(2)}\}$ and $\Delta(R)$ is (5). At each sufficiently small fixed $R$, $L(R)$ is finite and $\Delta(R)<0$. The raw pair is therefore negative for all sufficiently large finite positive gains, and it can vanish at only one gain. The intercept and the gain of the zero require the local age-controlled bracket. All gains use the same background light paths. The neighborhood of perturbed metrics on which an instrument stays in its preparation range can shrink as its gain increases.

Equations (4) and (5) establish properties of the ambient linearized theory with a global length controller. A nonzero independently sharpened number for a specified pair of purely local controllers and an inverse on an isolated capped diamond remain separate questions.

Run `python3 -B checks/local_clock_control.py` from the repository root and `make check` for the suite. The check derives the two leading coefficients by rational arithmetic and finite-differences both shape and physical launch age in the matched two-cone solver. Each numerical bracket is divided by $c_G R^{10}/T^8$. Independent waist shooting supplies the two stored launch ages used for the nested differences. [Executable check](../checks/local_clock_control.py)

~~~text
Common-window single-emitter coefficient -169/29412250
Nested clock bracket difference -24128/11167463671875; flat separation margin 2/15
R/T=0.04 normalized common-window limit -4.170684e-06
R/T=0.02 normalized common-window limit -4.883848e-06
R/T=0.14 normalized nested difference -2.409785e-09
R/T=0.08 normalized nested difference -2.284579e-09
~~~
