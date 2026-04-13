class Solution:

    def encode(self, strs: List[str]) -> str:
        # 4#neet4#code4#love3#you
        
        # edge case
        if not strs:
            return ''
        
        res = ''
        for str in strs:
            cnt = len(str)
            res += f'{cnt}#{str}'
        return res


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i : j])
            string = s[j + 1 : j + 1 + length]
            
            res.append(string)
            
            i = j + 1 + length
        
        return res


                
                