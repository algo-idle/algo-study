N = int(input())
dp = [[1 for _ in range(10)] for _ in range(N)]
dp[0][0] = 0

for i in range(1, N):
    dp[i][0] = dp[i - 1][1]
    dp[i][9] = dp[i - 1][8]
    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[-1]) % 1000000000)
