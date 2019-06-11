class UnionFind:
    def __init__(self, grid):
        self.count = 0
        r, c = len(grid), len(grid[0])
        self.parent = [-1] * (r * c)
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    self.parent[i * c + j] = i * c + j
                    self.count += 1

    def find_root(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find_root(self.parent[i])
        return self.parent[i]

    def union(self, p, q):
        proot = self.find_root(p)
        qroot = self.find_root(q)
        if proot != qroot:
            self.parent[proot] = qroot
            self.count -= 1

    def __str__(self):
        return 'TODO: show internal data for debug'