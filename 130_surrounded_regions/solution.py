from typing import List
from unionfind import UnionFind


def flip_inside_O_by_UF(board: List[List[str]]) -> None:
    if not board:
        board = []
        return

    uf = UnionFind(board)
    dummyIdx = uf.r * uf.c

    for i in range(uf.r):
        for j in range(uf.c):
            if board[i][j] == 'O':
                ijIdx = i * uf.c + j
                # connect all boundary nodes to the ONE dummy node
                if i in (0, uf.r - 1) or j in (0, uf.c - 1):
                    uf.union(ijIdx, dummyIdx)
                # check its right neighbor is connected ?
                if j + 1 < uf.c and board[i][j + 1] == 'O':
                    uf.union(ijIdx, ijIdx + 1)
                # check its down neighbor is connected ?
                if i + 1 < uf.r and board[i + 1][j] == 'O':
                    uf.union(ijIdx, ijIdx + uf.c)

    for i in range(uf.r):
        for j in range(uf.c):
            if uf.find_root(i * uf.c + j) != uf.find_root(uf.dummyIdx):
                board[i][j] = 'X'
