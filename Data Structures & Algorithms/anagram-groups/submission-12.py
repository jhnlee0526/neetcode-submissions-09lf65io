class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        strMap = {} # {[0,0, .., ord[char] - ord['a']] : [str1, str2, ..], }

        # set up the key using ord()
        for str in strs:
            arrKey = [0] * 26   # 26 alphabets
            for char in str:
                arrKey[ord(char) - ord('a')] += 1
            
            key = tuple(arrKey)
            if key not in strMap:
                strMap[key] = []
            strMap[key].append(str)

        return [each for each in strMap.values()]
            
