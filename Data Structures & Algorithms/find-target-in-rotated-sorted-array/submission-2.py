class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        #   time : O(log n)
        #   space: O(1)

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            
            # Determine which half [l..m] or [m..r] is sorted
            if nums[m] <= nums[r]: # right half is sorted
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:                   # left half is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
        return -1


                