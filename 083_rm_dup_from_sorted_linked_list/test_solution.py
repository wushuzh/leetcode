from random import randint
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from common.linkedlist import ListNode, convert_array, mklist
from solution import deleteDuplicates



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
