class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP - "bottom up" iteratively, space optimization
        rob1 = rob2 = 0
        for i in range(len(nums)):
            rob1, rob2 = rob2, max(rob2, rob1 + nums[i])
        return rob2