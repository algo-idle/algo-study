import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().rstrip().split())
graph = {i: {} for i in range(N)}
for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    a -= 1
    b -= 1
    try:
        graph[a][b] = min(graph[a][b], c)
    except:
        graph[a][b] = c


def dijkstra(start, end):
    distance = [float('inf') for _ in range(N)]
    distance[start] = 0
    h = []
    heapq.heappush(h, (0, start))
    while h:
        dist, now = heapq.heappop(h)
        if dist > distance[now]:
            continue
        for next in graph[now]:
            cost = dist + graph[now][next]
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(h, (cost, next))
    return distance[end]


ans = 0
for i in range(N):
    ans = max(ans, dijkstra(i, X - 1) + dijkstra(X - 1, i))

print(ans)


