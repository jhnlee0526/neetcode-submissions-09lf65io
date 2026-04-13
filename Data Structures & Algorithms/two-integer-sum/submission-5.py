class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## Brute Force - Two Pointers, Time O(n^2), Space O(1) ##
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        ## Regular Dictionary, time O(n) space O(n) ##
        # dict = {} # {val, index}
        # for i, num in enumerate(nums):
        #     otherNum = target - num

        #     if otherNum in dict:
        #         return [dict[otherNum], i]

        #     dict[num] = i

        ## Default Dictionary, time O(n) space O(n) ##
        dict = defaultdict(int)
        for i, num in enumerate(nums):
            otherNum = target - num
            
            if otherNum in dict:
                return [dict[otherNum], i]
            
            dict[num] = i