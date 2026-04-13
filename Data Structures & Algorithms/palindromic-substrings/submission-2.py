class Solution:
    def countSubstrings(self, s: str) -> int:
        # Two pointers (Expand from the center)
        #   Time : O(n^2)
        #   Space: O(1)

        # edge cases
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        self.cnt = 0
    
        # expanding from the center
        def isPalindromic(l, r):
            while (
                l >= 0 and r <= len(s) - 1 and
                s[l] == s[r]
            ):
                self.cnt += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            isPalindromic(i, i)     # odd length
            isPalindromic(i, i + 1) # even length
        
        return self.cnt
        

        