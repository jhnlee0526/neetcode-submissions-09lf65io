class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            strLen = int(s[i : j])  #
            strVal = s[j + 1 : j + 1 + strLen]
            res.append(strVal)
            i = j + 1 + strLen  #
        return res