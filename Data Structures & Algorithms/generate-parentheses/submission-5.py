class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtracking, dfs recursively 
        ## time :
        ## space:

        res = []

        curP = [] ##
        def dfs(openP, closeP):
            if openP == closeP == n: # base case
                res.append(''.join(curP)) ##
                return
            
            if openP < n:
                curP.append('(')
                dfs(openP + 1, closeP)
                curP.pop()
            
            if openP > closeP:
                curP.append(')')
                dfs(openP, closeP + 1)
                curP.pop()

        dfs(0, 0)
        return res