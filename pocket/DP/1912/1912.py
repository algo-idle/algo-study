import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))

dp = [0 for _ in range(n)]
dp[0] = nums[0]

for i in range(1, n):
    dp[i] = max(dp[i - 1] + nums[i], nums[i])

print(max(dp))

