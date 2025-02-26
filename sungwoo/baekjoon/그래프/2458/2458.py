import sys
read = sys.stdin.readline
from collections import defaultdict

N, M = map(int, read().split())

bigger = defaultdict(set)
smaller = defaultdict(set)

for _ in range(M):
    x, y = map(int, read().split())
    bigger[x].add(y)
    smaller[y].add(x)

def dfs(i, flag):
    if flag:
        for j in bigger[i]:
            if visited[j] == 0:
                visited[j] = 1
                dfs(j, flag)
    else:
        for j in smaller[i]:
            if visited[j] == 0:
                visited[j] = 1
                dfs(j, flag)

result = 0
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    visited[i] = 1
    dfs(i, True)
    dfs(i, False)

    if sum(visited) == N:
        result += 1

print(result)