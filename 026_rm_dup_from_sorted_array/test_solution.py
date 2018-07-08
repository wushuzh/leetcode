from typing import List


def rm_duplicates(nums: List[int]) -> int:
    if len(nums) <= 1:
        return len(nums)
    i = 0
    j = 1
    while j < len(nums):
        if nums[j] > nums[i]:
            i += 1
            nums[i] = nums[j]
        j += 1
    return i + 1


def test_empty():
    a = []
    assert rm_duplicates(a) == 0


def test_one():
    a = [1]
    assert rm_duplicates(a) == 1
    assert a == [1]


def test_no_dups():
    a = [1, 2, 3]
    assert rm_duplicates(a) == 3
    assert a == [1, 2, 3]


def test_dups():
    a = [1, 2, 2, 3, 4, 4, 5]
    assert rm_duplicates(a) == 5
    assert a[:5] == [1, 2, 3, 4, 5]
