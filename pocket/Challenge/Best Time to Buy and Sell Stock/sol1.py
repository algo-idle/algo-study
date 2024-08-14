# dp 815ms 9.8%

class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:
            return 0
        table = [0 for _ in range(len(prices))]
        table[1] = prices[1] - prices[0]
        for i in range(2, len(prices)):
            table[i] = max(prices[i] - prices[i - 1], prices[i] - (prices[i - 1] - table[i - 1]))
        return max(table)
