import pytest
import hypothesis as ht
import hypothesis.strategies as st

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from common.linkedlist import ListNode, mklist, convert_array
from solution import rm_nth_from_end_v1


@st.composite
def list_and_nthindex(draw):
    xs = draw(st.lists(st.integers(), min_size=1))
    n = draw(st.integers(min_value=1,
                         max_value=max(1, len(xs))))
    return (xs, n)


@ht.given(xs_n=list_and_nthindex())
def test_random(xs_n):
    xs, n = xs_n

    head1 = mklist(*xs)

    r1 = rm_nth_from_end_v1(head1, n)

    del xs[-n]
    assert convert_array(r1) == xs

    del xs_dup[-n]
    assert r1 == mklist(*xs_dup)
