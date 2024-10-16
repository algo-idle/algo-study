import sys
from collections import deque
read = sys.stdin.readline

M, N, H = map(int, read().split())
container = []
for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, input().split())))
    container.append(temp)

dh = [1, -1, 0, 0, 0, 0]
dn = [0, 0, 1, -1, 0, 0]
dm = [0, 0, 0, 0, 1, -1]
queue = deque()

def bfs():
    while queue:
        h, n, m = queue.popleft()
        for i in range(6):
            nh, nn, nm = h + dh[i], n + dn[i], m + dm[i]
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
                if container[nh][nn][nm] == 0:
                    container[nh][nn][nm] = container[h][n][m] + 1
                    queue.append((nh, nn, nm))

def tomato():
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if container[h][n][m] == 1:
                    queue.append((h, n, m))
    bfs()
    flag = False
    day = 0
    for h in range(H):
        if not flag:
            for n in range(N):
                if not flag:
                    for m in range(M):
                        if container[h][n][m] == 0:
                            day = 0
                            flag = True
                            break
                        day = max(day, container[h][n][m])

    return day - 1

print(tomato())