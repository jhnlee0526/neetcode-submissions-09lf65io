class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # {num: index, }
        for i, num in enumerate(nums):
            otherNum = target - num
            if otherNum in hashmap:
                return [hashmap[otherNum], i]
            
            hashmap[num] = i