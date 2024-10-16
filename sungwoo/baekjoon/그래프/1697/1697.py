import sys
from collections import deque

read = sys.stdin.readline
N, K = map(int, read().split())
visited_time = [0] * 100001

que = deque()
que.append(N)
while que:
    n = que.popleft()
    if n == K:
        print(visited_time[n])
        break
    for i in (n-1, n+1, n*2):
        if 0 <= i <= 100000 and not visited_time[i]:
            visited_time[i] = visited_time[n] + 1
            que.append(i)