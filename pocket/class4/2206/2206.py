from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
grid = [list(map(int, list(input().rstrip()))) for _ in range(N)]

def bfs(x, y, ex, ey):
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[x][y] = True

    q = deque([(x, y, True, 1)])

    while q:
        x, y, possible, cnt = q.popleft()
        if x == ex and y == ey:
            return cnt

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if grid[nx][ny] == 1:
                        if possible:
                            visited[nx][ny] = True
                            q.append((nx, ny, False, cnt + 1))
                    else:
                        visited[nx][ny] = True
                        q.append((nx, ny, possible, cnt + 1))

res1 = bfs(0, 0, N - 1, M - 1)
res2 = bfs(N - 1, M - 1, 0, 0)

if res1 is None and res2 is not None:
    print(res2)
elif res1 is not None and res2 is None:
    print(res1)
elif res1 is None and res2 is None:
    print(-1)
else:
    print(min(res1, res2))

