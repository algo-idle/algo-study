from collections import deque
import sys

input = sys.stdin.readline

N = int(input().rstrip())
graph = {i: {} for i in range(N)}

for _ in range(N):
    buf = list(map(int, input().rstrip().split()))
    node = buf[0] - 1
    for i in range(1, len(buf) - 1, 2):
        target = buf[i] - 1
        weight = buf[i + 1]
        graph[node][target] = weight
        graph[target][node] = weight


def bfs(start):
    dist = [-1] * N
    dist[start] = 0
    queue = deque([start])
    max_dist, max_node = 0, start

    while queue:
        node = queue.popleft()
        for next_node, d in graph[node].items():
            if dist[next_node] == -1:
                dist[next_node] = dist[node] + d
                queue.append(next_node)
                if dist[next_node] > max_dist:
                    max_dist = dist[next_node]
                    max_node = next_node

    return max_node, max_dist

farthest_node, _ = bfs(0)
_, diameter = bfs(farthest_node)
print(diameter)
