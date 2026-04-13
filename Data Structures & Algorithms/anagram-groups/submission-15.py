class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap
        #   time : O(n * k) - n: # of strings, k: max length of a string
        #   space: O(n * k) - store all strings in hashmap

        stringMap = {}  # {[0,0, ...]"alphabet key" : [str1, str2, ...], ...}
        for str in strs:
            # set up the alphabet key
            key = [0] * 26 # 26 alphabets
            for char in str:
                key[ord(char) - ord('a')] += 1 
            key = tuple(key)

            if key not in stringMap:
                stringMap[key] = []
            stringMap[key].append(str)

        return [ stringArr for stringArr in stringMap.values() ]