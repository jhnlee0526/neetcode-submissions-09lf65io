class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ## two pointers
        #### time : O(n)
        #### space: O(1)
        maxArea = 0
        
        l = 0
        r = len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])  # More concise height calculation
            currentArea = (r - l) * height
    
            maxArea = max(maxArea, currentArea)
            
            # Move the pointer with the smaller height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea

        