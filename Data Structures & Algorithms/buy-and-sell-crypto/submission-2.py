import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Decreasing interval
        # Increasing Interval
        # Interval with ups and downs and you want it to sell it at some pt

        price_bought = sys.maxsize
        max_profit = 0

        # Iterate through array and every time we see a lower price, we can update price_bought
        # Update max_profit every time (current_price - price_bought) is greater than the current max_profit

        for i in range(len(prices)):
            current_price = prices[i]

            if price_bought < current_price:
                max_profit = max(max_profit, current_price - price_bought)

            price_bought = min(current_price, price_bought)

        return max_profit