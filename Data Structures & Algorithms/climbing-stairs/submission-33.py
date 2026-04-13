class Solution:
    def climbStairs(self, n: int) -> int:
        # ------------------------------------------------------------
        # ✅ Bottom-Up DP — OPTIMAL SPACE (O(1))
        #   Time : O(n) — each step from 3 to n computed once
        #   Space: O(1) — only two variables tracked

        if n <= 2:                  # base case: 1 way to climb 1 step, 2 ways to climb 2 steps
            return n

        one, two = 1, 2             # ways to reach step1 & step2
        for i in range(3, n + 1):
            one, two = two, one + two

        return two                  # 'two' holds the number of ways to reach step 'n'

        #---------------------------------------------------------
        # # ✅ Bottom-Up DP (Tabulation)
        # #   Time : O(n) — each step from 3 to n computed once
        # #   Space: O(n) — stores intermediate results in memo
        
        # if n <= 2:                  # edge cases: 1 way to climb 1 step, 2 ways to climb 2 steps
        #     return n
        
        # dp = {}                     # {curPos: numWays}, cache for subproblem results
        
        # dp[1], dp[2] = 1, 2
        # for i in range(3, n + 1):   # from step 3 to step n (step 1 & 2 are done already)
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n]


        #######################################################
        # #✅ Top-Down DFS with Memoization (Optimized Recursion)
        # #   Time : O(n), each subproblem dfs(i) is computed once
        # #   Space: O(n) for memoization + O(n) recursion stack depth

        # memo = {}               # {curPos: numWays}, cache for subproblem results

        # def dfs(curPos):
        #     # base cases: return 1 if exactly at top, else 0
        #     if curPos > n:
        #         return 0
        #     if curPos == n:
        #         return 1

        #     if curPos in memo:  # MEMOIZATION: Makes each unique 'curPos' be computed ONCE!
        #         return memo[curPos]

        #     memo[curPos] = dfs(curPos + 1) + dfs(curPos + 2)    # O(n) time
        #     return memo[curPos]

        # return dfs(0)
        
        #---------------------------------------------------------
        # #❌ Top-Down DFS without Memoization (Brute-force Recursion)
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
