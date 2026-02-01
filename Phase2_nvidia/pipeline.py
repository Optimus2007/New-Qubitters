from Phase2_nvidia.quantum_seeding import (
    sample_qaoa_with_energy,
    select_top_k_quantum_seeds
)
from Phase2_nvidia.mts_cpu import run_mts


def run_quantum_seeded_mts(n, shots=200, k=10):
    samples = sample_qaoa_with_energy(n, shots)
    seeds = select_top_k_quantum_seeds(samples, k)

    best_seq, best_energy = run_mts(
        n,
        initial_population=seeds
    )

    return best_seq, best_energy
