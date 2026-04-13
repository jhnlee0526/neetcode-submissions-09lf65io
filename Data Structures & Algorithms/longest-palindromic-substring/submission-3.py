class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointers (starting from the middle, and expanding outter)
        res = ''
        maxLen = 0

        def isPalindromic(l, r):
            nonlocal res, maxLen

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if maxLen < r - l + 1:
                    res = s[l : r + 1]
                    maxLen = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            isPalindromic(i, i)    # odd#
            isPalindromic(i, i + 1)    # even#

        return res
