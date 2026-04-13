class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        maxlen = 0

        window = set()
        l = 0
        for r in range(len(s)):
            while s[r] in window:   ##
                window.remove(s[l])
                l += 1
            
            window.add(s[r])
            maxlen = max(maxlen, r - l + 1)

        return maxlen