class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit = None
        max_profit = 0
        for i in range(0, len(prices)):
            if not min_profit or prices[i] < min_profit:
                min_profit = prices[i]
            elif prices[i] - min_profit > max_profit:
                max_profit = prices[i] - min_profit
        return max_profit
