from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())

def bfs(start):
    visited = [False for _ in range(start + 1)]
    visited[start] = True

    q = deque([(start, [start])])

    while q:
        n, path = q.popleft()

        if n == 1:
            print(len(path) - 1)
            print(*path)
            exit(0)

        if n // 3 >= 1 and n % 3 == 0 and not visited[n // 3]:
            visited[n // 3] = True
            q.append((n // 3, path + [n // 3]))

        if n // 2 >= 1 and n % 2 == 0 and not visited[n // 2]:
            visited[n // 2] = True
            q.append((n // 2, path + [n // 2]))

        if n - 1 >= 1 and not visited[n - 1]:
             visited[n - 1] = True
             q.append((n - 1, path + [n - 1]))

bfs(N)
