class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #   Time : O(n) - visits each char once
        #   Space: O(n) - hashmap

        strMap = Counter(s) # {char : cnt, ..}

        for each in t:
            if each in strMap:
                if strMap[each] > 1:
                    strMap[each] -= 1
                else:
                    del strMap[each]
            else:
                return False
        
        return len(strMap) == 0
