import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().rstrip().split())
start = int(input().rstrip())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))

def dijkstra(graph, start):
    distances = [float('inf') for _ in range(N + 1)]
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

    return distances[1:]

distance = dijkstra(graph, start)
for dist in distance:
    print(dist if dist != float('inf') else 'INF')
