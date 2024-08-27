from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solution(maps):
    height = len(maps)
    width = len(maps[0])
    memo = [[999 for _ in range(width)] for _ in range(height)]
    memo[0][0] = 1
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        val = memo[y][x]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < width and 0 <= ny < height:
                if maps[ny][nx] == 1 and val + 1 < memo[ny][nx]:
                    memo[ny][nx] = val + 1
                    queue.append((nx, ny))
    answer = memo[height - 1][width - 1] if memo[height - 1][width - 1] != 999 else -1
    return answer


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))