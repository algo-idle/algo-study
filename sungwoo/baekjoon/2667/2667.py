import sys

read = sys.stdin.readline
from collections import deque

N = int(read())
apt = [list(map(int, list(read().rstrip()))) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()
aptCount = []


def dfs():
    count = 0
    while queue:
        x, y = queue.popleft()
        count += 1
        apt[y][x] = -1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if apt[ny][nx] == 1:
                    apt[ny][nx] = -1
                    queue.append((nx, ny))
    return count


for y in range(N):
    for x in range(N):
        if apt[y][x] == 1:
            queue.append((x, y))
            aptCount.append(dfs())

aptCount.sort()
print(len(aptCount))
print(*aptCount, sep='\n')