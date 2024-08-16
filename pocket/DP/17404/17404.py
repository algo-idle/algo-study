import sys
input = sys.stdin.readline

N = int(input().rstrip())
rgb = [list(map(int, input().rstrip().split())) for _ in range(N)]
rgb = [[-1, -1, -1]] + rgb
ans = float('inf')
for i in range(3):
    dp = [[0 for _ in range(3)] for _ in range(N + 1)]
    dp[1] = [float('inf'), float('inf'), float('inf')]
    dp[1][i] = rgb[1][i]
    for j in range(2, N + 1):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + rgb[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + rgb[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + rgb[j][2]
    dp[N][i] = float('inf')
    ans = min(ans, min(dp[-1]))
print(ans)
