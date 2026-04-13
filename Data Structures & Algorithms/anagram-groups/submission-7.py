class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## Regular Dictionary: time O(n * k) space O(n * k)
        #### n = length of strs list
        #### k = max length of word
        dict = {}
        for str in strs:
            cnts = [0] * 26
            
            for char in str:
                cnts[ord(char) - ord('a')] += 1
            
            dict.setdefault(tuple(cnts), []) # tuple() makes the list hashable & immutable, so it can be used as a key
            dict[tuple(cnts)].append(str)

        return dict.values()


        ## Default Dictionary: time O(n * k) space O(n * k)
        #### n = length of strs list
        #### k = max length of word
        # dict = defaultdict(list)
        # for str in strs:
        #     cnts = [0] * 26
            
        #     for char in str:
        #         cnts[ord(char) - ord('a')] += 1
            
        #     dict[tuple(cnts)].append(str)
        
        # return dict.values()