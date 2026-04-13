class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## [Brute Force]
        #### time : O(n^2)
        #### space: O(1)
        maxProfit = 0
        for buy in range(0, len(prices)):
            for sell in range(buy + 1, len(prices)):
                # if prices[sell] - prices[buy] > maxProfit:
                #     maxProfit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
                
        return maxProfit
