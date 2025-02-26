import sys

read = sys.stdin.readline
from collections import deque

dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

while(True):
    L, R, C = map(int, read().split())
    if L == 0 and R == 0 and C == 0:
        break

    building = []
    for _ in range(L):
        building.append([list(read().rstrip()) for _ in range(R)])
        read()

    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    for z in range(L):
        for y in range(R):
            for x in range(C):
                if building[z][y][x] == 'S':
                    start = (z, y, x, 0)
                    visited[z][y][x] = True
                if building[z][y][x] == 'E':
                    end = (z, y, x)

    queue = deque([start])

    isEscaped = False
    while queue:
        z, y, x, count = queue.popleft()

        if (z, y, x) == end:
            isEscaped = True
            print(f'Escaped in {count} minute(s).')
            break

        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < L and 0 <= ny < R and 0 <= nx < C and not visited[nz][ny][nx]:
                if building[nz][ny][nx] != '#':
                    queue.append((nz, ny, nx, count + 1))
                    visited[nz][ny][nx] = True

    if not isEscaped:
        print('Trapped!')