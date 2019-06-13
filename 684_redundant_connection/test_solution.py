from solution import find_redundant_conn_by_union_find


def test_sample_1():
    graph = [[1, 2], [1, 3], [2, 3]]
    expected_edge = [2, 3]
    assert expected_edge == find_redundant_conn_by_union_find(graph)


def test_sample_2():
    graph = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    expected_edge = [1, 4]
    assert expected_edge == find_redundant_conn_by_union_find(graph)
