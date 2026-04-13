class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap: {num: index, }
        # loop

        numsMap = {}
        for i in range(len(nums)):
            curnum = nums[i]
            othernum = target - curnum
            
            if othernum in numsMap:
                return [numsMap[othernum], i]
            numsMap[curnum] = i
        
        return []