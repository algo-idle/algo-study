import sys
read = sys.stdin.readline
from collections import deque

T = int(read())

for _ in range(T):
    A, B = map(int, read().split())
    visited = [False for _ in range(10000)]
    queue = deque()
    queue.append((A, ''))
    visited[A] = True
    while queue:
        num, command = queue.popleft()
        if num == B:
            print(command)
            break
        D = ['D', num * 2 % 10000]
        S = ['S', num - 1 if num != 0 else 9999]
        L = ['L', num // 1000 + (num % 1000) * 10]
        R = ['R', (num % 10) * 1000 + num // 10]
        for i in (D, S, L, R):
            if not visited[i[1]]:
                queue.append((i[1], command + i[0]))
                visited[i[1]] = True
