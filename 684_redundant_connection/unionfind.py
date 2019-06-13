class UnionFind:
    def __init__(self, num):
        self.parent = {i: i for i in range(1, num + 1)}

    def find_root(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find_root(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        xRoot = self.find_root(x)
        yRoot = self.find_root(y)
        if xRoot != yRoot:
            self.parent[yRoot] = xRoot
            return True
        else:
            return False
