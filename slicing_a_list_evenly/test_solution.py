import pytest
import hypothesis as ht
import hypothesis.strategies as st
import functools


from solution import chunk, chunk_iteratools


def test_chunk():
    with pytest.raises(AssertionError):
        assert chunk('', 1) == ['']
    assert chunk('ab', 2) == ['a', 'b']
    assert chunk('abc', 2) == ['ab', 'c']

    xs = list(range(8))
    assert chunk(xs, 2) == [[0, 1, 2, 3], [4, 5, 6, 7]]
    assert chunk(xs, 3) == [[0, 1, 2], [3, 4, 5], [6, 7]]
    assert chunk(xs, 5) == [[0, 1], [2, 3], [4, 5], [6], [7]]

    rs = range(1000000)
    assert chunk(rs, 2) == [range(500000), range(500000, 1000000)]


@st.composite
def items_and_chunk_count(draw):
    xs = draw(st.one_of(st.text(),
                        st.binary(),
                        st.lists(st.integers())))
    n = draw(st.integers(min_value=1,
                         max_value=max(1, len(xs))))
    return xs, n


@ht.given(xs_n=items_and_chunk_count())
def test_evenly_chunked(xs_n):
    '''Verify there are n evenly sized chunks'''
    xs, n = xs_n
    chunks = chunk_iteratools(xs, n)
    assert len(chunks) == n
    chunk_lens = {len(c) for c in chunks}
    assert len(chunk_lens) in {1, 2}
    assert max(chunk_lens) - min(chunk_lens) in {0, 1}


@ht.given(xs_n=items_and_chunk_count())
def test_combining_chunks(xs_n):
    '''Verify recombining the chunks reproduces the original sequence.'''
    xs, n = xs_n
    chunks = chunk_iteratools(xs, n)
    assert functools.reduce(lambda x, y: x+y, chunks) == xs