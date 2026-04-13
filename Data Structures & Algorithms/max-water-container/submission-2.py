class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers
        #   time : O(n)
        #   space: O(1)

        maxArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            curArea = (r - l) * min(heights[l], heights[r])
            maxArea = max(maxArea, curArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea