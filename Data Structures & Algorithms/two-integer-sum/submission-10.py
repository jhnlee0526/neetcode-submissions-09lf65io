class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {} #{num: index, }
        for i in range(len(nums)):
            otherNum = target - nums[i]
            if otherNum in numMap:
                return [numMap[otherNum], i]
            numMap[nums[i]] = i
