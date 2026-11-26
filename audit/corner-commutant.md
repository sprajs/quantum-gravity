# Does the marked corner area commute with the quantum clock?

At fixed positive total area, the local area moment in Venkatesa Chandrasekaran's version 1 is bounded. It cannot be a nonconstant linear coordinate in the global Schrödinger representation of (4.7). There is a different route to its spectrum. If one angular displacement at an external, physically marked corner acts covariantly on the area distribution, a particular area moment has **no eigenvectors**. Every nonzero clock window that commutes with that moment then has infinite rank. The covariance and clock commutation are distinct identities. An explicit two-cell model below satisfies the classical invariance and the positive quantum ordering of the clock while violating the second identity after a nonlinear change of canonical variables. [Source and version](https://arxiv.org/abs/2611.34924v1) · [Earlier conditional rank theorem](finite-kinematics.md)

## Which canonical variable could represent the area moment?

Write $M_f=\int_S f(y)\widehat w_y\,\epsilon_0(y)$ for the normalized area moment in (4.24), with $M_1=I$. It suffices to have a normalized positive operator-valued measure $M$ on the marked sphere, meaning that each vector has a positive scalar area measure. Its values on different sets need not commute. The dimensional surface charge is $K_f=\mathscr A M_f/(8\pi G_N)$. Positivity gives
$$
  (\min f)I\le M_f\le(\max f)I .
$$
Appendix B explicitly uses a pair $(\mathscr K(y),\Pi_{\mathscr K})$ for the classical angular generator. Read as a *global* linear Weyl coordinate, any nonconstant regular canonical smearing would have a conjugate unitary that translates its spectrum by every real amount. The displayed bounds exclude this for the physical $K_f$. The pair is meaningful locally, or as a field with restricted range. A global unconstrained coordinate such as a logarithmic shape variable could instead enter the density nonlinearly. The product Gaussian of (4.7) alone does not specify the multiplication law of that density. [Classical angular generator (B.24)](https://arxiv.org/html/2611.34924v1#A2.E24) · [Schrödinger pairs (4.7)](https://arxiv.org/html/2611.34924v1#S4.E7) · [Weyl relation (4.20)](https://arxiv.org/html/2611.34924v1#S4.E20) · [Area normalization (4.25)](https://arxiv.org/html/2611.34924v1#S4.E25)

## One angular displacement rules out point spectrum

Choose a marked round angular frame, let $h=\cos\theta$, and let $\phi_t$ be the complete smooth flow of $\xi=\nabla h$ in its unit round metric. The height satisfies $\xi h=1-h^2$. Suppose the angular area measure assigns zero operator mass to the two poles, as it does for a density with respect to solid angle. Assume there are unitaries $U_t$, strongly continuous at $t=0$ with $U_0=I$, on the **same fixed-area physical representation**, satisfying
$$
 U_tM_hU_t^*=M_{h\circ\phi_t}.
$$
This requires the transformation of just one moment along one flow. Its classical generator is suggested by the term $\Pi_{\mathscr K}\partial_A(\mathscr K\xi^A)$ in (B.24), with the sign of $t$ fixed by the pullback convention. The flow need not preserve the clock. [Angular generator (B.24)](https://arxiv.org/html/2611.34924v1#A2.E24)

**Proof.** Compactness of the sphere gives uniform convergence of the difference quotient of $h\circ\phi_t$ to $1-h^2$. The norm bound on $M_f$ gives operator-norm convergence
$$
  D_t=\frac{U_t M_hU_t^*-M_h}{t}\longrightarrow M_{1-h^2}.
$$
If $M_h\psi=\lambda\psi$ for a unit vector, then $\langle\psi,D_t U_t\psi\rangle=0$ for every $t\ne0$, by moving the bounded $M_h$ to the eigenvector on either side. Strong continuity and norm convergence imply $\langle\psi,M_{1-h^2}\psi\rangle=0$. Yet the integrand $1-h^2$ is positive off the two poles and the vector's scalar area measure has mass one there. This contradiction excludes every eigenvector without assuming that $\psi$ belongs to the domain of an angular generator. All scalar spectral measures of $M_h$ are atomless. The proof allows singular continuous spectrum.

For any finite clock cutoff let $P=\mathbf1_{[0,\ell]}(T)$ in this fixed-area sector. If $P\ne0$ and $PM_h=M_hP$, a finite-dimensional range would contain an eigenvector of the self-adjoint restriction of $M_h$. Thus its rank is infinite. The result applies to any nonzero window and dispenses with identifying a Gaussian shape coordinate. Even for a singular area measure one can choose the axis before testing the flow. In the separable incoming Fock space choose a dense sequence of unit vectors and form a weighted average of their scalar area probabilities, with all weights positive and summing to one. A singleton has nonzero operator mass precisely when the averaged probability assigns positive mass to it. There are only countably many such points, so almost every choice of antipodal axis has zero mass at both poles. The quantum covariance must then hold for that chosen axis. [Clock selection (5.20)](https://arxiv.org/html/2611.34924v1#S5.E20)

**Which action is physical?** Mark $h$ on the external reference sphere and displace its angular embedding relative to the bulk fields. A simultaneous diffeomorphism of embedding and fields preserves their pullback, and supplies no such flow. An internal subdivision can lose its frame after gluing. The matching maps, transformed normal connection and cap boundary conditions must permit the displacement on the fixed-area sector. Appendix C.1 compares amplitudes under changes of boundary variables. Appendix C.3 realizes exponentials of Weyl operators for Schwartz symbols of finitely many canonical pairs. Neither identifies a strongly continuous unitary for (B.24) obeying the moment identity above in the chosen continuum representation. Membership of some unitary in the full algebra of bounded operators would not establish its geometric action. [Embedding and pullback (3.40)](https://arxiv.org/html/2611.34924v1#S3.E40) · [Matching and internal frames, §3.6](https://arxiv.org/html/2611.34924v1#S3.SS6) · [Boundary phases (C.1)](https://arxiv.org/html/2611.34924v1#A3.E1) · [Finite-mode source unitaries (C.18)](https://arxiv.org/html/2611.34924v1#A3.E18)

## A classically invariant clock can lose the quantum commutation

The charge generates a relative boost in the smooth-vertex potential (3.42a). At fixed embedding, shifting the external boost angle leaves the area density and the conformal profiles in area coordinates invariant. Its quantum counterpart would be invariance of the closed clock form, including its domain, under $\exp(isK_h/\hbar)$. For a densely defined closed form this implies commutation with every clock spectral projection, by uniqueness of its associated operator. For one window, commutation with $P$ alone suffices. The following example tests the implication from the *classical* invariance when (4.22)–(4.26) are ordered in arbitrary canonical variables. [Smooth-vertex potential (3.42)](https://arxiv.org/html/2611.34924v1#S3.E42) · [Positive ordered clock (4.26)](https://arxiv.org/html/2611.34924v1#S4.E26)

Take two angular cells of unit quadrature weight and a dimensionless shape coordinate $x$. Assign their fields $f_+=x, f_-=-x$. On each cell set $z^2=0$ and $z^1(v)=(v-\epsilon)x^3$, where $0\le\epsilon<1$. This one-pair model constrains the radiation to a prescribed shape profile. In coordinates $(x,\pi_x)$, both fields are multiplication operators on $L^2(\mathbb R,dx)$, so the ordered clock commutes with the marked moment $M_h=\tanh x$ for $h=(1,-1)$. Classically the relative shift of $\pi_x$ leaves both fields invariant.

Use instead the global canonical chart $x=p+q^3, \pi_x=-q$, with $[q,p]=i\hbar I$. Quantize the *same classical field symbols* by Weyl ordering in this chart. Write $X=p+q^3$ for the operator and $b=3\hbar^2/2$. The Weyl product obeys $x\star x=x^2$ and
$$
 x^2\star x=x^3-\frac{\hbar^2}{8}(\partial_p^2 x^2)(\partial_q^2x)
             =x^3-bq .
$$
The possible cubic term vanishes since $\partial_p^3x^2=0$. Thus $Z=\mathcal Q(x^3)=X^3+bq$, and $e^{itX/\hbar}Z e^{-itX/\hbar}=Z+bt I$. The polynomial identities initially hold on Schwartz functions. Multiplication by a quartic phase and a Fourier transform put $X=k, q=i\hbar\partial_k$. In that representation $Z=k^3+bi\hbar\partial_k$ is itself a phase conjugate of $bi\hbar\partial_k$, with spectrum $\mathbb R$. In particular the translation is exact. Unitarily transporting the original operators to the new chart would preserve their commutation. [Weyl prescription (C.9)](https://arxiv.org/html/2611.34924v1#A3.E9)

Apply the manuscript's operator normalization and its focusing cap $c>0$. The area factors are $\rho_\pm=\sqrt{\mathscr A/(1+e^{\mp2X})}$, $M_h=\tanh X$, and $a=\rho_++\rho_-$ is bounded below by $\sqrt{\mathscr A}$. From (4.22) the integrated shear is $d(v)Z^2$ with $d(v)=(v^2-\epsilon^2)/8$. Consequently
$$
  T_c=\sum_{\pm}B_\pm\int_\epsilon^1
       e^{\min(d(v) Z^2,c)}\,dv\, B_\pm,
  \qquad B_\pm=\rho_\pm a^{-1/2}.
$$
Each factor of $T_c$ is bounded. Conjugation by $e^{itX/\hbar}$ replaces $Z$ with $Z+btI$. Spectral dominated convergence first in $Z$, then in $v$, gives the strong limit
$$
  e^{itX/\hbar}T_c e^{-itX/\hbar}
       \longrightarrow (1-\epsilon)e^c\mathscr A\,a^{-1}
       \quad (t\to+\infty).
$$
At $t=0$ the clock differs from this upper bound. The integrated deficit is positive on a spectral interval about $Z=0$. Each $B_\pm$ has dense range, so sandwiching it leaves a nonzero positive deficit. Since $\tanh$ is one-to-one, any bounded operator commuting with $M_h$ would commute with every $e^{itX/\hbar}$. Hence $[T_c,M_h]\ne0$, and at least one clock spectral window fails to commute. [Capped focusing in (5.5)](https://arxiv.org/html/2611.34924v1#S5.E5)

This is an ordering counterexample in a fixed-area model with prescribed profiles. It establishes a proof gap for transferring the boost invariance through an unspecified nonlinear canonical chart. The corner argument for infinite vacuum rank needs a physical angular action, a nonzero clock window, and local-boost invariance of that window. The last condition can be tested directly on the spectral projection, or for every window on a bounded clock resolvent, using the actual reduced fields and the cap and matching conditions of version 1.

## Reproduce a clock matrix element

Set $\hbar=\mathscr A=c=1$, $\epsilon=0$, and $b=3/2$. In the $X=k$ representation write $G(k)=e^{ik^4/(4b)}$, so $Z=G b i\partial_k G^*$. Take the square-integrable vector $\psi=B_+^{-1}G e^{-k^2/2}$. The two factors $G^*B_\pm\psi$ are proportional to translated Gaussians since $B_-/B_+=e^{-k}$. Both therefore have the same normalized Fourier intensity. Their common normalized $Z$ density is $e^{-(z/b)^2}/(b\sqrt\pi)$. The ratio of $\langle\psi,e^{itX}T_c e^{-itX}\psi\rangle$ to the zero-focus clock expectation $\langle\psi,T_0\psi\rangle$ is the average of $\exp[\min(v^2(z+bt)^2/8,1)]$ over this density and $0\le v\le1$. A commuting clock would give a constant ratio. The unitaries here are functions of the marked moment, as $X=\operatorname{arctanh}M_h$.

Run `python3 checks/corner_commutant.py` from the repository root. Expected ratios at $t=0,4,20$ are **1.05346849, 2.10587400, 2.59975135**, approaching $e$. The script integrates the capped radial factor by a convergent exponential series and compares two Simpson meshes for the Gaussian average. [Executable check](../checks/corner_commutant.py)
