from typing import List


def rm_dups(nums: List[int]) -> int:
    if len(nums) <= 2:
        return len(nums)
    i = 1
    j = 2
    while j < len(nums):
        if nums[j] > nums[i] or nums[j] > nums[i - 1]:
            i += 1
            nums[i] = nums[j]
        j += 1
    return i + 1

