class Solution:
    def rob(self, nums: List[int]) -> int:
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

