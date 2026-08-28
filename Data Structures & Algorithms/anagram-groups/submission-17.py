class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {} # {[0,...,0] : [str1, str2, ..], ...}
        
        for each in strs:
            key = [0] * 26
            for char in each:
                key[ord(char) - ord('a')] += 1
            key = tuple(key)

            if key not in strMap:
                strMap[key] = []
            
            strMap[key].append(each)

        return [val for key, val in strMap.items()]