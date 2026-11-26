# Angular momentum and normal boosts at the cap rim

On an internal cap rim a common angular displacement has zero charge, even if the null generator has angle-dependent normalization. In signs for which the incoming null segment has positive endpoint charge at the rim, the null normal connection contributes $+\varpi_A$, the spacelike momentum contributes $-K_{As}$, and the change between the two normal frames contributes $-D_A\log(-T\cdot\ell)$. The three add to zero at each point. The Einstein charge also determines which combination a pair of independently marked boundaries can measure. The calculation uses the torsion-free sector of Venkatesa Chandrasekaran's [arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924v1). [Metric potential (A.6)](https://arxiv.org/html/2611.34924v1#A1.E6) · [Noether charge (3.50)](https://arxiv.org/html/2611.34924v1#S3.E50.3) · [Extended potential (B.21)](https://arxiv.org/html/2611.34924v1#A2.E21)

## Computing the same charge in two frames

Let $C$ be a smooth, closed spacelike cut in a smooth vacuum solution. At the initial cap let $T$ be its future unit normal and $s$ the outward unit normal to $C$ within the cap. Write $\mu$ for the positive area form. Choose the four-volume orientation $\epsilon(T,s,e_1,e_2)>0$ for a positively oriented cut basis. Take the outgoing affine null generator $\ell$ and the complementary null normal $n$ with
$$
 \ell=e^b(T+s),\qquad n=\tfrac12 e^{-b}(T-s),\qquad b=\log(-T\cdot\ell).
$$
The projected derivatives are $K_{As}=s\cdot\nabla_A T$ and $\varpi_A=-n\cdot\nabla_A\ell=K_{As}+D_A b$. The cap can have any extrinsic curvature and $b$ can vary over the cut. [Cap normal (3.12)](https://arxiv.org/html/2611.34924v1#S3.E12) · [Cap and sheet geometry](joint-edges.md)

Let $\chi$ have value $V\in TC$ on $C$. Keep its first derivatives in the normal plane. For smooth extensions of the frames off the cut define
$$
 \lambda_\Sigma(\chi)=\tfrac12\big(s\cdot[T,\chi]-T\cdot[s,\chi]\big),
 \qquad
 \lambda_N(\chi)=\tfrac12\big(\ell\cdot[n,\chi]-n\cdot[\ell,\chi]\big).
 \tag{1}
$$
Only the tangential derivative of each frame enters its bracket with $\chi$ in addition to the derivative of $\chi$ itself along the normal. Thus its values on $C$ suffice to define the frame in (1). On substituting into the Komar two-form (3.50c), its pullback to the positively oriented cut is
$$
 \begin{split}
 Q_C[\chi]
 &=\frac{\mu}{16\pi G_N}
    (s\cdot\nabla_T\chi-T\cdot\nabla_s\chi)\\
 &=\frac{\mu}{8\pi G_N}\big(K_{As}V^A+\lambda_\Sigma(\chi)\big)
  =\frac{\mu}{8\pi G_N}\big(\varpi_A V^A+\lambda_N(\chi)\big).
 \end{split}
 \tag{2}
$$
Indeed torsion freedom gives $\nabla_T\chi=\nabla_\chi T+[T,\chi]$. Also $s\cdot\nabla_T\chi-T\cdot\nabla_s\chi=\ell\cdot\nabla_n\chi-n\cdot\nabla_\ell\chi$. The change of frame in the bracket is consequently
$$
    \lambda_\Sigma(\chi)=\lambda_N(\chi)+V^A D_A b.
    \tag{3}
$$
A unit boost with $\chi|_C=0$, $\nabla_T\chi=s$ and $\nabla_s\chi=T$ has positive charge $\mu/(8\pi G_N)$ in this orientation. An angular vector specified only by its value on $C$ leaves this boost derivative undetermined. [Unit boost (3.51)](https://arxiv.org/html/2611.34924v1#S3.E51)

Assign $+Q_C$ to the null endpoint and $-Q_C$ to the cap. Reversing the joined slice reverses both signs. For tangential motions the pullback of $i_\chi\theta$ to $C$ vanishes by antisymmetry. For motions depending on the gravitational fields the charge variation still contains $-Q_{\delta\chi}$. Identical smooth metric, field variation and displacement on both faces give cancellation of the entire covariant charge variation at $C$, including this term. Equality of the tangential boundary values and the scalar normal derivatives in a common frame suffices for cancellation of (2) itself. [Charge variation (3.50b)](https://arxiv.org/html/2611.34924v1#S3.E50.2)

## Recovering the three terms from the face momenta

For the lift in which the null normal frame is carried with the angular marks, $\lambda_N=0$. The sheet endpoint in (2) is then $+\mu\varpi_A V^A/(8\pi G_N)$. This coefficient also follows by integrating the angular null momentum constraint on a finite sheet. On the cap, take its canonical potential with $\pi^{ij}=\sqrt{h}(K^{ij}-Kh^{ij})/(16\pi G_N)$. For a shift tangent to the cap and its rim, integration of $\pi^{ij}(\mathcal L_V h)_{ij}$ by parts leaves the boundary density $2\mu s_i\pi^{ij}V_j/\sqrt{h}$ when the momentum constraint holds. The trace of $K$ drops out since $s\cdot V=0$. With the opposite cap orientation this gives $-\mu K_{As}V^A/(8\pi G_N)$. This is the cap-adapted lift $\lambda_\Sigma=0$. [Null endpoint potential, Eq. (5)](rim-potential.md) · [Boundary action (3.15)](https://arxiv.org/html/2611.34924v1#S3.E15.1)

The two adapted lifts have different first derivatives if $V(b)\ne0$. Converting them to the same lift supplies $-\mu V(b)/(8\pi G_N)$ in their signed sum by (3). In the canonical decomposition this is exactly the angular part of (A.18). With the negative oriented cap sign the latter is $+(8\pi G_N)^{-1}\int_C b\,\delta\mu$. Under common active angular transport $\delta\mu=\mathcal L_V\mu$, so on the closed rim $\int_C b\,\mathcal L_V\mu=-\int_C\mu V(b)$. The oriented angular momentum density is therefore
$$
  \frac{\mu}{8\pi G_N}(\varpi_A-K_{As}-D_A b)V^A=0.
  \tag{4}
$$
Using the same lifted vector in both copies of (2) already implements (4). Adding the joint correction again in that calculation would count the boost twice. Equation (4) evaluates the common-angular direction of the potential. General variations of the joint area and boost also have the two-form $+(8\pi G_N)^{-1}\int_C\delta b\wedge\delta\mu$ in this convention. In particular $D_A\delta b$ can enter a linearized comparison even where the background $b$ is constant. [Joint potential (A.18)](https://arxiv.org/html/2611.34924v1#A1.E18)

## Which motion a comparison map measures

Suppose the angular charts on the two faces are related by $Y:C_N\to C_\Sigma$. The matching equations on this cut include $q_N=Y^*q_\Sigma$ and $\varpi_N=Y^*K_s+db$, where $K_s=K_{As}dy^A$ and $b$ is evaluated on $C_N$. The second equation follows from the normal decomposition above after angular pullback. If $w=\delta Y\circ Y^{-1}$, variation of $Y^*q_\Sigma$ gives $Y^*(\delta q_\Sigma+\mathcal L_w q_\Sigma)$, and the same rule applies to $K_s$. Changes of the two normal curvatures also have to match. The analogous connection equation and map composition appear at the two-null waist $S$ in v1. [Embeddings (3.40)](https://arxiv.org/html/2611.34924v1#S3.E40) · [Matching (3.62)](https://arxiv.org/html/2611.34924v1#S3.E62.4) · [Composition (3.65)–(3.66)](https://arxiv.org/html/2611.34924v1#S3.E65)

For one physical internal embedding written $X_N=X_\Sigma\circ Y$ on the cut, the comparison must use the velocity of the composite. At matched points it is $\chi_\Sigma|_C+(X_\Sigma)_*w$. If the normal-frame identification extends this equality to a common first derivative in the normal boost direction, the two Komar contributions cancel. A coordinate transition can vary while this geometric displacement difference is identically zero.

Alternatively let downstream measurements refer to two independently marked faces. Evaluate their physical velocities $\chi_H,\chi_P$ at the same cut point, express their first derivatives in the same cap frame, and set $\Delta V=\chi_H|_C-\chi_P|_C$. For tangent boundary values the embedding charge remaining from (B.21) is
$$
 \int_C(Q_C[\chi_H]-Q_C[\chi_P])
 =\frac{1}{8\pi G_N}\int_C\mu
 \left(K_{As}\Delta V^A+\lambda_\Sigma(\chi_H)-\lambda_\Sigma(\chi_P)\right).
 \tag{5}
$$
Both marks can be evaluated in the null frame instead, replacing $K_s,\lambda_\Sigma$ by $\varpi,\lambda_N$. For example, the one-sided null angular term used in the spherical quadrupole test follows on fixing the cap mark and taking $\lambda_N(\chi_H)=0$. To infer a physical canonical pair from (5) requires boundary conditions that retain these marks, variations obeying the regulator and the metric and normal matching, and a nonzero two-form on the quotient by the gauge transformations. The difference of one-forms in (5) alone does not establish that quotient. At the waist v1 explicitly discusses charges for a relative frame in spatial sewing. For an isolated cap, (A.18) fixes its area–boost potential, while (3.18)–(3.19) specify the cut and compatibility of the gravitational data. A reduced angular degree of freedom at this cap would require an additional derivation. The clock response on this single test does not establish a smooth Hamiltonian vector. A separate test excludes a differentiable family of smooth generators when the added rim two-form has only finitely many independent responses in the chosen angular harmonic. [Capped-clock range test](match-packets.md) [Boundary data (3.18)–(3.19)](https://arxiv.org/html/2611.34924v1#S3.E19) · [Spherical quadrupole test](joint-angular.md)

## A local sign check in flat spacetime

In Cartesian normal coordinates $(t,z)$ take a planar cut $t=z=0$ with tangential coordinate $y$. Boost $(\partial_t,\partial_z)$ by the rapidity $2y$ to obtain $(T,s)$, and set $b=3y$. The local cap $t=z\tanh(2y)$ realizes these normal vectors at the cut. The common displacement $\chi=\partial_y+7(z\partial_t+t\partial_z)$ has $V=\partial_y$. Its Komar coefficient $8\pi G_N Q_C/\mu$ is $7$ directly from the normal derivative. At $y=0$ one obtains $K_{ys}=2$, $\varpi_y=5$, $\lambda_\Sigma=5$ and $\lambda_N=2$. Thus both frame calculations give $7$, and the adapted angular face coefficients in (4) sum to $5-2-3=0$. This example checks the signs even when all three terms are nonzero. It tests a local identity and needs no periodic extension of the rapidity.

The existing finite-sheet test independently integrates the null face term. Run `python3 -B checks/rim_potential.py` from the repository root. It reports the angular flux and endpoint charge as `0.00460096` in cut-average units. Run `make check` for the complete suite. [Finite-sheet test](../checks/rim_potential.py)
