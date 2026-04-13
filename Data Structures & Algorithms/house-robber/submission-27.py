class Solution:
    def rob(self, nums: List[int]) -> int:
        # [Tabulation / DP list] Bottom-up DP iteratively
        #   Time  : O(n)
        #   Space : O(n) — dp list to store max amounts

        # Edge cases
        if not nums:       # no houses
            return 0
        if len(nums) == 1: # only one house
            return nums[0]

        # dp[i] = max amount that can be robbed from house 0 to house i
        dp = [0] * len(nums)
        dp[0] = nums[0]                      # only one house to rob
        dp[1] = max(nums[0], nums[1])        # choose max of first two

        for i in range(2, len(nums)):
            # Option 1: rob current house + dp[i - 2]
            # Option 2: skip current house → dp[i - 1]
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]  # max amount from house 0 to last house


        #########################
        # [Memoization / Cache] Top-down DFS recursively
        #   Time  : O(n)
        #   Space : O(n) for memoization & recursion stack
        
        memo = {}   # {index : maxAmt, ..}

        def dfs(i):
            # base case
            if i > len(nums) - 1:
                return 0
            
            if i in memo:     # memoization / cache
                return memo[i]

            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1)) # O(n) time due to memoization/cache
            return memo[i]

        return dfs(0)


        #----------------------------
        # [Brute-Force] Top-down DFS recursively
        #   Time  : O(2^n) — exponential branching
        #   Space : O(n)   — recursion stack depth

        def dfs(i):
            # base case
            if i > len(nums) - 1:
                return 0
            return max(nums[i] + dfs(i + 2), dfs(i + 1))    # O(2^n) time for each dfs()

        return dfs(0)

