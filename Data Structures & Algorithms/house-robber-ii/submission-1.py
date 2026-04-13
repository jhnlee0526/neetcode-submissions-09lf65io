class Solution:
    def rob(self, nums: List[int]) -> int:
        # top-down DP recursively (DFS) with memoization
        #   Time : O(n) — each index computed once per subproblem
        #   Space: O(n) — memo + recursion stack
        
        # edge case : only one house
        if len(nums) == 1:
            return nums[0]

        def dfs(i, start, memo):
            # base case
            if i < start:   ##
                return 0
            
            if i in memo:                       # memoization/cache makes O(n) time
                return memo[i]
            
            ''' Option 1: skip current house → dfs(i - 1)
                Option 2: rob current house  → dfs(i - 2) + nums[i]
                => O(n) time due to memoization '''
            memo[i] = max(dfs(i - 1, start, memo), dfs(i - 2, start, memo) + nums[i])
            return memo[i]
        
        # Exclude the first house
        memo1 = {}                              # cache, {house : maxAmount, ...}
        case1 = dfs(len(nums) - 1, 1, memo1)    # dfs from the last house
        
        # Exclude the last house
        memo2 = {}                              # cache, {house : maxAmount, ...}
        case2 = dfs(len(nums) - 2, 0, memo2)    # dfs from the second to the last house

        return max(case1, case2)
        
