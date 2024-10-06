from collections import deque
import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
jewels = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
bag = [int(input().rstrip()) for _ in range(K)]
res = 0

jewels.sort()
bag.sort()

h = []

for i in range(K):
    while jewels and bag[i] >= jewels[0][0]:
        heapq.heappush(h, -jewels[0][1])
        heapq.heappop(jewels)
    if h:
        res -= heapq.heappop(h)

print(res)
