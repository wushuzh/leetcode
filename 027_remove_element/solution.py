from typing import List


def deprecated_rm_elem(nums: List[int], val: int) -> int:
    for i in nums[:]:
        if i == val:
            nums.remove(val)
    return len(nums)
