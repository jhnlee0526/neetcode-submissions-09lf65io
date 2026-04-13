class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {} # {num: index, }
        for i, num in enumerate(nums):
            otherNum = target - num
            if otherNum in numsMap:
                return [numsMap[otherNum], i]
            numsMap[num] = i
        return []
                