class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {} # {[0, 0, ..., cnt]: ["cat", "act", ... word]}
        for word in strs:
            cnts = [0] * 26
            for char in word:
                cnts[ord(char) - ord("a")] += 1
            dict.setdefault(tuple(cnts), []) #
            dict[tuple(cnts)].append(word) #
        return dict.values()