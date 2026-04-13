class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap
        #   Time : O(n * k) 
        #       n = number of strings 
        #       k = max length of a string
        #   Space: O(n * k) — stores all strings in hash map buckets

        str_map = {}    # {[0, 0, ..] : [str1, str2, ..], ..}
        for str in strs:
            key = [0] * 26  # 26 alphabets
            for char in str:
                key[ord(char) - ord('a')] += 1
            key = tuple(key)

            if key not in str_map:
                str_map[key] = []
            str_map[key].append(str)
        
        return [ str_arr for str_arr in str_map.values()]