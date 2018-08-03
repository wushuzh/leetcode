from random import randint
from functools import reduce
from solution import ListNode, deleteDuplicates

# TODO: remove dup code with 083
def cons(v, tail):
    head = ListNode(v)
    head.next = tail
    return head


def mklist(*args):
    return reduce(lambda tail, v: cons(v, tail), reversed(args), None)


def convert_array(head):
    a = []
    succ = head
    while succ:
        a.append(succ.val)
        succ = succ.next
    return a


def test_none():
    assert deleteDuplicates(None) is None


def test_one():
    assert [42] == convert_array(deleteDuplicates(ListNode(42)))


def test_ones():
    assert [] == convert_array(deleteDuplicates(mklist(42, 42, 42)))


def test_multi(check_itr=1000):
    for _ in range(check_itr):
        in_a = []
        expect_a = []
        last_num = randint(2, 100)
        for i in range(last_num):  # no dup array length
            repeat = randint(1, 3)
            if repeat == 1:
                expect_a += [i]
            in_a += [i] * repeat
        new_head = deleteDuplicates(mklist(*in_a))
        assert convert_array(new_head) == expect_a
