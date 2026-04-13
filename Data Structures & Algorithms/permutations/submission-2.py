class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ## backtracking
        res = []
        curPerm = []

        def backtracking(i):
            # base case
            if i >= len(nums):
                res.append(curPerm.copy())
                return
            
            for j in range(len(curPerm) + 1): # insert/remove at index 0, index2, and index3
                curPerm.insert(j, nums[i])
                backtracking(i + 1)
                curPerm.pop(j)

        backtracking(0)
        return res
