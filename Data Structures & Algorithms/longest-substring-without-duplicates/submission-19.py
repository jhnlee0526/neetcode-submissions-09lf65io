class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        #   Time : O(n)
        #   Space: O(1)

        maxLen = 0

        window = set()
        l = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
            