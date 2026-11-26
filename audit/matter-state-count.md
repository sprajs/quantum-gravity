# Can a geometric clock count states of a massless scalar?

A diamond that admits a state, preserves an exact noncompact scalar shift, and can measure the shifted field value has **infinite clock rank**. The measurement can have finite resolution. This conditional result applies even when the scalar gravitates. Chandrasekaran studies four-dimensional *vacuum* gravity in version 1. His matter example is in two-dimensional JT gravity. The question here concerns an extension of the four-dimensional theory. [Chandrasekaran, abstract and §§2–3, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1)

## A finite-rank obstruction

Let $P$ project onto the physical states accepted at one clock ceiling, with all other specified boundary conditions fixed. Suppose a unitary $U$ on this physical Hilbert space preserves the window, $UPU^\dagger=P$. Suppose there is a scalar-value measurement with outcomes on $\mathbb R$, represented by a countably additive positive operator-valued measure $E$ with $E(\mathbb R)=1$. Require, for a single fixed step $a>0$ and all Borel sets $B$,

$$
U E(B) U^\dagger=E(B+a).
$$

**Proof.** If $P$ had finite positive rank $d$, the uniform state $\rho=P/d$ would be invariant under $U$. Its scalar readout would define an ordinary probability $\mu(B)=\operatorname{Tr}(\rho E(B))$ with $\mu(B+a)=\mu(B)$. The intervals $[na,(n+1)a)$, $n\in\mathbb Z$, partition the line. Equal probabilities on these intervals cannot sum to one. Thus $P$ has rank zero or infinite. The proof requires no condition on the postmeasurement state and allows gravitational and scalar variables to be entangled.

A finite test follows from the same hypotheses. Prepare $N$ accepted density matrices $\rho_j$ and use a single measurement with pairwise disjoint outcome bins with effects $E_j$. If each intended bin has probability at least $s$, then $\rho_j\le P$ and

$$
Ns\le\sum_j\operatorname{Tr}(\rho_j E_j)
\le\operatorname{Tr}\!\left(P\sum_j E_j P\right)\le d
$$

whenever $d$ is finite. A translated packet can be read in a bin of fixed width with a fixed success probability. Sufficiently separated translates then give disjoint bins for any $N$. This formulation identifies what a regulated computation could test even when exact covariance is in question.

## What a shift changes in Einstein–scalar theory

For the minimally coupled free real scalar with action $-\tfrac12\int d\phi\wedge\star d\phi$, the equations and stress tensor are invariant under $\phi\mapsto\phi+a$. Each classical solution $(g,\phi)$ therefore has translates $(g,\phi+a)$ with the same metric and the same focusing along every generator. A candidate physical readout uses a normalized smearing of the scalar pulled back into the diamond's geometrically defined frame. Moving the fields and the frame together under a spacetime diffeomorphism preserves that reading. An internal scalar shift moves it by $a$. Even two different constant scalar solutions stay distinct under spacetime pullback if their constant values are physical. Their labels alone give no family of normalizable quantum states. [Chandrasekaran, frame pullback, Eq. (3.40)](https://arxiv.org/html/2611.34924v1#S3.E40) · [Barreto and da Rocha, scalar stress and null hypersurface equations (2), (12)](https://journals.aps.org/prd/pdf/10.1103/PhysRevD.105.064049)

The relevant unitary has to act *within* the physical diamond sector. Dirichlet data fixing the scalar at a cap or in the exterior send a global translate into a different boundary problem. Shifting only the interior against a fixed exterior introduces gradients and associated stress. In a phase space that allows the boundary scalar to vary, the shift charge and possible flux through the boundary still require calculation. Treating the shift as gauge requires the corresponding constraint or fixed-charge reduction and removes an absolute scalar-value readout. An algebra containing only derivatives also cannot distinguish translates by their offset. A change of algebra alone supplies no finite-rank theorem. A quantum implementation must specify how a calibration reference for the scalar is available in the stated ensemble. The vacuum boundary conditions in v1 prescribe gravitational data. [Chandrasekaran, Eqs. (3.18)–(3.19)](https://arxiv.org/html/2611.34924v1#S3.E18)

## A round-cone calculation at fixed size

On an expanding spherical null segment, fix corner radius $R$, cap fraction $0<\epsilon<1$, and areal coordinate $v=r/R\in[\epsilon,1]$. Choose the on-cone scalar data $\phi(v)=q+\alpha(v-\epsilon)$. The offset $q$ is its value on the initial cut. With affine tangent $k=\partial_u$, Einstein's equation gives $R_{kk}=8\pi G(\partial_u\phi)^2$. With zero shear, $r''=-4\pi G r(\partial_u\phi)^2$. Substituting $\partial_u\phi=\alpha r'/R$ and integrating gives

$$
\partial_v\log r'=-4\pi Gv\alpha^2,\qquad
u_*(\alpha)=r'(u_c)(u_S-u_c)
=R\int_\epsilon^1 \exp[\,2\pi G\alpha^2(v^2-\epsilon^2)\,]\,dv .
$$

This uses the affine clock and the cap normalization of v1. Roundness makes the angular average equal to this reading. The flux delays the clock even though its offset has no effect. [Chandrasekaran, Eqs. (3.25b)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27)

On this segment choose the orientation for which the scalar symplectic potential is $4\pi R^2\int_\epsilon^1 v^2\partial_v\phi\,\delta\phi\,dv$. This follows by pulling the scalar action's boundary variation onto the null sheet. Its $dq$ coefficient is $p=K\alpha$, with $K=4\pi R^2(1-\epsilon^3)/3$. The remaining term is proportional to $\alpha\,d\alpha$, giving zero exterior derivative. The resulting two-parameter form is $dp\wedge dq$. Geometric variations depending only on $\alpha$ have zero two-form pullback on this family. We quantize this segment model with this form. The cap, transverse data, joint matching, physical inner product, and invariance under full evolution would have to be supplied to embed this calculation in the quantum diamond.

**Real scalar.** Take $q\in\mathbb R$ and the Schrödinger representation $L^2(\mathbb R,dp)$. The clock is the multiplication operator $u_*(p/K)$. It increases strictly with $|p|$ from $u_0=(1-\epsilon)R$ to infinity. For every ceiling $\ell>u_0$ there is a unique $p_*>0$ with $u_*(p_*/K)=\ell$. Define

$$
\psi_n(p)=\frac{\mathbf 1_{[-p_*,p_*]}(p)}{\sqrt{2p_*}}
  \exp[-in\pi p/p_*],\qquad n\in\mathbb Z .
$$

Integrating the phase difference gives $\langle\psi_m,\psi_n\rangle=\delta_{mn}$. Every packet passes with probability one, with precisely the same distribution of $p$ and hence the same clock and null-focusing distributions at fixed cap slope. The conjugate momentum contributes stress, and its support is bounded uniformly in $n$. The packets differ by field translations of $n\pi\hbar/p_*$. Bin the field reading $q$ into intervals of width $\pi\hbar/p_*$ centered on the translated peaks. Fourier transformation gives the correct-bin probability $(2/\pi)\int_0^{\pi/2}(\sin x/x)^2\,dx=0.77369501$ for each. At $\ell=u_0$ the allowed momentum set is a single point of zero measure and the window is empty. The customary homogeneous spatial mode provides a parallel check in a fixed periodic cavity, where the conjugate momentum contributes energy $p^2/(2V)$ at spatial volume $V$. [Martín-Martínez and Louko, finite periodic cavity, Eqs. (II.10)–(II.14)](https://arxiv.org/pdf/1404.5621#page=3)

The sharp momentum edge gives those particular packets infinite field variance. A finite-variance preparation replaces the flat envelope with $\cos(\pi p/(2p_*))/\sqrt{p_*}$ on the band and uses shifts spaced by $2\pi\hbar/p_*$. Its squared envelope has only Fourier harmonics $0,\pm1$ on the band, so all nonzero even-harmonic overlaps vanish. Integrating the squared momentum derivative gives $\operatorname{Var}(q)=(\pi\hbar/(2p_*))^2$. Chebyshev's inequality gives correct-bin probability at least $3/4$ for every translate at this spacing. Direct integration of the Fourier probability across the doubled bin width gives $0.97009405$.

**Compact scalar.** Identify $q$ modulo $2\pi f$, with $f>0$, and use periodic wave functions. Now $p_n=n\hbar/f$. For the same segment and $\ell>u_0$ the rank is $2\lfloor f p_*/\hbar\rfloor+1$. A normalized uniform probability on the target circle exists. At the minimal reading the constant rotor state passes. Making the target compact removes the real-line obstruction, while the growth of the clock with $|p|$ supplies the finite count in this model.

For $\epsilon=1/2$ and $\ell=1.1u_0$, the accepted band is $|z|\le0.52947131$, where $z=\sqrt{2\pi G}\,p/K$. At rotor spacings $\Delta z=0.20,0.10,0.05$ the ranks are $5,11,21$. The real scalar admits the entire orthonormal family at that same geometric size. Run `python3 checks/matter_state_count.py` from the repository root. Expected output includes the three ranks, an orthonormality check for 16 packets, and the bin probability above. The repository suite runs the same calculation with `make check`. [Executable check](../checks/matter_state_count.py)

## Other internal labels

If one admitted spatial state can carry $N$ distinguishable orthogonal internal labels, and the constraints and clock preserve every copy with the same reading, the window has rank at least $N$. A continuous rotation of a finite spin multiplet still spans a finite space. An infinity of exactly degenerate distinguishable labels *in one physical theory* would force infinite rank. Increasing a finite species count across a sequence of theories gives a lower bound for each member. Its gravitational parameters and its admissible states can vary with the species content.

For an Einstein–matter diamond, the decisive calculation is to construct the physical shift and its calibrated readout after imposing the boundary data, then test shift invariance and nonemptiness of the same clock projection. A specified mechanism that breaks the shift, fixes the scalar boundary value, makes the target compact, or removes its charge sector changes those hypotheses. Each mechanism leaves its own clock-rank calculation. The segment gives an exact model obstruction and the measurement argument gives a conditional theorem. The vacuum conjecture remains open.
