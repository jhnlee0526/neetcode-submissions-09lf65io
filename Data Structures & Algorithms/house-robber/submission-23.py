class Solution:
    def rob(self, nums: List[int]) -> int:
        # # ✅ Bottom-Up DP iteratively — OPTIMAL SPACE (O(1))
        #   Time : O(n) — iterate through all houses once
        #   Space: O(1) — only two variables tracked

        rob1 = 0  # max money robbed from houses 0 to i-2
        rob2 = 0  # max money robbed from houses 0 to i-1

        # Compute max if we rob this house (rob1 + amount) vs skip it (rob2)
        for amount in nums:
            rob1, rob2 = rob2, max(rob2, rob1 + amount)
            ''' After this line:
                - rob1 becomes previous rob2 (i-1)
                - rob2 becomes MAX MONEY robbed up to current house (i) '''

        # rob2 now holds the max money robbed from all houses
        return rob2

        #------------------------------------------
        # ✅ Bottom-Up DP iteratively — Tabulation (dp list)
        #   Time : O(n) — iterate through all houses once
        #   Space: O(n) — store max robbed at each index

        n = len(nums)
        # edge case: 1) No houses to rob 2) Only one house, rob it
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n                    # dp[i] = max money robbed from house 0 to i
        dp[0] = nums[0]                 # base case: rob first house
        dp[1] = max(nums[0], nums[1])   # rob max of first vs. second house

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            '''Option 1: skip current house → dp[i - 1]
               Option 2: rob current house  → dp[i - 2] + nums[i]'''

        return dp[-1]                   # final result: max money robbed from all houses

        ######################################
        # # ✅ Top-Down DP recursively — Memoization (DFS) [Optimized Recursion]
        #   Time : O(n) — each index computed once and cached
        #   Space: O(n) — recursion stack + memo dictionary

        memo = {}                   # cache, {house: maxAmount, ...}

        def dfs(i):
            if i < 0:               # Base case: no houses left to rob
                return 0

            if i in memo:           # Return cached result if already computed
                return memo[i]
            '''
                Option 1: skip current house → dfs(i - 1)
                Option 2: rob current house  → dfs(i - 2) + nums[i]
            '''
            memo[i] = max(dfs(i - 1), dfs(i - 2) + nums[i])
            return memo[i]
        
        return dfs(len(nums) - 1)   # Start recursion from the LAST house


        #------------------------------------------
        # ❌ Top-Down DP recursively - Brute Force
        #   Time : O(2^n) — each house has TWO choices: rob or skip, leading to exponential growth
        #   Space: O(n)   — recursion stack depth in worst case

        def dfs(i):
            if i < 0:               # Base case: no houses left to rob
                return 0
            '''
                Option 1: skip current house → dfs(i - 1)
                Option 2: rob current house  → dfs(i - 2) + nums[i]
            '''
            return max(dfs(i - 1), dfs(i - 2) + nums[i])    # O(2^n) time
        
        return dfs(len(nums) - 1)   # Start recursion from the LAST house



