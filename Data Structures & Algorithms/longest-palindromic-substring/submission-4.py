class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Two Pointers (Expand Around Center)
        #   Time: O(n^2)
        #   Space: O(1)
        
        # edge cases
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s

        self.palStr = ''
        self.maxLen = 0

        # Expand around the center
        def isPalindromic(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen = r - l + 1
                if curLen > self.maxLen:
                    self.palStr = s[l : r + 1]
                    self.maxLen = curLen
                # move two pointers
                l -= 1
                r += 1
        
        for i in range(len(s)):
            isPalindromic(i, i)     # odd length
            isPalindromic(i, i + 1) # even length

        return self.palStr
