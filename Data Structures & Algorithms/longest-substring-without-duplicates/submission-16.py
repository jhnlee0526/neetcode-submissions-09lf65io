class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # [Sliding Window]
        #   Time : O(n)
        #       - Each character is added and removed at most once
        #   Space: O(k)
        #       - k = size of character set in window (≤ n)

        maxLength = 0

        strSet = set() # {char, ..}
        l = 0
        for r in range(len(s)):
            # shrink window until s[r] is unique
            while s[r] in strSet:
                strSet.remove(s[l])
                l += 1

            # expand window
            strSet.add(s[r])

            # update maxLength
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength
