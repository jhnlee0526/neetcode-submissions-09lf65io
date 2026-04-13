class Solution:
    def jump(self, nums: List[int]) -> int:
        # time : O(n)
        # space: O(1)
        
        jumps = 0
        l, r = 0, 0                                     # window

        while r < len(nums) - 1: ##
            furthest = 0
            
            for i in range(l, r + 1):                   # l ~ r
                furthest = max(furthest, i + nums[i])   # i + j

            # update the window
            l = r + 1
            r = furthest

            jumps += 1

        return jumps