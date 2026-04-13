class Solution:
    def climbStairs(self, n: int) -> int:
        # DFS recursively (top-down). LESS EFFECTIVE
        #   Time : O(2^n) — exponential due to overlapping subproblems
        #   Space: O(n)   — recursion stack depth

        def dfs(i):
            # base case
            if i >= n:
                return i == n   # return 1 if exactly at top, else 0

            return dfs(i + 1) + dfs(i + 2)  # O(2^n) time

        return dfs(0)
