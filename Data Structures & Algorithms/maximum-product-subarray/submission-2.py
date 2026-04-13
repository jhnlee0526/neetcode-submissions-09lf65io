class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # [Memoization / Cache] Top-down DFS recursively
        #   Time :
        #   Space:
        '''
        Why Memoization Isn’t Very Helpful Here
            The product depends on the entire path, not just the index.
            So caching memo[i] doesn’t avoid much work — each DFS path has unique state.
        '''
        #----------------------------
        # [Brute Force] Top-down DFS recursively
        #   Time : O(N^2)
        #       - For each index, we explore all subarrays starting there
        #       - Each DFS call multiplies forward → total ~N + (N-1) + ... + 1 = O(N^2)
        #   Space: O(N)
        #       - Recursion stack depth in worst case

        # edge case
        if not nums:
            return 0
        
        self.maxProd = float('-inf')

        def dfs(i, curProd):
            # base case : out of bounds
            if i > len(nums) - 1:
                return
            
            curProd *= nums[i]
            self.maxProd = max(self.maxProd, curProd)

            dfs(i + 1, curProd)

        # Try starting DFS() from every index
        for i in range(len(nums)):
            dfs(i, 1)   # index, current prod(reset as 1)

        return self.maxProd