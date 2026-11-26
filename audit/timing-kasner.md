# Two spherical cap clocks with a common proper-time midpoint

Two position-averaged spherical clocks can have a nonzero classical Peierls bracket in four-dimensional vacuum gravity even when both clocks use the **same two-tip diamond at each emitter**. The emitters cover a Kasner torus. A measured length around the torus selects the common midpoint. The two instruments differ only in the cap fraction, $1/3$ or $1/2$. If curvature age or total spatial volume selects the midpoint instead, the bracket vanishes exactly at the same background. These results concern how the clocks are prepared in the surrounding spacetime. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Kasner solution, sky and reduced symplectic form](joint-jacobi.md)

## What fixes the instant?

On the unit-period rectangular torus use proper age $t>0$, $a_i(t)=A_i(t/T)^{p_i}$ and $(p_1,p_2,p_3)=(-b,1+b,b(1+b))/(1+b+b^2)$ near $b=2$. Take $(A_1,A_2,A_3)=(6a/5,11a/10,a)$ at the background. The curvature scalar $\tau=4K/\sqrt{-\nabla K\cdot\nabla K}$, with $K=R_{abcd}R^{abcd}$, gives $\tau=t$ throughout this family. Its levels define the measurement slices also for nearby metrics with timelike $\nabla\tau$.

On each slice let $\ell(s)$ be the reciprocal square root of the smallest slice-averaged squared norm of a harmonic one-form in a primitive integral class. The class is unique up to sign near the chosen torus, by the gap in the norms. Here $\ell(s)=A_1(s/T)^{p_1}$. The fixed reading $\ell_* =6a/5$ selects the slice $\tau=t_*$ with $\ell(t_*)=\ell_*$. The branch through $T$ is unique since $p_1\ne0$. Both instruments use this *one* physical selection, including when the metric varies.

At each point of this slice follow its unit normal geodesic to tips at proper times $-L$ and $+L$ relative to the point. Launch the sky from the past tip in the comoving unit frame and use its uniform solid-angle average $\langle\cdot\rangle$. With $S$ the affine distance to the intersection with the future tip's past cone and $D_S$ the optical radius there, adjust $L$ until $M=\langle D_S^2\rangle/\langle D_S\rangle=R$. The experiment lies in a convex normal neighborhood, before torus images, and the waist matching has a unique small-$R$ root. On each ray set $D(C)=\epsilon D_S$, $U=D'(C)(S-C)$. Read the weighted sky mean $\langle D_S U\rangle/\langle D_S\rangle$ and average it over the midpoint slice with its normalized proper volume. Call the result $\mathcal U_\epsilon$. Changing $\epsilon$ preserves the two tips, the waist and the midpoint. [Differentiating the cap and the moving intersection](joint-jacobi.md)

## Why the ambient bracket reduces to two derivatives

Before a torus image is sampled, each homogeneous reading depends on $b$ and the midpoint age $t_*$ through a smooth function $u_\epsilon(b,t_*;R)$. Rescaling any $A_i$ at fixed $b,t_*$ is a local coordinate change, and all emitters on each homogeneous slice agree. For arbitrary smooth linearized vacuum solutions the differential of the position-averaged experiment is invariant under translations and the independent coordinate reflections. Its value therefore equals its value on the group-averaged solution. The resulting homogeneous diagonal vacuum perturbation is a Kasner tangent up to a time reparametrization. This proves on the full linearized solution space at this background that
$$
 d\mathcal U_\epsilon=u_{\epsilon,b}\,db+u_{\epsilon,t}\,dt_*.
$$

Both covectors on the right have smooth compact spacetime source representatives there. For $db$, time-smear the normalized slice average of $\tau^4 K$ and apply the local inverse of $-16p_1p_2p_3$. Denote this observable by $B$. For $dt_*$ choose a smooth weight in a narrow age band with $\int w(s)ds=1$ and $\int w(s)\log(s/T)ds=0$. Set $X=\int w(s)\log(\ell(s)/\ell_*)ds$. On the Kasner family $X=\log(A_1/\ell_*)$, so $T\exp[-X/p_1(B)]$ equals $t_*$. The symmetries give equality of their differentials on all linearized solutions. Time smearing permits integration by parts on the compact band. In the Hodge norm variation the change of harmonic representative is exact and orthogonal to the background harmonic form. The resulting source at the background is smooth. These representatives allow the Peierls pairing to be computed without multiplying sharp null distributions. [Normalized torus response and smearing proof](joint-jacobi.md) · [Fewster and Hunt on the ambient linearized phase space](https://arxiv.org/abs/1203.0261)

Write $V_T=\prod_i A_i$, $c_G=8\pi G_N T/V_T$, and use the retarded-minus-advanced convention $\{A,B\}=dA[Y_B]$. On the diagonal phase space at $t=T$, $q_{ii}=A_i^2$ and $\pi^{ii}=V_T(p_i-1)/(16\pi G_N T A_i^2)$. Contracting $\sum_i dq_{ii}\wedge d\pi^{ii}$ with the tangent $Y_b$ defined by $Y_b\log A_i=c_G p'_i/\sum_j(p'_j)^2$ and $Y_b b=0$ gives $db$. The contraction against each side-length variation vanishes since $\sum p'_i=\sum p_i p'_i=0$. At $b=2$ the components $p'_i=(3,-8,5)/49$. Differentiating the epoch condition gives
$$
 \{b,t_*\}=-Y_b t_*=c_G t_*\frac{p'_1}{p_1\sum_j(p'_j)^2}
 =-\tfrac{21}{4}c_G T\qquad (t_*=T).
$$
Consequently the exact bracket at this background is $\{b,t_*\}(u_{1,b}u_{2,t}-u_{1,t}u_{2,b})$, where subscripts $1,2$ label the cap settings. Fixing a curvature age $t_*=T$ makes $dt_*=0$. Choosing a total volume $V_*$ instead gives $t_*=TV_*/V_T$ and $Y_bV_T=0$. Both preparations therefore have **zero pair bracket at every admissible radius**, also for different fixed radii. Multiplying by an unnormalized total spatial volume would change the observable.

## The first term that distinguishes the two caps

Let $t_0=t_*-L$ be the age at emission, $f_i=p_i(1-p_i)$, $E_0=\operatorname{diag}(f_i)$, $F=\mathrm{tr}(E_0^2)=-2p_1p_2p_3$. Along a past-tip ray choose unit initial energy and a parallel screen. Denote its trace-free tidal matrix by $Q(s)=Q_0+sQ_1+O(s^2/t_0^4)$. The optical Riccati equation gives shear $sQ_0/3+s^2Q_1/4+O(s^3/t_0^4)$. Vacuum focusing integrates to
$$
 U-(1-\epsilon)D_S=\tfrac12\int_C^S(S-s)D(s)\,\mathrm{tr}(\sigma^2)(s)\,ds.
$$
Here $D(s)=s+O(s^5/t_0^4)$. In local inertial coordinates the tips are on one geodesic and $S=L+O(L^3/t_0^2)$ uniformly in direction. Thus $C=\epsilon L+O(L^3/t_0^2)$, $R=L+O(L^3/t_0^2)$, and the angular weight $D_S/\langle D_S\rangle$ differs from one at order $L^2/t_0^2$. Through sixth order the only radial moments are $B_\epsilon=1-5\epsilon^4+4\epsilon^5$ and $C_\epsilon=1-6\epsilon^5+5\epsilon^6$. Integrating the two shear terms yields respectively $B_\epsilon L^5\mathrm{tr}(Q_0^2)/360$ and $C_\epsilon L^6\mathrm{tr}(Q_0Q_1)/360$.

For the sky calculation write $p=\operatorname{diag}(p_i)$, $n$ for the instantaneous unit spatial ray direction and $e=dt/ds$. The electric Weyl eigenvalues are $f_i/t^2$. The squared screen tidal tensor is $e^4 H(n)/t^4$ with
$$
 H=4F-8n^T E_0^2 n+2(n^T E_0 n)^2,\qquad h=n^T p n.
$$
Conservation of spatial momenta gives $e'=-h/t_0$ and $n'=(hn-pn)/t_0$ at emission. On the unit sphere the divergence of $hn-pn=-\nabla h/2$ is $3h-1$. Differentiating the squared tensor and integrating by parts therefore gives
$$
 t_0^5\langle \mathrm{tr}(Q_0Q_1)\rangle
 =-\tfrac12\langle(3+7h)H\rangle=-\tfrac{16}{3}F.
$$
Indeed the isotropic second, fourth and sixth moments give $\langle H\rangle=8F/5$ and $\langle hH\rangle=(88F-96\,\mathrm{tr}(pE_0^2))/105$. The final trace vanishes by $\sum p_i=\sum p_i^2=1$: each $p_i$ solves $p_i^3-p_i^2=p_1p_2p_3$, so $p_i f_i^2=(p_1p_2p_3)(p_i^2-p_i)$.

Substitute $t_0=t_*-R+O(R^3/t_*^2)$ and apply the fixed-$M$ condition to the entire baseline $(1-\epsilon)M$. With $\alpha_\epsilon=B_\epsilon/225$ and $\beta_\epsilon=4B_\epsilon/225-2C_\epsilon/135$, the reading is
$$
 u_\epsilon=(1-\epsilon)R + F(b)\left(\alpha_\epsilon\frac{R^5}{t_*^4}
                    +\beta_\epsilon\frac{R^6}{t_*^5}\right)
                    +O(R^7/t_*^6).
$$
The scaled null propagation and transverse waist matching are smooth in $(R/t_*,b)$ at zero size. The cap root has positive radial slope. Taylor expansion on a compact parameter branch gives the stated remainder also after a $b$ derivative, and a $t_*$ derivative adds an inverse time. The fifth-order terms have parallel gradients, so their mutual bracket vanishes. With the sixth-order terms included the determinant is $FF'(\beta_1\alpha_2-\alpha_1\beta_2)R^{11}/t_*^{10}+O(R^{12}/t_*^{11})$. At the ordered cap settings $(1/3,1/2)$ the cap factor is $61/17714700$. At $b=2$, $F=72/343$ and $F'=-240/2401$. This yields a positive bracket for all sufficiently small positive $R/T$,
$$
 \boxed{\displaystyle
 \{\mathcal U_{1/3},\mathcal U_{1/2}\}
 = c_G\left[\frac{488}{1286491815}\frac{R^{11}}{T^9}
              +O(R^{12}/T^{10})\right].}
$$

The sign holds for each fixed pair $0<\epsilon_1<\epsilon_2<1$. Indeed $C_\epsilon/B_\epsilon$ is $3/2$ times the mean of $x$ on $[\epsilon,1]$ with weight $x^3(1-x)$. Raising the lower limit strictly raises the mean and thus strictly lowers $\beta_\epsilon/\alpha_\epsilon=4-(10/3)C_\epsilon/B_\epsilon$. Consequently $\beta_1\alpha_2-\alpha_1\beta_2>0$. Reversing the order of the clocks reverses the sign.

The common midpoint is simultaneous in observer proper time. Both readings use extended light paths and a global, metric-dependent method of selecting that midpoint. A single emitter loses the translation projection used in this calculation. On the homogeneous torus curvature scalars alone also cannot select a unique spatial point. A bracket for two individually located observers requires a spatial reference and control of their full clock differentials. The result here supplies neither an inverse for an isolated capped diamond nor a quantum commutator on a physical Hilbert space. [Sharp pair and causal domains](joint-peierls.md)

## Numerical check

Run `python3 -B checks/timing_kasner.py` and `make check` from the repository root. The focused script checks the directional moment against the conserved-momentum null evolution, verifies the exact rational coefficient, and independently finite-differences the two-cone clock integrals while adjusting both tips symmetrically. The printed pair is divided by $c_G R^{11}/T^9$. Its leading prediction is $3.7933\times10^{-7}$. Expected rounded output follows. [Executable check](../checks/timing_kasner.py)

```text
exact normalized pair coefficient  488/1286491815
R/T=0.10 normalized pair          4.582e-07
R/T=0.05 normalized pair          4.144e-07
linear extrapolation               3.707e-07
```
