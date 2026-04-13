class Solution:
    def climbStairs(self, n: int) -> int:
        ## I LOVE THESE SOLUTIONS.
        
        ## dp (bottom up) : SPACE OPTIMIZATION!!
        if n <= 2: ## edge case!
            return n

        one = 1    # ways to reach step 1
        two = 2    # ways to reach step 2

        for i in range(3, n + 1): #start from three up to (n + 1)*
            one, two = two, one + two  # shift the window forward

        return two  # two now holds the number of ways to reach step n


        ## dp (bottom up) 
        # if n <= 2: ## edge case!
        #     return n

        # dp = [0] * (n + 1) ## n + 1
        # dp[1] = 1
        # dp[2] = 2

        # for i in range(3, n + 1): ## n + 1
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n] ##