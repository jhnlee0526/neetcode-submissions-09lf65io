class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # [Sliding Window]
        #   Time : O(n)
        #   Space: O(n)

        maxLength = 0

        strSet = set() # {char, ..}
        l = 0
        for r in range(len(s)):
            while s[r] in strSet:
                strSet.remove(s[l])
                l += 1
            strSet.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength
