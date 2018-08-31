import pytest
import hypothesis as ht
import hypothesis.strategies as st

import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from common.linkedlist import ListNode, mklist
from solution import add_two_numbers_v1, add_two_numbers_v2, add_two_numbers_v3


def rll2int(rll):
    """ convert a reversed linked list to integer
    """
    s = ''
    while rll:
        s = str(rll.val) + s
        rll = rll.next
    return int(s)


@ht.settings(verbosity=ht.Verbosity.verbose)
@ht.given(n1=st.integers(min_value=0), n2=st.integers(min_value=0))
def test_random(n1, n2):
    l1 = mklist(*map(int, reversed(str(n1))))
    l2 = mklist(*map(int, reversed(str(n2))))

    r1 = add_two_numbers_v1(l1, l2)
    r2 = add_two_numbers_v2(l1, l2)
    r3 = add_two_numbers_v3(l1, l2)

    assert r1 == r2
    assert r1 == r3


@ht.settings(verbosity=ht.Verbosity.verbose)
@ht.given(n1=st.integers(min_value=0),
          n2=st.integers(min_value=0),
          n3=st.integers(min_value=0))
def test_multi(n1, n2, n3):
    l1 = mklist(*map(int, reversed(str(n1))))
    l2 = mklist(*map(int, reversed(str(n2))))
    l3 = mklist(*map(int, reversed(str(n3))))

    r = add_two_numbers_v2(l1, l2, l3)
    assert rll2int(r) == (n1 + n2 + n3)
