import pytest
from solution import calc_equation_by_union_find


def test_given_sample():
    equations = [['a', 'b'], ['b', 'c']]
    values = [2.0, 3.0]
    queries = [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]
    expected = [6.0, 0.5, -1.0, 1.0, -1.0]
    assert expected == calc_equation_by_union_find(equations, values, queries)


def test_bug_in_accumulate_factor_when_find_root_operation():
    equations = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x4'], ['x4', 'x5']]
    values = [3.0, 4.0, 5.0, 6.0]
    queries = [['x1', 'x5'], ['x5', 'x2'], ['x2', 'x4'], ['x2', 'x2'],
               ['x2', 'x9'], ["x9", "x9"]]
    expected = [360.0, 1 / 120, 20.0, 1.0, -1.0, -1.0]
    assert expected == pytest.approx(
        calc_equation_by_union_find(equations, values, queries))


def test_bug_in_factor_calc_in_union():
    equations = [["a", "b"], ["e", "f"], ["b", "e"]]
    values = [3.4, 1.4, 2.3]
    queries = [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"],
               ["a", "c"], ["f", "e"]]
    expected = [1 / 3.4, 3.4 * 1.4 * 2.3, 1.0, 1.0, -1.0, -1.0, 1 / 1.4]
    assert expected == calc_equation_by_union_find(equations, values, queries)


def test_sample_four():
    equations = [["x1", "x2"], ["x2", "x3"], ["x1", "x4"], ["x2", "x5"]]
    values = [3.0, 0.5, 3.4, 5.6]
    queries = [["x2", "x4"], ["x1", "x5"], ["x1", "x3"],
               ["x5", "x5"], ["x5", "x1"], ["x3", "x4"],
               ["x4", "x3"], ["x6", "x6"], ["x0", "x0"]]  # yapf: disable
    expected = [
        3.4 / 3, 16.8, 1.5, 1.0, 1 / 3 / 5.6, 3.4 / 1.5, 1.5 / 3.4, -1.0, -1.0
    ]
    assert expected == pytest.approx(
        calc_equation_by_union_find(equations, values, queries))


def test_sample_five():
    equations = [["a", "e"], ["b", "e"]]
    values = [4.0, 3.0]
    queries = [["a", "b"], ["e", "e"], ["x", "x"]]
    expected = [4 / 3, 1.0, -1.0]
    assert expected == calc_equation_by_union_find(equations, values, queries)
