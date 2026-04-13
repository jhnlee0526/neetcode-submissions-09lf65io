class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## Regular dictionary : time O(n), space O(n)
        # dict = {}
        # for n in nums:
        #     if n not in dict:
        #         dict[n] = 1
        #     else:
        #         dict[n] += 1
        
        # for key, val in dict.items():
        #     if val > len(nums) / 2:
        #         return key


        ## Default dictionary : time O(n), space O(n)
        dict = defaultdict(int)
        for n in nums:
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1
        
        for key, val in dict.items():
            if val > len(nums) / 2:
                return key