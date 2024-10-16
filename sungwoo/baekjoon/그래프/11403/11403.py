import sys
read = sys.stdin.readline

N = int(read())
routes = [list(map(int, read().split())) for _ in range(N)]

for i in range(N):
    for x in range(N):
        for y in range(N):
            if routes[x][y] == 0 and routes[x][i] and routes[i][y]:
                routes[x][y] = 1

for i in routes:
    print(*i, sep=' ')