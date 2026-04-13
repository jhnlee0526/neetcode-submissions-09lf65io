class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        pt1, pt2 = 0, 0
        while pt1 < len(word1) and pt2 < len(word2):
            res += word1[pt1] + word2[pt2]
            pt1 += 1
            pt2 += 1
        
        if pt1 < len(word1):
            res += word1[pt1:]
        if pt2 < len(word2):
            res += word2[pt2:]
        
        return res