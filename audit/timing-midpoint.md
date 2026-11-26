# Equal-time brackets of two spherical clock responses

Two different reference waves prepare different linear readings of the same spherical clock. When both detectors use the same narrowing time window, their equal-time bracket has a definite limit. For the optical slopes $s^4$ and $s^5$ at cap ratio $1/3$, in that order, it is $8126G_N/48715425$. Shared jumps of their Einstein responses account for the full difference between this limit and measurements made with independently chosen time windows. The calculation uses the flat, unit-radius diamond and its common decaying Minkowski radiative continuation. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Flat clock Hessian](joint-flat-hessian.md)

## The two one-sided measurements

Let $D=\bar u_*-(1-a)M$ be the affine clock excess above the matched-radius flat reading. Fix $0<a<1$ and prepare two smooth even-parity quadrupoles $W_i$ with common polarization $S=\operatorname{diag}(-1/2,-1/2,1)$. The observables are the linear covectors $L_i=d^2D_{\rm flat}(W_i,\cdot)$. For a proper-time delay $\tau$, translate the entire second experiment, including its tips, marks and incident wave. Let $f_{X_i}(s)=F_{X_i}(2s)$ be its zero-delay first-slot Hamiltonian master, with the full-line vertex terms and the affine tails fixed by the radiative continuation. Write $z_i=f_{X_i}^{(4)}$ and $A=3/(5120G_N)$. Each $z_i$ is compactly supported and piecewise smooth with finitely many jumps. Denote its distributional derivative (a finite signed measure) by $Dz_i$, and its right-minus-left jump at $x$ by $d_i(x)$. At a point of continuity set $d_i(x)=0$. [Einstein normalization and vertex terms](weak-normalization.md) · [Translation of the marked clock](weak-clock-contact.md)

The Einstein pairing of smooth responses is $\Omega(X_1,X_2)=A\int z_1' z_2\,ds$. With $\Omega=\int\delta\pi\wedge\delta q$, the usual canonical bracket is its negative. A delay translates the second field by $\tau/2$ in $s$. Moving smooth timing windows onto the delay gives the bounded distribution represented almost everywhere by
$$
 B_{12}(\tau)=-A\int z_2(s-\tau/2)\,Dz_1(s).
 \tag{1}
$$
For small nonzero delays the jumps of the two factors are separated. More generally (1) defines a regular distribution for compact functions of bounded variation (BV), since its absolute value is bounded by $A\|z_2\|_\infty |Dz_1|(\mathbb R)$ for almost every delay. A change of representative of $z_2$ on a Lebesgue-null set leaves this distribution invariant, by Fubini's theorem. Its value at a single delay requires a prescription.

Use the midpoint representative $z_i^*(s)=[z_i(s-)+z_i(s+)]/2$. Each one-dimensional BV function has both traces everywhere. With the midpoint representative in (1), dominated convergence against $|Dz_1|$ gives the positive-delay limit using $z_2(s-)$ and the negative-delay limit using $z_2(s+)$. Hence
$$
 \begin{aligned}
 B_{12}(0^\pm)&=M_{12}\ \pm C_{12},\\
 M_{12}&=-A\int z_2^*\,Dz_1,\qquad
 C_{12}=\frac A2\sum_x d_1(x)d_2(x).
 \end{aligned} \tag{2}
$$
The sum is absolutely convergent for compact BV profiles, since the jumps have summable magnitudes. Only shared jumps enter $C_{12}$. The smooth parts, and the continuous values of the second response at jumps of the first, also enter $M_{12}$.

The BV product rule $D(z_1z_2)=z_1^*Dz_2+z_2^*Dz_1$ and compact support give $M_{21}=-M_{12}$. For the physical piecewise smooth profiles this follows by ordinary integration by parts on each interval and the exact jump identity $[uv]=u^*[v]+v^*[u]$. Since $C_{21}=C_{12}$, exchanging the two readings sends $B_{12}(0^+)$ to $-B_{21}(0^-)$. An individual cross-bracket can have both one-sided limits positive. For a single reading $M_{11}=0$ and $C_{11}=A\sum_x d_1(x)^2/2$. [Vol'pert, *The spaces BV and quasilinear equations*, §5, Eq. (5.15)](https://www.mathnet.ru/eng/sm4127)

## What the timing filters select

Average each translated observable against $h^{-1}\rho_i(t/h)$, where $\rho_i$ are smooth compact probability densities. At every positive $h$ both responses are smooth in the master. Bilinearity weights (1) by $\rho_1(t)\rho_2(t')$ at delay $h(t'-t)$. The diagonal has zero measure, so bounded convergence gives
$$
 \lim_{h\downarrow0}\{L_{1,h},L_{2,h}\}
    =M_{12}+C_{12}\big[\Pr(t'>t)-\Pr(t'<t)\big].
 \tag{3}
$$
Here the two times have independent densities $\rho_1,\rho_2$ because the two smearing integrals form a product. **Synchronized filters** use identical profiles, widths and timing origins for the two readings. Exchanging the integration variables then gives each ordering probability $1/2$, even for an asymmetric common profile. Equivalently, the autocorrelation of the common window is even. This selects the midpoint Stieltjes pairing $M_{12}$. Distinct filters with balanced ordering probabilities give the same result. Drawing a single random time and inserting it in both *sharp* observables would instead sample the undetermined diagonal of (1).

The widths may also approach zero at different rates. Let $T_h,T'_h$ be the integration times in the two narrowing atomless windows, and suppose $T'_h-T_h\to0$ in probability. On each side of zero the error in replacing (1) by its one-sided limit tends uniformly to zero as the delay interval shrinks. Boundedness controls the probability outside that interval. Consequently (3) holds with the actual $h$-dependent ordering probabilities and an $o(1)$ remainder. Two even densities centered on the same time give balanced orderings at any widths. For an asymmetric example, center bumps of masses $2/3,1/3$ at $-1,2$. Give both bumps the same even smooth shape supported within $1/10$ of their centers. Use this centered mixture with scale $h$ in the first slot and scale $2h$ in the second. The second time is later only when sampled from its positive bump, with probability $1/3$. Reversing the width ratio reverses the bias. Alternating these two ratios prevents convergence whenever $C_{12}\ne0$.

For a fixed pair of covectors, independence from **all independently chosen** timing profiles holds exactly when $\sum_x d_1(x)d_2(x)=0$. Sufficiency follows from (3). For necessity, smooth profiles with disjoint chronologically ordered supports realize either sign of the bias. Even if their means and variances must match, the two equal-moment profiles have bias $-1/5$, while identical profiles have zero bias. Shared jumps with opposite products at different sites can cancel. A continuous response in either slot suffices, including a finite-energy response in this physical class. [Equal-moment timing profiles](weak-clock-contact.md) · [Explicit cancellation for two discontinuous responses](timing-two-clocks.md)

These statements extend the pairing on linear response covectors with compact BV fourth derivatives. Against a smooth response they reproduce the ordinary Einstein bracket. At a shared jump, (2) specifies a synchronized classical measurement on the stated continuation. Establishing a Poisson bracket for nonlinear regional clocks requires their field-dependent variations and corner pairings. A sharp wave's Hilbert-space domain is a separate question. [Domains for weak probes](weak-domain.md) · [One-particle norm of a sharp rim](weak-fock.md)

## A nonzero midpoint from smooth vacuum preparations

Take $a=1/3$. On a neighborhood of $[a,1]$ set $f_{W_1}=2s^{10}/1575$ and $f_{W_2}=s^{11}/1650$, and cut each master off smoothly away from this interval and the vertex. The regular vacuum quadrupoles they generate have $G'_1=s^4$ and $G'_2=s^5$ on $[a,1]$. To recover their responses directly, put $b_i(r)=r(1-r)G'_i(r)$ and $I_{i,m}(\ell)=\int_\ell^1 b_i(r)r^{-m}dr$. For $0<s<1$, excluding the rim itself,
$$
 z_i(s)=-16G_N\left[I_{i,2}(\ell)-6s^2 I_{i,4}(\ell)
                  +{\bf1}_{s>a}\frac{b_i(s)}{s}\right],
 \qquad \ell=\max(s,a).
 \tag{4}
$$
It vanishes for $s<0$ and $s>1$. To obtain (4), apply the full optical covector to $-(r-s)_+^4/4!$ in its test variable $r$ and divide by $A$. The fifth derivative in $s$ of this kernel is a Dirac measure at $r$. The initial and terminal fundamental solutions differ by a fourth-degree polynomial, whose action under the full optical covector vanishes. For $s>0$, its test jets at the vertex vanish. On $r>s$, the second, third and fourth derivatives of the positive kernel $(r-s)_+^4/4!$ in the optical slope give the combined coefficient $b_i(r)[1/(16r^2)-3s^2/(8r^4)]$. Its fifth derivative supplies the local term $b_i(s)/(16s)$. The overall factor follows from $(3/20)/A=256G_N$. For $s<0$ the test is a polynomial on a neighborhood of the entire source support and the vertex jets cancel its bulk contribution. [Full optical slope and its null polynomial moments](weak-normalization.md)

In units $G_N=1$, the vertex and rim jump pairs $(d_i(0),d_i(a))$ are $(-928/1215,-32/243)$ and $(-5728/10935,-32/729)$, respectively. The waist has zero jump. Substitution of the *whole* profiles (4) into (2) gives
$$
 B_{12}(0^+)=\frac{69593}{243577125}G_N,\qquad
 B_{12}(0^-)=\frac{3889}{81192375}G_N,\qquad
 M_{12}=\frac{8126}{48715425}G_N.
$$
The first two are ordered sharp limits and the third is the common-filter limit for the same pair of preparations.

Run `python3 -B checks/timing_midpoint.py` and `make check` from the repository root. The focused script evaluates (4) and the atom and bulk integrals with exact fractions. As a second calculation it convolves *both* profiles with the same unit-area rectangular window, differentiates the continuous filtered first profile and integrates against the filtered second profile. The rectangular window also obeys the bounded-convergence argument in (3). Its proper-time width is twice the master width below. The check verifies skewness at both finite widths. [Executable calculation](../checks/timing_midpoint.py)

~~~text
Distinct clock limits (G_N=1): later 69593/243577125, earlier 3889/81192375
Synchronized midpoint 8126/48715425, half-jump 2633/22143375
Common box of master width 0.001000: 0.000166802238
Common box of master width 0.000001: 0.000166805481
~~~
