class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):    # base case
            return False

        strMap = Counter(s)
        for char in t:
            if char in strMap:
                if strMap[char] > 1:
                    strMap[char] -= 1
                else:
                    del strMap[char]

        return len(strMap) == 0
