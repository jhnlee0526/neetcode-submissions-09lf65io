class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = defaultdict(int)
        for charS in s:
            map[charS] += 1
        
        for charT in t:
            if map[charT] > 0:
                map[charT] -= 1
            else:
                return False
        
        return True