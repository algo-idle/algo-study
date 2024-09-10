import sys
input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
edges = [list(map(int, input().rstrip().split())) for _ in range(E)]
parent = [i for i in range(V + 1)]
edges.sort(key=lambda x: x[2])

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

def union(x, y):
    if x > y:
        x, y = y, x
    px, py = find(x), find(y)
    if px < py:
        parent[px] = py
    else:
        parent[py] = px

res = 0
for u, v, cost in edges:
    if find(u) != find(v):
        union(u, v)
        res += cost

print(res)
