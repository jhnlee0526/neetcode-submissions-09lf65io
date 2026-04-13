class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search (search left part, and right part)

        def binarySearch(leftCheck):
            l = 0
            r = len(nums) - 1
            index = -1  # Store the latest index where target is found
            
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    index = m
                    # Keep searching to the LEFT/RIGHT for the first occurrence
                    if leftCheck:
                        r = m - 1
                    else:
                        l = m + 1
            return index

        
        left = binarySearch(True)
        right = binarySearch(False)

        return [left, right]