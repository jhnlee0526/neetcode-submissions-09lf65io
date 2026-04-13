class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # [sliding window]
        # hashmap {} for window
        # l from the starting
        # for loop to find max length

        ## time : O(n)
        ## space: O(1) becuase it's only 26 characters

        maxLen = 0

        window = {} # window , {char: cnt, }
        l = 0
        for r in range(len(s)):
            # expanding window
            window[s[r]] = window.get(s[r], 0) + 1

            # sliding/shrinking window
            while (r - l + 1) - max(window.values()) > k: ## have to be <= k because of "upto k"
                window[s[l]] -= 1
                l += 1
            
            # find max length
            maxLen = max(maxLen, r - l + 1)

        return maxLen
            
