from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]
start = [(i, j) for i in range(N) for j in range(M) if board[i][j] == 2]

def bfs():
    q = deque(start)
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i, j in start:
        visited[i][j] = True
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and board[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True
    res = sum([1 for i in range(N) for j in range(M) if board[i][j] == 0 and not visited[i][j]])
    return res


ans = 0
def dfs(cnt):
    global ans
    if cnt == 3:
        ans = max(ans, bfs())
    else:
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    board[i][j] = 1
                    dfs(cnt + 1)
                    board[i][j] = 0

dfs(0)
print(ans)
