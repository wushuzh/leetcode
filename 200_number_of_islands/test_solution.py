from solution import find_num_islands_with_uf


def test_example_1():
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]  # yapf: disable
    assert 1 == find_num_islands_with_uf(grid)


def test_example_2():
    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '0']]  # yapf: disable
    assert 3 == find_num_islands_with_uf(grid)
