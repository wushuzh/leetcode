class UnionFind:
    def __init__(self):
        self.p = dict()

    def find_root(self, i):
        if not self.p.get(i):
            self.p[i] = i
        elif self.p[i] != i:
            self.p[i] = self.find_root(self.p[i])
        return self.p[i]

    def union(self, x, y):
        xRoot = self.find_root(x)
        yRoot = self.find_root(y)
        if xRoot != yRoot:
            self.p[xRoot] = yRoot