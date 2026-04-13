class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtracking with dfs recursively
        ## time : O(4^n / √n)
        ## space: O(n)
        
        res = []
        curStack = []

        def dfs(openN, closeN): # recursive
            # base case
            if openN == closeN == n:
                res.append(''.join(curStack))
                return

            if openN < n:
                # backtracking
                curStack.append('(')    # add
                dfs(openN + 1, closeN)  # dfs
                curStack.pop()          # remove
            
            if openN > closeN:
                # backtracking
                curStack.append(')')    # add
                dfs(openN, closeN + 1)  # dfs
                curStack.pop()          # remove

        dfs(0, 0)
        return res