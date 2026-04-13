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