from typing import List
from unionfind import UnionFind


def num_similiar_groups_using_union_find(A: List[str]) -> int:
    def is_similiar(w1, w2):
        cnt = 0
        for i1, i2 in zip(w1, w2):
            cnt += (i1 != i2)
            if cnt > 2:
                return False
        return cnt == 2

    uf = UnionFind(A)

    strlen, wordlen = len(A[0]), len(A)
    if wordlen < strlen * strlen:
        for i, w1 in enumerate(A[:-1]):
            for w2 in A[i + 1:]:
                if is_similiar(w1, w2):
                    uf.union(w1, w2)
    else:
        given_words = set(A)
        for w in given_words:
            for i in range(strlen):
                for j in range(i + 1, strlen):
                    new = w[:i] + w[j] + w[i + 1:j] + w[i] + w[j + 1:]
                    if new in given_words:
                        uf.union(w, new)

    return len({uf.find_root(w) for w in uf.p})
