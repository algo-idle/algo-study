from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

nodes = {i: {'cnt': 0, 'next': []} for i in range(1, N + 1)}

for _ in range(M):
    buf = list(map(int, input().rstrip().split()))
    for i in range(1, len(buf) - 1):
        nodes[buf[i]]['next'].append(buf[i + 1])
        nodes[buf[i + 1]]['cnt'] += 1

q = deque([i for i in nodes if nodes[i]['cnt'] == 0])

res = []

while q:
    x = q.popleft()
    res.append(x)
    for next in nodes[x]['next']:
        nodes[next]['cnt'] -= 1
        if nodes[next]['cnt'] == 0:
            q.append(next)

if len(res) == N:
    print(*res, sep='\n')
else:
    print(0)
