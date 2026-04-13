class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for n in nums:
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1
        
        for key, val in dict.items():
            if val > len(nums)/2:
                return key