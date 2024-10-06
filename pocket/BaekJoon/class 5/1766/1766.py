import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
prob = {i: {'cnt': 0, 'next': []} for i in range(1, N + 1)}
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    prob[b]['cnt'] += 1
    prob[a]['next'].append(b)

h = [i for i in range(1, N + 1) if prob[i]['cnt'] == 0]
res = []

while h:
    p = heapq.heappop(h)
    res.append(p)
    for next in prob[p]['next']:
        prob[next]['cnt'] -= 1
        if prob[next]['cnt'] == 0:
            heapq.heappush(h, next)

print(*res)
