from Phase2_nvidia.labs_energy import labs_energy

def test_energy_symmetry():
    s = [1, -1, 1]
    assert labs_energy(s) == labs_energy([-x for x in s])
