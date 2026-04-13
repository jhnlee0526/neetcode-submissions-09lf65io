class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        #   Time : O(log n)
        #   Space: O(1)

        l, r = 0, len(nums) - 1
        while l <= r: #
            m = l + (r - l) // 2

            if nums[m] == target:
                return m

            if nums[m] < nums[r]:   # right part is sorted
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:                   # left part is sorted
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
        return -1