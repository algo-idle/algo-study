class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, maxProfit = 0, 0, 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if (buy < prices[i]):
                sell = prices[i]
                if (sell - buy > maxProfit): maxProfit = sell - buy
            if (buy > prices[i]): buy = prices[i]
        
        if (maxProfit > 0): return maxProfit
        else: return 0