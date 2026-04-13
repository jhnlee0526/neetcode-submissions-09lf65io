class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # [sliding window] with set() checking duplication
        # set() for window
        # 'l' pointer starting from 0
        # for loop to find the max length

        ## time : O(n)
        ## sapce: O(n)

        maxLen = 0
        
        window = set()
        l = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            
            maxLen = max(maxLen, r - l + 1)

        return maxLen