# A simultaneous Poisson bracket for linear spherical clock readings

Can one assign a bracket to two ideal readings made at the same time? On the linear span of the translated scalar quadrupole clocks in the common Minkowski continuation, bilinearity and antisymmetry determine that value once one retains the established pairings for profiles with no common jump. It is the midpoint of the two time-order limits. A detector that resolves which reading occurs first can retain additional information. Exact sharp Weyl relations for a continuum of translated clocks require a nonseparable representation, and proper-time translations cannot act strongly continuously in any such representation. These conclusions concern the mixed Hessian of the matched-radius clock at flat space. [Translated clock calculation](weak-clock-contact.md) · [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27)

## The midpoint pairing and its uniqueness

Use the dimensionless full-line master and write $z=f_X^{(4)}$ for the Hamiltonian response of a linear reading $L_z$. Each clock profile used here is compactly supported and piecewise smooth with finitely many jumps. Write $Dz$ for its distributional derivative, $d_z(x)=z(x+)-z(x-)$ for its jump, and $z^*(x)=[z(x+)+z(x-)]/2$. With $A=3/(5120G_N)$ and the canonical bracket convention of the translated experiment, set

$$
 K(z,w)=-A\int w^*(x)\,Dz(dx)
 =-\frac A2\iint\operatorname{sgn}(x-y)\,Dz(dx)\,Dw(dy),\qquad \operatorname{sgn}(0)=0. \tag{1}
$$

Indeed $Dw$ has total mass zero, and its mass strictly below $x$ plus half its atom at $x$ equals $w^*(x)$. Formula (1) gives an alternating bilinear pairing bounded by $A\,|Dz|(\mathbb R)|Dw|(\mathbb R)/2$. It also defines the midpoint pairing on all compactly supported functions of bounded variation. For smooth profiles four integrations by parts recover the Einstein bracket. The ordered integral depends only on the order of the master points under a common increasing reparametrization with scalar profiles pulled back. The physical translations below move the whole marked Minkowski experiment. A window specified in the marked emitter’s proper time is invariant under a simultaneous change of coordinates of the metric and apparatus. The same is true for two different proper-time response functions, so coordinate covariance alone leaves their relative ordering bias free. [Einstein normalization](weak-normalization.md) · [Vol'pert's calculus for functions of bounded variation](https://doi.org/10.1070/SM1967v002n02ABEH002340)

Smooth both readings using the same normalized, compact proper-time window, shrinking to zero width. In (1) the signed difference of two independent draws from the same window is symmetric. The averaged sign tends to the usual sign off $x=y$ and vanishes on $x=y$ at every width. Bounded convergence against $|Dz|\otimes |Dw|$ gives (1), even for an asymmetric common window. If $z,w$ have no common jump, the diagonal has zero product variation measure, and independent normalized positive windows with supports shrinking to zero give the same limit. At a shared jump, a small positive delay of the second experiment samples $w(x-)$, and a negative delay samples $w(x+)$. The respective limits are $K(z,w)\pm (A/2)\sum_x d_z(x)d_w(x)$. [Two different clock preparations and the synchronized measurement](timing-midpoint.md)

**Uniqueness on the scalar clock span.** Suppose an alternating bilinear bracket $B$ agrees with (1) on every pair with disjoint jump sets. Suppose the span contains, for each allowed jump position $x$, a carrier $e_x$ with just one value jump there, of size one. The calibrated clock has a nonzero rim jump and zero vertex jump. Translating the whole experiment and rescaling its reading supplies these carriers. Given a profile $z$ in the span, subtract $\sum_x d_z(x)e_x$. The remainder is continuous and pairs unambiguously with every profile. Likewise decompose $w$. The difference $B-K$ vanishes between carriers at different points, and alternation makes it vanish on $(e_x,e_x)$. Bilinearity now gives $B=K$. This argument uses finitely many jumps per reading. The scalar profiles give faithful labels on the full smooth master test space. If $L_z(g)=A\int g^{(4)}(x)\,Dz(dx)$ vanishes for every compact smooth $g$, then $D^5z=0$ and compact support gives $z=0$. [Single-jump preparation](weak-clock-contact.md) · [Full-line master tests](weak-normalization.md)

## What a detector label can add

For a space $E$ of jump amplitudes, suppose the span analogously contains single-jump carriers for a basis of $E$ at each point. The same decomposition classifies every ambiguity compatible with the disjoint-jump test. Its general form is

$$
 B(z,w)-K(z,w)=\sum_x C_x(d_z(x),d_w(x)),\qquad C_x\in\bigwedge^2 E^*. \tag{2}
$$

Here the midpoint uses the measured symmetric inner product on the channels. Translation covariance makes $C_x$ independent of $x$ for an experiment with no preferred origin. For one real polar quadrupole multiplet, $E$ is the five-dimensional space of trace-free symmetric spatial tensors. A rotation-invariant alternating form on this irreducible real representation vanishes. Every alternating form in odd dimension has a kernel, and rotational invariance makes the kernel an invariant subspace. Rotations of the calibrated tensor span this multiplet. With two distinct copies, $C((p,q),(p',q'))=c\,[\operatorname{tr}(pq')-\operatorname{tr}(p'q)]$ is rotation invariant for every real $c$. A symmetry interchanging the copies while preserving the bracket forces this coefficient to vanish. Rotations of the spatial frame alone allow it.

There is an operational realization for scalar probes carrying two timing-window labels. Let $d_1(x),d_2(x)$ be the jumps for the two components of a linear combination. Its reading on smooth fields depends only on the sum of the two profiles. With windows $a,b$ of common shrinking scale, the underlying midpoint bracket acts on these sums. The cross correction in (2) acts on the labelled jumps with coefficient $c=(A/2)\mathbb E[\operatorname{sgn}(T_b-T_a)]$, where $T_a,T_b$ are independent draws from the unscaled timing windows. This follows by the diagonal calculation in (1), using the positive-delay sign above. The two coincident-mean, coincident-variance windows in the translated experiment give $c=-A/10$. Applied to two copies of the same calibrated clock they give $-G_N/150$. A bracket with this term cannot descend through the identification of those two copies, since their difference has nonzero bracket with one copy. Thus keeping apparatus labels explains exactly which linear relation the observed bias would violate in an algebra of ideal readings. [Detector preparations and coefficients](weak-clock-contact.md)

## Functions of readings and time translations

For any finite list of independent linear readings, set $K_{ij}=K(z_i,z_j)$. For smooth functions $F,G$ of their values $\ell_i$, the bracket is

$$
 \{F,G\}=\sum_{ij} (\partial_i F)K_{ij}(\partial_j G). \tag{3}
$$

Adding readings or taking linear combinations preserves (3) by the chain rule. Constants commute, and the product rule gives the Leibniz identity. In the cyclic Jacobi sum the first derivatives of $K_{ij}$ vanish, and terms containing a Hessian cancel in pairs by symmetry of second derivatives and skewness of $K$. Smooth functions with bounded derivatives of every order, including order zero, give a bounded Poisson algebra of functions of finitely many readings. One may also use polynomials. Bounded first derivatives alone supply insufficient regularity for iterated brackets. The same calculation works with any fixed alternating form (2) on genuinely labelled data. None of these Jacobi tests chooses the coefficient $c$.

The finite linear combinations of Weyl symbols have the associative multiplication

$$
 W(z)W(w)=e^{-i\hbar K(z,w)/2}W(z+w),\qquad W(z)^*=W(-z),\quad W(0)=1.
$$

Bilinearity gives $K(z,w)+K(z+w,v)=K(w,v)+K(z,w+v)$ for every three symbols, which proves associativity. The symbols can be considered for the full real linear span, including all proper-time translates. [Fewster and Verch, Weyl quantization, §6](https://arxiv.org/pdf/1109.6732#page=25)

**Obstruction to continuous time evolution.** Suppose a nonzero unital Hilbert-space representation has unitaries $U(t)$ implementing translations of *all* the sharp Weyl clocks, with $U(t)$ strongly continuous at zero. Then $W(\mu z_t)=U(t)W(\mu z)U(t)^*$ and its adjoint converge strongly to their zero-delay values. The group commutator with $W(\lambda z)$ must converge strongly to the identity, since the two zero-delay symbols commute. The exact separated Weyl relation instead gives the scalar commutator $e^{-i\hbar\lambda\mu K(z,z_t)}1$. For the calibrated clock its positive-delay limit is $e^{-i\hbar\lambda\mu G_N/30}1$. The amplitudes can be chosen so this differs from $1$. The contradiction holds for any nonzero $\hbar$ and needs neither a vacuum nor continuity in the Weyl amplitudes. Even a time-dependent scalar phase in the covariance law cancels in this commutator. The input is the separated bracket, so a change of simultaneous prescription cannot restore strong continuity.

**A continuum of sharp clocks requires a nonseparable representation.** Even if time translations need no implementer, suppose $V_t=W(\lambda z_t)$ exists for each $t$ in a real interval, in a common nonzero unital representation. Fix $\lambda$ with $\hbar\lambda^2 G_N/30=\pi$ for $\hbar>0$. The limiting commutator phase is $-1$ in both time orders. By taking the interval sufficiently short, for all distinct $t,s$ in it the scalar group commutator of $V_t,V_s$ stays at least distance one from the identity. For each $t$ and a fixed unit vector $\xi$, the set of unitaries $V$ satisfying $\|(V_t V V_t^* V^*-1)\xi\|<1/2$ is a strong-operator neighborhood of $V_t$. Multiplication and adjoints are strongly continuous on the unitary group. This neighborhood excludes every other $V_s$ in the interval. Thus $\{V_t\}$ is an uncountable discrete subspace. On a separable Hilbert space the strong unitary group has a countable base, as seen by evaluating unitaries on a countable dense sequence. Every discrete subspace of a second-countable space is countable, giving the contradiction. Only the separated commutation phases and one coupling entered this argument. [Espinoza and Uribe, strong topology of the unitary group, Theorem 1.2](https://arxiv.org/abs/1407.1869)

The abstract algebra does have a representation. On $\ell^2(\mathcal V)$, where $\mathcal V$ is the linear label space equipped with counting measure, set $W(z)e_v=e^{-i\hbar K(z,v)/2}e_{z+v}$ on its orthonormal basis. This realizes the product and adjoint above. Time translation permutes the basis by $e_v\mapsto e_{v_t}$, and a translated calibrated clock label gives mutually orthogonal basis vectors at distinct times.

Both obstructions concern sharp unitaries in the linearized model. At finite resolution the translated bracket is continuous. The earlier logarithmic one-particle calculation concerns a particular Fock representation and a different criterion. The existence and dynamics of the nonlinear clock in full gravity remain open. [Minkowski vacuum norm](weak-fock.md) · [Finite-duration quantum measurements](timing-quantum.md)

## Reproduce the checks

Run `python3 -B checks/timing_algebra.py` and `make check` from the repository root. The focused check solves the rotation-invariance equations on alternating forms by rational elimination. In units $G_N=\hbar=1$, it then evaluates the exact optical bracket at positive delay with $\lambda\mu=30\pi$. Expected output follows. [Executable check](../checks/timing_algebra.py)

```text
Rotation-invariant alternating contacts, one and two quadrupole copies: [0, 1]
Weyl commutator distance from identity at delay 1e-7: 1.99999999 (limit 2)
```
