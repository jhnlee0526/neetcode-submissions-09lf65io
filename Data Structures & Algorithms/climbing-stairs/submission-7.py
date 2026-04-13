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
            if cache[i] > 0:
                return cache[i]
            
            # Recursive Case: sum of ways from taking 1 step and 2 steps
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        
        return dfs(0) # Start climbing from step 0


        ## [Dynamic Programming] BOTTOM-UP (iteratively)
        #### Time : O(n)
        #### Space: O(n)
        # Example: n = 5 → number of ways to reach step 5
        if n <= 2:
            return n # For n=1 → 1 way, n=2 → 2 ways
        # Create a DP array to hold the number of ways to reach each step
        cache = [0] * (n + 1)  # We need cache[0] through dp[n]

        # Base cases:
        cache[1] = 1  # One way to reach step 1: [1]
        cache[2] = 2  # Two ways to reach step 2: [1+1], [2]

        # Fill the DP table from step 3 to step n
        for i in range(3, n + 1):
            # To get to step i, you could've come from:
            # - step i-1 (taking 1 step)
            # - step i-2 (taking 2 steps)
            cache[i] = cache[i - 1] + cache[i - 2]
            # For n = 5, you’d see:
            # i = 3 → cache[3] = 2 + 1 = 3    ([1+1+1], [1+2], [2+1])
            # i = 4 → cache[4] = 3 + 2 = 5    ([1+1+1+1], [1+1+2], [1+2+1], [2+1+1], [2+2])
            # i = 5 → cache[5] = 5 + 3 = 8    (total 8 unique sequences)

        return cache[n]  # Return the number of ways to reach step n
        

        ## [Dynamic Programming] BOTTOM-UP w/ "Space Optimization"! (iteratively)
        #### Time : O(n)
        #### Space: O(1)
        # Initialize two variables to represent:
        # one → number of ways to reach the current step (cache[i - 1])
        # two → number of ways to reach the previous step (cache[i - 2])
        one, two = 1, 1
        # Loop runs n - 1 times because:
        # - We've already set up base cases for steps 1 and 2.
        # - We only need to calculate up to step n.
        for i in range(n - 1):
            temp = one          # Save current value of one
            one = one + two     # Compute new number of ways to reach the next step
            two = temp          # Move one step forward in the sequence

            # Example trace for n = 5:
            # Iter 0: one = 2, two = 1  (step 3)
            # Iter 1: one = 3, two = 2  (step 4)
            # Iter 2: one = 5, two = 3  (step 5)
            # Iter 3: one = 8, two = 5  (done!)

        # 'one' now holds the total number of distinct ways to climb n stairs
        return one
            