class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        for charS in s:
            dict[charS] = dict.get(charS, 0) + 1
        for charT in t:
            if dict.get(charT, 0) >= 1:
                dict[charT] -= 1
            else:
                return False
        return True
        

