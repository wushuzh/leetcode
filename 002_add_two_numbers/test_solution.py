import hypothesis as ht
import hypothesis.strategies as st

import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from common.linkedlist import ListNode, mklist

from solution import add_two_numbers_v1


def rll2int(l):
    s = ''
    while l:
        s = str(l.val) + s
        l = l.next
    return int(s)


@ht.settings(verbosity=ht.Verbosity.verbose)
@ht.given(n1=st.integers(min_value=0), n2=st.integers(min_value=0))
def test_random(n1, n2):
    l1 = mklist(*map(int, reversed(str(n1))))
    l2 = mklist(*map(int, reversed(str(n2))))
    r = add_two_numbers_v1(l1, l2)
    assert rll2int(r) == n1 + n2
