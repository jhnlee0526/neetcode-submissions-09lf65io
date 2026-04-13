class Solution:
    def countSubstrings(self, s: str) -> int:
        # Two Pointers (Expand Around Center)
        #   Time : O(n^2) — Each center can expand up to n times.
        #   Space: O(1) — No extra space beyond variables.

        self.cnt = 0

        def isPalindromic(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.cnt += 1
                # move two pointers
                l -= 1
                r += 1
        
        for i in range(len(s)):
            isPalindromic(i, i)     # odd length
            isPalindromic(i, i + 1) # even length

        return self.cnt