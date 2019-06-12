class UnionFind():
    def __init__(self, equations):
        self.parent = dict()
        self.factor = dict()
        for i in set([x for e in equations for x in e]):
            self.parent[i] = i
            self.factor[i] = 1.0

    def find_root(self, i):
        if self.parent.get(i) is None:
            return None
        if self.parent[i] != i:
            # accumulate_factor case
            to_be_replaced_parent = self.parent[i]
            self.parent[i] = self.find_root(self.parent[i])
            self.factor[i] *= self.factor[to_be_replaced_parent]
        return self.parent[i]

    def union(self, x, y, v):
        xRoot = self.find_root(x)
        yRoot = self.find_root(y)
        if xRoot != yRoot:
            if yRoot == y:
                # case 5
                self.parent[y] = x
                self.factor[y] = 1 / v
            else:
                # case 4
                self.parent[x] = y
                self.factor[x] = v
