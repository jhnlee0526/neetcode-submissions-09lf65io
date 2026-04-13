class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #   Time : O(n)
        #   Space: O(1)

        maxAmt = 0
        
        l, r = 0, len(heights) - 1
        while l < r:
            curAmt = min(heights[l], heights[r]) * (r - l)
            maxAmt = max(maxAmt, curAmt)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxAmt

