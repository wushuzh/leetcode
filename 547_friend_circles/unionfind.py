class UnionFind:
    def __init__(self, num):
        self.num = num
        self.parent = list(range(num))

    def find_root(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find_root(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        xRoot = self.find_root(x)
        yRoot = self.find_root(y)
        if xRoot != yRoot:
            self.parent[xRoot] = yRoot
