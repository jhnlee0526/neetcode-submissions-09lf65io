class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # [backtracking] dfs() recursively
        ## Time : O(2^(m+n)) in the worst case since it explores every possible path without memoization.
        ## Space: O(m + n) for the recursion stack. 
        def dfs(r, c):
            # base case
            if (
                r == m - 1 and 
                c == n - 1
            ):  # If we've reached the destination cell
                return 1
            if (
                r not in range(m) or 
                c not in range(n)
            ):  # If we're out of bounds
                return 0
                
            # Explore both paths: down and right
            return dfs(r + 1, c) + dfs(r, c + 1)

        return dfs(0, 0)


        
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



        # Dynamic Programming (Bottom-Up with Padding)
        # Time: O(m * n) — one pass through the grid
        # Space: O(m * n) — for the DP table (with extra row/column for padding)
        '''
        Create a grid of (m+1) rows and (n+1) columns, all initialized to 0
        Why m+1 and n+1?
            → It prevents index errors when accessing dp[r + 1][c] or dp[r][c + 1]
            → We pad the grid to avoid writing explicit edge-checking if-statements
        '''
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: there's 1 path from the destination to itself
        dp[m - 1][n - 1] = 1

        # Start filling the table from bottom-right to top-left
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    continue  # already initialized base case
                # Each cell accumulates paths from the cell below and to the right
                dp[r][c] = dp[r + 1][c] + dp[r][c + 1]

        # The answer — number of unique paths — is at the top-left corner
        return dp[0][0]



        # Space-Optimized Bottom-Up DP
        # Time: O(m * n) — compute each cell once
        # Space: O(n) — only one row (the current row) is stored at a time

        row = [1] * n  # Bottom row: only one way to reach the goal from each cell

        # Iterate from second-to-last row upward
        for r in range(m - 1):
            newRow = [1] * n  # Rightmost cell is always 1
            for c in range(n - 2, -1, -1):  # Fill leftward across the row
                newRow[c] = newRow[c + 1] + row[c]
            row = newRow  # Move up: current row becomes row below

        return row[0]  # Top-left cell contains total unique paths
        
        
        
        # Optimized Bottom-up DP
        # Time: O(m * n) — total cells processed
        # Space: O(n) — we're using just one row of length n

        dp = [1] * n  # Initialize bottom row: all cells have 1 path to the destination

        # Start from the second-to-last row and move upward
        for r in range(m - 2, -1, -1):
            # For each cell, move from right to left, excluding the last column
            for c in range(n - 2, -1, -1):
                # Update dp[c]: paths from right + paths from below
                dp[c] += dp[c + 1]

        # The number of unique paths from the top-left corner ends up in dp[0]
        return dp[0]