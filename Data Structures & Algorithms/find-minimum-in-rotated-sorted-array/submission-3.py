class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        #   time : O(log n)
        #   space: O(1)

        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2

            if nums[l] < nums[r]:  # Already sorted
                return nums[l]

            if nums[m] < nums[r]:  # Right half is sorted
                r = m              #    Minimum could be at m
            else:                  # Minimum is in right half
                l = m + 1
        
        return nums[l]


