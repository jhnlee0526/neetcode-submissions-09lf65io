class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # start pivot index (from the back)
        i = len(nums) - 2                        # to compare nums[i] v. nums[i + 2]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:           # while loop until you find nums[j] larger than nums[i]
                j -= 1
            nums[i], nums[j] = nums[j], nums[i] # swap
        
        # reverse, starting at i + 1
        l, r = i + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1