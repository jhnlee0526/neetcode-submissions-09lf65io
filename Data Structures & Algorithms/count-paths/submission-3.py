class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
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

