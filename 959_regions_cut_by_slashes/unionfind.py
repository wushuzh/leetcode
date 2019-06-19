class UnionFind:
    def __init__(self, grid):
        self.length = len(grid)
        self.parent = list(range(4 * self.length * self.length))

    def find_root(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find_root(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        xRoot = self.find_root(x)
        yRoot = self.find_root(y)
        if xRoot != yRoot:
            self.parent[xRoot] = yRoot