from typing import List


def rm_duplicates(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
        j += 1
    return i + 1
