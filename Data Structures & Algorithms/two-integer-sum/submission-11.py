class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {} # {num: index, }
        for i, num in enumerate(nums):
            otherNum = target - num
            if otherNum in numMap:
                return [numMap[otherNum], i]
            else:
                numMap[num] = i
            