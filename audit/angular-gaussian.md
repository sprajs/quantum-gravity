# Can a fixed-area Gaussian corner implement an angular twist?

A twist of a marked sphere preserves its total area while shearing its angular pattern. In the Gaussian model below, a measurement of increasingly fine angular modes of the local area distinguishes the original preparation from its twisted image with probability one. Consequently a nonzero twist has no unitary implementation on the model's Gaussian Hilbert space. This tests a physical displacement of the external marking relative to the fields. The covariance of the log area and the commutativity of its local values are model assumptions. Chandrasekaran's version 1 gives a Gaussian in canonical coordinates and an operator normalization of the area. Deriving the joint law of the reduced corner from these prescriptions remains a proof gap. [Original work, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Canonical Gaussian (4.7)](https://arxiv.org/html/2611.34924v1#S4.E7) · [Area weight (4.24) and fixed area (4.25)](https://arxiv.org/html/2611.34924v1#S4.E24) · [Marked angular covariance and the clock](corner-commutant.md)

## The area measurement

On a unit round sphere write $z=\cos\theta$, with longitude $\varphi$, and use its solid-angle measure $d\Omega$. Set $A=1-\Delta$, with $\Delta$ the nonpositive round Laplacian. Prepare a real, mean-zero-in-angle log field $f$ with centered Gaussian law $\mu$ and covariance $C=A^{-\alpha}$ on $L^2_0(S^2,d\Omega)$, for $\alpha>2$. Each unit harmonic of degree $\ell\ge1$ has variance $\lambda_\ell^{-\alpha}$, where $\lambda_\ell=1+\ell(\ell+1)$. The expected squared $H^s$ norm is $\sum_{\ell\ge1}(2\ell+1)\lambda_\ell^{s-\alpha}<\infty$ for $s<\alpha-1$. Choosing $1<s<\alpha-1$ gives a continuous field almost surely by Sobolev embedding. [Spherical Gaussian regularity, Lang and Schwab](https://arxiv.org/abs/1305.1170)

At fixed total area $\mathscr A>0$, the measured area is $\mathscr A w\,d\Omega$, where
$$
 w=\frac{e^f}{\int_{S^2}e^f d\Omega},\qquad
 f=\log w-\frac{1}{4\pi}\int_{S^2}\log w\,d\Omega .
 \tag{1}
$$
These maps are continuous inverses between centered continuous log fields and normalized strictly positive continuous densities in their uniform topologies. Measuring the commuting area moments $\int h w\,d\Omega$ for all smooth real $h$ determines the density. For example, its spherical harmonic moments determine every positive-time heat smoothing, which converges uniformly to $w$. Formula (1) therefore recovers a measurable log field from the area moments alone.

The smooth twist $g_t(z,\varphi)=(z,\varphi+t z)$ rotates each latitude through its own angle, fixes the poles, and preserves $d\Omega$. For the active displacement of a density set $T_t f=f\circ g_t^{-1}$ and $\mu_t=(T_t)_*\mu$. Normalization (1) commutes with $T_t$.

## What the highest-weight modes measure

Let $h_\ell$ be the unit complex spherical harmonic proportional to $(1-z^2)^{\ell/2}e^{i\ell\varphi}$. Its order $m=\ell$ is called the highest weight. Take $q_\ell(f)=\int\overline{h_\ell} f\,d\Omega$. Under $\mu$, its real and imaginary parts are independent Gaussians of variance $\lambda_\ell^{-\alpha}/2$. Indeed $\sqrt{2}\,\mathrm{Re}\,h_\ell$ and $\sqrt{2}\,\mathrm{Im}\,h_\ell$ are orthonormal real test functions. Together the two quadratures contribute $\mathbb E|q_\ell|^2=\lambda_\ell^{-\alpha}$. For a field drawn from $\mu_t$, the test function on the original preparation becomes $v_\ell=T_t^*h_\ell=e^{i\ell t z}h_\ell$. Its normalized mean square is
$$
 r_\ell(t)=\lambda_\ell^\alpha\mathbb E_{\mu_t}|q_\ell|^2
 =\langle v_\ell,(A/\lambda_\ell)^{-\alpha}v_\ell\rangle .
 \tag{2}
$$

In these coordinates $\Delta=\partial_z[(1-z^2)\partial_z]+(1-z^2)^{-1}\partial_\varphi^2$. Differentiating $v_\ell$, with $k=\ell t$, gives the exact identity
$$
 A v_\ell=\big[\lambda_\ell+k^2(1-z^2)+2ik(\ell+1)z\big]v_\ell .
 \tag{3}
$$
Under the normalized measure $|v_\ell|^2d\Omega$ the $z$ density is proportional to $(1-z^2)^\ell$. Its second and fourth moments are $1/(2\ell+3)$ and $3/[(2\ell+3)(2\ell+5)]$. Thus $\|[A/\lambda_\ell-(1+t^2)]v_\ell\|\to0$. The field $v_\ell$ only has azimuthal order $m=\ell$, so its angular degrees $j$ all obey $j\ge\ell$. On that subspace $A/\lambda_\ell\ge1$. The Lipschitz bound $|x^{-\alpha}-y^{-\alpha}|\le\alpha|x-y|$ on $[1,\infty)$ and the spectral theorem applied to (2) give
$$
 0<r_\ell(t)\le1,\qquad
 \lim_{\ell\to\infty}r_\ell(t)=(1+t^2)^{-\alpha}.
 \tag{4}
$$

For the preparation itself, measure
$$
 B_N(f)=\frac1N\sum_{\ell=1}^N\lambda_\ell^\alpha |q_\ell(f)|^2.
 \tag{5}
$$
Both Gaussian laws are invariant under axial rotations. The real two-dimensional mode planes for distinct positive orders have vanishing cross covariances, since their azimuthal frequencies differ. Joint Gaussianity then gives independence across $\ell$. Within each mode the complex coefficient is circular Gaussian, with independent equal-variance real and imaginary parts. Hence each summand in (5) is exponential with mean $r_\ell(t)$ and variance $r_\ell(t)^2\le1$, including $r_\ell(0)=1$.

Equation (4) gives the limiting expectation of (5), and independence gives $\operatorname{Var}(B_N)\le1/N$. Chebyshev's inequality and Borel–Cantelli yield almost-sure convergence along $N=n^2$. The unnormalized partial sums are increasing and $(n+1)^2/n^2\to1$, giving the same limit along all $N$. Thus $B_N\to1$ almost surely for the original preparation and $B_N\to(1+t^2)^{-\alpha}$ almost surely for its twisted image. For every $t\ne0$ the two events are disjoint. They can be tested on $w$ using (1), proving mutual singularity of the fixed-area laws. A measurement at finite $N$ has statistical spread. The disjoint events concern the continuum of angular resolutions.

## Which other angular maps preserve the Gaussian law?

Every round isometry preserves the covariance exactly. For any smooth area-preserving diffeomorphism $g$, let $T f=f\circ g^{-1}$ and $C'=TCT^*$. The common Cameron–Martin space is the mean-zero Sobolev space $H^\alpha_0$, since a smooth diffeomorphism of the compact sphere acts invertibly there. For the two centered Gaussian laws, equivalence then requires the bounded extension of $R=C^{-1/2} C' C^{-1/2}-I$ to be Hilbert–Schmidt. Failure gives mutual singularity. [Feldman–Hájek criterion, Bolin and Kirchner, Theorem B.1](https://arxiv.org/pdf/2101.07860#page=31)

Writing $y=g^{-1}x$, the order-zero principal symbol of $R$ is
$$
 \left(\frac{|\xi|_{x}^2}{|(Dg_y)^T\xi|_{y}^2}\right)^\alpha-1 .
$$
Here $|\cdot|$ is the round covector norm. The formula follows by composing the principal symbols of the elliptic powers and transporting a test phase at $x$ back to $y$ by $g$. Projection away from the constant mode changes no principal symbol. If $g$ fails to preserve the round metric, the symbol is nonzero at some unit covector. Unit high-frequency packets concentrating there tend weakly to zero while their $R$ expectations tend to the nonzero symbol. This excludes compactness and hence the required Hilbert–Schmidt property. For the latitude twist and the equatorial covector $d\varphi$, the symbol agrees with (4) minus one. [Seeley, elliptic powers](https://doi.org/10.1090/pspum/010/0237943) · [Melo, principal symbol modulo compact operators](https://arxiv.org/abs/math/0312261)

## Consequences for the representation

In the Gaussian Schrödinger space $L^2(\mu)$, the area measurements act by multiplication. Every vector assigns zero probability to every $\mu$-null event. A unitary implementing a single nonzero twist on all these measurements would carry the constant unit vector to one whose area law is the singular transformed law (up to the sign convention for the unitary). This is impossible. The same argument applies with arbitrary multiplicity whenever $\mu$ gives the maximal spectral type of the commuting area algebra.

More generally, suppose a Hilbert space represents the joint area spectral measure and contains a unit vector $\Omega$ with this Gaussian area law. If unitaries implement every $g_t$, their orbit vectors have pairwise singular area laws. Indeed pulling the laws at $s$ and $t$ back by $g_{-s}$ gives the original law and the law at $t-s$. This comparison includes $s=-t\ne0$, even though (5) alone gives equal limits in the original coordinates for those two parameters. The spectral projection of a separating event fixes one vector and annihilates the other. Thus the orbit consists of uncountably many orthogonal unit vectors, and $\|U_t\Omega-\Omega\|=\sqrt{2}$ for every $t\ne0$ when $U_0=I$. Such an orbit excludes a separable representation of the entire family and excludes strong continuity in any Hilbert space containing this vector law. A larger direct sum can carry one discrete twist by permuting sectors.

The test requires the full commuting marked area algebra and a specified vector law. In the interacting corner, the log area may depend nonlinearly on canonical pairs, and local area operators may fail to commute. Testing a single marked moment, enforcing a gauge identification, or changing the representation can therefore pose a different question. Applying this obstruction to the gravitational state count would require deriving the physical area representation and the action of the proposed displacement after matching. [Classical angular generator (B.24)](https://arxiv.org/html/2611.34924v1#A2.E24) · [Matching across subregions, §3.6](https://arxiv.org/html/2611.34924v1#S3.SS6)

## Reproduce the finite-resolution variances

Run `python3 -B checks/angular_gaussian.py` and `make check` from the repository root. For $t=1$ and $\alpha=3$ the expected normalized variances at $\ell=8,32,128$ are **0.23249645, 0.14709651, 0.13022480**, approaching **0.12500000**. The program projects the twisted harmonic onto the ordinary spherical harmonics at the same $m$. It checks the total spectral mass, the mean and variance of $A/\lambda_\ell$ independently against (3), then refines the quadrature and the maximum angular degree. [Executable check](../checks/angular_gaussian.py)
