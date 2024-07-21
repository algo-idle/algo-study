import sys
input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
grid = [list(input().rstrip()) for _ in range(R)]

def bfs(_grid, x, y):
    res = 1
    q = set()
    q.add((x, y, _grid[x][y]))

    while q:
        x, y, s = q.pop()
        res = max(res, len(s))

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and _grid[nx][ny] not in s:
                q.add((nx, ny, s + _grid[nx][ny]))

    return res

print(bfs(grid, 0, 0))
