class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # [two pointers]
        ## time : O(n)
        ## space: O(1)
        
        # left from the start, right from the end
        # tracking maxArea
        # while loop until l and r meet each other:
            # tracking curHeight( min(heights[l], heights[r])) and curArea
            # find maxArea: max(maxArea, curArea)
            # move smaller height for the next iteration
        # return maxArea

        maxArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            minHeight = min(heights[l], heights[r])
            curArea = (r - l) * minHeight
            maxArea = max(maxArea, curArea)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea

    