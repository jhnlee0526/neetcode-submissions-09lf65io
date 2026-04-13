class Solution:
    def climbStairs(self, n: int) -> int:
        ## [DFS from step 0 to step n] Recursion
        #### time : Exponential O(2^n), because it branches at every step
        #### space: O(n) — the max depth of recursion stack can be n
        def dfs(i):
            # Base Case: If we reach or pass step n
            if i >= n:
                return i == n  
                # If i == n → True → return 1 (valid way)
                # If i > n  → False → return 0 (overshot, not valid)

            # Recursive Step: Try taking 1 step or 2 steps
            return dfs(i + 1) + dfs(i + 2)
        return dfs(0)


        ## [Dynamic Programming] TOP-DOWN using DFS w/ "cache"
        #### time : O(n) — each index from 0 to n−1 is computed at most once
        #### space: O(n) — for both the recursion stack and the cache array
        cache = [-1] * n
        def dfs(i):
            # Base Case: If we reach or pass step n
            if i >= n:
                return i == n  
                # If i == n → True → return 1 (valid way)
                # If i > n  → False → return 0 (overshot, not valid)
            
            # If already computed, reuse cached result
            if cache[i] != -1:
                return cache[i]
            
            # Recursive Case: sum of ways from taking 1 step and 2 steps
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        
        return dfs(0) # Start climbing from step 0
            