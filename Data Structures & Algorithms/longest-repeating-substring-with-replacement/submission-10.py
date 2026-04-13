class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        #   Time : O(n)
        #   Space: O(1)

        maxLen = 0

        window = {}     # {char : cnt, ..}
        l = 0
        for r in range(len(s)):
            # expand
            window[s[r]] = window.get(s[r], 0) + 1

            # slide / shrink
            while (r - l + 1) - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
