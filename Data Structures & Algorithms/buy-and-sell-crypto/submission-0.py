class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = 101
        for price in prices:
            profit = max(price - lowest, profit)
            lowest = min(price, lowest)
        return profit