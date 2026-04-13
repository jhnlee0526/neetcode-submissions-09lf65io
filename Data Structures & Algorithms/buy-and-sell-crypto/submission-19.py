class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #   Time : O(n)
        #   Space: O(1)

        maxProfit = 0
        buyPrice = prices[0]

        for sellPrice in prices[1:]:
            if sellPrice < buyPrice:
                buyPrice = sellPrice
            else:
                maxProfit = max(maxProfit, sellPrice - buyPrice)
        
        return maxProfit


        #################################
        # [Brute-force]
        #   Time : O(n^2)
        #       - Outer loop: O(n)
        #       - Inner loop: O(n)
        #       - Total: O(n^2)
        #   Space: O(1)
        
        if len(prices) < 2:
            return 0

        maxProfit = 0
        buy = 0
        while buy <= len(prices) - 1:
            sell = buy + 1
            while sell <= len(prices) - 1:
                curProfit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, curProfit)

                sell += 1
            buy += 1
        
        return maxProfit
