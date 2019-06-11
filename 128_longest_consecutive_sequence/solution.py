from typing import List
from unionfind import UnionFind


def longest_consecutive_by_uf(nums: List[int]) -> int:
    if not nums:
        return 0

    uf = UnionFind(nums)
    valToIdx = {nums[i]: i for i in range(len(nums))}
    for v in valToIdx.keys():
        # When get value == 0, which is false,
        # so always check None instead of false,
        #   otherwise may cause union operations is missing
        if valToIdx.get(v + 1) is not None:
            uf.union(valToIdx[v], valToIdx[v + 1])
            print("union %s and %s" % (valToIdx[v], valToIdx[v + 1]))
    return uf.largest_one_union()
