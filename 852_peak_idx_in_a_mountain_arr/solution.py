from typing import List


def peak_idx_in_mountain_arr_recursive(A: List[int]) -> int:
    def search(nums, l, r):
        if l == r:
            return l
        m = (l + r) // 2
        if nums[m] > nums[m + 1]:
            return search(nums, l, m)
        return search(nums, m + 1, r)

    return search(A, 0, len(A) - 1)


def peak_idx_in_mountain_arr_iterative(A: List[int]) -> int:
    l = 0
    r = len(A) - 1
    while l < r:
        m = (l + r) // 2
        if A[m] > A[m + 1]:
            r = m
        else:
            l = m + 1

    return l
