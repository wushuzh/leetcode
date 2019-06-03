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


def find_peak_element_v2(nums: List[int]) -> int:
    def search(nums: List[int], l: int, r: int) -> int:
        if (l == r):
            return l
        m = (l + r) // 2
        if (nums[m] > nums[m + 1]):
            return search(nums, l, m)
        return search(nums, m + 1, r)

    return search(nums, 0, len(nums) - 1)


def find_peak_element_v3(nums: List[int]) -> int:
    l: int = 0
    r: int = len(nums) - 1
    while (l < r):
        m = (l + r) // 2
        if (nums[m] < nums[m + 1]):
            l = m + 1
        else:
            r = m
    return l
