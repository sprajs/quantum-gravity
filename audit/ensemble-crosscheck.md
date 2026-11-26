# Which Schwarzschild entropy does the conical determinant compute?

**The short answer.** *The paper's clock, area-packet, and fixed-mass formulas are algebraically consistent with one another, but assigning the local conical coefficient directly to the finite-width Gaussian packet requires an additional measure or determinant calculation.*

**Verdict.** Equations (5.66), (5.68), and (5.69) are mutually consistent. Because a Gaussian window of width $\Delta s \propto \sqrt{s}$ sums over an area band that grows with horizon size, a fixed-area count and a finite-width packet trace naturally differ by a half-logarithm ($\tfrac12\log s$). That difference is real, but it does *not* by itself establish a numerical error in the Schwarzschild prediction. What Eq. (5.67c) still needs is an ensemble-specific determinant and collective-coordinate measure calculation showing that the displayed conical coefficient belongs to the full finite-width trace.

## The trace and the width

Write $b=s_b$, $s=A/(4G_N\hbar)$, and $\nu_\ell(ds)=\sum_{i\in\mathcal H_{\mathscr D}}e^{-s_i}\delta_{s_i}(ds)$, with multiplicity in the sum. The boost weight and Eq. (5.25) give the exact packet trace

$$
T(b)=\operatorname{Tr}(C_b^\dagger C_b)=\int e^{-(s-b)^2/(4b)}\,\nu_\ell(ds).
$$

For $s\ge0$, integration of the kernel against $db/\sqrt{4\pi b}$ gives $e^{(s-|s|)/2}=1$. This verifies the resolution of unity in Eq. (5.66) even for an irregular discrete spectrum. The kernel has height one and standard deviation $\sqrt{2b}$ in $s$. Its area under $ds$ grows as $\sqrt{4\pi b}$. [Eq. (5.25)](https://arxiv.org/html/2611.34924v1#S5.E25) · [Eq. (5.66)](https://arxiv.org/html/2611.34924v1#S5.E66)

For the following comparison alone, take an interior packet separated from the cutoff by many widths and assume a sufficiently smooth local coarse-grained density $\nu_\ell(ds)\sim C s^p ds$ over the relevant range. Changing variables to $s=b+\sqrt{2b}\,x$ gives

$$
T(b)\sim C\sqrt{4\pi}\,b^{p+1/2},\qquad
\int^{s_*}\nu_\ell(ds)\propto s_*^{p+1}\quad(p>-1).
$$

The cumulative result also holds for a fixed fractional band of $s_*$ under the stated scaling. Restoring $e^s$ to the **local** density gives $dN/dM\sim C e^s s^p\,ds/dM\propto e^s s^{p+1/2}$, since $s\propto M^2$. The packet of the boost-weighted trace thus has the same logarithmic coefficient as the unweighted density **per unit mass** in this model. It would be incorrect to undo the boost weight inside a broad, unweighted state count by simply multiplying the integrated count by its central value $e^b$. The local scaling assumption is additional to the exact resolution of unity. A cumulative power law alone permits structure in windows much narrower than $s_*$.

## An explicit test of the replica distinction

If the exact area eigenspace $j$ has rank $g_j$, the normalized packet gives this eigenspace total probability $P_j=g_j e^{-s_j}f_b(s_j)/T(b)$. All its occupied vectors have equal weight within that eigenspace. The von Neumann entropy therefore satisfies two exact expressions,

$$
S_b=\sum_j P_j\log g_j-\sum_j P_j\log P_j
    =\langle s\rangle_b-\langle\log f_b\rangle_b+\log T(b).
$$

For integer levels $s_j=j\ge1$ and $g_j=\lceil e^j j^p\rceil$, truncated above the packet, the area-label distribution approaches a discrete Gaussian of variance $2b[1+o(1)]$. Its Shannon entropy is $\tfrac12\log(4\pi e b)+o(1)$. Meanwhile $-\langle\log f_b\rangle_b=\tfrac12+o(1)$. These two terms can have different orders because the former contains the normalization and the level weights. The fixed-level entropy has coefficient $p$, whereas the normalized packet entropy relative to $\langle s\rangle_b$ has coefficient $p+1/2$. This example isolates the effect of the width without making assumptions about the gravitational spectrum. If the true area spacing also scales, even a fixed-level degeneracy needs a level-density factor for conversion to a density per unit $s$. [Packet entropy argument](https://arxiv.org/html/2611.34924v1#S5.SS3.p10.2) · [Fixed-eigenspace entropy in the manuscript](https://arxiv.org/html/2611.34924v1#S5.SS4.p5.2)

## The two conditional predictions

Let $c=106/45$. The purely local arithmetic yields $c\log s_b$ from the Euler surface term on a sphere. Write $k=q/[2(1-q)]$ for the coefficient in the clock-restricted trace. The relevant possibilities are

| Quantity | $c$ assigned to full packet | $c$ assigned to density per unit $s$ |
|---|---:|---:|
| Power $p$ per unit $s$, with boost weight | $167/90$ | $106/45$ |
| Packet and per-unit-mass logarithmic coefficient | $106/45$ | $257/90$ |
| Clock coefficient $k=p+1$ | $257/90$ | $151/45$ |
| Clock ratio $q=2k/(1+2k)$ | $257/302$ | $302/347$ |

The second column reproduces the manuscript. The third is a conditional sensitivity test. Neither the exact integral identity nor the difference between a level and a packet selects a column. [Eqs. (5.67)–(5.69)](https://arxiv.org/html/2611.34924v1#S5.E67)

**Strongest defense.** Evaluating a local invariant at a background of specified area need not impose a sharp area constraint on the path integral over fluctuations. In four dimensions a packet with $\Delta s\propto\sqrt{s}$ has an asymptotically constant mass width. If the full reflected one-loop functional, including its area collective coordinate, yields a natural measure proportional to $dM\propto ds/\sqrt{s}$ multiplying $s^c$, the integration across one packet gives an order-one factor in mass units. The conical coefficient may then be the complete answer in Eq. (5.67c). Sen's independent calculation supports the physical value in this ensemble. His Eqs. (1.3)–(1.4) define a density per unit mass with angular momenta summed. At $D=4$, $C_{\rm local}=212/45$ multiplies the logarithm of a length, giving $106/45$ times the logarithm of area. [Sen, Eqs. (1.3)–(1.5)](https://arxiv.org/pdf/1205.0971#page=6)

**What the manuscript still needs.** Before Eq. (5.67a) the replica cancellation is stated at fixed $s$. The surface curvature integral has no specification of the normalization of a sharp area constraint, the induced measure along the Schwarzschild family, or the integration over area fluctuations on one joined replica versus independently closed copies. Appendix D.1 supplies a formal constrained measure including corner pairs. Appendix D.3 writes regular integrals over $ds$ with unspecified weights $k_a(s)$. Neither evaluates the power those factors contribute in the Schwarzschild packet. A derivation can resolve this by showing the constrained determinant per $ds$, with the Jacobian for the area mode, and then performing the Gaussian integral. An equivalent check is to evaluate the normalized full-packet replica derivative with those modes and boundary conditions retained and compare to Sen's spin-summed density. Until then the numerical agreement is verified and the Lorentzian extraction is conditional. [Conical argument](https://arxiv.org/html/2611.34924v1#S5.SS3.p11.1) · [Appendix D.1 measure](https://arxiv.org/html/2611.34924v1#A4.SS1.p4.1) · [Appendix D.3 area integral](https://arxiv.org/html/2611.34924v1#A4.SS3.p8.1)
