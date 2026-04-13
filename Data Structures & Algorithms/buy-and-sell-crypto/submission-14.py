class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window: trakcing minimum price
        maxProfit = 0

        minPrice = prices[0]    # window
        for curPrice in prices:
            minPrice = min(minPrice, curPrice)
            maxProfit = max(maxProfit, curPrice - minPrice) ##

        return maxProfit