class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search
        #   Time  : O(log n)
        #   Space : O(1)

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            # Case 1: Entire interval is already sorted
            #   → Minimum must be at the left boundary
            if nums[l] < nums[r]:
                return nums[l]

            # Case 2: Right half is sorted
            #   → Minimum must be in the left half (including mid)
            if nums[mid] < nums[r]:
                r = mid     # ✅ keep mid — it could be the minimum

            # Case 3: Left half is sorted
            #   → Minimum must be in the right half (excluding mid)
            else:
                l = mid + 1 # ✅ discard mid — it's too large to be the minimum

        # Loop ends when l == r
        # → Only one candidate remains, which is the minimum
        return nums[l]
