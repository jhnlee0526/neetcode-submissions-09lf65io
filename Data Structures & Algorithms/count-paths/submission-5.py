class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
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