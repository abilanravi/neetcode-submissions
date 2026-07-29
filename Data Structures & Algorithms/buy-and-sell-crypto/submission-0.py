from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buydate = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buydate:
                buydate = prices[i]
            else:
                profit = prices[i] - buydate
                if profit > max_profit:
                    max_profit = profit

        return max_profit