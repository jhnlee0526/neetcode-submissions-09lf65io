class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## Regular Dictionary time: O(n) space: O(n) ##
        # if len(s) != len(t):
        #     return False

        # dict = {}
        # for char in s:
        #     dict[char] = dict.get(char, 0) + 1

        # for char in t:
        #     if dict.get(char, 0) > 0:
        #         dict[char] -= 1
        #     else:
        #         return False
        
        # return True

        ## Default Dictionary time: O(n) space: O(n) ##
        if len(s) != len(t):
            return False

        dict = defaultdict(int)
        for char in s:
            dict[char] += 1
        
        for char in t:
            if dict[char] > 0:
                dict[char] -= 1
            else:
                return False
        
        return True
