# Two quadrupole clock readings at the same proper time

On a flat diamond of waist radius one and cap fraction $a=1/3$, use two reference waves with optical strain slopes $s^4$ and $s^5$. Measure the linear change in the matched-radius clock response along each reference. Give the two readings the same proper-time window, centered on the same instant, and shrink its width. Their classical bracket in the order $s^4,s^5$ tends to
$$
                  \frac{8126}{48715425}\,G_N.
$$
Changing which reading comes first gives two different sharp limits, both positive in this ordering of the observables. A second pair of reference waves below has the same nonzero limit for every relative ordering of the two time windows. These experiments use the radiative Minkowski continuation and the mixed Hessian at flat space. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27) · [Matched-radius Hessian and vacuum preparations](joint-flat-hessian.md)

## Preparing the two readings

Use the same freely falling observer, tetrad, tips at times 0 and 2, marked cap and waist, and quadrupole $S=\operatorname{diag}(-1/2,-1/2,1)$. Let $D=\bar u_*-(1-a)M$ be the excess above the flat reading, with weighted radius $M=1$. For a reference wave $W_n$ write $L_n[h]=d^2D_{\rm flat}(W_n,h)$. This is the coefficient linear in both the reference amplitude and the test amplitude. To realize the two slopes, use the regular transverse-traceless waves built from $[F(t+r)-F(t-r)]/r$. Take their masters $f(s)=F(2s)$ equal to $2s^{10}/1575$ and $s^{11}/1650$, respectively, on a neighborhood of $[a,1]$. Extend both smoothly to zero near $s=0$ and outside a compact interval. Substitution in the screen strain gives $G'_{W_n}(s)=s^n$ there for $n=4,5$. Arbitrary smooth test masters can reach the vertex and continue beyond the waist. [Actual clock and optical slope](joint-flat-hessian.md) · [Full-line vertex and Einstein normalization](weak-normalization.md)

For a smooth test master $g$, the optical reading is
$$
 L_n[g]=\frac3{20}\int_a^1 w_n(s) G'_g(s)\,ds,\qquad
 w_n(s)=s^{n+1}(1-s).
$$
Write $A=3/(5120G_N)$. The fourth derivative $z_n=f_{X_n}^{(4)}$ of the response master solves $A z_n^{(5)}=L_n$ in distributions. To compute it, integrate from $s=-\infty$ and use the full vertex-normalized slope
$$
 G'_g(s)=-\frac{3g''(s)}{4s^4}+\frac{3g'''(s)}{4s^3}
         -\frac{5g^{(4)}(s)}{16s^2}+\frac{g^{(5)}(s)}{16s}
         +\frac{3g''(0)}{4s^4}-\frac{g^{(4)}(0)}{16s^2}.
$$
The last two terms generate a quadratic and a constant on $0<s<a$. For the bulk terms, if $b_j(s)$ denotes the coefficient of $g^{(j)}(s)$, their contribution is
$$
 \frac{3}{20A}\sum_{j=2}^5(-1)^j
  \partial_s^j \int_a^1
   \frac{(s-y)_+^4}{4!}\,w_n(y)b_j(y)\,dy .
$$
Integration over the full interval retains the waist contribution. The vertex-normalized slope annihilates all polynomials through degree six, which makes the fourth derivative of the response vanish for $s>1$. The resulting profiles in units of $G_N$ are

| Slope | $z_n/G_N$ on $0<s<a$ | $z_n/G_N$ on $a<s<1$ |
|---|---|---|
| $s^4$ | $-928/1215+320s^2/27$ | $-4/5+16s^2-60s^4+224s^5/5$ |
| $s^5$ | $-5728/10935+64s^2/9$ | $-8/15+8s^2-224s^5/5+112s^6/3$ |

Both profiles vanish outside $[0,1]$. At the waist the two outer polynomials reach zero continuously. At the vertex and cap their jumps $d_n(x)=z_n(x+)-z_n(x-)$ are
$$
  \frac{(d_4(0),d_4(a))}{G_N}
     =\left(-\frac{928}{1215},-\frac{32}{243}\right),\qquad
  \frac{(d_5(0),d_5(a))}{G_N}
     =\left(-\frac{5728}{10935},-\frac{32}{729}\right).
$$
These vertex jumps persist even though the reference masters vanish near the vertex. They come from testing against arbitrary incident waves there.

## Ordering the measurements

Translate the complete second preparation by observer proper time $\tau$, including its reference wave. The profile $z_5$ translates by $\tau/2$. With the canonical bracket convention of the time-translation calculation,
$$
 B_{45}(\tau)=-A\int z_5(s-\tau/2)\,dz_4(s).
$$
For sufficiently small nonzero $\tau$, this pairs the ordinary derivative on each open interval and the two jumps at $0,a$. In either limit the ordinary term contributes $64588G_N/243577125$. At each jump the later experiment samples $z_5(x-)$ and the earlier experiment samples $z_5(x+)$. The table gives the totals. Swapping the two observables reverses the sign and the delay, $B_{54}(-\tau)=-B_{45}(\tau)$. [Translated conserved sources and sign convention](weak-clock-contact.md)

| Timing of $L_5$ relative to $L_4$ | Limiting bracket divided by $G_N$ |
|---|---:|
| Later | $69593/243577125$ |
| Earlier | $3889/81192375$ |
| Same timing window | $8126/48715425$ |

These values can all be measured with smooth time windows. For the earlier and later experiments use two nonoverlapping, time-ordered smooth probability profiles and shrink both offsets and widths to zero. For the common-window experiment the two integration times have the same continuous distribution, so each delay sign has probability $1/2$, even for an asymmetric profile. The function $B_{45}$ is bounded by $A\|z_5\|_\infty\|dz_4\|_{\rm TV}$. Dominated convergence gives the midpoint in the table. This is a prescription for coincident linear clock readings on the specified continuation. [Independent terminal primitive and timing-window calculation](timing-midpoint.md)

The difference of the two ordered limits is $A\sum_{x=0,a} d_4(x)d_5(x)$. To make it zero while preserving the midpoint, use $W_5-cW_4$ as the second reference, where
$$
 c=\frac{\sum_x d_4(x)d_5(x)}{\sum_x d_4(x)^2}
   =\frac{2633}{3897}.
$$
Using $W_4$ for both readings with a common window gives zero by antisymmetry. Thus the new pair has **both** ordered limits $8126G_N/48715425$. Each of its profiles still jumps at the vertex and cap. The two jump products cancel in the sum. Because the delay function has a continuous extension at zero, every pair of normalized nonnegative time windows concentrating there gives this value, provided each window translates its entire marked experiment. This cancellation need not survive independent changes to the timing of the cap and vertex.

## Reproduce the pairing

Run `python3 -B checks/timing_two_clocks.py` from the repository root and `make check` for the suite. The check tests the reconstructed profiles against the optical Hessian on monomials through degree 16. It integrates the two shifted profiles exactly at positive and negative rational delays and verifies both traces and their exchange signs. The time-delay evaluations below are rounded. [Executable calculation](../checks/timing_two_clocks.py)

~~~text
At delays +/-0.0010000, B/G_N = 0.0002911184, 0.0000424829
At delays +/-0.0000100, B/G_N = 0.0002857666, 0.0000478444
At delays +/-0.0000001, B/G_N = 0.0002857129, 0.0000478980
Later 69593/243577125, earlier 3889/81192375, common-window midpoint 8126/48715425 (G_N=1)
For reference slope s^5 - (2633/3897)s^4, both limits = 8126/48715425
~~~
