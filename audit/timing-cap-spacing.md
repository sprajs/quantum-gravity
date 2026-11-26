# Resolving two nearby cap radii in time

Two clocks use the same emitter, waist and incident vacuum wave, with cap fractions $a=b-\varepsilon$ and $b$. For the clock responses studied here the bracket is nonzero for every fixed positive separation, even arbitrarily small. It is zero for identical fractions and identical timing windows. How much of the bracket survives if the two caps approach one another while the timing window also narrows? [Spherical clock construction](spherical-generator.md) · [Different cap fractions](timing-caps.md) · [Original affine clock, version 1](https://arxiv.org/html/2611.34924v1#S3.E27)

## Geometry and time scales

Set the flat waist radius $R=1$, with proper time in the same length units. Work with the mixed response of the matched-waist clock excess on the common decaying Minkowski radiative continuation. The reference quadrupole has smooth optical slope $p(s)$ for $s$ near $[b,1]$, with $p(b)\ne0$ and $\int_b^1 (s^{-1}-1)p(s)ds=0$. The second condition removes the jump of the outer clock response at the vertex. Let $z_c$ denote the fourth derivative of the master response for fraction $c$, in the normalized radial variable $s$. At a cap, $z_c$ jumps by $d_c=-16G_N(1-c)p(c)$. Translating the entire experiment by a proper time $\tau$ shifts this master by $\tau/2$. The cap singularities of the two experiments therefore meet at $\tau=-2\varepsilon$. [Response profile and symplectic normalization](weak-clock-contact.md)

The delay bracket in the stated order is
$$
 B_{ab}(\tau)=-A\int z_b(s-\tau/2)\,d z_a(s),\qquad A=3/(5120G_N).
$$
Write $dz_a=v_a ds+e_a\delta_0+d_a\delta_a$. The full optical primitives on the two intervals give $e_a=O(\varepsilon)$, $d_a=d_b+O(\varepsilon)$ and $\|v_a-v_b\|_1=O(\varepsilon)$. For example the two smooth branches have bounded spatial derivatives uniformly near a fixed $0<b<1$, their coefficients vary smoothly with the cap, and the interval on which one uses different branches has length $\varepsilon$. There is no waist jump. Since $z_b$ has bounded variation, the integral of the translated density part differs from $\int v_b z_b$ by $O(\varepsilon+|\tau|)$. The cap atom reads the left trace of $z_b$ for $2\varepsilon+\tau>0$ and its right trace for $2\varepsilon+\tau<0$, up to the same error. Integration of $d(z_b^2)/2$ over the complete line yields $\int v_b z_b=-d_b(z_b^-+z_b^+)/2$. Consequently, away from the coincidence line,
$$
 B_{b-\varepsilon,b}(\tau)
 = C_b\,\operatorname{sgn}(2\varepsilon+\tau)+O(\varepsilon+|\tau|),
 \qquad C_b=\frac{A}{2}d_b^2=\frac{3G_N}{40}(1-b)^2p(b)^2 .
$$
The remainder is uniform on the two open sides near $(\varepsilon,\tau)=(0,0)$ for fixed calibrated $p,b$. If both readings sample one incident wave at different launch times $t_1,t_2$, smooth time dependence of that wave adds $O(|t_1|+|t_2|)$ in the pairing. [Common-wave variation](timing-caps.md)

## A prediction for shrinking detectors

Give both readings the same proper-time profile and common timestamp. If the profiles are Gaussian with individual standard deviation $h$, the delay has variance $2h^2$. As $h,\varepsilon\to0$ with $\varepsilon/h\to x\ge0$, the resulting bracket tends to $C_b\operatorname{erf}(x)$. For a measurement defined only over a short time interval, smoothly truncate and normalize the Gaussians within that interval. The Gaussian tail removed has vanishing weight. For a flat diamond expressed in physical units, $x=R\varepsilon/h$ when $h$ is expressed as a length.

For two equal rectangular windows of full duration $h$, both ending at the recorded time, the triangular delay density instead gives
$$
  \frac{B_{\mathrm{windows}}}{C_b}\ \longrightarrow\
  1-\big[\max(1-2x,0)\big]^2 .
$$
These finite-width integrals are ordinary averages of a bounded delay function. Rectangular windows can also be obtained as limits of smooth windows in $L^1$. The two displayed curves use different definitions of width. A limit in which $h$ shrinks first resolves distinct rims and retains $C_b$. Bringing the rims together first gives zero for two identical readings. This calculation concerns the spherical clock's linearized responses. Uniform control of higher orders in gravitational wave amplitude would be needed for a simultaneous nonlinear limit.

At $b=1/2$ choose $p(s)=(152/3)s^4(1-26s/19)$, giving $p(b)=1$ and $C_b=3G_N/160$. Run `python3 -B checks/timing_cap_spacing.py` from the root. At $h=10^{-6}$ it gives normalized brackets $0$, $0.43750012$, $0.75000010$ and $1.00000000$ for $x=0,1/8,1/4,3/4$. The respective exact limits are $0,7/16,3/4,1$. Each piece of the finite-width integrand for this wave is a polynomial of degree at most thirteen in delay. The check uses fourteen interior rational nodes per piece and integrates those polynomials exactly. Run `make check` for the suite. [Reproduction script](../checks/timing_cap_spacing.py)
