from typing import List
from unionfind import UnionFind


def find_num_islands_with_uf(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    uf = UnionFind(grid)
    r, c = len(grid), len(grid[0])
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '1':
                # check its right neighbor till right bound
                if j + 1 < c and grid[i][j + 1] == '1':
                    uf.union(i * c + j, i * c + j + 1)
                # check its down neighbor till down bound
                if i + 1 < r and grid[i + 1][j] == '1':
                    uf.union(i * c + j, c * (i + 1) + j)
    return uf.count