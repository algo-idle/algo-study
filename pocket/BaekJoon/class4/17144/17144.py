from collections import deque
import sys
input = sys.stdin.readline

N, M, T = map(int, input().rstrip().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(N)]
air_pu = [(i, j) for i in range(N) for j in range(M) if grid[i][j] == -1]

for _ in range(T):
    q = deque([(i, j) for i in range(N) for j in range(M) if grid[i][j] not in [-1, 0]])
    res = []
    while q:
        x, y = q.popleft()
        can_go = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] != -1:
                    can_go.append((nx, ny))
        for nx, ny in can_go:
            res.append((nx, ny, grid[x][y] // 5))
        grid[x][y] -= (grid[x][y] // 5) * len(can_go)
    for i, j, cost in res:
        grid[i][j] += cost
    grid[air_pu[0][0] - 1][0] = 0
    for i in range(air_pu[0][0] - 1, 0, -1):
        grid[i][0] = grid[i - 1][0]
        grid[i - 1][0] = 0
    for i in range(M - 1):
        grid[0][i] = grid[0][i + 1]
        grid[0][i + 1] = 0
    for i in range(air_pu[0][0]):
        grid[i][-1] = grid[i + 1][-1]
        grid[i + 1][-1] = 0
    for i in range(M - 1, 1, -1):
        grid[air_pu[0][0]][i] = grid[air_pu[0][0]][i - 1]
        grid[air_pu[0][0]][i - 1] = 0

    grid[air_pu[1][0] + 1][0] = 0
    for i in range(air_pu[1][0] + 1, N - 1):
        grid[i][0] = grid[i + 1][0]
        grid[i + 1][0] = 0
    for i in range(M - 1):
        grid[-1][i] = grid[-1][i + 1]
        grid[-1][i + 1] = 0
    for i in range(N - 1, air_pu[1][0], -1):
        grid[i][-1] = grid[i - 1][-1]
        grid[i - 1][-1] = 0
    for i in range(M - 1, 1, -1):
        grid[air_pu[1][0]][i] = grid[air_pu[1][0]][i - 1]
        grid[air_pu[1][0]][i - 1] = 0

print(sum([sum(grid[i]) for i in range(N)]) + 2)
