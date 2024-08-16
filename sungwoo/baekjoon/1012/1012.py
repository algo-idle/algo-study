import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

T = int(read())
def dfs(x, y):
    if x < 0 or y < 0 or x >= M or y >= N:
        return False
    if field[x][y] == 1:
        field[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for _ in range(T):
    M, N, K = map(int, read().split())
    field = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, read().split())
        field[x][y] = 1
    worm = 0
    for x in range(M):
        for y in range(N):
            if dfs(x, y):
                worm += 1
    print(worm)