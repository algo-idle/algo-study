import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
grid = [list(input().rstrip()) for _ in range(N)]
visit = [[-1 for _ in range(M)] for _ in range(N)]

direction = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def sol(x, y, idx):
    global answer
    if visit[x][y] != -1:   # 방문함
        if visit[x][y] == idx:
            answer += 1
        return

    visit[x][y] = idx
    i = direction.index(grid[x][y])
    sol(x + dx[i], y + dy[i], idx)

idx = 0
answer = 0
for n in range(N):
    for m in range(M):
        sol(n, m, idx)
        idx += 1

print(answer)
