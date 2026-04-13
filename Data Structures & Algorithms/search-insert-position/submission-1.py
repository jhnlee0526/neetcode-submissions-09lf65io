class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        #   time : O(log n), n = len(nums)
        #   space: O(1)

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        # `l` is the correct insertion index when target not found
        return l