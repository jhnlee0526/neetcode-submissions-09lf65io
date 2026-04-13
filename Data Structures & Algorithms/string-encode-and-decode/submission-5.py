class Solution:

    def encode(self, strs: List[str]) -> str:
        # "4#word3#char ..."
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
            
            # now j is at '#'
            strLen = int(s[i : j])
            strVal = s[j + 1 : j + 1 + strLen]  # 'j + 1 + strLen' is on next number
            
            res.append(strVal)
            i = j + 1 + strLen

        return res