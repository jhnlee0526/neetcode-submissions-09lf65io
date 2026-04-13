class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ## [Sliding Window] : remove negative prefix
        #### time : O(n)
        #### space: O(1)
        maxSum = nums[0]
        curSum = 0
        for num in nums:
            # remove any negative prefix
            if curSum < 0:
                curSum = 0
            
            curSum += num
            maxSum = max(maxSum, curSum)

        return maxSum


        

