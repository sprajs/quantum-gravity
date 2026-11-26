# The Schwarzschild logarithm and Sen’s ensembles

**The physical question.** *Does the paper's logarithmic correction to Schwarzschild black-hole entropy genuinely match Ashoke Sen's benchmark calculation—and what does that numerical match actually prove?*

**The short answer.** **The numerical comparison passes, but the match is currently a local one-loop consistency check rather than an independent microscopic derivation.** For pure Einstein gravity in four dimensions, Sen's density of states per unit mass—summed over all angular momenta—has a positive logarithmic correction of $(106/45)\log[A_H/(4G_N\hbar)]$. That matches both the ensemble named and the coefficient printed in (5.69). However, the manuscript extracts this number from a known local graviton-and-ghost heat-kernel coefficient. Its stronger claim requires identifying the full trace of the clock-restricted interior Hilbert space with the fixed-mass density at infinity, and a local curvature integral supplies only part of that identification. [Manuscript, (5.66)–(5.69), pp. 48–49](https://arxiv.org/pdf/2611.34924v1#page=48) · [Sen, (1.1)–(1.5) and §3.2](https://arxiv.org/pdf/1205.0971#page=6)

## What Sen counts

Let $c=k_B=1$, $\ell_P^2=G_N\hbar$, $r_h=2G_N M$, and $s=A_H/(4\ell_P^2)=\pi r_h^2/\ell_P^2=4\pi G_N M^2/\hbar$. Sen uses $G_N=\hbar=c=1$ and a length parameter $a$ proportional to $r_h$. Thus $\log(a/\ell_P)=\tfrac12\log s+\text{constant}$. A choice of reference mass for defining the density also changes only a constant. Sen (1.2) gives $C_{\rm local}=424/90=212/45$ for a graviton with its ghosts. The following coefficients multiply the indicated logarithm in the **entropy**, with its leading term $s$ removed. [Sen, introduction and §3](https://arxiv.org/pdf/1205.0971#page=5)

| Four-dimensional ensemble, per unit mass at the Schwarzschild saddle | Coefficient of $\log(a/\ell_P)$ | Coefficient of $\log s$ | Sen |
| --- | ---: | ---: | --- |
| Sum over all angular momentum states | $212/45$ | $106/45$ | (1.4), (3.16) |
| Specify one Cartan component $J_3=0$, sum over allowed total spins | $212/45-1=167/45$ | $167/90$ | (1.1), (3.12) |
| Select only rotational singlets $J=0$ | $212/45-3=77/45$ | $77/90$ | (1.5), (3.21) |

The mixed ensemble sets the angular chemical potential to zero and includes states with nonzero spin on a spherical saddle. The inverse temperature integration contributes zero powers of $a$ in four dimensions. Sen’s footnote 10 assumes a suitable complex saddle contour because an asymptotically flat Schwarzschild black hole has negative specific heat. A projection onto one magnetic quantum number costs one power of $a$, and the singlet projection costs three through the local rotation-group Haar integral. Sen also treats the translational zero modes, the center-of-mass phase space and the ambient thermal gas in defining the intrinsic density. These steps explain why his final mixed-ensemble coefficient reduces to the local coefficient. [Sen, (2.41), (3.4)–(3.5), (3.13)–(3.21) and Appendix B](https://arxiv.org/pdf/1205.0971#page=24)

## Two independent ways to check the local number

1. Bastianelli, Bonezzi and Melis (44) give the total four-dimensional spin-two and ghost coefficient on an Einstein background. On Ricci-flat Schwarzschild its curvature term is $53 R_{abcd}R^{abcd}/45$. For the smooth Euclidean solution, $R_{abcd}R^{abcd}=12r_h^2/r^6$, the Euclidean time period is $4\pi r_h$ and the radial volume factor after angular integration is $4\pi r^2dr$. Hence the full curvature integral is $(4\pi r_h)(4\pi)\int_{r_h}^\infty 12r_h^2r^{-4}dr=64\pi^2$. Multiplication by $53/[45(4\pi)^2]$ gives $212/45$ per log length. The $1/2$ in a bosonic log determinant is compensated by the factor of two in scaling eigenvalues of a second-order operator. Adding a separate polarization factor or ghost subtraction would count degrees of freedom twice. [Bastianelli, Bonezzi and Melis, (18), (36), (44)](https://arxiv.org/pdf/2206.13287#page=7)

2. El-Menoufi’s Schwarzschild effective-action calculation gives the coefficient of $\log(\mu^2 A_H)$ as $64\pi^2\Xi$. With only the graviton, $\Xi=424/(11520\pi^2)$, which again gives $106/45$. The renormalized curvature-squared coupling absorbs the dependence on the arbitrary subtraction scale. The calculation checks the sign, the logarithm’s argument and the factor of two by a different route using the same low-energy gravitational field content. [El-Menoufi, (1.7)–(1.9)](https://arxiv.org/pdf/1511.08816#page=6)

The manuscript uses the surface version of the curvature calculation. The linear replica defect of the Euler integral contains $8\pi(1-n)\int_S R[q]dA$. A spherical cut has $\int_S R[q]dA=8\pi$, again giving $64\pi^2$. The entropy derivative $-\partial_n [\log Z_n-n\log Z_1]_{n=1}$ changes the sign of $1-n$, giving the positive term in (5.67c). The terms proportional to the square of the mean-curvature vector vanish under the stated marginality condition, and the ambient Ricci tensor vanishes on Schwarzschild. This verifies the local surface computation. The curvature-squared identity on a smooth saddle alone would be insufficient for taking the replica derivative. The defect formulas give the required surface variation. [Fursaev, Patrushev and Solodukhin, (1.4)–(1.6) and (3.14)](https://arxiv.org/pdf/1306.4000#page=14) · [Manuscript, (5.67)](https://arxiv.org/html/2611.34924v1#S5.E67)

## Keep the packet, integrated trace and density distinct

Write $z=s_b$ and $T(z)=\operatorname{Tr}[f_z(\hat s)e^{-\hat s}P_\ell]$ with $f_z(s)=e^{-(s-z)^2/(4z)}$. The identity $\int_0^\infty f_z(s)\,dz/\sqrt{4\pi z}=1$ holds for every $s\ge0$. Expanding the square reduces it to the Gaussian integral $\int_0^\infty z^{-1/2}e^{-z/4-s^2/(4z)}dz=2\sqrt\pi e^{-s/2}$. If $T(z)$ scales as $z^C$ uniformly in a fixed fractional area band that supplies a nonzero fraction of $Z(\ell)$, then (5.66) gives $Z(\ell)$ scaling as $s_*^{C+1/2}$. With $C=106/45$ and $s_*\propto\ell^2$,

$$
\frac{q}{2(1-q)}=\frac{257}{90},\qquad q=\frac{257}{302}.
$$

Equations (5.60)–(5.61) then require $x^2=257/347$, where $x=(1-\epsilon)r_h/\ell$. An independent clock-distribution calculation could test this additional prediction. Using both equations fixes the limiting clock-to-radius ratio. [Manuscript, (5.56)–(5.66)](https://arxiv.org/pdf/2611.34924v1#page=47)

For a direct density check, suppose the weighted number of states per unit $s$ has the smooth asymptotic form $w(s)=e^{-s}dN/ds\sim K s^p$. At an interior packet center, integrating over $s=z+2\sqrt z\,t$ gives $T(z)\sim 2\sqrt\pi K z^{p+1/2}$. Thus $p=C-1/2$. Restoring $e^s$ **in the spectral measure** and changing variables gives

$$
\frac{dN}{dM}=e^{s(M)}w(s(M))\frac{ds}{dM}
\sim {\rm const}\,e^{s(M)}s(M)^C,\qquad
\frac{ds}{dM}=4\sqrt{\pi G_N/\hbar}\sqrt{s}.
$$

There is no spare $1/2$ to add to (5.69). The packet width $\Delta s\sim\sqrt s$ is a mass width of constant order, and integrating a fixed fractional band gives a mass range of order $M$. Differentiating the integrated weighted count and changing variables accounts for both factors. Numerically integrating the smooth model with $K=1$ gives $T(z)/z^C=3.60123,3.54547,3.54491$ for $z=10^2,10^4,10^6$, tending to $2\sqrt\pi=3.54491$. This checks the conversion under the stated smooth-density hypothesis. [Manuscript, (5.66) and (5.69)](https://arxiv.org/html/2611.34924v1#S5.E66) · [Sen, §4 on converting area and mass densities](https://arxiv.org/pdf/1205.0971#page=28)

## What still needs a derivation

- **The full replica measure.** The known bulk coefficient fixes the local scale term. The manuscript compares replicas at fixed $s$, then assigns that coefficient to the Gaussian packet trace $T(z)$. For a discrete area spectrum of degeneracies $d_s$, its normalized packet entropy obeys $S_b=H(P_s)+\sum_sP_s\log d_s$, where $P_s\propto d_se^{-s}f_z(s)$. If contributing levels have fixed additive spacing and a smooth weighted density, the mixing entropy $H(P_s)$ itself contains $\tfrac12\log z$. Establishing (5.67c) requires showing where the area integration and its normalization enter the replicated determinant, together with any surviving ghost zero modes, corner modes or contact terms. The cited focusing appendix gives a bound on a two-replica ratio. Its bound does not evaluate these terms with their scale dependence. A demonstration could evaluate the full normalized packet replica derivative with a specified regulator and boundary conditions. Counting an area-width factor a second time after such a calculation would give a spurious shift. [Manuscript, (5.66)–(5.67)](https://arxiv.org/html/2611.34924v1#S5.E66) · [Appendix D, replicated measure](https://arxiv.org/html/2611.34924v1#A4.SS3.p7.1)
- **The ensemble at infinity.** At the classical Schwarzschild saddle, the displayed mass–area relation is exact. In Planck units a small Kerr spin gives $s(M,J)=4\pi M^2-\pi J^2/M^2+O(J^4/M^6)$, so spins of order $M$ change the area entropy by order unity. This explains the paper’s scale estimate. The number of such angular states still grows with $M$, as Sen’s projection factors demonstrate. The finite interior trace has no displayed projector for the asymptotic mass and no explicit resolution into asymptotic spin representations or subtraction of exterior excitations. Showing that its boundary conditions implement the unrestricted spin sum and intrinsic rest-mass density is an additional step. A Gaussian asymptotic for the weighted area measure also leaves its pointwise behavior between discrete eigenvalues undetermined. A specified mass coarse graining or a local spectral asymptotic would make the density statement precise. [Manuscript, discussion before (5.69)](https://arxiv.org/html/2611.34924v1#S5.E69) · [Sen, mixed ensemble](https://arxiv.org/pdf/1205.0971#page=26)

The match to Sen is genuine at the level of the proposed one-loop coefficient. Its strongest evidential use is as a check that the proposal can accommodate the known infrared answer. The additional physical claims depend on the packet determinant, the clock projection and the identification of the states counted at infinity.
