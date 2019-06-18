from typing import List
from unionfind import UnionFind


def equations_possible_using_union_find(equations: List[str]) -> bool:
    uf = UnionFind()
    for leftvar, op, _, rightvar in equations:
        if op == '=':
            uf.union(leftvar, rightvar)
    return not any(op == '!' and uf.is_connect(l, r)
                   for l, op, _, r in equations)
