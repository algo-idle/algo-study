import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

nums = list(map(int, input().rstrip().split()))[:-1]
dp = [[[-1 for _ in range(len(nums))] for _ in range(5)] for _ in range(5)]
costs = {
    0: {0: 1, 1: 2, 2: 2, 3: 2, 4: 2},
    1: {0: 2, 1: 1, 2: 3, 3: 4, 4: 3},
    2: {0: 2, 1: 3, 2: 1, 3: 3, 4: 4},
    3: {0: 2, 1: 4, 2: 3, 3: 1, 4: 3},
    4: {0: 2, 1: 3, 2: 4, 3: 3, 4: 1}
}

def sol(l, r, depth):
    if depth == len(nums):
        return 0
    if dp[l][r][depth] != -1:
        return dp[l][r][depth]

    left = sol(nums[depth], r, depth + 1) + costs[l][nums[depth]]
    right = sol(l, nums[depth], depth + 1) + costs[r][nums[depth]]
    dp[l][r][depth] = min(left, right)
    return dp[l][r][depth]

res = sol(0, 0, 0)
print(res)
