import heapq
import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
graph = [[0 if i == j else 1e9 for j in range(N + 1)] for i in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().strip().split())
    graph[a][b] = min(graph[a][b], c)

start, end = map(int, input().strip().split())

def dijkstra(start, end):
    distance = [[1e9, []] for _ in range(N + 1)]
    distance[start] = [0, [start]]
    heap = []
    heapq.heappush(heap, (0, start, [start]))
    while heap:
        dist, now, path = heapq.heappop(heap)
        if dist > distance[now][0]:
            continue
        for next in range(len(graph[now])):
            cost = dist + graph[now][next]
            if cost < distance[next][0]:
                distance[next] = [cost, path + [next]]
                heapq.heappush(heap, (cost, next, path + [next]))

    return distance[end]

cost, path = dijkstra(start, end)
print(cost, len(path), ' '.join(map(str, path)), sep='\n')