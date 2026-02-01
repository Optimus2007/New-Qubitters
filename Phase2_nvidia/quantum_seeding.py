import cudaq
from math import pi
from Phase2_nvidia.labs_energy import labs_energy
from Phase2_nvidia.qaoa_kernel import qaoa_labs_kernel



def bitstring_to_sequence(bitstring):
    return [1 if b == '0' else -1 for b in bitstring]

def sample_qaoa_with_energy(n, shots=200):
    gamma = pi / 4
    beta = pi / 8

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

def select_top_k_quantum_seeds(samples, k=10):
    samples_sorted = sorted(samples, key=lambda x: x[1])
    return [seq for seq, _ in samples_sorted[:k]]
