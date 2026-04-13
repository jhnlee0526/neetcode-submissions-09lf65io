class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create empty hashmap: num-index
        # loop thru nums to find the result

        numMap = {} # {num: index, }
        for i in range(len(nums)):
            otherNum = target - nums[i]
            if otherNum in numMap:
                return [numMap[otherNum], i]
            numMap[nums[i]] = i
        return []
