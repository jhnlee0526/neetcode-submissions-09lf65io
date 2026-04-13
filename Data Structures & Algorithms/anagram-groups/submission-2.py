class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## using defaultdict(): time O(m*n*26)
        # dict = defaultdict(list) #{[0,0,...,0]: ["act", "cat"], }
        # for str in strs:
        #     cnts = [0] * 26
        #     for s in str:
        #         cnts[ord(s) - ord("a")] += 1
        #     cnts = tuple(cnts)
        #     dict[cnts].append(str)
        # return dict.values()

        ## using regular dictionary: time O(m*n*26)
        dict = {} #{[0,0,...,0]: ["act", "cat"], }
        for str in strs:
            cnts = [0] * 26
            for s in str:
                cnts[ord(s) - ord("a")] += 1
            cnts = tuple(cnts)
            dict.setdefault(cnts, []) #needs for regular dict
            dict[cnts].append(str)
        return dict.values()