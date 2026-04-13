class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # {num, index}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            else:
                seen[n] = i
                


