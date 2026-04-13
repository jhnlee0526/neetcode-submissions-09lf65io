class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## [Brute Force]
        #### time : O(n^2)
        #### space: O(1)
        # maxProfit = 0
        # for buy in range(0, len(prices)):
        #     for sell in range(buy + 1, len(prices)):
        #         # if prices[sell] - prices[buy] > maxProfit:
        #         #     maxProfit = prices[sell] - prices[buy]
        #         maxProfit = max(maxProfit, prices[sell] - prices[buy])
                
        # return maxProfit


        ## [Two Pointers]
        #### time : O(n)
        #### space: O(1)
        buy = 0
        sell = 1
        maxProfit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
            else:
                buy = sell # ✅ Update `buy` only when we find a lower price

            sell += 1 # Always move `sell`

        return maxProfit
