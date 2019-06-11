class UnionFind:
    def __init__(self, grid):
        self.count = 0
        self.r, self.c = r, c = len(grid), len(grid[0])
        self.parent = [-1] * (r * c)
        self.weight = [0] * (r * c)
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
            if self.weight[proot] > self.weight[qroot]:
                self.parent[proot] = qroot
            elif self.weight[proot] < self.weight[qroot]:
                self.parent[qroot] = proot
            else:
                self.parent[proot] = qroot
                self.weight[q] += 1
            self.count -= 1

    def __str__(self):
        """TODO: visualization for debug and performance checking
        """
        roots = []
        for i in range(self.r * self.c):
            if self.parent[i] == i:
                roots.append("root: %s, %s" % (i // self.c, i % self.c))
        return "%s\ncount: %s\n" % ('\n'.join(roots), self.count)