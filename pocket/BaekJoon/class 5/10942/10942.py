import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
se = [list(map(int, input().rstrip().split())) for _ in range(M)]

dp = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    for start in range(N - i):
        if start == start + i:
            dp[start][start + i] = True
        else:
            if nums[start] == nums[start + i]:
                if i == 1:
                    dp[start][start + i] = True
                else:
                    if dp[start + 1][start + i - 1]:
                        dp[start][start + i] = True

for s, e in se:
    print(1 if dp[s - 1][e - 1] else 0)