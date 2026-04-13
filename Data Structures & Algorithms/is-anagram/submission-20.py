class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False
        
        # charMap = Counter(s)
        charMap = {}
        for char in s:
            charMap[char] = charMap.get(char, 0) + 1
        
        for char in t:
            if char in charMap:
                if charMap[char] > 1:
                    charMap[char] -= 1
                else:
                    del charMap[char]
                    
            else:
                return False
        
        return True
            