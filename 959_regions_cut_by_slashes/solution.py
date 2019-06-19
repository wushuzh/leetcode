from typing import List
from unionfind import UnionFind


def regions_by_slashes_using_union_find(grid: List[str]) -> int:
    if not grid:
        return 0

    uf = UnionFind(grid)
    N = len(grid)

    for i, row in enumerate(grid):
        for j, slash in enumerate(row):
            ijIdx = 4 * (i * N + j)
            #    1
            # 0     3
            #    2
            if slash == '/':
                uf.union(ijIdx + 0, ijIdx + 1)
                uf.union(ijIdx + 2, ijIdx + 3)
            elif slash == '\\':
                uf.union(ijIdx + 0, ijIdx + 2)
                uf.union(ijIdx + 1, ijIdx + 3)
            else:
                uf.union(ijIdx, ijIdx + 1)
                uf.union(ijIdx, ijIdx + 2)
                uf.union(ijIdx, ijIdx + 3)

            # union down 1/4 cell except last row N - 1
            if i < N - 1:
                uf.union(ijIdx + 2, ijIdx + 4 * N + 1)

            # union up 1/4 cell except first row 0
            if i >= 1:
                uf.union(ijIdx + 1, ijIdx - 4 * N + 2)

            # union right 1/4 cell except first column N - 1
            if j < N - 1:
                uf.union(ijIdx + 3, ijIdx + 4)

            # union left 1/4 cell except last column 0
            if j >= 1:
                uf.union(ijIdx + 0, ijIdx - 1)

    return sum(uf.find_root(i) == i for i in range(4 * N * N))
