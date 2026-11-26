# Translating a cap across gravitational radiation

The expansion of a null face gives a measurable charge at its moving rim. Its change between two cuts includes both shear and expansion. Generating time translations of the radiative data requires more information. Below we recover a Hamiltonian when both sides of the cut are retained, and construct pulses for which every intrinsic metric variation vanishes near both end cuts although the intervening symplectic flux is nonzero. This identifies a condition on repairs of the cap evolution in Venkatesa Chandrasekaran's version 1. [arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1) · [Cap charge variation (3.50b)](https://arxiv.org/html/2611.34924v1#S3.E50.2) · [Earlier single-cut audit](03-4.md)

## What a moving rim measures

Fix a smooth null hypersurface before caustics and its generator structure. In an affine representative write $\ell=\partial_u$, $\mu$ for the positive area element on each cut and $\theta=\partial_u\log\sqrt q$. Compare sections along $\xi=f(y)\ell$ with $\partial_u f=0$ and fixed normalization in field space. For the Einstein metric potential $\boldsymbol\theta$ the unmodified cut variation is $k_\xi=\delta Q_\xi-i_\xi\boldsymbol\theta$. On a fixed cut the field-space curl of $\int_C k_\xi$ is $-\int_C i_\xi\omega$, where $\omega=\delta\boldsymbol\theta$. Chandrasekaran, Flanagan and Prabhu choose a boundary potential $\Theta_N$ with $\delta\Theta_N=\omega|_N$. Adding $\int_C i_\xi\Theta_N$ cancels that curl and gives their Wald–Zoupas localized charge. With their reference constant and the stated cut orientation it is

$$
Q^{\rm loc}_f(C)=\frac{1}{8\pi G}\int_C f\,\mu\,\theta .
$$

For $f=1$ this measures the affine derivative of the cut area divided by $8\pi G$. Holding generator labels fixed, $\partial_u\mu=\theta\mu$ and vacuum Raychaudhuri gives $\partial_u\theta=-\theta^2/2-\sigma_{AB}\sigma^{AB}$. Thus the later-minus-earlier reading is

$$
8\pi G\,[Q^{\rm loc}_f(C_2)-Q^{\rm loc}_f(C_1)]
=\int_{u_1}^{u_2}du\int_C f\,\mu
\left(\tfrac12\theta^2-\sigma_{AB}\sigma^{AB}\right).
$$

Here $du\,\mu$ is the positive coordinate measure for increasing $u$. With $\mu$ as the positive cut two-form, the null three-form in their (6.32) obeys $i_\ell\epsilon_N=-\mu$, accounting for the reversed coefficient in that oriented flux. The added one-form changes the generator equation for the open cap. The localized charge balances flux on a single face. A constant affine displacement on that face also moves the bifurcation sphere of a complete diamond, where the two face generators point in distinct null directions. Chandrasekaran and Prabhu explicitly exclude these displacements from their matched diamond symmetry. [Boundary potential and cut variation, (2.24)–(2.25)](https://arxiv.org/pdf/1807.11499#page=16) · [Charge and flux, (6.30)–(6.32)](https://arxiv.org/pdf/1807.11499#page=48) · [Causal diamonds, Remark 4.1](https://arxiv.org/pdf/1908.00017#page=19)

**Exact vacuum example.** Take $ds^2=-2du\,dv+u^{2p}dx^2+u^{2q}dy^2$ on $1\leq u\leq32$ with unit coordinate periods in $x,y$ and $(p,q)=(3/5,-1/5)$. The only possible Ricci component is $R_{uu}=-[p(p-1)+q(q-1)]/u^2=0$. The nonzero tidal component $R_{uxux}=-p(p-1)u^{2p-2}$ distinguishes this wave from flat spacetime. On $v=\mathrm{const}$, $\sqrt q=u^{2/5}$, $\theta=2/(5u)$ and $\sigma^2=8/(25u^2)$. The endpoint change of $\sqrt q\,\theta$ and the directly integrated density $-(6/25)u^{-8/5}$ both give **$-7/20$**. The compact torus makes the transverse integral finite. The balance law itself also applies to spherical cuts.

## Recovering the generator when the radiation is retained

Let a slab have oriented boundary $\partial V=\Sigma_t-\Sigma_0+N_{0t}$ and rim $\partial\Sigma_t=C_t$, with other boundary contributions absent or held fixed so that they contribute zero. Thus $\partial N_{0t}=C_0-C_t$. For a smooth vacuum solution and two linearized solutions, $d\omega=0$. For prescribed embeddings, pulled back to the common solution space, Stokes' theorem gives the conserved two-form

$$
\Omega_{\rm total}(t)=\int_{\Sigma_t}\omega+\int_{N_{0t}}\omega
=\int_{\Sigma_0}\omega .
$$

For a fixed vector field $\xi$ that induces an allowed variation $X_\xi g=\mathcal L_\xi g$, the on-shell identity $\omega(\delta,X_\xi)=d k_\xi$ gives $\Omega_{\rm total}(t)(\delta,X_\xi)=\int_{C_0}k_\xi$. The two copies of $\int_{C_t}k_\xi$ cancel. If the anchor ensemble admits a differentiable generator at $C_0$, its Hamiltonian therefore works on the completed data. A diffeomorphism supported away from the anchor has zero charge there. This prescription retains the intervening field history or, equivalently for the symplectic balance, matches a complementary region across the cut. The physical evolution of a cap with independent embedding data requires its own boundary conditions. A field-dependent lapse or freely varied embedding requires the extra terms in (3.50b) and (B.21). [Iyer and Wald, (75)](https://arxiv.org/pdf/gr-qc/9403028#page=14) · [Version 1, (B.21)](https://arxiv.org/html/2611.34924v1#A2.E21)

A radiative sector makes the cancellation and a nonzero generator explicit. On flat $ds^2=-2du\,dv+dx^2+dy^2$, take the real, transverse trace-free perturbation $h(u)T_{AB}$ with constant polarization on a transverse torus. On the $v=\mathrm{const}$ sheet choose increasing-$u$ orientation and put $c=\int T_{AB}T^{AB}\,dx\,dy/(32\pi G)>0$. In this linearized sector (3.39) gives $\Omega_I=c\int_I D h'\wedge D h\,du$ for an interval $I$, where $D$ is the field-space derivative. Translating the profile means $Xh=h'$. Integrating once by parts gives

$$
\Omega_I(\delta,X)=D\!\left[c\int_I(h')^2du\right](\delta)
                -c[h'\delta h]_{\partial I}.
$$

The endpoint one-form $c h' D h$ has curl $c\,D h'\wedge D h$. Split the full affine line at any cut into two intervals and require smooth matching of $h,h'$ there and compactly supported smooth profiles. The two rim terms cancel and $H=c\int_{\mathbb R}(h')^2du$ generates translations of the entire profile. This Hamiltonian is quadratic in the linearized graviton and belongs to the matched system. [Null potential, (3.39)](https://arxiv.org/html/2611.34924v1#S3.E39)

## A restriction on instantaneous corner repairs

Suppose the symplectic flux through every translated strip could be written as the difference between field-space two-forms on its end cuts. First allow each cut form to depend smoothly on the intrinsic cut metric, any finite set of its derivatives along or across the cut *within the null face*, and fixed frame data. At a round Minkowski cone with affine radius $u=1+s$, $0\leq s\leq1$, vary $q_{AB}$ by $u^2 a(s) T_{AB}(y)$, where $T$ is a nonzero smooth trace-free tensor on the unit sphere. Fix the optical area and its first derivative at the initial rim. Since the shear source in Raychaudhuri is quadratic at this background, $D\mu=0$ along the cone at first order. The shear term in (3.39) then gives, with $T$ contracted on the unit sphere and increasing-$u$ orientation,

$$
\int_N\omega(\delta_a,\delta_b)=
\frac{\int_{S^2} T^{AB}T_{AB}\,d\Omega}{32\pi G}
\int_0^1 (1+s)^2(a'b-b'a)\,ds .
$$

Take any nonzero smooth bump $a$ supported strictly inside the interval and $b=-s a$. The integrand is $(1+s)^2 a^2$. All variations of the intrinsic metric and its derivatives at both rims vanish. Every stipulated corner two-form therefore evaluates to zero at both ends, while the swept symplectic flux is strictly positive. Tangential total divergences integrate to zero on these closed cuts. The counterexample excludes an intrinsic instantaneous primitive for unrestricted profiles on a spherical null face. Transverse data, the interior of a spacelike cap, and independent fields with their own evolution fall outside the hypothesis. [Fixed-frame shear current](03-4.md) · [Characteristic data and optical constraints in version 1](https://arxiv.org/html/2611.34924v1#S3.SS2)

There is a stronger test in the plane-wave sector. Take variations $h=a$ and $h=a'$ for a bump on the null strip. Both metric perturbations vanish in open spacetime neighborhoods of the two end cuts, including all transverse derivatives. Yet their flux is $2c\int (a')^2du>0$. These variations are tangent to genuine local vacuum families. Write the transverse metric as $R^2\operatorname{diag}(e^h,e^{-h})$, set $h=\lambda a+\nu a'$, and solve $R''=-R(h')^2/4$ with $R=1,R'=0$ initially. On a fixed finite strip $R>0$ for sufficiently small amplitudes and $D R=0$ at $\lambda=\nu=0$. The argument applies to two-forms built from finitely many spacetime derivatives of the metric in this sector.

There is also a dimension bound if one adds independent endpoint variables. For $n$ disjoint bumps the $n$ pairs $(a_j,a'_j)$ have zero cross-pairings and give a flux matrix of rank $2n$. Suppose all initial auxiliary data are fixed, the remaining metric jets at the final cut have zero variation on these test vectors, and the final auxiliary state lies in a smooth manifold of dimension $d$. Pulling back any two-form on this endpoint state gives rank at most $d$. Taking $2n>d$ rules out a finite-dimensional store for all such pulses. For fields on a cut the bound applies only if the chosen homogeneous sector and its evolution leave finitely many endpoint variables. An angular field space, a full cap, or an entire radiative history can carry infinite rank.

The remaining **proof gap** concerns the external, freely radiating caps of version 1. An unrestricted repair must exhibit the compensating two-form and its generator for the chosen embeddings and joints, or specify how the admissible boundary conditions restrict the test profiles. The separate nonclosure of the printed finite-cap two-form concerns a field-space three-form already on one slice. This flux test concerns transport of a two-form between slices. [Reduced Hamiltonian (3.53b)](https://arxiv.org/html/2611.34924v1#S3.E53.2) · [Finite-cap closure test](cap-crosscheck.md)

## Reproduce the calculations

Run `python3 checks/radiative_flux.py` from the repository root. The five lines should report, in order, `-7/20`, `5/415701`, `1/1716099`, `0` and `5/415701`. The script uses exact fractions and the polynomial $a(s)=s^5(1-s)^5$ on the unit interval. It checks the flux integrals and the separate rim terms before summing. The all-orders endpoint argument above uses a smooth compact bump. Run `make check` for the repository suite, which should exit successfully. [Executable calculation](../checks/radiative_flux.py)
