class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [1, 1]
        for i in range(2, n+1):
            memo.append(memo[i-2] + memo[i-1])
        return memo[n]

    # def climbStairs(self, n: int) -> int:
    #     first, second = 1, 1
    #     curr = 1
    #     for i in range(n-1):
    #         curr = first + second
    #         first = second
    #         second = curr
    #     return curr