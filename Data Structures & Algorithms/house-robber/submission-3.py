class Solution:
    def rob(self, nums: List[int]) -> int:
        ## [Dynamic Programming] *Space Optimized
        #### time : O(n) 
        #### space: O(1)
        # rob1 = 0
        # rob2 = 0
        # for num in nums:
        #     # max(nums[0] + nums[2: n], nums[1 : n])
        #     rob1, rob2 = rob2, max(rob1 + num, rob2)
        # return rob2
        

        ## [Dynamic Programming] BOTTOM-UP "Iterative"
        #### time : O(n) Bottom-up iterates through the list once, updating two variables.
        #### space: O(n)
        # Step 1: Handle edge cases
        if not nums:  # If the list is empty, return 0 (nothing to rob)
            return 0
        if len(nums) == 1:  # If only one house, rob it
            return nums[0]
        
        # Step 2: Initialize `dp` array to store MAX MONEY robbed at each house
        dp = [0] * len(nums)  # Example: nums = [2,7,9,3,1] → dp = [0,0,0,0,0]
        
        # Step 3: Base cases (starting points)
        dp[0] = nums[0]  # First house → You can only rob it
        dp[1] = max(nums[0], nums[1])  # Second house → Choose max of first OR second
        
        # Step 4: Iterate through the remaining houses (start from index 2)
        for i in range(2, len(nums)):
            # Either:  
            # - Rob current house (`nums[i] + dp[i-2]`) → If robbing this house, skip previous one
            # - Skip current house (`dp[i-1]`) → If skipping, keep previous max robbed amount
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        # Step 5: Return final computed value (max robbed money at last house)
        return dp[-1]


        ## [Dynamic Programming] TOP-DOWN "Recursive"
        #### time : O(n) visits each index exactly once because Top-down prevents duplicate recursion calls using memo. 
        #### space: O(n)
        """
        < Step-by-Step Call Sequence >
            1️⃣ Initial Call: dfs(0)
                Calls dfs(2) and dfs(1)

            2️⃣ Expanding dfs(2)
                Calls dfs(4) and dfs(3)

            3️⃣ Expanding dfs(4)
                Calls dfs(6) and dfs(5), but since they exceed the array, they return 0.

            4️⃣ Backtracking:
                dfs(4) → max(nums[4] + dfs(6), dfs(5)) → max(1 + 0, 0) → 1
                dfs(3) → max(nums[3] + dfs(5), dfs(4)) → max(3 + 0, 1) → 3
                dfs(2) → max(nums[2] + dfs(4), dfs(3)) → max(9 + 1, 3) → 10
                dfs(1) → max(nums[1] + dfs(3), dfs(2)) → max(7 + 3, 10) → 10
                dfs(0) → max(nums[0] + dfs(2), dfs(1)) → max(2 + 10, 10) → 12


        < Steps(Recursive Calls with Memoization) >
            Call	dfs(i)	                        memo Update
            dfs(4)	max(1, 0) → 1	                [ -1, -1, -1, -1, 1 ]
            dfs(3)	max(3+dfs(5), dfs(4)) → 3	    [ -1, -1, -1, 3, 1 ]
            dfs(2)	max(9+dfs(4), dfs(3)) → 10	    [ -1, -1, 10, 3, 1 ]
            dfs(1)	max(7+dfs(3), dfs(2)) → 10	    [ -1, 10, 10, 3, 1 ]
            dfs(0)	max(2+dfs(2), dfs(1)) → 12	    [ 12, 10, 10, 3, 1 ]
        """
        # memo = [-1] * len(nums) # [-1, -1, -1, ...]
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     if memo[i] != -1:
        #         return memo[i]
        #     else:
        #         memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
        #     return memo[i]

        # return dfs(0)


        ## [Recursion]
        #### time : O(2^n)
        #### space: O(n)
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     return max(nums[i] + dfs(i + 2), dfs(i + 1))

        # return dfs(0)