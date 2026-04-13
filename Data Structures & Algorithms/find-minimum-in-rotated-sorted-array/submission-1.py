class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        #   time :
        #   space:

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2

            if nums[l] <= nums[r]:  # The subarray [l..r] is already sorted
                return nums[l]  # nums[l] is the minimum

            if nums[m] <= nums[r]:  # Right segment [m..r] is in ascending order
                r = m       # the minimum lies between l and m

            else:                   # Pivot falls after m
                l = m + 1   # the minimum must be in the unsorted segment [m+1..r]

        return nums[l]
                

