class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hashmap
        #   time : O(n * k), n = # of string, k = max length of string
        #   space: O(n * k), stores all strings in hashmap

        stringMap = {}  # {stringKey : stringList, [0,0,..] : [str1,str2, ..], ..}
        
        for str in strs:
            stringKey = [0] * 26    # 26 alphabets
            for char in str:
                stringKey[ord(char) - ord('a')] += 1
            stringKey = tuple(stringKey) ##

            if stringKey not in stringMap:
                stringMap[stringKey] = []
            stringMap[stringKey].append(str)
        
        return [ stringList for stringList in stringMap.values()]
        