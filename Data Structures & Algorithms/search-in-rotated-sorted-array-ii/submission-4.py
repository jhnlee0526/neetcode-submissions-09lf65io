class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # binary search
        #   time : O(log n) average, O(n) due to duplicates
        #   space: O(1)

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return True
            
            ###
            if nums[l] == nums[m] == nums[r]:   # When l, m, r are the same, skip duplicates
                l += 1
                r -= 1
            elif nums[m] <= nums[r]:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return False
