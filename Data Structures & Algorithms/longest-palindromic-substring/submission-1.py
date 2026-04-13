class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointers(start from the middle, and expand outter)
        res = ""
        maxLen = 0

        def isPalindromic(l, r):
            nonlocal res, maxLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    res = s[l : r + 1]
                    maxLen = r - l + 1
                l -= 1
                r += 1
        

        for i in range(len(s)):
            isPalindromic(i, i)     # odd count
            isPalindromic(i, i + 1) # even count
        
        return res