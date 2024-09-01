import sys
read = sys.stdin.readline
from collections import deque

N, M = map(int, read().split())
relation = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, read().split())
    relation[a].append(b)
    relation[b].append(a)

queue = deque()
min_val = sys.maxsize
result = 0
for i in range(1, N + 1):
    count = [0 for _ in range(N + 1)]
    visited = [i]
    queue.append(i)
    while queue:
        a = queue.popleft()
        for j in relation[a]:
            if j not in visited:
                count[j] = count[a] + 1
                visited.append(j)
                queue.append(j)
    if sum(count) < min_val:
        min_val = sum(count)
        result = i
print(result)
