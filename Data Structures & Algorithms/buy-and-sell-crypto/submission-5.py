class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small = prices[0]
        large = prices[0]
        profit = 0

        for i in range(1,len(prices)):
            if prices[i]<small:
                small = prices[i]
                large = prices[i]
            elif prices[i]>large:
                large = prices[i]
            profit = max(profit,large-small)
        return profit
        