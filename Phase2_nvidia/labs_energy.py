def labs_energy(sequence):
    n = len(sequence)
    energy = 0.0

    for k in range(1, n):
        c_k = 0
        for i in range(n - k):
            c_k += sequence[i] * sequence[i + k]
        energy += c_k ** 2

    return energy
