class Solution:
    def numDecodings(self, s: str) -> int:
        # [Memoization / cache] Top-down DFS recursively 
        #   Time : O(n) - each index is computed once due to memoization
        #   Space: O(n) - memoization + recusion stack

        # edge case
        if not s:
            return 0
        
        memo = {}   # cache - {i: count of ways from index i, ..}

        def dfs(i):
            # base case
            if i == len(s):     # after decoding the last character → count this path
                return 1
            if s[i] == '0': # '0' not in map
                return 0

            if i in memo:   # memoization / cache
                return memo[i]
            
            cnt = dfs(i + 1)        # one-digit decode
            if (
                i + 1 <= len(s) - 1 and
                10 <= int(s[i : i + 2]) <= 26
            ):
                cnt += dfs(i + 2)   # ADD two-digit decode
            
            memo[i] = cnt   # save cnt to memo/cache
            return memo[i]

        return dfs(0)   # index