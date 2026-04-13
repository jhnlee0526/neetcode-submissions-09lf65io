class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for i in range(len(nums)):
            rob1, rob2 = rob2, max(rob1 + nums[i], rob2)
        
        return rob2 
        
        
        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # return dp[-1]