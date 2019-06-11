from solution import longest_consecutive_by_uf


def test_given_sample():
    assert 4 == longest_consecutive_by_uf([100, 4, 200, 1, 3, 2])


def test_with_neg_element():
    assert 2 == longest_consecutive_by_uf([0, -1])