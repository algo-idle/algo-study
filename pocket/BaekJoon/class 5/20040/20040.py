import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
edges = [list(map(int, input().rstrip().split())) for _ in range(M)]
parent = [_ for _ in range(N)]

def find(x):
    if parent[x] == x:
        return parent[x]
    return find(parent[x])

def union(x, y):
    x, y = find(x), find(y)
    if x <= y:
        parent[y] = x
    else:
        parent[x] = y

res = 0
for i in range(M):
    if find(edges[i][0]) == find(edges[i][1]):
        res = max(res, i + 1)
        break
    union(edges[i][0], edges[i][1])

print(res)

