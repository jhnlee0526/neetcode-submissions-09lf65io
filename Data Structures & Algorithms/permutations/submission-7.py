class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Backtracking with DFS recursively
        ## time : O(n × n!) **
        '''
            n!- permutations
            O(n)- time per permutation for insert/pop
        '''
        ## space: O(n) if 'res' is not included. Otherwise O(n x n!) because that’s how many full permutations you're storing.

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