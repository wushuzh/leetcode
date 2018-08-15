from random import randint

import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from common.linkedlist import ListNode, convert_array, mklist
from solution import deleteDuplicates


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
