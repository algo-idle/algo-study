from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
cheese = [list(map(int, input().rstrip().split())) for _ in range(N)]

res = 0

def find_side():
    q = deque([(0, 0)])
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True
    while q:
        x, y = q.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if cheese[nx][ny] == 0:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                elif cheese[nx][ny] >= 1:
                    cheese[nx][ny] += 1

res = 0
while True:
    find_side()
    for i in range(N):
        for j in range(M):
            if cheese[i][j] >= 3:
                cheese[i][j] = 0
            elif 0 < cheese[i][j] <= 2:
                cheese[i][j] = 1
    res += 1
    if sum([sum(c) for c in cheese]) == 0:
        break

print(res)
