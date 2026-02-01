from Phase2_nvidia.pipeline import run_quantum_seeded_mts

def test_pipeline_small_n():
    seq, energy = run_quantum_seeded_mts(5)
    assert len(seq) == 5
    assert energy >= 0
    
def test_iteration_budget_monotonic():
    from Phase2_nvidia.pipeline import iteration_budget

    best = 10.0
    max_iters = 1000

    it_good = iteration_budget(10.2, best, max_iters)
    it_mid  = iteration_budget(11.5, best, max_iters)
    it_bad  = iteration_budget(15.0, best, max_iters)

    assert it_good < it_mid
    assert it_mid >= it_bad
