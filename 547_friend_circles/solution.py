from typing import List
from unionfind import UnionFind


def find_circle_num_using_union_find(M: List[List[int]]) -> int:
    uf = UnionFind(len(M))
    for i in range(uf.num):
        # ignore upper-right triangle in matrix
        for j in range(0, i):
            if M[i][j] == 1:
                uf.union(i, j)

    return len([1 for i, v in enumerate(uf.parent) if i == v])