from typing import List
import pytest


def deprecated_rm_elem(nums: List[int], val: int) -> int:
    for i in nums[:]:
        if i == val:
            nums.remove(val)
    return len(nums)


def rm_elem_2_points(nums: List[int], val: int) -> int:
    i = j = 0
    while j < len(nums):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
        j += 1
    return i


def rm_elem_swap(nums: List[int], val: int) -> int:
    i = 0
    n = len(nums)
    while i < n:
        if (nums[i] == val):
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1
    return n


@pytest.fixture(params=[deprecated_rm_elem, rm_elem_2_points, rm_elem_swap])
def diff_solution(request):
    return request.param


def test_empty(diff_solution):
    assert diff_solution([], 1) == 0


def test_one_keep(diff_solution):
    a = [1]
    assert diff_solution(a, 2) == 1
    assert a == [1]


def test_one_rm(diff_solution):
    a = [1]
    assert diff_solution(a, 1) == 0


def test_multi_rm_first(diff_solution):
    a = [1, 2, 2]
    assert diff_solution(a, 1) == 2
    assert a[:2] == [2, 2]


def test_multi_rm_mid(diff_solution):
    a = [1, 2, 3]
    assert diff_solution(a, 2) == 2
    assert a[:2] == [1, 3]


def test_multi_rm_all(diff_solution):
    a = [1, 1, 1]
    assert diff_solution(a, 1) == 0


def test_multi_left_last(diff_solution):
    a = [2, 2, 1]
    assert diff_solution(a, 1) == 2
    assert a[:2] == [2, 2]
