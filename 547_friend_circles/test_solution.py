from solution import find_circle_num_using_union_find


def test_sample_1():
    M = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]  # yapf: disable
    assert 2 == find_circle_num_using_union_find(M)


def test_sample_2():
    M = [[1, 1, 0],
         [1, 1, 1],
         [0, 1, 1]]  # yapf: disable
    assert 1 == find_circle_num_using_union_find(M)


def test_sample_3():
    M = [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]  # yapf: disable
    assert 1 == find_circle_num_using_union_find(M)


def test_sample_5():
    M = [[1, 0, 0, 1],
         [0, 1, 1, 0],
         [0, 1, 1, 1],
         [1, 0, 1, 1]]  # yapf: disable
    assert 1 == find_circle_num_using_union_find(M)


def test_sample_4():
    M = [[1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]  # yapf: disable
    assert 3 == find_circle_num_using_union_find(M)
