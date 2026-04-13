class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #   Time : O(n * k) — n = number of strings, k = max length of a string
        #   Space: O(n * k) — stores all strings in hash map buckets

        strMap = {} # {[ord(char) - ord('a'), ..] : [str, ..], }
        for str in strs:
            arr = [0] * 26 # 26 alphabets
            for char in str:
                arr[ord(char) - ord('a')] += 1
            key = tuple(arr)

            if key not in strMap:
                strMap[key] = []
            strMap[key].append(str)
        
        return [strArr for strArr in strMap.values()]