class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = defaultdict(int)
        for charS in s:
            dict[charS] += 1
        for charT in t:
            if dict[charT] >= 1:
                dict[charT] -= 1
            else:
                return False
        return True