class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #   Time : O(n) — two passes over the array
        #   Space: O(n) - hashmap
        
        res = [0] * len(nums)

        prefix = 1  ##
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1 ##
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix   ##
            postfix *= nums[i]

        return res