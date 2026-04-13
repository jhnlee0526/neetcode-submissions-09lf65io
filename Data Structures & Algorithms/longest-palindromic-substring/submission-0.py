class Solution:
    def longestPalindrome(self, s: str) -> str:
        ## Two Pointers (start from the middle, and l & r expand outwards)
        #### Time: O(n^2)
        #### Space: O(1)
        
        res = ""
        maxLen = 0

        def isPalindromic(l, r):
            nonlocal res, maxLen
            # starting from the middle, expanding outwards while it's palindromic
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # if the current length is greater than maxLen, update
                if r - l + 1 > maxLen:
                    res = s[l : r + 1]
                    maxLen = r - l + 1
                # expand outwards
                l -= 1
                r += 1

        for i in range(len(s)):
            isPalindromic(i, i)     # odd-length palindromes
            isPalindromic(i, i + 1) # even-length palindromes

        return res

