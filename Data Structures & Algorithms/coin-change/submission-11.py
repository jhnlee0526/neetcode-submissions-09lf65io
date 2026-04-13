class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # [Tabulation / DP list] Bottom-up DP iteratively
        #   Time : O(S × A)
        #       - S = number of coin types
        #       - A = target amount
        #       - For each amount, we try all coins
        #   Space: O(A)
        #       - DP array of size (amount + 1)

        if not coins:
            return -1
        
        # dp[i] = min coin count, i = amount // [0, _, _, _, ...]
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0   # base case: no coins needed for amount 0

        for curAmt in range(1, amount + 1):
            minCnt = float('inf')   # reset for each amount : infinity (unreachable)
            # Try all coin choices and track the minimum count
            for coin in coins:
                remain = curAmt - coin
                if remain >= 0:
                    minCnt = min(minCnt, 1 + dp[remain])    # use 1 coin + recurse                
            
            dp[curAmt] = minCnt
        
        return -1 if dp[amount] == float('inf') else dp[amount]


        ################################
        # [Memoization / Cache] Top-down DFS recursively
        #   Time : O(S * A)
        #       - S = number of coin types
        #       - A = target amount
        #       - Each amount is computed ONCE and cached
        #   Space: O(A)
        #       - Memoization dictionary + recursion stack depth

        # Edge case: no coins means no solution
        if not coins:
            return -1
        
        memo = {}   # Cache - {amount : min coin count, ..}

        def dfs(amt):
            # base cases
            if amt == 0:    # exact match → no coins needed
                return 0
            if amt < 0:     # overshot → invalid path
                return float('inf')
            
            if amt in memo: # Memoization
                return memo[amt]

            # Try all coin choices and track the minimum count
            minCnt = float('inf')
            for coin in coins:
                remain = amt - coin
                if remain >= 0:
                    minCnt = min(minCnt, 1 + dfs(remain))   # use 1 coin + recurse
            
            memo[amt] = minCnt
            return memo[amt]
        
        res = dfs(amount) # Start DFS from the full amount
        return -1 if res == float('inf') else res   # If no valid path, return -1

        
        #--------------------------------
        # [Brute-Force] Top-down DFS recursively
        #   Time : O(S^A)
        #       - S = number of coin types
        #       - A = amount
        #       - Each amount can branch into S choices → exponential growth
        #   Space: O(A)
        #       - Max recursion depth is amount (worst case: using 1 repeatedly)

        # edge case
        if not coins:
            return -1
        
        def dfs(amt):
            # base case
            if amt == 0:    # exact match → no more coins needed
                return 0
            if amt < 0:     # overshot → invalid path
                return float('inf')
            
            # Try all coin choices and track the minimum count
            minCnt = float('inf')   # max number
            for coin in coins:
                remain = amt - coin
                if remain >= 0:
                    # Use 1 coin now + recurse on remaining amount
                    minCnt = min(minCnt, 1 + dfs(remain))
            
            return minCnt
        
        # Start DFS from the FULL AMOUNT
        res = dfs(amount)

        # If valid path is not found, return -1
        return -1 if res == float('inf') else res

