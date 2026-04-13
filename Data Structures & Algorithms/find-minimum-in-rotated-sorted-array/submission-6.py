class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        #   Time : O(log n)
        #   Space: O(1)

        # edge case
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2

            if nums[l] < nums[m] < nums[r]:
                return nums[l]
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            
        return nums[l]
        
