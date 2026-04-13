class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## [sliding window]
        #### time : O(n) → Each character is processed once
        #### space: O(k) → At most `k` unique characters stored in set
        window = set()
        l = 0
        maxLength = 0
        for r in range(len(s)): # Expand the window by moving `r`
            while s[r] in window: # while duplicate found, keep shrinking window
                window.remove(s[l])
                l += 1 # Move left pointer forward
            
            window.add(s[r]) # Add current character to window
            maxLength = max(maxLength, r - l + 1) # Update max length

        return maxLength
        