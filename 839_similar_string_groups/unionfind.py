class UnionFind:
    def __init__(self, A):
        self.p = {w: w for w in A}
        self.sz = {w: 1 for w in A}

    def find_root(self, i):
        while self.p[i] != i:
            self.p[i] = self.p[self.p[i]]
            i = self.p[i]
        return i

    def union(self, x, y):
        xRoot = self.find_root(x)
        yRoot = self.find_root(y)
        if xRoot != yRoot:
            if self.sz[xRoot] > self.sz[xRoot]:
                self.p[yRoot] = xRoot
                self.sz[xRoot] += self.sz[yRoot]
            else:
                self.p[xRoot] = yRoot
                self.sz[yRoot] += self.sz[xRoot]