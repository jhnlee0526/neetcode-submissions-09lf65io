class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ## time : O(n)
        ## space : O(n)
        res = []
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        
        for num, cnt in dict.items():
            if cnt > len(nums) / 3:
                res.append(num)
        
        return res