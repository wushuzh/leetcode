import collections


class UnionFind:
    def __init__(self):
        self.parent = dict()

    def find_root(self, i):
        if self.parent.get(i) is None:
            self.parent[i] = i
        elif self.parent[i] != i:
            self.parent[i] = self.find_root(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        xRoot = self.find_root(x)
        yRoot = self.find_root(y)
        if xRoot != yRoot:
            self.parent[xRoot] = yRoot

    def groups(self):
        merge_accounts = collections.defaultdict(list)
        for email in self.parent.keys():
            merge_accounts[self.find_root(email)].append(email)
        return merge_accounts
