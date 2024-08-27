import heapq
import sys
input = sys.stdin.readline

n, m, r = map(int, input().rstrip().split())
items = list(map(int, input().rstrip().split()))
graph = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]

for _ in range(r):
    a, b, c = map(int, input().rstrip().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)
    graph[b - 1][a - 1] = min(graph[b - 1][a - 1], c)

def dijkstra(start):
    distance = [float('inf') for i in range(n)]
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in range(n):
            cost = dist + graph[now][i]
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(heap, (cost, i))
    return distance

answer = 0
for i in range(n):
    buf = dijkstra(i)
    answer = max(answer, sum([items[i] for i in range(len(buf)) if buf[i] <= m]))

print(answer)

