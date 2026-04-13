class Solution:
    def climbStairs(self, n: int) -> int:
        ## [DFS from step 0 to step n] Recursion
        #### time : Exponential O(2^n), because it branches at every step
        #### space: O(n) — the max depth of recursion stack can be n
        def dfs(i):
            # Base Case 1: If we've gone beyond step n, it's an invalid path
            if i > n:
                return 0
            # Base Case 2: If we land exactly on step n, it's a valid path
            if i == n:
                return 1
            # Recursive Step: Try taking 1 step or 2 steps
            return dfs(i + 1) + dfs(i + 2)
        return dfs(0)
            