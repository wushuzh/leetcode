from typing import List
from unionfind import UnionFind


def find_redundant_conn_by_union_find(edges: List[List[int]]) -> List[int]:
    uf = UnionFind(len(edges))
    for a, b in edges:
        if not uf.union(a, b):
            return [a, b]
