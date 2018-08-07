import pytest

from solution import chunk


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