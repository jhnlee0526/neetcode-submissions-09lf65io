class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list) # { [0, 0, 0, ..., 0]:["act", "cat", ...]}
        for word in strs:
            each = [0] * 26
            for char in word:
                each[ord(char) - ord("a")] += 1
            dict[tuple(each)].append(word)
        return dict.values()
