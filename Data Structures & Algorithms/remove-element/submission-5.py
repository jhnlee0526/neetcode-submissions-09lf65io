class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Two pointers: time O(n), space O(1)
        ## n = length of the nums list
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k