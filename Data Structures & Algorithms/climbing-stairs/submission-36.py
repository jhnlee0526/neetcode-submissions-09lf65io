class Solution:
    def climbStairs(self, n: int) -> int:
        # [Brute Force] Top-down DFS recursively
        #   Time  : O(2^n) — exponential due to branching
        #   Space : O(n)   — recursion stack depth
        
        def dfs(curLevel):
            # base cases: 
            if curLevel == n:   # return 1 if exactly at top (valid path)
                return 1            
            if curLevel > n:    # otherwise, return 0
                return 0
            return dfs(curLevel + 1) + dfs(curLevel + 2)    # O(2^n) time
        
        return dfs(0)