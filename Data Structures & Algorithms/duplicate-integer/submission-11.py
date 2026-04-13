class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ### brute force time O(n^2) ###
        # p1 = 0
        # while p1 < len(nums):
        #     p2 = p1 + 1
        #     while p2 < len(nums):
        #         if nums[p1] == nums[p2]:
        #             return True
        #         else: 
        #             p2 += 1
        #     p1 += 1
        # return False

        ## Regular Dictionary : time O(n), space O(n) ##
        # dict = {}
        # for n in nums:
        #     if n not in dict:
        #         dict[n] = 1
        #     else:
        #         return True
        # return False

        ## Default Dictionary : time O(n), space O(n) ##
        # dict = defaultdict(int)
        # for n in nums:
        #     if n not in dict:
        #         dict[n] = 1
        #     else:
        #         return True
        # return False

        ## Set : time O(n), space O(n) ##
        numSet = set()
        for n in nums:
            if n not in numSet:
                numSet.add(n)
            else:
                return True
        return False
            
        
