class UnionFind():
    def __init__(self, nums):
        length = len(nums)
        self.parent = list(range(length))
        self.nodesNum = [1] * length

    def find_root(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find_root(self.parent[i])
        return self.parent[i]

    def union(self, p, q):
        proot = self.find_root(p)
        qroot = self.find_root(q)
        if proot != qroot:
            if self.nodesNum[proot] > self.nodesNum[qroot]:
                self.parent[proot] = qroot
                self.nodesNum[qroot] += self.nodesNum[proot]
            else:
                self.parent[qroot] = proot
                self.nodesNum[proot] += self.nodesNum[qroot]

    def largest_one_union(self):
        return max(self.nodesNum)

    def __str__(self):
        roots = [p for p in self.parent if self.parent[p] == p]
        return "\nroots:%s\nPaIdx:%s\nnodeN:%s" % (roots, self.parent,
                                                   self.nodesNum)
