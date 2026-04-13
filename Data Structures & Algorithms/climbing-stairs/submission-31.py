class Solution:
    def climbStairs(self, n: int) -> int:
        # Top-down DFS recursively. OPTIMIZED with memoization
        #   Time : O(n), each subproblem dfs(i) is computed once
        #   Space: O(n) for memoization + O(n) recursion stack depth

        memo = {}               # {curPos: numWays}, cache for subproblem results

        def dfs(curPos):
            # base cases: return 1 if exactly at top, else 0
            if curPos > n:
                return 0
            if curPos == n:
                return 1

            if curPos in memo:  # MEMOIZATION: Makes each unique 'curPos' be computed ONCE!
                return memo[curPos]

            memo[curPos] = dfs(curPos + 1) + dfs(curPos + 2)    # O(n) time
            return memo[curPos]

        return dfs(0)
        
        #######################################################
        # # Top-down DFS recursively. LESS EFFECTIVE...
        # #   Time : O(2^n) — exponential due to overlapping subproblems
        # #   Space: O(n)   — recursion stack depth
        
        # def dfs(curPos):
        #     # base cases: return 1 if exactly at top, else 0
        #     if curPos > n:
        #         return 0
        #     if curPos == n:
        #         return 1

        #     return dfs(curPos + 1) + dfs(curPos + 2)  # O(2^n) time

        # return dfs(0)
