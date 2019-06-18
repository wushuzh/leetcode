class UnionFind:
    def __init__(self):
        self.parent = dict()

    def find_root(self, i):
        if not self.parent.get(i):
            self.parent[i] = i
        elif self.parent[i] != i:
            self.parent[i] = self.find_root(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        xRoot = self.find_root(x)
        yRoot = self.find_root(y)
        if xRoot != yRoot:
            self.parent[xRoot] = yRoot

    def is_connect(self, x, y):
        return self.find_root(x) == self.find_root(y)