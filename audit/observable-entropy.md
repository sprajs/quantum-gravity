# Which entropy prediction could be tested?

Venkatesa Chandrasekaran's null-cone proposal assigns a probability to the area of a clock-selected diamond. For its large Schwarzschild ensemble, **13.82%** of the boost-weighted trace should lie below half the allowed area. This gives a target for a calculation with an independently constructed gravitational state space. At infinity, the proposed logarithmic coefficient agrees with an existing prediction of effective gravity. A radiation experiment that recovered this coefficient would test both descriptions together. [Chandrasekaran, arXiv:2611.34924v1, Eqs. (5.63)–(5.69)](https://arxiv.org/html/2611.34924v1#S5.E63) · [Sen, Eqs. (1.2)–(1.5)](https://arxiv.org/pdf/1205.0971#page=6)

## A ratio for the clock ensemble

Write $s=A/(4\ell_P^2)$, $\ell_P^2=\hbar G/c^3$. The clock projector $P_\ell$ keeps states with affine clock reading $\bar u_*\leq\ell$. Focusing bounds $s$ by $s_*=\pi\ell^2/[(1-\epsilon)^2\ell_P^2]$. Count physical states with their multiplicities. The normalized trace below a fraction $z$ of the area bound is

$$
F_\ell(z)=
\frac{\operatorname{Tr}[P_\ell\,e^{-\hat s}\,\mathbf1_{[0,zs_*]}(\hat s)]}
     {\operatorname{Tr}[P_\ell\,e^{-\hat s}]} .
$$

Equation (5.63) gives $F_\ell(z)\to z^k$ with $k=q/[2(1-q)]$. Here $q$ is the limiting mean clock reading divided by $\ell$. This uses the same nested clock projections as $\ell$ grows, a finite trace, and the claimed asymptotic saturation of the clock–area relation in the Schwarzschild ensemble. With $q=257/302$, $k=257/90$ and $F_\ell(1/2)\to0.138163$. The boundary $zs_*$ is a cut on *area*. Halving the radius would select one quarter of the area. [Clock weighting and Eq. (5.63)](https://arxiv.org/html/2611.34924v1#S5.E63) · [Eq. (5.68)](https://arxiv.org/html/2611.34924v1#S5.E68)

Why does the probability depend on the measure? Suppose the boost-weighted number of states per unit $s$ has a smooth density proportional to $s^p$ in the relevant bands, with $p>-1$. Integrating to $zs_*$ gives $F_\ell(z)\to z^{p+1}$ if this scaling controls the normalized distribution over the allowed range. The paper's Gaussian packet has width $\sqrt{2s_b}$ in $s$, so its trace near $s_b$ scales as $s_b^{p+1/2}$. The power $106/45$ assigned to this **packet** implies $p=167/90$ and gives the probability above. Assigning $106/45$ instead to the **density per unit $s$** would give $k=151/45$ and $F_\ell(1/2)\to0.097696$. This second number illustrates the size of a change to the *physical* spectral measure. It would give a different density at fixed mass from Sen's result. [Packet definition and determinant](https://arxiv.org/html/2611.34924v1#S5.E66) · [Derivation of the two assignments](ensemble-crosscheck.md)

An independent test would construct the reflected trace, impose the Schwarzschild boundary and clock conditions, retain the area mode and cap, corner and ghost factors, and evaluate the numerator and denominator with the same regulator. Remove the radial and angular cutoffs at fixed physical $\ell$ before taking the large-diamond limit, or demonstrate uniform control for a joint limit. Uncertainties in the limiting probability must be small compared with the $0.04047$ gap to distinguish these two measures. A stable different limit would challenge their assignment or a hypothesis behind the clock distribution. Inserting the power law into the trace checks the arithmetic. Testing it requires deriving the weights independently. An astronomical observation would additionally require a preparation with this weighting and access to its relational interior area and clock. [Proposed preparations](https://arxiv.org/html/2611.34924v1#S5.SS1) · [Replicated measure](https://arxiv.org/html/2611.34924v1#A4.SS3)

## What survives a change of counting variable?

At a Schwarzschild saddle $s(M)=4\pi(M/m_P)^2$ with $m_P=\sqrt{\hbar c/G}$. Suppose $dN/dM\propto e^s s^\alpha$ in a smooth spin-summed rest-mass density. Then $dN/ds\propto e^s s^{\alpha-1/2}$ because $ds/dM=2s/M$. The count in any physical mass interval equals the area integral between its mapped endpoints. A detector or calculation using matched intervals obtains the same ratio in either coordinate. The half-log changes when one holds the numerical bin widths fixed in different coordinates. Treating the per-area coefficient as a second mass-temperature prediction would change the experiment. [Sen, footnote 3](https://arxiv.org/pdf/1205.0971#page=7)

There is a separate count that can distinguish **spin ensembles**. Let $\rho_X(M)$ be the rest-mass density for spin selection $X$ and let $\rho_{\rm all}$ include all angular momenta. In four-dimensional pure gravity Sen finds the respective $\log s$ coefficients $106/45$ (all), $167/90$ ($J_3=0$) and $77/90$ (rotational singlets). With smooth one-loop prefactors approaching constants, the unknown normalizations and the leading $e^s$ cancel in the double ratio

$$
\frac{(\rho_X/\rho_{\rm all})(2M)}{(\rho_X/\rho_{\rm all})(M)}
\ \longrightarrow\
4^{\alpha_X-\alpha_{\rm all}}=
\begin{cases}
1/2 & X \text{ fixes }J_3=0,\\
1/8 & X \text{ selects }J=0 .
\end{cases}
$$

An interior-to-asymptotic state count could test these factors after identifying the rest-mass observable, spin projectors, center-of-mass normalization and exterior subtraction. They offer low-energy benchmarks for that identification. Measured astrophysical spin distributions also depend on formation and accretion and do not sample those state densities. [Sen, §3.2](https://arxiv.org/pdf/1205.0971#page=26)

## How large would a temperature or radiation effect be?

Use the intrinsic spin-summed density per unit energy $\rho_E$, where $E=Mc^2$. Multiplying by a fixed reference energy $E_0$ makes the logarithm dimensionless. Write $\mathcal S(E)=\log[E_0\rho_E(E)]=s+\alpha\log s+r(E)$, so that the dimensionful entropy is $k_B\mathcal S$. Sen's $\alpha=106/45$ and the Schwarzschild effective-action result use the same low-energy massless-graviton content. Additional massless species change the coefficient. [Sen, Eqs. (1.2)–(1.4)](https://arxiv.org/pdf/1205.0971#page=6) · [El-Menoufi, Eqs. (1.7)–(1.9)](https://arxiv.org/pdf/1511.08816#page=6)

If this density supplies the thermodynamic entropy for energy exchanged at infinity, $1/(k_BT_{\rm th})=\partial_E\mathcal S$. Since $s\propto E^2$,

$$
\frac{1}{k_BT_{\rm th}}=\frac{2s}{E}+\frac{2\alpha}{E}+r'(E),
\qquad
T_H=\frac{\hbar c^3}{8\pi G M k_B},
\qquad
\frac{T_{\rm th}-T_H}{T_H}=-\frac{\alpha}{s}+o(s^{-1}).
$$

The last step requires $E r'(E)=o(1)$, or a smooth one-loop expansion to that accuracy. A bounded remainder in the entropy alone does not control its derivative. For $M=1.98847\times10^{31}\ {\rm kg}$ (about ten solar masses) this gives $s=1.0490\times10^{79}$, $\alpha\log s=428.60$ and $T_H=6.17\times10^{-9}\ {\rm K}$. The inferred shift is **$-1.39\times10^{-87}\ {\rm K}$**, or **$-2.25\times10^{-79}$** fractionally. This is a pure-gravity scale estimate for the specified entropy. A temperature inferred from outgoing quanta also depends on the state and on transmission through the exterior gravitational potential. Gravitational-wave observations such as GW250114 instead infer the change of horizon area during a merger from the waveform. That measurement supplies neither a state count nor a radiation temperature. [Page on particle transmission and emission](https://doi.org/10.1103/PhysRevD.13.198) · [LIGO–Virgo–KAGRA on GW250114](https://arxiv.org/abs/2509.08054)

One can also isolate an energy dependence in a *model* of the emission-to-reverse-absorption ratio. Suppose microscopic reversibility, uniform averaging within matched energy bins, and identical external mode and phase-space normalization allow the squared transition elements to cancel in that ratio. Let $w$ be the loss of intrinsic energy, including the chosen recoil accounting. Then its log density factor is $D_E(w)=\mathcal S(E-w)-\mathcal S(E)$. For two losses $x_i=w_i/E$ with $x_1+x_2<1$, the mixed difference $D_E(w_1+w_2)-D_E(w_1)-D_E(w_2)$ from the area and logarithm is

$$
2s x_1x_2+
2\alpha\log\!\left[1-\frac{x_1x_2}{(1-x_1)(1-x_2)}\right].
$$

At $w_1=w_2=k_BT_H$, $x_i=1/(2s)$. The leading area term is $1/(2s)$, already present from energy conservation, and the logarithmic term is $-\alpha/(2s^2)+O(s^{-3})$. At the example mass these terms are $4.77\times10^{-80}$ and $-1.07\times10^{-158}$ respectively. To control that second term against the omitted entropy remainder requires $E^2r''(E)=o(1)$ uniformly over these small energy intervals. A measured correlation between two outgoing quanta requires the joint transition rates, their normalization, angular momentum channels, time windows and detector response. This mixed difference is a ratio of density factors and has no interpretation by itself as a covariance or mutual information. [Parikh and Wilczek, energy-conserving emission model, Eq. (10)](https://arxiv.org/pdf/hep-th/9907001#page=5) · [Page on mode-dependent rates](https://doi.org/10.1103/PhysRevD.13.198)

## Reproduce the numerical checks

From the repository root run `python3 checks/observable_entropy.py`. It integrates each trial measure, checks that matched mass and area intervals give unit count ratio, and compares the two-loss formula with a direct finite difference at moderate area before evaluating the separated terms for the stellar mass. Expected outputs include $0.138163$, $0.097696$, a count ratio of $1.000000000000$ and the fractional temperature shift $-2.2456\times10^{-79}$. The input spectra are trial densities. [Calculation](../checks/observable_entropy.py)
