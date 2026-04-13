class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #   Time : O(n) - visits each char once
        #   Space: O(n) - hashmap

        # edge case
        if len(s) != len(t):
            return False

        strMap = Counter(s) # {char : cnt, ..}

        for each in t:
            if each not in strMap:
                return False
            
            strMap[each] -= 1
            
            if strMap[each] == 0:
                del strMap[each]
        
        return len(strMap) == 0
