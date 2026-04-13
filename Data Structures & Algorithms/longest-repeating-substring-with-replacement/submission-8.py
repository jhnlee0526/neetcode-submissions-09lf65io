class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # [Sliding Window]
        #   Time : O(n)
        #       - Each character is visited at most twice (expand/shrink window)
        #   Space: O(26) → O(1)
        #       - Fixed alphabet size (uppercase A–Z)

        maxLength = 0
        strCnt = {} # window - {str : cnt, ..}
        l = 0
        for r in range(len(s)):
            # expand window
            strCnt[s[r]] = strCnt.get(s[r], 0) + 1
            
            # slide/shrink window : must be "<= k" because of "upto k"
            while (r - l + 1) - max(strCnt.values()) > k:
                strCnt[s[l]] -= 1
                l += 1
            
            # update maxLength
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength
