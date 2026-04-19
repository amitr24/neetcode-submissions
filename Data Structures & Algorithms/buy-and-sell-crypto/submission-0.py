class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyPrice = sys.maxsize
        for price in prices:
            buyPrice = min(buyPrice, price)
            profit = price - buyPrice
            maxProfit = max(profit, maxProfit)

        return maxProfit