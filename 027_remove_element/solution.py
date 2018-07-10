from typing import List


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
