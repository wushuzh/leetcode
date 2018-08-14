from random import randint
from functools import reduce
from solution import ListNode, deleteDuplicates


def cons(v, tail):
    head = ListNode(v)
    head.next = tail
    return head


def mklist(*args):
    return reduce(lambda tail, v: cons(v, tail), reversed(args), None)


def printSSL(lst):
    if lst:
        print("{} -> ".format(lst), end="")
        printSSL(lst.next)
    else:
        print('None')


def convert_array(head):
    a = []
    succ = head
    while succ:
        a.append(succ.val)
        succ = succ.next
    return a


def test_multi(check_itr=1000):
    for _ in range(check_itr):
        a = []
        no_dup = randint(2, 100)
        for i in range(no_dup):  # no dup array length
            repeat = randint(1, 3)
            a += [i] * repeat
        new_head = deleteDuplicates(mklist(*a))
        assert convert_array(new_head) == list(range(no_dup))


def test_none():
    assert deleteDuplicates(None) is None


def test_one():
    assert [42] == convert_array(deleteDuplicates(ListNode(42)))


def test_ones():
    assert [42] == convert_array(deleteDuplicates(mklist(42, 42, 42)))
