class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [Greedy]
        # time : O(n)
        # space: O(1)

        # find pivot index
        i = len(nums) - 2 # starting at the end to compare nums[i] v. nums[i + 1]
        while i >= 0 and nums[i] >= nums[i + 1]: # find the point where current num is smaller than next num
            i -= 1
        
        # find the number larger than nums[i] after index
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # reverse the suffix starting at i + 1
        l, r = i + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            