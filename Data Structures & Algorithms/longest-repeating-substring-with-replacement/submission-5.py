class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding Window
        ## time : O(n)
        ## space: O(1)

        maxLen = 0

        charCnts = {}   # window : {char, cnt}
        L = 0
        for R in range(len(s)):
            # expand the window
            charCnts[s[R]] = charCnts.get(s[R], 0) + 1            

            # sliding the window
            while (R - L + 1) - max(charCnts.values()) > k:     # slide until it finds '<= k'
                charCnts[s[L]] -= 1
                L += 1
            
            maxLen = max(maxLen, R - L + 1)

        return maxLen