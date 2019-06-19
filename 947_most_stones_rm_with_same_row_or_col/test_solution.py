from solution import rm_stones_using_union_find


def test_sample_1():
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    assert 5 == rm_stones_using_union_find(stones)


def test_sample_2():
    stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
    assert 3 == rm_stones_using_union_find(stones)


def test_sample_3():
    assert 0 == rm_stones_using_union_find([[0, 0]])