class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## [sliding window] tracking minimum values
        maxProfit = 0
        minVal = prices[0]

        for curVal in prices:
            minVal = min(minVal, curVal)
            maxProfit = max(maxProfit, curVal - minVal)
            
        return maxProfit