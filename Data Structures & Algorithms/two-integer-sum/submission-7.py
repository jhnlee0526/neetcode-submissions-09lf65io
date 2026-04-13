class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary
        # time: O(n)
        # space O(n)
        dict = {} # {value:index, }
        for i in range(len(nums)):
            otherNum = target - nums[i]
            
            if otherNum in dict: 
                return [dict[otherNum], i]
            
            dict[nums[i]] = i # add current val to dict
        
        