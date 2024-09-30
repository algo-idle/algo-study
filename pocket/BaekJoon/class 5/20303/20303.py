import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M, K = map(int, input().rstrip().split())
candy = [0] + list(map(int, input().rstrip().split()))

friend = [i for i in range(N + 1)]
group = [0 for _ in range(N + 1)]

K -= 1

def find(x):
    if friend[x] != x:
        friend[x] = find(friend[x])
    return friend[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        friend[y] = x
    else:
        friend[x] = y

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    union(a, b)

for i in range(1, N + 1):
    if i != friend[i]:
        _i = find(i)
        candy[_i] += candy[i]
        group[_i] += 1
    else:
        group[i] += 1

dp = [0 for _ in range(K + 1)]

for i in range(1, N + 1):
    if group[i] != 0:
        w = group[i]
        v = candy[i]
        if w > K:
            continue
        for j in range(K, 0, -1):
            if j + w <= K and dp[j] != 0:
                dp[j + w] = max(dp[j + w], dp[j] + v)
        dp[w] = max(dp[w], v)

print(max(dp))
