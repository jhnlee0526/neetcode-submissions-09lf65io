class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        #   time : O(n)
        #   space: O(1) b/c 26 characters

        longestLen = 0

        strCnt = {}     # Window, {str : cnt, }
        l = 0
        for r in range(len(s)):
            # Expand the strCnt(window)
            strCnt[s[r]] = strCnt.get(s[r], 0) + 1

            # Slide/shrink the strCnt(window)
            while (r - l + 1) - max(strCnt.values()) > k:   ## have to be <= k because of "upto k"
                strCnt[s[l]] -= 1
                l += 1

            # Update longestLen
            longestLen = max(longestLen, r - l + 1)

        return longestLen
        