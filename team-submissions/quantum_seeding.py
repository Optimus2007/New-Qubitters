import cudaq
import numpy as np
from math import pi
from Phase2_nvidia.labs_energy import labs_energy
from Phase2_nvidia.qaoa_kernel import qaoa_labs_kernel


def bitstring_to_sequence(bitstring):
    return [1 if b == '0' else -1 for b in bitstring]


# -------------------------------
# NEW: LABS-informed QAOA params
# -------------------------------
def labs_informed_qaoa_params(n):
    """
    Simple heuristic inspired by LABS structure.
    Keeps parameters deterministic and testable.
    """
    gamma = pi / (2 * n)
    beta = pi / 8
    return gamma, beta


def sample_qaoa_with_energy(n, shots=200):
    # Use LABS-informed parameters instead of fixed generic ones
    gamma, beta = labs_informed_qaoa_params(n)

    result = cudaq.sample(
        qaoa_labs_kernel,
        n,
        gamma,
        beta,
        shots_count=shots
    )

    samples = []
    for bitstring in result:
        seq = bitstring_to_sequence(bitstring)
        energy = labs_energy(seq)
        samples.append((seq, energy))

    return samples


# ---------------------------------------
# NEW: symmetry-aware duplicate filtering
# ---------------------------------------
def remove_symmetric_duplicates(samples):
    """
    LABS symmetry: S and -S have identical energy.
    Keep only one representative.
    """
    seen = set()
    filtered = []

    for seq, energy in samples:
        key = tuple(seq)
        neg_key = tuple(-x for x in seq)

        if key not in seen and neg_key not in seen:
            filtered.append((seq, energy))
            seen.add(key)

    return filtered


def select_top_k_quantum_seeds(samples, k=10):
    # Apply symmetry filtering before selecting best seeds
    samples = remove_symmetric_duplicates(samples)
    samples_sorted = sorted(samples, key=lambda x: x[1])
    return [seq for seq, _ in samples_sorted[:k]]
