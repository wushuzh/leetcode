from random import randint
from solution import rm_duplicates


def test_empty():
    a = []
    assert rm_duplicates(a) == 0


def test_one():
    a = [1]
    assert rm_duplicates(a) == 1
    assert a == [1]


def test_no_dups():
    a = [1, 2, 3]
    assert rm_duplicates(a) == 3
    assert a == [1, 2, 3]


def test_dups():
    a = [1, 2, 2, 3, 4, 4, 5]
    assert rm_duplicates(a) == 5
    assert a[:5] == [1, 2, 3, 4, 5]


def test_multi(random_chk=1000):
    for _ in range(random_chk):  # test how many times
        a = []
        no_dup = randint(2, 100)
        for i in range(no_dup):  # no dup array length
            repeat = randint(1, 5)
            [a.append(i) for _ in range(repeat)]
        assert rm_duplicates(a) == no_dup
        assert a[:no_dup] == list(range(no_dup))
    # TODO: get the branchmark of a function
