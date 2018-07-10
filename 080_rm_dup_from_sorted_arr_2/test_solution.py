from random import randint
from solution import rm_dups


def test_empty():
    assert rm_dups([]) == 0


def test_one():
    assert rm_dups([1]) == 1


def test_two_same():
    assert rm_dups([1, 1]) == 2


def test_two_diff():
    assert rm_dups([1, 2]) == 2


def test_mult(random_chk=1000):
    for _ in range(random_chk):
        a = []
        b = []
        final_len = no_dup = randint(2, 100)
        for i in range(no_dup):
            a.append(i)
            b.append(i)
            repeat = randint(0, 5)
            if repeat != 0:
                a.extend([i]*repeat)
                b.extend([i])
                final_len += 1
        assert rm_dups(a) == final_len
        assert a[:final_len] == b[:final_len]


def test_three():
    a = [1, 1, 2]
    assert rm_dups(a) == 3


def test_three_same():
    a = [1, 1, 1]
    assert rm_dups(a) == 2


def test_four_1():
    a = [1, 1, 2, 2]
    assert rm_dups(a) == 4


def test_four_2():
    a = [1, 1, 1, 2]
    assert rm_dups(a) == 3
