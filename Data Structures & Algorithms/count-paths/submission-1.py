class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Dynamic Programming (Top-Down) with memoization
        ## Time: O(m * n) — each subproblem (cell) is computed once
        ## Space: O(m * n) for the DP table + O(m + n) for recursion stack

        '''
        input: m = 3, n = 6
            [
                [m1, m2, m3, m4, m5, m6], 
                [m1, m2, m3, m4, m5, m6], 
                [m1, m2, m3, m4, m5, m6]
            ]
        
            dp = [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1]
            ]
        '''
        dp = [[-1] * n for _ in range(m)]
        
        def dfs(r, c):
            # Base case: reached bottom-right cell
            if r == m - 1 and c == n - 1:
                return 1
            # Out of bounds
            if r not in range(m) or c not in range(n):
                return 0
            # If already computed, return the cached value
            if dp[r][c] != -1:
                return dp[r][c]

            # Recursive case: go right and down
            dp[r][c] = dfs(r, c + 1) + dfs(r + 1, c)
            return dp[r][c]

        return dfs(0, 0)