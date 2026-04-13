class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window : tracking the buying price
        #   time : O(n)
        #   space: O(1)

        maxProfit = 0

        buyPrice = prices[0]            # window
        for sellPrice in prices[1:]:
            if sellPrice < buyPrice:    # sell needs to be higher than buy for profit
                buyPrice = sellPrice
            else:
                maxProfit = max(maxProfit, sellPrice - buyPrice)

        return maxProfit