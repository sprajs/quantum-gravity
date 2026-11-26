# The Einstein normalization and the point-vertex contribution

A full Minkowski Cauchy slice fixes the symplectic normalization of the spherical quadrupole and allows an arbitrary smooth incident wave at the initial vertex. Such a wave measures a second singular contribution to the sharp clock. At cap ratio one third we exhibit a preparation with zero rim strain slope and vertex coefficient **$81/32$**. The calculation concerns the Hessian of the matched-radius clock at flat space, projected onto one real, even-parity quadrupole. [Venkatesa Chandrasekaran, arXiv:2611.34924v1, (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Vacuum preparation and Hessian](joint-flat-hessian.md)

## Cauchy normalization

Fix waist radius one. Use the master $F(u)$, radial scalar $\phi_F=[F(t+r)-F(t-r)]/r$ and fourth-order spatial TT projection of $S=\operatorname{diag}(-1/2,-1/2,1)$ from the vacuum preparation. Start with smooth compact profiles on the whole line. For the convention $\Omega(X,Z)=dH(Z)$, the future-oriented ADM form in this gauge is
$$
 \Omega(X,Z)=\frac1{32\pi G_N}\int_{\mathbb R^3}
       (\dot h_X:h_Z-\dot h_Z:h_X)\,d^3x .
 \tag{1}
$$
Indeed, the canonical potential is $\int\pi^{ij}\delta h_{ij}$ with linear TT momentum $\dot h^{ij}/(32\pi G_N)$. [Arnowitt, Deser and Misner, canonical action](https://arxiv.org/abs/gr-qc/0405109) · [v1, cap potential (3.46)](https://arxiv.org/html/2611.34924v1#S3.E46)

At spatial Fourier covector $k$, the TT differential operator multiplies the radial scalar amplitude by $|k|^4 B(\hat k)$, where $B$ is the screen trace-free projection of $S$. Its angular mean square is $\langle B:B\rangle=3/5$. Plancherel and the radial wave equation therefore replace the two TT fields in (1) by $\partial_t^4\phi_X$ and $\partial_t^4\phi_Z$, with angular factor $4\pi(3/5)$. Write $j=F_X^{(4)},\ k=F_Z^{(4)}$ and $j_\pm=j(t\pm r)$, and likewise for $k$. In the radial integral the mixed terms are $\partial_r(j_- k_+-j_+ k_-)$, whose primitive vanishes at zero and infinity. The two same-direction integrals cover the full profile line once. Hence
$$
 \begin{aligned}
 \Omega(X,Z)&=\frac3{40G_N}\int_{\mathbb R}(j' k-k' j)\,du
             =\frac3{20G_N}\langle F_X^{(9)},F_Z\rangle,\\
 E[X]&=\tfrac12\Omega(X,\partial_t X)
             =\frac3{40G_N}\int_{\mathbb R}|F_X^{(5)}|^2\,du .
 \end{aligned} \tag{2}
$$
This energy equals the integrated quadratic TT wave energy $(64\pi G_N)^{-1}\int (|\dot h|^2+|\nabla h|^2)d^3x$. For $f(s)=F(2s)$ the ninth-derivative coefficient in (2) is $3/(5120G_N)$.

On the unit waist ball at $t=1$, every test with $F_Z\in C_c^\infty(0,2)$ has zero Cauchy data near and outside $r=1$. Thus its pairing with a smooth response equals the full-space pairing. For a distributional response the same conclusion follows by testing its Cauchy data with these compactly supported smooth data. The argument requires only an extension agreeing on their support. Arbitrary tests on Minkowski space can cross the rim of the ball. The global integral then includes exterior data, and a singular response on $r=1$ also requires a prescription for its regional trace. A cutoff of the ADM integral at finite radius does not in general commute with the Fourier calculation. [Interior tests on the waist disk](match-packets.md)

## Optical data when the master reaches the vertex

Let $LZ=Z^{(4)}(2s)/s-2Z^{(3)}(2s)/s^2+Z''(2s)/s^3$, where $Z$ here denotes a test master in the $u$ coordinate. For a master supported away from $u=0$, the vertex-normalized screen strain is $(LZ)B$. For general $Z\in C_c^\infty(\mathbb R)$ the strain amplitude is
$$
 G_Z=LZ-\frac{Z''(0)}{s^3}+\frac{Z^{(4)}(0)}s
                      +\frac23 Z^{(5)}(0).
 \tag{3}
$$
To derive (3), subtract the Taylor polynomial of $Z$ through degree six at zero. Its radial scalar is polynomial of total degree at most five in $(t,\mathbf x)$. Four spatial derivatives give a metric affine in the coordinates, with zero linearized curvature. The fixed orthonormal vertex frame and regular Jacobi initial conditions give zero optical strain for these polynomial metrics. For the Taylor remainder, every retarded-phase contribution to the optical tidal tensor on $t=r$ vanishes, since the calculation uses only derivatives through order six at $t-r=0$. The direct Jacobi solution is $L$ applied to this remainder, regular and $O(s^2)$ at the vertex. On monomials $u^k$ for $0\le k\le6$, $L$ detects only $k=2,4,5$ with respective values $2/s^3,-24/s,-80$. This gives (3). [Tidal curvature and regular integration constants](joint-flat-hessian.md)

Fix a smooth reference wave $W$, put $A=s(1-s)G'_W$, and define the full-line clock covector $J$ by $\langle J,Z\rangle=(3/20)\int_a^1 A G'_Z\,ds$. It is supported on $[2a,2]\cup\{0\}$. Relative to using $LZ$ alone, its extra vertex terms in the $u$ coordinate are
$$
 J_0=\frac3{20}\left(3\int_a^1\frac{A}{s^4}\,ds\right)\delta''_0
      -\frac3{20}\left(\int_a^1\frac{A}{s^2}\,ds\right)\delta^{(4)}_0 .
 \tag{4}
$$
The ninth primitive $F_X=(20G_N/3)(u_+^8/8!)*J$ solves the Hamilton equation on every compact test master in this ambient sector. One can obtain its metric as a distributional limit by smoothing the master. The radial scalar is $\int_{-1}^1 F'_X(t+yr)\,dy$, even and smooth in $r$ with values in time distributions at the axis. Formula (2) extends by duality against each compact smooth master. For instance one can localize the response master before smoothing, since its values on a bounded interval suffice on the compact spatial support of each fixed test's Cauchy data.

The moments of $J$ through degree six vanish by (3). Consequently its primitive above vanishes on the left and is at most affine on the right. The right- and left-supported fundamental solutions of $\partial_u^9$ differ by $u^8/8!$. Convolution with $J$ makes their difference globally affine, producing zero metric. This choice of growth at infinity fixes the metric response in the stated master class. On the waist slice at $r>1$ and in a spacetime neighborhood of each such point, the two tails give $\phi=B+(A_0+Bt)/r$ for constants $A_0,B$. It is spatially harmonic, so the TT metric there reduces to $h_{ij}=\partial_i\partial_j (S_{kl}\partial_k\partial_l\phi)/2$. This spatial Hessian is affine in time and its full linearized Riemann tensor vanishes. Thus the spatial TT gauge can have an exterior metric tail with zero physical curvature.

On interior tests alone the homogeneous ambiguity is any polynomial of degree at most eight on $(0,2)$. For example $F_X=u^7$ on that interval gives $G_X=1344s^2$ and nonzero optical tidal curvature, despite $F_X^{(9)}=0$ there. Smooth cutoff extensions retain this local mode. The global continuation and its point-vertex test data are additional physical choices for an isolated subregion.

## When the ambient response has finite energy

The coefficient of $\delta_{2a}^{(4)}$ in $J$ is $-3(1-a)G'_W(a)/20$, obtained by integrating the term $2A Z^{(5)}(2s)/s$ in the optical slope once by parts with the common prefactor $3/20$. The corresponding waist coefficient vanishes since $A(1)=0$. Every other term on $[2a,2]$ is at most third order at an endpoint, with a smooth interior density. Equation (4) supplies the only other fourth derivative, at zero. After five derivatives of the ninth primitive, each fourth derivative of a point mass gives a point mass in $F_X^{(5)}$. The remaining terms are locally bounded, and $F_X^{(5)}$ vanishes outside a compact interval. Thus for $0<a<1$ the global response in (2) has finite wave energy exactly when
$$
 G'_W(a)=0,\qquad \int_a^1 (s^{-1}-1)G'_W(s)\,ds=0 .
 \tag{5}
$$
The two conditions are distinct. Choose $f(s)=F_W(2s)=(s-a)^2+(s-a)^5/(5a^3)$ near $a$ and cut off smoothly inside $(0,1)$. Then $G_W(a)=1/(2a^3)$ and $G'_W(a)=0$. With primes on $f$ denoting $s$ derivatives, $s^{-2}G_W=[f'''/(16s^3)-f''/(16s^4)]'$. Integration by parts gives the second quantity in (5) as $(4a-3)/(8a^4)$. At $a=1/3$ it equals $-135/8$, giving the vertex coefficient $81/32$ in (4). Its propagated singularity reaches the waist sphere at $t=r=1$. Compact interior tests miss this contribution. For the calibrated references with fifth- and tenth-order zeros at $2a$, the vertex integral instead vanishes by the same endpoint primitive. The opposed-packet response then has finite global wave energy even though the probes detect its ninth-derivative jump. [Calibrated interior responses](weak-master.md)

This example concerns the energy of the linearized Hamiltonian response of the measurement. A regional Poisson bracket with arbitrary cap and frame variations, and a quantum clock domain, remain open.

Run `python3 -B checks/weak_normalization.py`. It compares the radial and tangential components of the Cartesian TT metric in (1) directly with (2) for overlapping advanced and retarded lobes on the waist ball and an additional exterior lobe on the complete slice. Piecewise polynomial bells of class $C^{11}$ suffice for this quadrature. Expected output includes unit ADM/master ratios for the symplectic product and energy and ends with `Rim slope = 0, vertex fourth-derivative coefficient = 81/32.` Run `make check` for the full suite. [Executable calculation](../checks/weak_normalization.py)
