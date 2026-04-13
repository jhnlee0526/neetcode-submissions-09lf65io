class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        actualSum = sum(nums)
        expectedSum = sum(range(len(nums) + 1))
        res = expectedSum - actualSum
        return res