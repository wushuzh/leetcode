from solution import find_peak_element_v1, find_peak_element_v2, find_peak_element_v3


def test_single_element():
    assert 0 == find_peak_element_v1([1])
    assert 0 == find_peak_element_v2([1])
    assert 0 == find_peak_element_v3([1])


def test_two_element_later_peak():
    assert 1 == find_peak_element_v1([0, 1])
    assert 1 == find_peak_element_v2([0, 1])
    assert 1 == find_peak_element_v3([0, 1])


def test_two_element_first_peak():
    assert 0 == find_peak_element_v1([1, 0])
    assert 0 == find_peak_element_v2([1, 0])
    assert 0 == find_peak_element_v3([1, 0])


def test_3_elements_first_peak():
    assert 0 == find_peak_element_v1([3, 2, 1])
    assert 0 == find_peak_element_v2([3, 2, 1])
    assert 0 == find_peak_element_v3([3, 2, 1])


def test_3_elements_mid_peak():
    assert 1 == find_peak_element_v1([1, 3, 2])
    assert 1 == find_peak_element_v2([1, 3, 2])
    assert 1 == find_peak_element_v3([1, 3, 2])


def test_3_elements_last_peak():
    assert 2 == find_peak_element_v1([1, 2, 3])
    assert 2 == find_peak_element_v2([1, 2, 3])
    assert 2 == find_peak_element_v3([1, 2, 3])
