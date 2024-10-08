import sys
input = sys.stdin.readline

N = int(input().rstrip())
dp = [[0 for _ in range(10)] for _ in range(N)]

for i in range(10):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(0, 10):
        for k in range(0, j + 1):
            dp[i][j] += dp[i - 1][k]

print(sum(dp[-1]) % 10007)
