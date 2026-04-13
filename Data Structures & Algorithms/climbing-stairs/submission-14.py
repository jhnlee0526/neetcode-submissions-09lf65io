class Solution:
    def climbStairs(self, n: int) -> int:
        ## dp (bottom up) with space optimization
        one = 1
        two = 1
        for i in range(n - 1): ## n - 1
            one, two = two, one + two

        return two
        
        
        ## dp (bottom up) 
        # if n <= 2: ## edge case!
        #     return n

        # dp = [0] * (n + 1) ## n + 1
        # dp[1] = 1
        # dp[2] = 2

        # for i in range(3, n + 1): ## n + 1
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n] ##