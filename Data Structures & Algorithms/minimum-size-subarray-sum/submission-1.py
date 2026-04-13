class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sum = 0
        minLength = float('inf')

        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                minLength = min(minLength, r - l + 1)
                sum -= nums[l]
                l += 1
        
        return minLength if minLength != float('inf') else 0