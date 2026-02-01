from Phase2_nvidia.pipeline import run_quantum_seeded_mts

def test_pipeline_small_n():
    seq, energy = run_quantum_seeded_mts(5)
    assert len(seq) == 5
    assert energy >= 0
