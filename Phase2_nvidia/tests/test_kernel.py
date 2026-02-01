import cudaq
from Phase2_nvidia.qaoa_kernel import qaoa_labs_kernel

def test_qaoa_kernel_runs():
    result = cudaq.sample(qaoa_labs_kernel, 3, 0.5, 0.3, shots_count=10)
    assert len(result) > 0
