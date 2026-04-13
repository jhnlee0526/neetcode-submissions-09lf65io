class Solution:
    def climbStairs(self, n: int) -> int:
        # dp - bottom up
        # time : O(n)
        # space: O(n)
        
        if n <= 2: # edge case
            return n

        dp = [0] * (n + 1)  # from step 0 to step n
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):   # from step3 to step n
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n] # Return the number of ways to reach step n