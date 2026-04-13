class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find pivot, starting from the back: len(nums) - 2 (second to last)
        p = len(nums) - 2
        while p >= 0 and nums[p] >= nums[p + 1]:
            p -= 1

        # find number larger than pivot number, then swap them
        if p >= 0:
            i = len(nums) - 1
            while nums[i] <= nums[p]:               # find number
                i -= 1
            nums[i], nums[p] = nums[p], nums[i]     # swap
        
        # reverse l & r ... starting at pivot + 1
        l, r = p + 1, len(nums) - 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1




