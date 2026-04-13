class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
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


