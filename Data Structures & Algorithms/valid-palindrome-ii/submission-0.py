class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                skipL = s[left + 1 : right + 1]
                skipR = s[left : right]
                # checking the palindrome using reverse / [::-1]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
                
            left = left + 1
            right = right - 1
        return True
                    
                