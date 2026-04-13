class Solution:
    def rob(self, nums: List[int]) -> int:
        ## [Dynamic programing] "Bottom UP" iteratively
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums) #store max Money
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1]) # either first house or second house

        for i in range(2, len(nums)): # starting at index#2 (3rd house)
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[-1] # the last item in dp is the final value
