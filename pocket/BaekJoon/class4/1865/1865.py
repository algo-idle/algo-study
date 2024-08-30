from collections import defaultdict
import sys
input = sys.stdin.readline

def cycle(start, node_num, edges):
    distance = [1e9] * (node_num + 1)
    distance[start] = 0

    for i in range(node_num):
        for (cur, next), cost in edges.items():
            if distance[cur] + cost < distance[next]:
                distance[next] = distance[cur] + cost
                if i == node_num - 1:
                    return True

    return False

for _ in range(int(input())):
    N, M, W = map(int, input().rstrip().split())
    edges = defaultdict(lambda: float('inf'))
    for _ in range(M):
        s, e, c = map(int, input().rstrip().split())
        edges[(s, e)] = min(edges[(s, e)], c)
        edges[(e, s)] = min(edges[(e, s)], c)

    for _ in range(W):
        s, e, c = map(int, input().rstrip().split())
        edges[(s, e)] = min(edges[(s, e)], -c)

    print('YES' if cycle(1, N, edges) else 'NO')

