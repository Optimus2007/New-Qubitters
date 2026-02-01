from Phase2_nvidia.quantum_seeding import (
    sample_qaoa_with_energy,
    select_top_k_quantum_seeds
)
from Phase2_nvidia.mts_cpu import run_mts

def iteration_budget(seed_energy, best_energy, max_iters):
    """
    Simple adaptive iteration allocation.
    Better seeds get fewer iterations.
    """
    if seed_energy <= 1.05 * best_energy:
        return int(0.3 * max_iters)
    elif seed_energy <= 1.20 * best_energy:
        return int(0.6 * max_iters)
    else:
        return int(0.2 * max_iters)



from Phase2_nvidia.labs_energy import labs_energy

def run_quantum_seeded_mts(n, shots=200, k=10, max_iters=1000):
    samples = sample_qaoa_with_energy(n, shots)
    seeds = select_top_k_quantum_seeds(samples, k)

    # Compute best seed energy
    seed_energies = [(seed, labs_energy(seed)) for seed in seeds]
    best_seed_energy = min(e for _, e in seed_energies)

    best_seq = None
    best_energy = float("inf")

    for seed, energy in seed_energies:
        iters = iteration_budget(energy, best_seed_energy, max_iters)

        seq, e = run_mts(
            n,
            initial_population=[seed],
            max_iters=iters
        )

        if e < best_energy:
            best_energy = e
            best_seq = seq

    return best_seq, best_energy

