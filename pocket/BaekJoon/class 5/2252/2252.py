from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
tall = {i: {'cnt': 0, 'next': []} for i in range(1, N + 1)}

for _ in range(M):
    s, e = map(int, input().rstrip().split())
    tall[s]['next'].append(e)
    tall[e]['cnt'] += 1

q = deque([i for i in tall if tall[i]['cnt'] == 0])
res = []
while q:
    now = q.popleft()
    res.append(now)

    for next in tall[now]['next']:
        tall[next]['cnt'] -= 1
        if tall[next]['cnt'] == 0:
            q.append(next)

print(*res)