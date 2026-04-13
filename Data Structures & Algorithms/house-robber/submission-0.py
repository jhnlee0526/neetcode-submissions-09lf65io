class Solution:
    def rob(self, nums: List[int]) -> int:
        ## [Dynamic Programming] Space Optimized
        #### time : O(n) 
        #### space: O(1)
        rob1 = 0
        rob2 = 0
        for num in nums:
            # max(nums[0] + nums[2: n], nums[1 : n])
            rob1, rob2 = rob2, max(rob1 + num, rob2)
        return rob2