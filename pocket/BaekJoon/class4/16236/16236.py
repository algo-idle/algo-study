from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
grid = [list(map(int, input().rstrip().split())) for _ in range(N)]
baby = [(x, y) for x in range(N) for y in range(N) if grid[x][y] == 9][-1]
size = 2
grid[baby[0]][baby[1]] = 0

def find_can_eat(x, y, size):
    can_eat = []
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[x][y] = 0
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        if 0 < grid[x][y] < size:
            can_eat.append((visited[x][y], x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] <= size and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return can_eat

res = 0
cnt = 0
while True:
    can_eat = find_can_eat(baby[0], baby[1], size)
    if can_eat:
        can_eat = min(can_eat, key=lambda x: (x[0], x[1], x[2]))
        baby = (can_eat[1], can_eat[2])
        res += can_eat[0]
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0
        grid[can_eat[1]][can_eat[2]] = 0
    else:
        print(res)
        break
