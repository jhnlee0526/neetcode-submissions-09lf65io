class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        #   Time : O(n)
        #   Space: O(1)

        maxP = 0
        buyP = prices[0]    # window
        for curP in prices[1:]:
            if curP < buyP:
                buyP = curP # slide/shrink the window
            else:
                maxP = max(maxP, curP - buyP)

        return maxP