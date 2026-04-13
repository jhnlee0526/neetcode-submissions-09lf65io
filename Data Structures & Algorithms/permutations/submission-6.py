class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Backtracking with DFS recursively
        ## time : 
        ## space:

        res = []
        curPerm = []
        
        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(curPerm[:])
                return
            
            for j in range(len(curPerm) + 1): # front + mid + *back
                # backtracking
                curPerm.insert(j, nums[i]) # add
                dfs(i + 1)                 # searching depth
                curPerm.pop(j)             # remove
            
        dfs(0)
        return res