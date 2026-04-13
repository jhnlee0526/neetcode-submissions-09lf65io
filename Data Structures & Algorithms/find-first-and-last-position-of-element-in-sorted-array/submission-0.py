class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search
        ## time : O(2 * log n) - binary search twice : left(start) and right(end)
        ## space: O(1)

        # Helper function to find either the left or right boundary of the target
        def binarySearch(target, leftCheck):
            l = 0
            r = len(nums) - 1
            res = -1    # Store the latest index where target is found

            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    res = m
                    
                    if leftCheck:   # Keep searching to the LEFT for the first occurrence
                        r = m - 1
                    else:           # Keep searching to the RIGHT for the last occurrence
                        l = m + 1
            return res

        left = binarySearch(target, True)   # Search for the leftmost index where target appears
        right = binarySearch(target, False) # Search for the rightmost index where target appears

        return [left, right]
        