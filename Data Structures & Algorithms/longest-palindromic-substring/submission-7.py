class Solution:
    def longestPalindrome(self, s: str) -> str:
        # *Two Pointers (Expand Around Center)
        #   Time: O(n^2)
        #   Space: O(1)
        
        # edge cases
        if not s:
            return ''
        if len(s) == 1:
            return s

        self.palStr = ''
        self.maxLen = 0
        
        # Expand from the center
        def isPalindromic(l, r):
            while (
                l >= 0 and
                r <= len(s) - 1 and
                s[l] == s[r]
            ):
                curLen = r - l + 1  ##
                if curLen > self.maxLen:    # new max length found
                    self.palStr = s[l : r + 1]
                    self.maxLen = curLen
                l -= 1  # move pointers
                r += 1


        for i in range(len(s)):
            isPalindromic(i, i)     # odd length
            isPalindromic(i, i + 1) # even length

        return self.palStr


        #############################    
        # [Tabulation / DP list] Bottom-up DP iteratively
        #   Time :
        #   Space:
        

        
        # [Memoization / Cache] Top-down DFS recursively
        # NOT GOING TO DO IT for this question...too complicated


        #-----------------------------
        # [Brute Force] Top-down DFS recursively
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
        