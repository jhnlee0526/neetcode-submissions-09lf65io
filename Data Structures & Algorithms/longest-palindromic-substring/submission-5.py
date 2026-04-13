class Solution:
    def longestPalindrome(self, s: str) -> str:
        # [Brute Force] Top-down DFS iteratively
        #   Time : O(n^3)   - O(n^2) substrings * O(n) palindrome
        #   Space: O(n)     - recursion stack
        
        # edge cases
        if not s:
            return ""
        if len(s) == 1:
            return s
        
        self.res = ''

        def dfs(i):
            # base case
            if i > len(s) - 1:
                return self.res
            
            for j in range(i, len(s)):  # i: start, j: end
                substr = s[i : j + 1]               # O(n^2) time: substring
                if (
                    substr == substr[::-1] and      # O(n) time: checking palindrome
                    len(substr) > len(self.res)
                ):
                    self.res = substr
            
            return dfs(i + 1)
        
        return dfs(0)
        