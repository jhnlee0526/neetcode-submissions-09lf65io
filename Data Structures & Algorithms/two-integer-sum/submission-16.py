class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #   Time : O(n) - visits each numbers once
        #   Space: O(n) - hashmap
        
        numMap = {}     # {num : index, ..}
        for i, curNum in enumerate(nums):
            otherNum = target - curNum
            if otherNum in numMap:
                return [numMap[otherNum], i]
            numMap[curNum] = i
        
        return []