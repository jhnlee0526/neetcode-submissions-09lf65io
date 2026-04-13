class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## [Two Pointers]
        #### time : O(n²) → Worst-case scenario if many duplicates
        #### space: O(1) → No extra data structures used
        # l = 0 # Left pointer
        # maxLength = 0 # Tracks longest substring found

        # for r in range(len(s)): # Right pointer moves forward
        #     # Move `l` forward if there's a duplicate within the window
        #     for i in range(l, r): # Scan previous characters in window
        #         if s[i] == s[r]: # If duplicate found, update `l`
        #             l = i + 1
        #             break
        #     maxLength = max(maxLength, r - l + 1)
        # return maxLength

        
        ## **[sliding window]
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
        


            