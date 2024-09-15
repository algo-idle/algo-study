import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

N, R, Q = map(int, input().rstrip().split())
tree = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1):
    u, v = map(int, input().rstrip().split())
    tree[u].append(v)
    tree[v].append(u)

cnt = {i: 0 for i in range(1, N + 1)}

def count_node(now):
    global cnt
    cnt[now] = 1
    for next in tree[now]:
        if not cnt[next]:
            cnt[now] += count_node(next)
    return cnt[now]

count_node(R)

for _ in range(Q):
    print(cnt[int(input().rstrip())])