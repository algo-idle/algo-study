from collections import deque
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True
    q = deque([(0, 0, 1)])

    while q:
        x, y, cnt = q.popleft()

        if (x, y) == (N - 1, M - 1):
            return cnt

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1))
    return -1
