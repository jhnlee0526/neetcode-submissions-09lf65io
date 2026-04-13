class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        maxLen = 0
        window = set()
        L = 0
        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            maxLen = max(maxLen, R - L + 1)

        return maxLen