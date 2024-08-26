import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

dist = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    dist[a - 1][b - 1] = min(dist[a - 1][b - 1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for d in dist:
    print(' '.join(map(str, [_d if _d != float('inf') else 0 for _d in d])))
