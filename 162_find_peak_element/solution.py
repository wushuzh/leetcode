from typing import List


def find_peak_element_v1(nums: List[int]) -> int:
    length = len(nums)
    if (length == 1):
        return 0
    if (length == 2):
        return 1 if nums[0] < nums[1] else 0

    m = length // 2
    if nums[m] >= nums[m - 1] and nums[m] > nums[m + 1]:
        return m
    elif nums[m - 1] > nums[m]:
        return find_peak_element_v1(nums[:m])
    elif nums[m] < nums[m + 1]:
        return m + 1 + find_peak_element_v1(nums[m + 1:])
