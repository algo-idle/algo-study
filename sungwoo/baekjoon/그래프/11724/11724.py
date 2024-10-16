import sys
read = sys.stdin.readline

N, M = map(int, read().split())
edge = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, read().split())
    edge[u].append(v)
    edge[v].append(u)


def bfs(edge, visited, u):
    queue = [u]
    visited[u] = True
    while queue:
        start = queue.pop(0)
        for v in edge[start]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True


visited = [False for _ in range(N + 1)]
count = 0
for u in range(1, N + 1):
    if not visited[u]:
        bfs(edge, visited, u)
        count += 1
print(count)
