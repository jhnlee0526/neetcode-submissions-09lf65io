class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [Greedy]
        ## time : 
        ## space:

        maxProfit = 0
        for i in range(1, len(prices)):
            prevPrice = prices[i - 1]
            curPrice = prices[i]

            if curPrice > prevPrice:
                maxProfit += curPrice - prevPrice
        
        return maxProfit
