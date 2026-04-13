class Solution:
    def climbStairs(self, n: int) -> int:
        ## [DFS from step 0 to step n] Recursion
        #### time : Exponential O(2^n), because it branches at every step
        #### space: O(n) — the max depth of recursion stack can be n
        def dfs(i):
            # Base case: past the end → invalid path
            if i > n:
                return 0
            # Base case: exactly at step n → valid way
            if i == n:
                return 1

            # Recursive Step: Try taking 1 step or 2 steps
            return dfs(i + 1) + dfs(i + 2)
        return dfs(0)


        ## [Dynamic Programming] TOP-DOWN using DFS w/ "cache" (recursively)
        #### time : O(n) — each index from 0 to n−1 is computed at most once
        #### space: O(n) — for both the recursion stack and the cache array
        cache = [0] * (n + 1)
        def dfs(i):
            # Base case: past the end → invalid path
            if i > n:
                return 0
            # Base case: exactly at step n → valid way
            if i == n:
                return 1
            
            # If already computed, reuse cached result
            if cache[i] != -1:
                return cache[i]
            
            # Recursive Case: sum of ways from taking 1 step and 2 steps
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        
        return dfs(0) # Start climbing from step 0


        
            