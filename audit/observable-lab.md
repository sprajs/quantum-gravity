# Can gravity entangle two laboratory masses?

Prepare two separated masses independently, each in a superposition of two positions. After a shared interval of free fall, reunite each pair of paths and measure the two spins that labelled them. The coherent Newtonian interaction predicts an entangled spin state. A local measurement-and-classical-feedback model of gravity predicts a separable state. At the 2017 design point used here, the ideal quantum prediction exceeds the largest spin fidelity of any unentangled state by **0.078**. This comparison tests how gravity couples to quantum matter. Venkatesa Chandrasekaran quantizes four-dimensional **vacuum** gravity in arXiv:2611.34924v1. The scalar matter in his two-dimensional example does not supply the four-dimensional masses, their backreaction or their detector. [Chandrasekaran, abstract and §§2–3](https://arxiv.org/abs/2611.34924v1) · [Bose et al., experimental proposal](https://arxiv.org/abs/1707.06050v1) · [Marletto and Vedral, mediator argument](https://arxiv.org/abs/1707.06036v2)

## The phase that survives local recalibration

Let $i,j=L,R$ label the arms of interferometers $A,B$. Assume equal branch amplitudes, narrow nonoverlapping packets, negligible deflection and coherent evolution under the two-body potential $V_{ij}=-Gm_A m_B/r_{ij}$. During a hold of duration $T$, write

$$
|\psi\rangle=\frac12\sum_{ij} e^{i\phi_{ij}} |ij\rangle,\qquad
\phi_{ij}=\frac{Gm_A m_B}{\hbar}\int_0^T\frac{dt}{r_{ij}(t)},\qquad
\Phi=\phi_{LL}+\phi_{RR}-\phi_{LR}-\phi_{RL}.
$$

An arbitrary one-body phase $\alpha_i+\beta_j$ cancels from $\Phi$. The pure-state concurrence is twice the absolute determinant of the $2\times2$ amplitude matrix,

$$
C=\tfrac12\left|e^{i(\phi_{LL}+\phi_{RR})}-e^{i(\phi_{LR}+\phi_{RL})}\right|
=|\sin(\Phi/2)|.
$$

Thus equal local fringe shifts can coexist with separability, while a nonzero $\Phi$ modulo $2\pi$ entangles the ideal product input. The concurrence formula assumes the output stays pure. Actual spin counts can test a separability bound without that assumption.

For a collinear geometry place the centres $d$ apart and split each mass through a total distance $s<d$, with $R$ to the right for both. The four constant centre-to-centre distances in the hold are $d,d+s,d-s,d$. The exact phase in this geometry is

$$
\Phi=\frac{Gm_A m_B T}{\hbar}
\left(\frac{2}{d}-\frac{1}{d+s}-\frac{1}{d-s}\right)
=-\frac{2Gm_A m_B T s^2}{\hbar d(d^2-s^2)} .
$$

Use the nominal Bose et al. values $m_A=m_B=10^{-14}\,\mathrm{kg}$, $d=450\,\mu\mathrm m$, $s=250\,\mu\mathrm m$, $T=2.5\,\mathrm s$. The distances are $450,700,200,450\,\mu\mathrm m$. With these inputs the hold contributes $\Phi=-0.314$ rad and $C=0.156$. Keeping only the leading small-splitting term would give 69% of this phase. The proposal gives approximate masses and dimensions. A forecast for a particular instrument would also integrate the measured splitting and recombination trajectories. [Bose et al., geometry and parameters, pp. 2–4](https://arxiv.org/pdf/1707.06050v1#page=2)

## A spin measurement with a classical bound

Identify $L,R$ with the two spin $Z$ labels after coherent recombination. Calibrated local $Z$ rotations remove the one-body phases. The resulting spin state is $e^{i\Phi Z_A Z_B/4}|++\rangle=\cos(\Phi/4)|++\rangle+i\sin(\Phi/4)|--\rangle$, where $|+\rangle,|-\rangle$ are $X$ eigenstates. For the negative phase above, fix the Bell target $|B\rangle=(|++\rangle-i|--\rangle)/\sqrt2$ before collecting data. Its fidelity $F=\langle B|\rho|B\rangle$ is accessible from three pairs of local Pauli settings,

$$
F=\frac{1+\langle X_A X_B\rangle+\langle Z_A Y_B\rangle+\langle Y_A Z_B\rangle}{4}.
$$

The squared overlap of a product state with this Bell state is at most $1/2$, its largest squared Schmidt coefficient. Convexity gives the same bound for every separable mixture. The ideal hold gives $F=(1+C)/2=0.5782$. An experimental lower confidence bound above $0.5$, including readout and calibration uncertainty, would witness entanglement. As a sensitivity illustration, replacing the ideal state by $v|\psi\rangle\langle\psi|+(1-v)I/4$ after local recalibration requires $v>0.762$ to pass the witness. Here $v$ is the ideal-state fraction for this particular white-noise model. An apparatus with dephasing, spin loss or readout bias needs its own noise model.

From the repository root run **python3 checks/observable_lab.py**. The check sums the four branch phases, compares them with the rational expression, calculates concurrence from the amplitude determinant and projects the locally recalibrated state onto the Bell target. Expected outputs are $-0.31393449$ rad, $0.15632346$ and $0.57816173$, respectively. The displayed precision checks arithmetic on nominal inputs. [Runnable calculation](../checks/observable_lab.py)

## What would establish gravitational mediation?

* **Exclude other interactions that can entangle the masses.** Bare electric charges have the same $1/r$ potential as Newtonian gravity. One excess elementary charge on each benchmark mass gives a magnitude ratio $e^2/(4\pi\epsilon_0 Gm_A m_B)=3.46\times10^{10}$. Changing the spacing alone cannot distinguish these two contributions. Certify neutrality, measure residual dipoles and magnetic coupling, and bound the differential four-path phase due to Casimir–Polder forces. A conducting screen can suppress direct electromagnetic coupling. Its vibration and surface forces enter the error budget. [Bose et al., p. 4](https://arxiv.org/pdf/1707.06050v1#page=4) · [Schut et al., screening analysis](https://arxiv.org/abs/2307.07536v2)
* **Demonstrate coherence and an independent start.** Measure each interferometer’s visibility and spin readout with the masses far apart. Check that the preparation, control electronics and readout cannot supply entanglement or correlated selection. With one splitting set to zero, the Newtonian entangling phase vanishes even at finite separation. Vary both spacing and hold time, accounting for phase acquired during the ramps. Residual gas, thermal radiation, mechanical motion and magnetic fluctuations can suppress the signal. A null witness constrains only a benchmark whose expected noisy signal exceeded the measured sensitivity. [Bose et al., coherence estimates](https://arxiv.org/pdf/1707.06050v1#page=4) · [QGEM experimental requirements, 2026](https://arxiv.org/abs/2610.07422v1)
* **Name the competing dynamics.** A deterministic mean field sourced by the expectation of each mass density gives a sum of single-particle Hamiltonians for initially independent masses and leaves the product form intact. Local measurements followed by classical messages and feedback give a mixture of local product branches and also preserve separability. Kafri, Taylor and Milburn construct a specific example for coupled resonators. If the mediator and apparatus supply no initial quantum correlation between laboratories, all interactions act locally through the proposed mediator, and controls bound competing quantum channels, a verified excess over the separability bound excludes these mechanisms. A direct two-body operator $V(\hat x_A-\hat x_B)$ already gives the displayed phase without specifying a mediating field. Aziz and Howl argue that quantum matter fields can allow two masses to become entangled in a classical gravitational field. Marletto, Oppenheim, Vedral and Wilson dispute that the model produces entanglement and assign any direct quantum matter interaction to the matter channel. Marletto and Vedral identify a direct nonlocal coupling in the proposed entangling Hamiltonian. Tang and colleagues estimate that atomic binding limits the range of virtual matter exchange to picometres in their example. These are distinct criticisms. Inferring a quantum property of a local gravitational mediator from entanglement requires excluding direct quantum exchange between the masses and controlling other interactions. [Kafri, Taylor and Milburn](https://arxiv.org/abs/1401.0946) · [Marletto and Vedral](https://arxiv.org/abs/1707.06036v2) · [Aziz and Howl](https://doi.org/10.1038/s41586-025-09595-7) · [Marletto, Oppenheim, Vedral and Wilson](https://arxiv.org/abs/2511.07348v1) · [Marletto and Vedral](https://arxiv.org/abs/2510.19969) · [Tang et al.](https://doi.org/10.1103/bg9v-ln16)

**Experimental status, 26 November 2026.** The primary reports reviewed here contain no detection of gravity-mediated entanglement between independently prepared masses. The 2026 QGEM white paper gives interferometer and low-frequency-noise requirements. Herbst et al. report a related measurement of gravitational force from an 87 mg source on a 1.3 mg test mass. Their readout measures driven motion. The two-spin correlations above would provide a different observable. [QGEM white paper](https://arxiv.org/abs/2610.07422v1) · [Herbst et al., experimental preprint](https://arxiv.org/abs/2611.08619v1)

**What the null-cone theory would have to predict.** Couple localized four-dimensional matter and its stress tensor to the gravitational constraints. Define the two preparation operations, relational paths and spin readouts, then trace out the unmeasured gravity and apparatus degrees of freedom to predict $\rho_{AB}$. Recovering the phase above would check the weak-field matter coupling shared with other coherent theories. A distinctive test needs a residual change in the spin probabilities or their scaling that a matched low-energy alternative cannot reproduce, together with an uncertainty small enough to resolve it. The vacuum manuscript gives no magnitude or sign for such a residual. [Chandrasekaran, §§3 and 6](https://arxiv.org/pdf/2611.34924v1#page=52)
