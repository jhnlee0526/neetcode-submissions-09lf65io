class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search in a rotated sorted array
        # Time: O(log n)
        # Space: O(1)

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:  # Left half is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:   # Right half is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1