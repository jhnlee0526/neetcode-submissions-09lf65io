class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        suffix = 1
        for i in range(len(nums)):
            res[i] = suffix
            suffix *= nums[i]

        prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prefix
            prefix *= nums[i]
        
        return res