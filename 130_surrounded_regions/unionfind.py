class UnionFind:
    def __init__(self, board):
        self.r, self.c = len(board), len(board[0])
        self.dummyIdx = self.r * self.c
        self.parent = list(range(self.dummyIdx)) + [self.dummyIdx]
        for i in range(self.r):
            for j in range(self.c):
                if board[i][j] == 'O':
                    self.parent[i * self.c + j] = i * self.c + j

    def find_root(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find_root(self.parent[i])
        return self.parent[i]

    def union(self, p, q):
        pRoot = self.find_root(p)
        qRoot = self.find_root(q)
        if pRoot != qRoot:
            # put p as child of q
            self.parent[pRoot] = qRoot
