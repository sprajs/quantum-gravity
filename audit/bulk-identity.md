# The off-shell bulk density for a shearing null foliation

For every smooth affine metric (B.1) with positive definite cut metric, the sum in (B.10)–(B.11) equals the Einstein–Hilbert density pointwise. Both shear polarizations, the angular shift and its radial derivative, the cut curvature and the angular dependence of $F$ are unrestricted. The result holds on the oriented, nondegenerate gravitational branch after eliminating the torsion-free spin connection. It requires no Einstein equation, null constraint, boundary condition or integration over a cut. This closes the local bulk-identity question left by the round-metric check. Differentiability of the Hamiltonian at a radiating boundary is a separate question. [Chandrasekaran, arXiv:2611.34924v1, Appendix B](https://arxiv.org/html/2611.34924v1#A2.E10) · [Gravitational branch](03-1.md) · [Boundary variation and round-sector checks](03-4.md)

## Curvature in a frame normal to the cuts

Write $A=\sqrt{\det q}$, so $A=\varrho^2$ in the paper's unit reference-area coordinates. Set $e_t=\partial_t-V^A\partial_A$, $e_r=\partial_r$, and $E_A=\partial_A$. The $e_i$ are orthogonal to the cuts, with metric $h_{tt}=-F$, $h_{tr}=-1$, $h_{rr}=0$. Their only independent commutator is $[e_t,e_r]=(\partial_r V^A)E_A$. Define
$$
 k_{i\,AB}=\tfrac12(\mathcal L_{e_i}g)(E_A,E_B),\qquad
 \theta_i=q^{AB}k_{i\,AB},\qquad
 c_{ij}=\tfrac12[e_i,e_j]^{\rm cut}.
$$
A colon contracts two cut-tensor indices with $q^{-1}$. A dot contracts cut vectors with $q$. Then $c_{tr}=-w^\sharp$, where $w_A=-q_{AB}\partial_rV^B/2$. Raising both normal indices gives $c^2=c_{ij}\cdot c^{ij}=-2w_Aw^A$. The Lorentzian sign in this contraction fixes the sign of the shift term.

We use $R(X,Y)Z=\nabla_X\nabla_Y Z-\nabla_Y\nabla_X Z-\nabla_{[X,Y]}Z$. For clarity, the three independent contractions of the Riemann tensor are given below. Let $\Gamma^s{}_{ij}$ be the horizontal part of $\nabla_{e_i}e_j$, and put $Z=h^{ij}(e_i\theta_j-\Gamma^s{}_{ij}\theta_s)$. The horizontal projection of the commutator vanishes, so $\Gamma$ is given by the Christoffel formula for $h$ with derivatives $e_i$. Define $R_H=h^{ik}h^{jl}\langle R(e_i,e_j)e_l,e_k\rangle$, $R_V$ by the corresponding contraction on the cut, and $M=h^{ij}q^{AB}\langle R(e_i,E_A)E_B,e_j\rangle$. Koszul's formula gives
$$
\begin{aligned}
 R_V &= R[q]-h^{ij}(\theta_i\theta_j-k_i:k_j),\\
 R_H &= -F_{rr}-3c^2,\\
 M &= -Z-h^{ij} k_i:k_j+c^2 .
\end{aligned}
$$

The first line is the Gauss equation for a cut. To see how the $F$ gradients enter the other two lines, the cut projection of $\nabla_{e_i}e_j$ is $U_{ij}=-\tfrac12\operatorname{grad}_q h_{ij}+c_{ij}$. Its symmetric part has only a $tt$ component. Both its horizontal trace and its contracted square vanish because $h^{tt}=0$. The formal horizontal connection has $\Gamma^t{}_{tt}=-F_r/2$, $\Gamma^r{}_{tr}=F_r/2$ and $\Gamma^r{}_{tt}=(e_t F+FF_r)/2$. Contracting its curvature gives $-F_{rr}$. The remaining terms in $R_H$ are
$$
 -|\operatorname{tr}_h U|^2+U_{ij}\cdot U^{ji}+2c_{ij}\cdot U^{ji}=-3c^2 .
$$
The last summand comes from the commutator term in $R(e_i,e_j)$. In $M$, differentiating the cut extrinsic curvature and contracting the two shape operators gives $-Z-h^{ij}k_i:k_j$. The remaining terms are $D_A(h^{ij}U_{ij}{}^A)-U_{ij}\cdot U^{ji}=c^2$, where $D$ is the derivative of $q$. This also accounts for angular derivatives of $F$ in a general frame.

Since $\operatorname{div}_g(\theta^i e_i)=Z+h^{ij}\theta_i\theta_j$, summing $R_H+2M+R_V$ gives
$$
 R[g]=R[q]-F_{rr}
       +h^{ij}(\theta_i\theta_j-k_i:k_j)-c^2
       -2\operatorname{div}_g(\theta^i e_i).
$$
Decompose $k_i=\sigma_i+\tfrac12\theta_iq$. Substitution of $h^{tr}=-1$, $h^{rr}=F$ yields
$$
 h^{ij}(\theta_i\theta_j-k_i:k_j)
 =2\sigma_t:\sigma_r-\theta_t\theta_r
     +F\bigl(\tfrac12\theta_r^2-\sigma_r:\sigma_r\bigr).
$$
Finally, $A\theta_r=A_r$ and $A\theta_t=A_t-\partial_A(AV^A)$. Multiplying by $A$ and using $-AF_{rr}=A_r F_r-\partial_r(AF_r)$ produces the current
$$
 L^t=2A_r,\qquad
 L^r=2[A_t-\partial_A(AV^A)]-AF_r-2F A_r,\qquad
 L^A=-2A_rV^A.
$$
The rest of the density is
$$
 A[2\sigma_t:\sigma_r-\theta_t\theta_r+R[q]+2w_Aw^A-2\Lambda]
 +A_r F_r+FA(\tfrac12\theta_r^2-\sigma_r:\sigma_r).
$$
These are the individual terms of (B.11), including the angular divergence before integration. [Expansions and shears, (B.9)](https://arxiv.org/html/2611.34924v1#A2.E9) · [Densities, (B.11)](https://arxiv.org/html/2611.34924v1#A2.E11)

## Returning to the original radial coordinate

For (B.1) in a chart $(t,v,y)$ with $N>0$, choose a local primitive $r=s(t,v,y)$ with $s_v=N$. For example, integrate $N$ from a fixed $v_0$ and choose the origin of $r$ smoothly on that cut. The fields in the affine chart, pulled back to $(t,v,y)$, are
$$
 \widehat q_{AB}=q_{AB},\qquad
 \widehat V^A=V^A+q^{AB}s_B,\qquad
 \widehat F=F-2s_t+2V^A s_A+q^{AB}s_As_B .
$$
These follow by substituting $N\,dv=dr-s_tdt-s_A dy^A$ into the metric. In the affine formulas $\partial_r=N^{-1}\partial_v$, $\partial_t|_r=\partial_t|_v-(s_t/N)\partial_v$ and $\partial_A|_r=\partial_A|_v-(s_A/N)\partial_v$. In particular, the angular curvature in the affine split is evaluated on the constant-$r$ cuts.

Let $\widehat L_0,\widehat{\Delta L_0},\widehat L^i$ denote (B.11) evaluated on these affine fields and pulled back. The Jacobian gives the full identity in the original coordinates,
$$
 NA(R[g]-2\Lambda)=N(\widehat L_0+\widehat{\Delta L_0})+\partial_\mu J^\mu,
 \qquad
 (J^t,J^v,J^A)
 =(N\widehat L^t,\ \widehat L^r-s_t\widehat L^t-s_A\widehat L^A,\ N\widehat L^A).
$$
Here $J^\mu$ represents the pullback of the particular affine divergence three-form of (B.11). The radial primitive selects a family of cuts for this split. The equality of the full four-form is independent of that choice. On a $t$-constant face the pullback gives $J^t=2A_v$. Performing the usual Christoffel integration by parts anew in the $v$ chart gives $2A_v+A\,\partial_v\log N=2A_v-Af_v$ for the time component of the Einstein divergence, the integrand in (B.22). They agree when $f_v=0$. For a general parameter the extra term requires an accounting of the changed bulk and boundary split if (B.22) is to be identified with the inherited affine current. [Original-coordinate interval, (B.22)](https://arxiv.org/html/2611.34924v1#A2.E22)

## Independent coordinate certificate

The executable evaluates $g^{ij}R_{ij}$ from the four-dimensional coordinate Christoffel symbols. A separate expression implements (B.9)–(B.11), including $R[q]$ calculated from the two-dimensional metric and derivatives of the *unrestricted* currents. Every first derivative and symmetric second derivative of each of the six fields $F,V^x,V^y,q_{xx},q_{xy},q_{yy}$ is an independent symbol. The 24 first derivatives and 60 second derivatives are never sampled numerically. [Exact SymPy calculation](../checks/bulk_identity.py)

To justify the pointwise normalization, make the constant change $Y=M y+b t$, leaving $t,r$ fixed. Choose $M$ so that the transformed $q$ is the identity at the selected point and $b=M V$ there. Then $V'=MV-b$ vanishes at that point. The area density and both bulk densities acquire the common factor $1/|\det M|$, and $L'^t,L'^r$ acquire the same factor. The angular components obey $L'^{A}=(M^A{}_B L^B+b^A L^t)/|\det M|$, since $L^A=-V^A L^t$. Thus the divergence also transforms as a density. This proof of normalization uses only the transformation of the printed quantities. Invertibility leaves their derivatives unrestricted at the point. The code replaces derivatives by independent symbols *before* inserting the point values. $F$ itself remains an indeterminate.

As a curved control, take $q=\operatorname{diag}(e^{2(ar+bt)},e^{-2(ar+bt)})$, constant $F=F_0$ and $V=(\omega r,0)$. At $t=r=0$ the direct Ricci scalar is $4ab-2F_0 a^2+\omega^2/2$. Here the cuts have constant area density while their shape changes. For $a\ne0$ the affine null component $R_{rr}=-2a^2$ precludes the vacuum Einstein equation for any $\Lambda$.

Run from the repository root with `uv run --script checks/bulk_identity.py`. The expected output is

```text
B.10–11 general affine two-jet residual: 0
Matched expanded monomials: 39
Shear and twist curvature control: 0
```

The two cosmological contributions are identically $-2\Lambda A$. The machine comparison checks the remaining polynomial identity. The repository-wide command is `make check`.
