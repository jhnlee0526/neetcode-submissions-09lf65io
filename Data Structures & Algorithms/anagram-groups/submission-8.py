class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charMap = {} # {[0, ..., 0]: [str1, str2, ... ], }
        for curStr in strs:
            cnts = [0] * 26
            for char in curStr:
                cnts[ord(char) - ord('a')] += 1
            
            charMap.setdefault(tuple(cnts), [])
            # if tuple(cnts) not in charMap:
            #     charMap[tuple(cnt)] = []
            charMap[tuple(cnts)].append(curStr)
        
        return list(charMap.values())
            
        

