class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charMap = {} # {[0,...,0] : [str, ...], }
        for str in strs:
            cnt = [0] * 26
            # set up the cnt for the current string
            for char in str:
                cnt[ord(char) - ord('a')] += 1
            
            charMap.setdefault(tuple(cnt), [])
            charMap[tuple(cnt)].append(str)

        return list(charMap.values())
        
