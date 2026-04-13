class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Return False if the lengths of s and t are not equal
        # create dictionaries for S and T: dictS, dictT = {char, cnt}
        # run iteration on s:
            # if current char is not in dictS, add it with 1 cnt
            # else, increase the cnt by 1
        # run iteration on t:
            # if current char is not in dictT, add it with 1 cnt
            # else, increase the cnt by 1
        # run iteration on dictS: (comparing with dictT)
            # if current item in dictS doesn't have the same cnt as dicT, return False
        # return True

        # using regular dictionary: time O(n + m), space O(n + m)
        if len(s) != len(t):
            return False 
        dictS, dictT = {}, {}
        for char in s:
            dictS[char] = dictS.get(char, 0) + 1
        for char in t:
            dictT[char] = dictT.get(char, 0) + 1
        for char in dictS:
            if dictS[char] != dictT.get(char, 0):
                return False
        return True

        # using defaultdict: time O(n + m), space O(n + m)
        # if len(s) != len(t):
        #     return False 
        # dictS, dictT = defaultdict(int), defaultdict(int)
        # for char in s:
        #     dictS[char] += 1
        # for char in t:
        #     dictT[char] += 1
        # for char in dictS:
        #     if dictS[char] != dictT[char]:
        #         return False
        # return True