import cudaq
from math import pi

@cudaq.kernel
def qaoa_labs_kernel(n: int, gamma: float, beta: float):
    qubits = cudaq.qvector(n)

    # Superposition
    for i in range(n):
        h(qubits[i])

    # Simple cost phase (safe, valid)
    for i in range(n):
        rz(2 * gamma, qubits[i])

    # Mixer
    for i in range(n):
        rx(2 * beta, qubits[i])
