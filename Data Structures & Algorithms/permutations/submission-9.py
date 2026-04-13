class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i):
            # base case
            if i == len(nums):
                res.append(nums[:])
                return
            
            for j in range(i, len(nums)): ##
                nums[i], nums[j] = nums[j], nums[i] # swap
                dfs(i + 1)
                nums[i], nums[j] = nums[j], nums[i] # undo

        dfs(0)
        return res