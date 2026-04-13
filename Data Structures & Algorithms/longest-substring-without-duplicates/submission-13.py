class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        #   time : O(n)
        #   space: O(n)

        maxlength = 0
        
        strset = set()  # window
        l = 0
        for r in range(len(s)):
            while s[r] in strset:   ##
                strset.remove(s[l])
                l += 1
            
            strset.add(s[r])
            maxlength = max(maxlength, r - l + 1)   ##
        
        return maxlength