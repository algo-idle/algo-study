import sys
read = sys.stdin.readline
import heapq

N = int(read())
posHeap, negHeap = [], []
for _ in range(N):
    x = int(read())
    if x == 0:
        if posHeap and negHeap:
            a = heapq.heappop(posHeap)
            b = heapq.heappop(negHeap)
            if abs(a) < abs(b):
                heapq.heappush(negHeap, b)
                print(a)
            else:
                heapq.heappush(posHeap, a)
                print(-b)
        elif posHeap:
            print(heapq.heappop(posHeap))
        elif negHeap:
            print(-heapq.heappop(negHeap))
        else:
            print(0)
    elif x > 0:
        heapq.heappush(posHeap, x)
    else:
        heapq.heappush(negHeap, -x)