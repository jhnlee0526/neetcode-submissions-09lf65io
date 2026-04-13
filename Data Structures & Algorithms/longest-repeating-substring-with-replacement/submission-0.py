class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## [Sliding Window]
        #### time : O(n)
        #### space: O(1) because the dictionary size never exceeds 26
        counts = {}
        longestLength = 0

        l = 0
        for r in range(len(s)):
            # Expanding the window
            counts[s[r]] = 1 + counts.get(s[r], 0)
            
            # While loop until the "window length - max of counts" is greater than k
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1 # decrease the counts of the val at "l"
                l += 1 # shrink / sliding window

            # assign the longest length
            longestLength = max(longestLength, r - l + 1) # r - l + 1 is the length of window
        
        return longestLength