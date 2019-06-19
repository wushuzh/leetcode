from typing import List
from unionfind import UnionFind


def rm_stones_using_union_find(stones: List[List[int]]) -> int:
    if not stones:
        return 0

    uf = UnionFind()
    for x, y in stones:
        for i, j in stones:
            if x == i or y == j:
                uf.union(10000 * x + y, 10000 * i + j)

    return len(uf.p) - len({uf.find_root(10000 * x + y) for x, y in stones})


def rm_stones_using_union_find_simple_view(stones):
    uf = UnionFind()
    for x, y in stones:
        uf.union(x, 10000 + y)

    return len(stones) - len({uf.find_root(i) for i, _ in stones})
