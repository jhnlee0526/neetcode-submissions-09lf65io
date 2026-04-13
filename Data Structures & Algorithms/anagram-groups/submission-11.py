class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap {[0, 0, ..., ord(char) - ord('a')] : [str1, str2, ...], }
        # return list of values in hashmap

        # time : O(m * n)
        # space: O(m * n)
        #   m = length of input list
        #   n = max length of word  

        strMap = {}
        
        for str in strs:
            cnt = [0] * 26
            for char in str:
                cnt[ord(char) - ord('a')] += 1
            
            strMap.setdefault(tuple(cnt), [])
            strMap[tuple(cnt)].append(str)
        
        return list(strMap.values())
        