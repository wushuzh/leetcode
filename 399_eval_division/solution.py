from typing import List
from unionfind import UnionFind


def calc_equation_by_union_find(equations: List[List[str]],
                                values: List[float],
                                queries: List[List[str]]) -> List[float]:

    uf = UnionFind(equations)
    for i, e in enumerate(equations):
        numer, deno = e
        factor = values[i]
        uf.union(numer, deno, factor)

    ans = []
    for x, y in queries:
        xRoot = uf.find_root(x)
        yRoot = uf.find_root(y)
        # new variable not exist in equations, result must -1.0
        if None in (xRoot, yRoot):
            ans.append(-1.0)
        else:
            if xRoot != yRoot:
                ans.append(-1.0)
            else:
                ans.append(uf.factor[x] / uf.factor[y])

    return ans
