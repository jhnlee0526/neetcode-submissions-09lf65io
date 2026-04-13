class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        #   Time : O(log n)
        #   Space: O(1)

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target: # found the target
                return mid
            
            if nums[mid] < nums[r]: # right half sorted -> check right
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:                   # left half sorted -> check left
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
            
                


