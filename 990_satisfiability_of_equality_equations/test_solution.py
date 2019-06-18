from solution import equations_possible_using_union_find


def test_sample_1():
    assert not equations_possible_using_union_find(["a==b", "b!=a"])


def test_sample_2():
    assert equations_possible_using_union_find(["b==a", "a==b"])


def test_sample_3():
    assert equations_possible_using_union_find(["a==b", "b==c", "a==c"])


def test_sample_4():
    assert not equations_possible_using_union_find(["a==b", "b!=c", "c==a"])


def test_sample_5():
    assert equations_possible_using_union_find(["c==c", "b==d", "x!=z"])
