import random
from Phase2_nvidia.labs_energy import labs_energy

def random_sequence(n):
    return [random.choice([1, -1]) for _ in range(n)]

def run_mts(n, initial_population=None, max_iters=300):
    if initial_population is None:
        population = [random_sequence(n) for _ in range(10)]
    else:
        population = initial_population

    best_seq = min(population, key=labs_energy)
    best_energy = labs_energy(best_seq)

    tabu = set()

    for _ in range(max_iters):
        neighbors = []

        for i in range(n):
            cand = best_seq.copy()
            cand[i] *= -1
            if tuple(cand) not in tabu:
                neighbors.append((cand, labs_energy(cand)))

        if not neighbors:
            break

        cand, energy = min(neighbors, key=lambda x: x[1])

        if energy < best_energy:
            best_seq = cand
            best_energy = energy

        tabu.add(tuple(best_seq))

    return best_seq, best_energy
