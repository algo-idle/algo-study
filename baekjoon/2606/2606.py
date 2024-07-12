import sys

read = sys.stdin.readline
N = int(read())
M = int(read())
network = [[] for _ in range(N)]
visited = [0 for _ in range(N)]
for i in range(M):
    start, end = map(int, read().split())
    start -= 1
    end -= 1
    network[start].append(end)
    network[end].append(start)

count = 0
def dfs(num):
    global count
    visited[num] = 1
    for i in network[num]:
        if visited[i] == 0:
            dfs(i)
            count += 1

dfs(0)
print(count)