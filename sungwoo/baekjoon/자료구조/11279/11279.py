import sys
read = sys.stdin.readline
import heapq

N = int(read())
heap = []
for _ in range(N):
    x = int(read())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)