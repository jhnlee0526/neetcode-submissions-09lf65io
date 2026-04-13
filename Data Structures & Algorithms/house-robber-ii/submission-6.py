class Solution:
    def rob(self, nums: List[int]) -> int:
        # [Memoization] Top-down DFS recursively
        #   Time : O(n)
        #   Space: O(n) - memoization & recursion stack
        
        # edge case
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        memo1, memo2 = {}, {}   ## cache - {i : maxAmt, ..}
        
        def dfs(i, end, memo):
            # base case
            if i > end:
                return 0
            
            if i in memo:
                return memo[i]

            ''' Option 1: rob current house + dfs(i + 2)
                Option 2: skip current house → dfs(i + 1)'''
            memo[i] = max(nums[i] + dfs(i + 2, end, memo), dfs(i + 1, end, memo))
            return memo[i]

        ''' - start from index 0 & exclude the last index
            - start from index 1 & inlucde the last index '''
        return max(dfs(0, len(nums) - 2, memo1), dfs(1, len(nums) - 1, memo2))
        
        #-----------------------
        # [Brute-Force] Top-down DFS recursively
        #   Time  : O(2^n) — exponential branching
        #   Space : O(n)   - recursion stack

        # edge cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def dfs(i, end):
            # base case
            if i > end:
                return 0
            return max(nums[i] + dfs(i + 2, end), dfs(i + 1, end))
        
        ''' - start from index 0 & exclude the last index
            - start from index 1 & inlucde the last index '''
        return max (dfs(0, len(nums) - 2), dfs(1, len(nums) - 1))
