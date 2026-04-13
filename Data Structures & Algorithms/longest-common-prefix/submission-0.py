class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ## Vertical Scanning: Time O(n * m) Space O(m)
        #### n = # of strings/items in strs
        #### m = length of the shortest string
        
        res = ""
        for i in range(len(strs[0])):
            for eachStr in strs:
                # if i is out of bound OR ...
                if i == len(eachStr) or eachStr[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res 