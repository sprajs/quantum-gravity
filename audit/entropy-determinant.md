# Which Schwarzschild cuts and measures enter the area packet?

**An intrinsically round marginal surface on the Schwarzschild horizon can give a clock excess proportional to the horizon radius.** At the same mass and area, displacing the cut along the horizon by a quadrupole of amplitude $\alpha r_h$ gives
$$
\frac{\bar u_*-(1-\epsilon)r_h}{r_h}
=\frac35\left(\frac{1-\epsilon}{\epsilon}\right)^2\alpha^2
+O_\epsilon(\alpha^3).
$$
Here $\epsilon$ is the fixed ratio of cap to corner area radius. A cut on a fixed radial ingoing null hypersurface has a different property. Marginality selects exactly one cut there, and its transverse shape determinant cancels in a normalized insertion that locates the cut. Finally, the reduced spherical mass mode gives a packet of constant weight per fixed conjugate-time width, or of weight proportional to $\sqrt{s_b}$ per fixed conjugate-boost width. These results isolate geometric and measure conditions on the proposed one-loop calculation. [Venkatesa Chandrasekaran, *An algebraic quantization of gravity from the null cone*, arXiv:2611.34924v1, Eqs. (5.51)–(5.53)](https://arxiv.org/html/2611.34924v1#S5.E51) · [Area packet, Eqs. (5.66)–(5.69)](https://arxiv.org/html/2611.34924v1#S5.E66)

## A clock test at fixed mass and horizon area

Use ingoing Eddington–Finkelstein coordinates with metric $-Fdv^2+2dv\,dr+r^2d\Omega^2$, $F=1-r_h/r$. On the future horizon $r=r_h$ take the cut $v=V(y)$, with $y$ a point of the unit sphere. Write $D$ for the unit-sphere covariant derivative, $\Delta=D^AD_A$, $\Omega_{AB}$ for its metric and $\kappa=1/(2r_h)$. All these cuts have induced metric $q_{AB}=r_h^2\Omega_{AB}$, corner area $4\pi r_h^2$ and outgoing null normal $\ell=\partial_v$ of zero expansion and shear. Orthogonality to $e_A=\partial_A+V_A\partial_v$, nullness and $\ell\cdot n=-1$ give the future inward normal at the cut,
$$
n=-\partial_r+\frac{D^AV}{r_h^2}\partial_A
+\frac{|DV|^2}{2r_h^2}\partial_v .
$$
Using $\chi^{(n)}_{AB}=-n\cdot\nabla_{e_A}e_B$ gives exactly
$$
\chi^{(n)}_{AB}=-r_h\Omega_{AB}+D_AD_BV+\kappa V_AV_B .
$$
Consequently $\Theta_{(n)}<0$ uniformly for $V=\alpha r_hY(y)$ with fixed smooth $Y$ and small enough $|\alpha|$. The trace-free Hessian in this equation produces inward shear even with the same intrinsic round metric and stationary ambient vacuum geometry. [Marginal boundary condition, Eq. (5.51)](https://arxiv.org/html/2611.34924v1#S5.E51)

Choose the area reference element $d\Omega$ in the angular labels of the emitters on the cut. The corner area radius is $\varrho_S=r_h$ in each direction. Follow the inward, hypersurface-orthogonal null geodesics until their area radius is $\epsilon r_h$. Use a fixed $0<\epsilon<1$. At $\alpha=0$ this entire segment has positive screen area and monotone radius. Smooth dependence of the geodesics and their angular separation on initial data preserves these properties, uniformly on the sphere, for sufficiently small $|\alpha|$ at that $\epsilon$. This supplies the caustic-free inward sheet used for the future-half clock in §5.3. Along the horizon sheet itself the area radius is constant. The v1 clock is invariant under a constant affine rescaling on each generator. For an affine parameter $u$ increasing from cap to corner, use the prime for $d/du$. Twice integrating the vacuum equation $\varrho''=-\varrho\sigma_{ab}\sigma^{ab}/2$ gives the exact identity
$$
u_*-(1-\epsilon)r_h
=\varrho'_c(u_S-u_c)-(\varrho_S-\varrho_c)
=\frac12\int_{u_c}^{u_S}(u_S-u)\varrho\sigma_{ab}\sigma^{ab}\,du .
$$
In particular, nonzero shear on an open portion of the sheet produces a strictly positive average excess. [Focusing and capped clock, Eqs. (3.25)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E25)

Normalize the inward Killing energy of each geodesic to one. Its initial angular momentum covector is $D_AV$ and $dr/d\lambda=-1+O_\epsilon(\alpha^2)$ in an inward affine parameter $\lambda$. The angular displacement from the emitter at radius $r$ is $(1/r-1/r_h)D^AV+O_\epsilon(\alpha^2)$ in local sphere coordinates. The pullback angular metric divided by $r^2$ is therefore $\Omega_{AB}+2(1/r-1/r_h)D_AD_BV+O_\epsilon(\alpha^2)$. The $dv^2$ part of the induced metric at fixed $r$ starts at second order. Taking the trace-free derivative of the screen metric gives
$$
\sigma_{ab}\sigma^{ab}
=\frac{|(D^2V)^{\rm TF}|^2}{r^4}
+O_\epsilon(\alpha^3/r_h^2).
$$
In the quadratic excess one may evaluate the affine interval, radius and endpoints on the background. Its radial integral is $\frac12\int_{\epsilon r_h}^{r_h}(r_h-r)r^{-3}dr=(1-\epsilon)^2/(4r_h\epsilon^2)$. The angular average in v1 is the ordinary sphere mean because $\varrho_S$ is constant. For $Y=P_2(\cos\theta)=(3\cos^2\theta-1)/2$, integration by parts gives $\langle|(D^2Y)^{\rm TF}|^2\rangle=(6^2/2-6)\langle Y^2\rangle=12/5$. These factors give the coefficient above. All error estimates keep $\epsilon$ fixed.

At fixed small nonzero $\alpha$, Schwarzschild length scaling makes the entire dimensionless clock reading independent of $r_h$. At any fixed clock ceiling $\ell/r_h>1-\epsilon$ the deformation can be chosen small enough for this reading to pass. Averaging over spatial rotations of this quadrupole gives a rotationally invariant classical distribution with the same positive excess in every member. This example disproves a uniform $o(r_h)$ estimate based solely on the mass, intrinsic sphere metric and marginal expansions, even for exact vacuum Schwarzschild. The spherically symmetric **embedding** used in v1 has $V$ constant and gives the claimed zero excess. Equation (5.53) concerns an expectation in the prescribed trace. Extending the estimate to that trace requires control of its weight on cuts or equivalent interior data with shear, or boundary conditions that select the symmetric embedding. Whether two embeddings describe distinct preparations depends on how the physical cap and emitters are specified. No degeneracy is assigned to the set of embeddings in this calculation. [Clock estimate in v1, Eqs. (5.52)–(5.53)](https://arxiv.org/html/2611.34924v1#S5.E53)

## The transverse shape determinant on a fixed null sheet

Fix $v=v_0$ and allow any positive smooth graph $r=R(y)$. This is a different deformation from moving along the horizon. Now $n=-\partial_r$ and $\Theta_{(n)}=-2/R$. The other future null normal with $\ell\cdot n=-1$ has components $\ell^v=1$, $\ell^A=-D^AR/R^2$ and $\ell^r=(F-|DR|^2/R^2)/2$. Tracing $-\ell\cdot\nabla_{e_A}e_B$ on this graph gives
$$
\Theta_{(\ell)}=\frac{1-r_h/R-\Delta\log(R/r_h)}{R}.
$$
At a maximum of $R$ the Laplacian of $\log R$ is nonpositive. If $\Theta_{(\ell)}=0$, this implies $R_{\max}\le r_h$. Its minimum similarly gives $R_{\min}\ge r_h$. The only marginal graph is $R=r_h$. This removes the assumption of a round trial graph on this specified null hypersurface. Linearizing under $R=r_h+f$ at fixed $M$ gives the transverse shape operator and eigenvalues
$$
L_{r_h}=\frac{1-\Delta}{r_h^2},\qquad
\lambda_j=\frac{1+j(j+1)}{r_h^2}
\quad\text{with multiplicity }2j+1 .
$$
It is strictly positive, including the radial monopole. In the general marginal-surface stability formula, the normal connection and the vacuum Einstein-tensor term vanish on this round cut and the Gaussian curvature equals $1/r_h^2$, giving the same operator. [Senovilla, Eq. (1)](https://arxiv.org/pdf/1210.3731#page=2)

Let $L_1=1-\Delta$ on the unit sphere. Its scalar heat trace is $e^{-t}[t^{-1}+1/3+O(t)]=t^{-1}-2/3+O(t)$. This expansion can also be obtained directly by Euler–Maclaurin summation of $(2j+1)e^{-t j(j+1)}$ before multiplying by $e^{-t}$. There are no zero modes, hence $\zeta_{L_1}(0)=-2/3$. With a fixed inverse length $\mu$, zeta scaling gives
$$
\log\det{}_\zeta(L_{r_h}/\mu^2)
=\log\det{}_\zeta L_1+\frac23\log(\mu^2 r_h^2).
$$
Holding the area fixed to first order removes the monopole ($\delta A=2r_h\int f\,d\Omega$). Omitting it shifts the constant term in the heat trace to $-5/3$ and the determinant coefficient to $+5/3$ per $\log(\mu^2 r_h^2)$. A mass change along the Schwarzschild family changes both $r_h$ and the metric. This direction is distinct from the radial displacement at fixed metric above.

One implementation of marginality uses the cut as a derived location. At any finite angular cutoff the normalized linear locator integrates to one,
$$
\int d^N f\;\delta^{(N)}(L_{r_h} f)\,|\det L_{r_h}|=1 .
$$
Both factors must use the same mode set and normalization. The same cancellation holds with a small metric source displacing the root of the linear equation. Thus a cut located in this way has zero net shape logarithm from this pair of factors. A constraint insertion at a physically specified surface has its own measure. A bare inverse determinant in a specified mode measure would instead carry the opposite sign of the displayed determinant. None of these individual powers can be added to Eq. (5.67c) without specifying which cut variables are integrated and the corner, metric and ghost measure for the replicated trace. [v1 replica calculation](https://arxiv.org/html/2611.34924v1#S5.E67) · [Constrained measure in Appendix D.1](https://arxiv.org/html/2611.34924v1#A4.SS1)

## The spherical mass mode and the packet width

Use Planck units. Kuchař's canonical reduction of the two-ended, spherically symmetric vacuum Schwarzschild solution has the mass $M$ and a conjugate relative asymptotic time $T$, up to an orientation choice. With $s=4\pi M^2$, set $p=s/(2\pi)$ and $\eta=\kappa T=T/(4M)$. The stationary Killing orbit accumulates boost angle $\kappa T$ in the normal plane at the bifurcation sphere. Directly on this two-dimensional phase space,
$$
dM\wedge dT=4M\, dM\wedge d\eta=dp\wedge d\eta .
$$
A strip of constant $T$ width $W_T$ has Liouville volume density $W_T\,dM\propto s^{-1/2}ds$. A strip of constant $\eta$ width $W_\eta$ has density $W_\eta\,ds/(2\pi)$. Changing coordinates with the boundaries of a given strip carried along gives identical volume. Fixing each width independently prepares different strips. These are contributions per chosen conjugate orbit volume. The analytic continuation through a fixed boost in v1 supplies the Boltzmann weight and by itself specifies no real width $W_\eta$. [Kuchař, *Geometrodynamics of Schwarzschild black holes*](https://doi.org/10.1103/PhysRevD.50.3961)

For the height-one area packet $f_b(s)=e^{-(s-b)^2/(4b)}$, the two stripped integrals are
$$
\int_0^\infty s^{-1/2}f_b(s)\,ds
=2\sqrt\pi[1+3/(4b)+O(b^{-2})],\qquad
\int_0^\infty f_b(s)\,ds
=\sqrt{\pi b}\,[1+\operatorname{erf}(\sqrt b/2)] .
$$
Thus the spherical collective measure contributes respectively zero or $+1/2$ to the coefficient of $\log b$. The calculation concerns phase-space volumes in the reduced sector. If a separate graviton and ghost factor behaves as $s^c$ across the packet and the residual measure factorizes, these slopes would add to $c$. A finite clock-projected Hilbert-space trace requires its own construction. In the related boxed Schwarzschild reduction, Louko and Whiting obtained a normalized $dM$ integral with a specified trace regulator and discussed the effect of changing its measure. Their box and normalization are additional boundary input. The spherical sector has no spin fluctuations and supplies no test of Sen's angular-momentum sum. The full null-cone packet coefficient $106/45$ and clock ratio $257/302$ remain conditional on the trace measure, the marginal ensemble and the matching to infinity. [Louko and Whiting, Eqs. (5.10)–(5.11) and Appendix A](https://arxiv.org/pdf/gr-qc/9411017#page=16) · [Sen, Eqs. (1.3)–(1.5)](https://arxiv.org/pdf/1205.0971#page=6) · [Prior ensemble comparison](ensemble-crosscheck.md)

## Reproduce the calculations

Run `python3 checks/entropy_determinant.py` or the full `make check` from the repository root. The script independently follows the exact axisymmetric geodesics at $r_h=1$. For angular momentum $J=\partial_{\theta_0}V$ it integrates $w=-dr/d\lambda=\sqrt{1-FJ^2/r^2}$ and $d\theta/dr=-J/(r^2w)$. At fixed $r$ the angular separation $\partial_{\theta_0}\theta$ and the orthogonality relation $\partial_{\theta_0}v=J\partial_{\theta_0}\theta$ give $\varrho^2=r^2w\sin\theta\,(\partial_{\theta_0}\theta)/\sin\theta_0$. The script locates each cap at the prescribed $\varrho$ and uses its affine slope to obtain the measured clock. Averaging the signs of $\alpha=0.002$ cancels the cubic correction. The spectral sum and direct packet integrals use their respective eigenvalues and mass-coordinate Jacobian. [Executable calculation](../checks/entropy_determinant.py)

```text
shape heat constant, first l=0: -0.666667
shape heat constant, first l=1: -1.666666
packet powers, fixed time and boost widths: -0.00004, 0.50000
quadrupole delay / alpha^2 at epsilon=0.5: 0.600017, analytic 0.600000
quadrupole delay / alpha^2 at epsilon=0.65: 0.173968, analytic 0.173964
```
