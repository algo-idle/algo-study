class Solution:
    def maxProfit(self, prices) -> int:
        buy = prices[0]
        res = 0

        for i in range(1, len(prices)):
            if res < prices[i] - buy:
                res = prices[i] - buy
            if prices[i] < buy:
                buy = prices[i]

        return res
