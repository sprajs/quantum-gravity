# Which clock timing protocols select the equal-time bracket?

Put two marked spherical experiments on the same inertial worldline. At each trigger time translate the whole preparation, including the reference wave and the tips. In the calibrated vacuum quadrupole experiment the bracket tends to $+G_N/30$ when the second trigger is later and $-G_N/30$ when it is earlier. A timing calibration that gives the two orders equal weight therefore selects zero for two copies of that reading. For two distinct readings it selects the mean of their separated-time limits, which can be nonzero. What must be calibrated is the **relative trigger delay**. Even complete knowledge of the individual timing distributions can leave that delay undetermined. [Spherical delay kernel and normalization](weak-clock-contact.md) · [Original affine clock, Chandrasekaran, arXiv:2611.34924v1, (3.26)–(3.28)](https://arxiv.org/html/2611.34924v1#S3.E27)

## What the separated readings determine

Work on the ordinary radiative Minkowski continuation of the round unit diamond, with its common metric and frame. Take two mixed clock readings $L_i=d^2D_{\rm flat}(W_i,\cdot)$ in the same real polar quadrupole sector. Write $B_{12}(u)=\{L_{1,0},L_{2,u}\}$ for their translated bracket. In the profile coordinate $s$, the fourth derivatives $z_i$ of their response masters have compact support and are piecewise smooth. Write $dz_i=v_i\,ds+\sum_x d_{i,x}\delta_x$, with ordinary bounded density $v_i$ and jump $d_{i,x}$ at $x$, set to zero at regular points. The time-delay formula is
$$
 B_{12}(u)=-A\int z_2(s-u/2)\,dz_1(s),\qquad A=\frac{3}{5120G_N}.
$$
For sufficiently small nonzero delay this expression is unambiguous. Each atom at $x$ samples the left limit of $z_2$ at positive delay and its right limit at negative delay. The integral against $v_1$ has a common limit by bounded convergence. Thus
$$
 B_{12}(0^\pm)=M_{12}\pm C_{12},\qquad C_{12}=\frac A2\sum_x d_{1,x}d_{2,x},
 \qquad
 M_{12}=-A\left[\int v_1z_2\,ds+
 \sum_x d_{1,x}\frac{z_2(x^-)+z_2(x^+)}2\right].                 \tag{1}
$$
At a jump, the symmetric values $m_i=(z_i(x^-)+z_i(x^+))/2$ satisfy $[z_1z_2]=d_{1,x} m_2+m_1d_{2,x}$. Integration over the full line gives $M_{12}=-M_{21}$, and $C_{12}=C_{21}$ by (1). A self-pair has $M_{11}=0$. For the unit-rim-slope preparation at $a=1/3$ with vanishing vertex jump, $C_{11}=G_N/30$. These formulas concern linear observables obtained from a Hessian on a fixed background. The isolated regional inverse and the nonlinear and quantum brackets require separate constructions. [Full-line response including the vertex](weak-normalization.md) · [Domain of the continued bracket](weak-domain.md)

For two same-time reference preparations with optical slopes $s^4$ and $s^5$, the midpoint is $8126G_N/48715425$. A second simple check compares $L_t$ with $(L_t+L_{t+d})/2$ in the calibrated translation family. This readout intentionally samples two times. At $d=10^{-3}$ waist-radius units, the bracket has midpoint $B_{11}(d)/2\simeq0.0257783\,G_N$ and one-sided values differing from it by $\pm G_N/60$. The first component supplies the jump and the second contributes its continuous value at $d$. [Distinct reference waves](timing-two-clocks.md) · [Finite-delay evaluation](weak-clock-contact.md)

## Bracket of two time-averaged readings

Suppose the reported readings are $\int a_h(t)L_{1,t}\,dt$ and $\int b_h(t)L_{2,t}\,dt$, with smooth compact nonnegative unit-mass responses. Bilinearity fixes the averaging measure to be $a_h(t)b_h(t')\,dt\,dt'$. The timing density seen by the bracket is the cross-correlation $q_h(u)=\int a_h(t)b_h(t+u)\,dt$. This product follows even when one device produces both averages from a single time series. [Smoothed gravitational sources](weak-domain.md)

More generally, consider a positive paired timing protocol with delay $D_h=T_2-T_1$, zero probability of a tie at every width, and $D_h\to0$ in probability. It reports the expected separated bracket. Assume its delay law avoids the other jump coincidences, as holds for smooth densities or supports shrinking uniformly to zero. With $p_h=\Pr(D_h>0)$, boundedness of the delay kernel and (1) give
$$
 \mathbb E B_{12}(D_h)=M_{12}+C_{12}(2p_h-1)+o(1).                \tag{2}
$$
Indeed the error is uniformly small for sufficiently small $|D_h|>0$, while the probability of the remaining delays tends to zero. The kernel is bounded by $A\|z_2\|_\infty |dz_1|(\mathbb R)$. With a nonzero shared jump coefficient, convergence to the midpoint is equivalent to $p_h\to1/2$. The unique normalized order weights invariant under reversing the delay are $(1/2,1/2)$. Many different timing densities realize those weights. Reversing the relative delay describes a calibration of the apparatus. Translating the entire experiment leaves any relative timing bias intact. Among fixed mixtures of the two limits that use the same weights for every pair, the midpoint is also the unique skew rule, since the self-pair with $C_{11}>0$ already fixes the mixture.

* **Synchronized symmetric responses.** Independent errors with any even densities around a common center give a symmetric difference, including unequal shapes and widths. Exchangeable trigger times also give a symmetric difference. Either assumption gives exact cancellation of the self-pair bracket at every smooth width by oddness. For distinct readings the midpoint is the sharp limit.
* **Systematic offset.** For independent errors $X,Y$ take $D_h=\delta_h+\sigma_{2,h}Y-\sigma_{1,h}X$ with $\delta_h,\sigma_{1,h},\sigma_{2,h}\to0$ and positive widths. Set $w_h=\max(\sigma_{1,h},\sigma_{2,h})$. If $(\delta_h,\sigma_{1,h},\sigma_{2,h})/w_h\to(d,\alpha,\beta)$, then $p_h\to\Pr(d+\beta Y>\alpha X)$, provided the limiting tie probability is zero. With smooth error densities, this holds for finite $d$ since at least one of $\alpha,\beta$ equals one. For $d=\pm\infty$ the two one-sided limits are obtained. Even identical detectors can give a finite order bias when their mean offset shrinks at the same rate as their resolution.
* **Matching shape without reflection symmetry.** Give each device the same centered error distribution consisting of smooth peaks at $-2$ with mass $1/5$ and at $1/2$ with mass $4/5$. Use the same even bump of radius less than $1/8$ at both peaks. Independent responses of widths $h$ and $2h$ at the same mean time give $T_2>T_1$ precisely when the second detector chooses its positive peak. The cross-bracket tends to $3C_{11}/5=G_N/50$. Matching both mean and variance while allowing different shapes also permits bias. [Equal-variance example](weak-clock-contact.md)

## Paired trials and shared timing errors

A run may instead sample a *pair* of trigger times using an external random source. Taking the separated bracket in each run, then averaging those brackets, uses the joint timing law. An arbitrary common shift $J$ cancels from $(T_2+J)-(T_1+J)$ by translation invariance. If the residual errors vanish identically, the protocol lies on the diagonal. A law supported there needs a trace of the discontinuous kernel. For repeated copies of the same sharp symbol, skewness sets the algebraic self-bracket to zero. For two sharp symbols, specify a diagonal prescription or resolve the two residual orders. With exact-tie probability $r_h$ and assigned diagonal value $b_0$, the ties contribute $r_h b_0$ in addition to the two off-diagonal contributions.

Here is a smooth paired-trial distribution with **fixed identical even marginals** and arbitrary order bias. Choose any smooth compactly supported probability density $a$ that is even and positive in the interior of its support interval. Let $F$ be its cumulative distribution. Draw $U$ uniformly on $[0,1)$ and an independent shift $S$ with smooth density $k$ compactly supported inside $(0,1)$. Set
$$
 X=F^{-1}(U),\qquad Y=F^{-1}((U+S)\bmod 1),\qquad
 (T_1,T_2)=(hX,hY).
$$
The two marginals both have density $a$ in scaled units. The joint density is $a(x)a(y)k((F(y)-F(x))\bmod 1)$, using the smooth periodic extension of $k$. Conditional on $S=s$, the second trigger is later precisely for $U<1-s$. Consequently $p_h=1-\mathbb E S$. A symmetric bump centered at $1/3$ gives the paired-trial limit $+G_N/90$. Moving it to $2/3$ reverses the sign. In both cases the bracket of the two marginally averaged reports is exactly zero. Any value strictly between $-G_N/30$ and $+G_N/30$ is attainable by choosing the mean shift, while keeping the entire single-detector calibration fixed. A record of which trigger occurred first distinguishes these protocols even as every reading converges on smooth perturbations to the same sharp reading.

One can obtain the two stated values with smooth responses in *each individual trial*. Select a center uniformly from $(-h,0,h)$ for the first window and give the second the next center cyclically. At each center use the same even smooth unit-mass window of radius $h/8$. Conditional on the selected center, the bracket of the two smooth reports uses their product timing law. On two of the three choices the entire second window comes later. The wrapped choice comes earlier. Averaging these three conditional brackets therefore tends to $+G_N/90$. Reversing the cycle yields $-G_N/90$. The marginally averaged report for each detector uses exactly the same even three-peak window in both protocols.

## Reproduction

Run the commands below from the repository root. The focused check computes exact pulse-order weights, checks the circular shift of a uniform phase, and compares the timing predictions with the translated Einstein pairing. [Executable check](../checks/timing_protocol.py)

~~~sh
python3 -B checks/timing_protocol.py
make check
~~~

Expected output follows in units of $G_N$.

~~~text
Centered even windows: midpoint at unequal widths
Centered skew window at double width: 1/50
Identical marginals, paired cyclic triggers: 1/90 and -1/90
Distinct readouts: nonzero midpoint and half the calibrated jump
~~~
