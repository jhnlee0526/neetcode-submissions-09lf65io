class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [Greedy]
        ## time : O(n)
        ## space: O(1)

        # find the pivot index
        i = len(nums) - 2 # We start checking from the second-to-last element... to compare nums[i] v. nums[i + 1]
        while i >= 0 and nums[i] >= nums[i + 1]: # from the back
            i -= 1
        
        # find the number larger than nums[i] after index
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]: # while loop until nums[j] is larger than nums[i]
                j -= 1
            nums[i], nums[j] = nums[j], nums[i] # swap two

        # reverse the suffix starting at i + 1
        # This transforms a descending tail (largest permutation) into an ascending one (smallest permutation)
        l, r = i + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        
            