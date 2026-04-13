class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap
        #   Time : O(n)
        #   Space: O(n)

        sMap = Counter(s)   # {char : cnt, ..}
        tMap = Counter(t)
        
        return True if sMap == tMap else False