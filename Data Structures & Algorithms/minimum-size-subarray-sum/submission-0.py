class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ## [Sliding Window]
        #### time : O(n)
        #### space: O(1)
        l = 0  # Left pointer of the sliding window
        sum = 0  # Current sum of the window
        minLength = float('inf')  # Stores the smallest valid window size (set to infinity initially)

        # Step 1: Expand the window by moving the right pointer `r`
        for r in range(len(nums)):  
            sum += nums[r]  # Add the current element to the sum
            
            # Step 2: Shrink the window from the left while sum >= target
            while sum >= target:
                minLength = min(minLength, r - l + 1)  # Update the minimum window size
                sum -= nums[l]  # Remove the leftmost element from the sum
                l += 1  # Move the left pointer forward (shrink the window)

        # Step 3: If no valid subarray is found, return 0. Otherwise, return the smallest window size found.
        return minLength if minLength != float('inf') else 0