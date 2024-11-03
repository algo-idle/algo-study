import sys
input = sys.stdin.readline

G = int(input().rstrip())
P = int(input().rstrip())
g = [int(input().rstrip()) for _ in range(P)]
parent = [i for i in range(P + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


print(*enumerate(g))
print(*enumerate(parent))
