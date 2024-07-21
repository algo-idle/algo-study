from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
grid = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if grid[i][j] and dp[i][j]:
            try:
                dp[i + grid[i][j]][j] += dp[i][j]
            except:
                pass
            try:
                dp[i][j + grid[i][j]] += dp[i][j]
            except:
                pass

print(dp[-1][-1])
