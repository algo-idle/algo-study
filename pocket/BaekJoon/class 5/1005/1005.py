from collections import deque
import sys
input = sys.stdin.readline

def sol(build, cost, target):
    q = [b for b in build if build[b]['cnt'] == 0]
    res = [0 for _ in range(len(build.keys()) + 1)]
    for _q in q:
        res[_q] = cost[_q - 1]
    q = deque(q)

    while q:
        now = q.popleft()
        for next in build[now]['next']:
            build[next]['cnt'] -= 1
            res[next] = max(res[next], res[now] + cost[next - 1])
            if build[next]['cnt'] == 0:
                q.append(next)

    return res[target]


for _ in range(int(input().rstrip())):
    N, K = map(int, input().rstrip().split())
    cost = list(map(int, input().rstrip().split()))
    build = {i: {'cnt': 0, 'next': []} for i in range(1, N + 1)}
    for _ in range(K):
        s, e = map(int, input().rstrip().split())
        build[s]['next'].append(e)
        build[e]['cnt'] += 1
    W = int(input().rstrip())
    ans = sol(build, cost, W)
    print(ans)
