class Solution:

    def encode(self, strs: List[str]) -> str:
        # cnt#str
        res = ''
        for str in strs:
            res += f'{len(str)}#{str}'
        return res

    def decode(self, s: str) -> List[str]:
        # edge case
        if not s:
            return []
        
        res = []
        
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i : j])
            str_val = s[j + 1 : j + 1 + length]
            res.append(str_val)

            i = j + 1 + length
        
        return res

