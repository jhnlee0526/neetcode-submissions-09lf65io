class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        #   Time : O(log n) — each step halves the search range via binary search
        #   Space: O(1)    — only constant extra pointers (l, r, m) are used

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if nums[l] <= nums[r]:  # If the subarray [l..r] is already sorted, nums[l] is the minimum
                return nums[l]
                    
            if nums[m] <= nums[r]:
                r = m               # right segment [m..r] is in ascending order, so the minimum lies between l and m
            else:
                l = m + 1           # pivot falls after m, so the minimum must be in the unsorted segment [m+1..r]

        return nums[l]              # l has converged on the smallest element, so nums[l] is the minimum

             