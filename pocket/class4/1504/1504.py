import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().rstrip().split())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

node1, node2 = map(int, input().rstrip().split())

def dijkstra(graph, start, end):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    q = []
    heapq.heappush(q, [0, start])

    while q:
        curr_dist, curr_dest = heapq.heappop(q)
        if distances[curr_dest] < curr_dist:
            continue

        for new_dest, new_dist in graph[curr_dest]:
            dist = curr_dist + new_dist
            if dist < distances[new_dest]:
                distances[new_dest] = dist
                heapq.heappush(q, [dist, new_dest])

    return distances[end]

distance1 = dijkstra(graph, 1, node1) + dijkstra(graph, node1, node2) + dijkstra(graph, node2, N)
distance2 = dijkstra(graph, 1, node2) + dijkstra(graph, node2, node1) + dijkstra(graph, node1, N)
res = min(distance1, distance2)
print(-1 if res == float('inf') else res)
