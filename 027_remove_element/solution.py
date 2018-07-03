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
