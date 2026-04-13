class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
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

        
        #-------------------------------------------------
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

