class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find pivot, starting from the back
        p = len(nums) - 2
        while p >= 0 and nums[p] >= nums[p + 1]:
            p -= 1
        
        # find number larger than the pivot number
        if p >= 0:
            i = len(nums) - 1           
            while nums[p] >= nums[i]:   # while from the back
                i -= 1
            nums[p], nums[i] = nums[i], nums[p] # swap
            
        # reverse, start at pivot + 1
        l, r = p + 1, len(nums) - 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1




        