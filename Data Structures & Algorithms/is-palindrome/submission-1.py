class Solution:
    def isPalindrome(self, s: str) -> bool:
        # [two pointer]
        # left from the start, right from the end
        # the each char has to be alphanumeric

        # time : O(n)
        # space: O(1)

        l, r = 0, len(s) - 1
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True

