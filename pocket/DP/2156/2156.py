import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(N)]

dp = [0 for _ in range(N)]
dp[0] = nums[0]
if N > 1:
    dp[1] = nums[0] + nums[1]
if N > 2:
    dp[2] = max([nums[0] + nums[2], nums[1] + nums[2], dp[1]])
for i in range(3, N):
    dp[i] = max([dp[i - 3] + nums[i - 1] + nums[i], dp[i - 2] + nums[i], dp[i - 1]])

print(max(dp))
