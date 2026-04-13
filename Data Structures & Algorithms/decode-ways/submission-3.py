class Solution:
    def numDecodings(self, s: str) -> int:
        # [Brute Force] Top-down DFS recursively
        #   Time : O(2^n)
        #       - At each index i, you can branch to i+1 or i+2
        #       - This creates a binary tree of calls → exponential growth
        #   Space: O(1)

        # edge case
        if not s :
            return 0

        def dfs(i):
            # base cases
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            cnt = dfs(i + 1)        # O(n^2) time
            if (
                i + 1 <= len(s) - 1 and
                10 <= int(s[i : i + 2]) <=26
            ): 
                cnt += dfs(i + 2)   # O(n^2) time
            
            return cnt

        return dfs(0)