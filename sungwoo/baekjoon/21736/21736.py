import sys
read = sys.stdin.readline
from collections import deque

N, M = map(int, read().split())
campus = []
for _ in range(N):
    campus.append(list(str(read().rstrip())))

queue = deque()
for y in range(N):
    for x in range(M):
        if campus[y][x] == 'I':
            queue.append((x, y))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
friend = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if campus[ny][nx] == 'X':
                continue
            elif campus[ny][nx] == 'P':
                friend += 1
            campus[ny][nx] = 'X'
            queue.append((nx, ny))

print(friend if friend != 0 else 'TT')