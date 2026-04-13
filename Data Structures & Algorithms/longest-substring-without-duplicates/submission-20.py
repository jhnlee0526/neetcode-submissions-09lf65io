class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        #   Time : O(n)
        #   Space: O(1)

        maxLen = 0

        window = set()  # window
        l = 0
        for r in range(len(s)):
            while s[r] in window:   # slide / shrink
                window.remove(s[l])
                l += 1
            window.add(s[r])        # expand
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
            