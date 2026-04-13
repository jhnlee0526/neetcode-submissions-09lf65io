class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sliding window: tracking max sum, and remove the negative prefix
        maxSum = nums[0]
        curSum = 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            
            maxSum = max(maxSum, curSum + num)
            curSum += num
            
        return maxSum