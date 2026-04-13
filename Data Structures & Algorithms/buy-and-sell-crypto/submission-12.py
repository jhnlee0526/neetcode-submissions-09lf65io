class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window : tracking the min price dynamically
        maxProfit = 0
        minPrice = prices[0]
        for curPrice in prices:
            minPrice = min(minPrice, curPrice)
            maxProfit = max(maxProfit, curPrice - minPrice)
        
        return maxProfit
        

        # two pointers
        maxProfit = 0
        buyPt, sellPt = 0, 1

        while sellPt < len(prices):
            if prices[buyPt] < prices[sellPt]:
                maxProfit = max(maxProfit, prices[sellPt] - prices[buyPt])
            else:
                # update buyPt only when a lower price has been found
                buyPt = sellPt
            sellPt += 1

        return maxProfit
        


        