class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {} #{[0,0,...,0]: ["act", "cat"], }
        for str in strs:
            cnts = [0] * 26
            for s in str:
                cnts[ord(s) - ord("a")] += 1
            cnts = tuple(cnts)
            dict.setdefault(cnts, [])
            dict[cnts].append(str)
        
        return dict.values()