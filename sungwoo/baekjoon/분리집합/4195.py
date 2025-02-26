import sys

read = sys.stdin.readline

N = int(read())

class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]

        return self.size[self.find(x)]

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1


for _ in range(N):
    F = int(read())
    ds = DisjointSet()

    for _ in range(F):
        x, y = map(str, read().split())
        ds.add(x), ds.add(y)
        print((ds.union(x, y)))
