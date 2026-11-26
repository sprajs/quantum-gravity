"""Reproduce the ideal, hold-only, two-mass phase and spin witness in SI units."""

import cmath
import math


def check_lab_benchmark():
    gravitation = 6.67430e-11
    hbar = 6.62607015e-34 / math.tau
    mass = 1.0e-14
    hold = 2.5
    spacing = 450.0e-6
    splitting = 250.0e-6
    paths_a = (-splitting / 2, splitting / 2)
    paths_b = (spacing - splitting / 2, spacing + splitting / 2)
    distances = [abs(b - a) for a in paths_a for b in paths_b]
    prefactor = gravitation * mass**2 * hold / hbar
    phases = [prefactor / distance for distance in distances]
    phase_ll, phase_lr, phase_rl, phase_rr = phases
    phi = phase_ll + phase_rr - phase_lr - phase_rl
    rational_phi = -2 * prefactor * splitting**2 / (spacing * (spacing**2 - splitting**2))
    assert math.isclose(phi, rational_phi, abs_tol=1e-14)

    # A pure two-qubit state's concurrence is twice its amplitude determinant in modulus.
    a_ll, a_lr, a_rl, a_rr = (cmath.exp(1j * phase) / 2 for phase in phases)
    concurrence = 2 * abs(a_ll * a_rr - a_lr * a_rl)
    assert math.isclose(concurrence, abs(math.sin(phi / 2)), abs_tol=1e-14)

    # Subtract the common and single-qubit Z phases implied by the four paths.
    mean_phase = sum(phases) / 4
    local_a = (phase_ll + phase_lr - phase_rl - phase_rr) / 4
    local_b = (phase_ll - phase_lr + phase_rl - phase_rr) / 4
    spin_state = []
    for phase, (z_a, z_b) in zip(phases, [(1, 1), (1, -1), (-1, 1), (-1, -1)]):
        phase -= mean_phase + local_a * z_a + local_b * z_b
        spin_state.append(cmath.exp(1j * phase) / 2)

    # |B> = (|++> - i|-->)/sqrt(2), written in the path/spin Z basis.
    bell_state = [(1 - 1j * parity) / math.sqrt(8) for parity in (1, -1, -1, 1)]
    fidelity = abs(sum(b.conjugate() * a for b, a in zip(bell_state, spin_state)))**2
    assert math.isclose(fidelity, (1 + concurrence) / 2, abs_tol=1e-14)
    # Apply the three Pauli products directly in the ordered Z basis.
    a, b, c, d = spin_state
    xx = [d, c, b, a]
    zy = [-1j * b, 1j * a, 1j * d, -1j * c]
    yz = [-1j * c, 1j * d, 1j * a, -1j * b]
    correlations = [
        sum(u.conjugate() * v for u, v in zip(spin_state, acted)).real
        for acted in (xx, zy, yz)
    ]
    assert math.isclose((1 + sum(correlations)) / 4, fidelity, abs_tol=1e-14)
    threshold = 0.25 / (fidelity - 0.25)
    assert math.isclose(threshold * fidelity + (1 - threshold) / 4, 0.5)

    charge = 1.602176634e-19
    coulomb_constant = 8.987551786e9
    charge_ratio = coulomb_constant * charge**2 / (gravitation * mass**2)
    print("Hold distances LL, LR, RL, RR (um):", *(f"{r * 1e6:.0f}" for r in distances))
    print(f"Four-path phase (rad): {phi:.8f}")
    print(f"Pure-state concurrence: {concurrence:.8f}")
    print(f"Bell fidelity: {fidelity:.8f} (separable bound 0.5)")
    print(f"White-noise threshold on ideal-state weight: {threshold:.8f}")
    print(f"Coulomb / Newton magnitude for one elementary charge each: {charge_ratio:.3e}")


if __name__ == "__main__":
    check_lab_benchmark()
