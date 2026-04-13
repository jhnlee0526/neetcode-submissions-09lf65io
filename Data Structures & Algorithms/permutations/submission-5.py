class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking (recursively)
        ## time : n^2 * n!
        res = []
        curNum = []

        def backtracking(i): # recursively
            # base case
            if i >= len(nums):
                res.append(curNum.copy()) # curNum[:]
                return
            
            for j in range(len(curNum) + 1): # adding front, middle, and *back
                curNum.insert(j, nums[i])
                backtracking(i + 1)
                curNum.pop(j)
            
        backtracking(0)
        return res