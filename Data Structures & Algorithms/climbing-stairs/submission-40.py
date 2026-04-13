class Solution:
    def climbStairs(self, n: int) -> int:
        # "Space-optimized" Bottom-up DP iteratively (not BFS)
        #   Time : O(n)
        #   Space: O(1)*

        # edge case:
        if n < 2:
            return n
        
        one, two = 1, 2
        for i in range(3, n + 1):   # from 3 to n
            one, two = two, one + two
        
        return two  # 'two' holds the number of ways to reach step 'n'

        #----------------------------
        # [Tabulation / dp list] Bottom-up DP iteratively (not BFS)
        #   Time : O(n)
        #   Space: O(n) — dp list

        # edge case:
        if n < 2:
            return n
        
        dp = {} # {level : cnts, ...}

        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):   # start from 3 to n
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]


        ############################
        # [Memoization/Cache] Top-down DFS recusively
        #   Time : O(n)
        #   Space: O(n) for memoization & recursion stack depth

        memo = {}   # cache - {level : cnts, ..}
        def dfs(curLevel):
            # base cases
            if curLevel == n:   # valid path, return 1
                return 1
            if curLevel > n:
                return 0
            
            if curLevel in memo:    # memoization / cache
                return memo[curLevel]
            
            memo[curLevel] = dfs(curLevel + 1) + dfs(curLevel + 2) # O(n) time due to memoization
            return memo[curLevel]

        return dfs(0)

        #----------------------------
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