class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [Sliding Window] : tracking minimum price for buying
        # find maxProfit to return

        ## time : O(n)
        ## space: O(1)

        maxProfit = 0

        minPrice = prices[0]
        for curPrice in prices:
            minPrice = min(minPrice, curPrice)
            maxProfit = max(maxProfit, curPrice - minPrice)
        
        return maxProfit




        
