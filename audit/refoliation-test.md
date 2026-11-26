# Do two interior cuts give the same amplitude?

Jonathan Oppenheim asks whether Venkatesa Chandrasekaran’s null-cone theory ([arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1)) preserves the diffeomorphism symmetry of general relativity at the quantum level. Checking this directly requires separating three distinct levels:

1. **One-particle symplectic conservation (passes in a $(t,z)$-restricted free graviton model).** On a flat cut and a bent cut, the one-particle pairing of a single graviton polarization is exactly equal—a consequence of symplectic current conservation. However, restricting the wave to $(t,z)$ removes the transverse directions where unitary non-implementability between generic curved cuts is already known to occur for free fields in $3+1$ dimensions ([Torre and Varadarajan](https://arxiv.org/abs/hep-th/9811222)).
2. **Fixed-slice quantum stress commutators (central anomaly appears unless embedding dependence cancels it).** In the corresponding free oscillator theory, two normal displacements obey the right commutator, whereas a normal displacement and a tangential relabeling produce a central term ($1$ and $4$ at levels $2$ and $3$) that no constant shift of $H_0$ removes.
3. **Nonlinear null-cone lapse variation (open quantum test).** In version 1’s own sheared null geometry, the inner lapse varies quadratically with the shear ($\partial_a\log N(v)=-a(1-v^2)$), so linear checks never probe the nonlinear gravitational transport needed for quantum refoliation.

[Oppenheim’s critique](https://superposer.substack.com/p/has-ai-come-for-quantum-gravity) · [Venkatesa Chandrasekaran, arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1)

---

## Which symmetry is at issue?

Version 1 verifies several classical and algebraic symmetry identities, none of which proves full quantum refoliation invariance:

| Operation | What version 1 checks vs. what remains open |
|---|---|
| Bulk diffeomorphism moving solution and reference frame together | With $\delta g=\mathcal L_\xi g$ and embedding shift $\chi=-\xi$, $X^*(\delta g+\mathcal L_\chi g)=0$. Proves **classical** gauge invariance of the dressed observable in (3.59). |
| Frame transformation at a single matched corner | Outward charges of a common boost cancel at equal corner area; a relative boost remains physical (§§3.5–3.6). |
| Basis insertion or boundary relabeling on one fixed intermediate cap | Completeness gives open sewing (4.29) once both propagators are represented; matched boundary unitaries cancel in (C.1). |
| **Moving the intermediate cap** while holding external preparations and source locations fixed (**refoliation**) | Requires mapping states between two distinct embeddings and comparing independently generated evolutions. Invoked in the abstract, Figure 28(a), Figure 30, §5.2, and Appendix E.1 (including for closed preparations). **Open.** |

Testing refoliation does not require a Dirac quantization of every constraint: a reduced theory can establish it by constructing consistent quantum transport of states and observables across embeddings. [Classical matching](03-5-6.md) · [Open and closed sewing](04-gluing.md) · [Appendix C.1 and Appendix E.1](https://arxiv.org/src/2611.34924v1)

---

## 1. One-particle pairing on a deformed spacelike cut

*Linearized symmetry-reduced control.* In flat four-dimensional spacetime, consider a transverse-traceless perturbation $h_{xx}=-h_{yy}$ depending only on $(t,z)$ (all other components zero). The linearized vacuum equations reduce to $(\partial_t^2-\partial_z^2)h_{xx}=0$, with quadratic action $\tfrac12\int[(\partial_t q)^2-(\partial_z q)^2]\,dt\,dz$ after absorbing transverse area and gravitational normalization. Take $z$ to be $2\pi$-periodic as an infrared convention.

Compare the flat cut $t=0$ with a smooth spacelike graph $t=f(z)$ ($|f'|<1$), such as $f(z)=0.6(1-\cos z)$, which meets the ends of the period with matching tangents. For right-moving modes $u_n=e^{in(z-t)}/\sqrt{4\pi n}$ ($n\ge 1$), the momentum density on the graph is $\Pi_f=(\partial_t+f'\partial_z)q|_{t=f}$ (the $\sqrt{1-f'^2}$ factor in the induced length cancels its inverse in the future unit normal). The symplectic pairing on the bent cut is

$$
(u_m,u_n)_f =
\frac{m+n}{4\pi\sqrt{mn}}\int_0^{2\pi}
(1-f'(z))\, e^{i(n-m)(z-f(z))}\,dz
=\delta_{mn}.
$$

Because $w=z-f(z)$ traverses one period monotonically, the pairing is exact for every smooth periodic spacelike graph in this family and for finite linear combinations of wave packets. Prepared on fixed exterior caps and evolved via the free wave equation, two packets resolve the same one-particle inner product on either cut.

**Sensitive control on the tilt.** Omitting the tilt term—keeping $\partial_t q$ instead of $\Pi_f$ on the bent cut—drops $(1-f')$ from the integrand and produces a spurious overlap $|(u_1,u_2)|=0.304092$ in place of $0$. Properly accounting for cap motion matters even in the free theory.

**Why this does not settle quantum refoliation.** Exact equality of the one-particle pairing follows from classical conservation of the symplectic current. The decisive quantum question is whether evolution between two cuts is implemented by a **unitary operator** on the full Fock (or physical) Hilbert space. Dropping the two transverse coordinates suppresses the infinite transverse multiplicity where unitary non-implementability arises even for free fields in $3+1$ dimensions. [Torre and Varadarajan](https://arxiv.org/abs/hep-th/9811222)

---

## 2. Two displacements in opposite order: the fixed-slice commutator anomaly

*Free oscillator control.* On the flat slice of the same $(t,z)$-restricted free field ($\hbar=1$, $p=\partial_t q$), a lapse $F(z)$ generates normal motion and a shift $w(z)$ generates tangential motion:

$$
H[F]=\tfrac12\int F(p^2+q'^2)\,dz,\qquad
D[w]=\int w p q'\,dz .
$$

Classically, the Poisson bracket gives $\{H[F],H[G]\}=D[FG'-GF']$: the difference between applying two normal motions in opposite orders is a tangential relabeling.

Quantizing with the standard free oscillator representation (zero mode fixed to zero) and vacuum-normal-ordered chiral Virasoro generators $L_m,\bar L_m$, set $H_m=L_m+\bar L_{-m}$ and $D_m=L_m-\bar L_{-m}$. Each chiral sector satisfies

$$
[L_m,L_n]=(m-n)L_{m+n}+c_m\delta_{m+n,0},
\qquad c_m=(m^3-m)/12,
$$

as checked directly on the vacuum via $\|L_{-m}|0\rangle\|^2=\tfrac12\sum_{j=1}^{m-1}j(m-j)=c_m$ for $m>0$. Because reversing indices on the opposite chirality flips its central term, the normal and tangential generators obey

$$
[H_m,H_n]=(m-n)D_{m+n},\qquad
[D_m,H_n]=(m-n)H_{m+n}+2c_m\delta_{m+n,0}.
$$

- The normal–normal commutator passes without anomaly.
- The bare mixed commutator carries excess central terms $1$ for $(m,n)=(2,-2)$ and $4$ for $(3,-3)$. No fixed constant shift of $H_0$ can absorb both (a shift contributes in the ratio $4:6$, not $1:4$).

This calculation tests fixed-slice stress generators alone. True geometric transport also differentiates the generators with respect to the embedding itself: in the parametrized two-dimensional free scalar theory, an embedding-dependent contribution cancels the curvature phase around a closed loop of slices. The calculation therefore flags a concrete term to check in gravitational transport rather than computing an anomaly coefficient for four-dimensional interacting gravity. [Kuchař’s scalar construction](https://doi.org/10.1103/PhysRevD.39.2263) · [Torre on phase cancellation](https://arxiv.org/abs/0708.3115)

## Executable check

Run `python3 checks/refoliation.py` from the repository root. Expected checks:

- maximum one-particle pairing error across modes $1$ through $8$ is $1.72\times 10^{-16}$ ($<10^{-12}$);
- mode $(1,2)$ overlap magnitude with the tilt omitted equals $0.304092$;
- exact vacuum commutators at levels $2$ and $3$ are $0$ (normal–normal) and $1, 4$ (mixed). [Executable check](../checks/refoliation.py)

---

## 3. What the nonlinear null-cone generator must reproduce

Version 1’s own null geometry already exhibits field dependence invisible to the linear checks above. Along a regular null segment in an area-normalized angular frame, choose the smooth one-parameter unimodular conformal metric $\bar q=\operatorname{diag}(e^{2a(v-1)},e^{-2a(v-1)})$, whose radial derivative has squared norm $8a^2$. Substituting into (3.26c) and (3.55) at fixed corner lapse yields

$$
\frac{N(v)}{N(1)}=\exp[-a^2(1-v^2)/2],\qquad
\partial_a\log N(v)=-a(1-v^2).
$$

At $a=v=1/2$, this logarithmic derivative equals $-3/8$. Freezing the inner lapse as shear varies misses this term, and expanding around shear-free data sees it only at quadratic order—beyond the reach of the linear graviton pairing check. (Likewise, moving a corner along the *same* cone simply rescales the area parameter—a Möbius map—whereas changing between cuts or between area gauge and affine parameter on a sheared cone introduces nonlinear, shear-dependent maps.) [Null data and focusing](03-2.md) · [Hamiltonian in §3.4](https://arxiv.org/pdf/2611.34924v1#page=19)

**The concrete nonlinear quantum test.** Pick two small, independent deformations of an internal cap inside a regular sheared solution while holding the rim, outer states, and relational sources fixed. Construct all four short propagators from (3.53b) with their boundary phases in a single regularization, transport around the closed loop, and undo the geometrically induced tangential relabeling. Refoliation invariance requires the resulting operator—including both operator commutators and the embedding/lapse dependence above—to equal the identity to mixed order on a dense domain, with matching matrix elements as the regulator is removed. Any surviving phase after physical boundary terms are included would make amplitudes path-dependent, while the closed-cut sewing of §5.2 additionally requires an independent convergence argument. [Continuum evolution audit](evolution.md) · [Closed-trace audit](compactness-stress.md)

**Bottom line.** Oppenheim’s diffeomorphism objection targets this full quantum change of cut. Version 1 proves classical relational invariance and algebraic sewing for given propagators; the $(t,z)$ free one-particle pairing is conserved as expected, while unitary implementability and nonlinear quantum refoliation remain open.
