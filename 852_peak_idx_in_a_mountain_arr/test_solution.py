from solution import peak_idx_in_mountain_arr_recursive, peak_idx_in_mountain_arr_iterative


def test_even_case():
    assert 1 == peak_idx_in_mountain_arr_recursive([0, 2, 1, 0])
    assert 1 == peak_idx_in_mountain_arr_iterative([0, 2, 1, 0])


def test_odd_case():
    assert 1 == peak_idx_in_mountain_arr_recursive([0, 1, 0])
    assert 1 == peak_idx_in_mountain_arr_iterative([0, 1, 0])
