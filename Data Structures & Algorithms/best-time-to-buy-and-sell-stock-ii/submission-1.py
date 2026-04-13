class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [Greedy]
        ## time : 
        ## space:

        maxProfit = 0
        for i in range(1, len(prices)):
            curPrice, prevPrice = prices[i], prices[i - 1]
            
            if curPrice > prevPrice:
                maxProfit += curPrice - prevPrice
            
        return maxProfit
