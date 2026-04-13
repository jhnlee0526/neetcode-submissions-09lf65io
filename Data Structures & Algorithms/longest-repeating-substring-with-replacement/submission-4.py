class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # [sliding window] OPTIMIZED with 'maxCnt'
        ## time : O(n)
        ## space: O(1) because the dictionary size never exceeds 26
        maxLen = 0
        maxCnt = 0 ##

        counts = {} # window : {char : cnt, }
        L = 0
        for R in range(len(s)):
            # expand window
            counts[s[R]] = 1 + counts.get(s[R], 0)
            maxCnt = max(maxCnt, counts[s[R]])

            # slide/shrink window
            while (R - L + 1) - maxCnt > k: # While loop until the "window length - max of counts" is greater than k
                counts[s[L]] -= 1
                L += 1
            
            # update maxLen
            maxLen = max(maxLen, R - L + 1)
        
        return maxLen


        # [sliding window]
        ## time : O(n)
        ## space: O(1) because the dictionary size never exceeds 26
        maxLen = 0

        counts = {} # window : {char : cnt, }
        L = 0
        for R in range(len(s)):
            # expand window
            counts[s[R]] = 1 + counts.get(s[R], 0)

            # slide/shrink window
            while (R - L + 1) - max(counts.values()) > k: # While loop until the "window length - max of counts" is greater than k
                counts[s[L]] -= 1
                L += 1
            
            # update maxLen
            maxLen = max(maxLen, R - L + 1)
        
        return maxLen