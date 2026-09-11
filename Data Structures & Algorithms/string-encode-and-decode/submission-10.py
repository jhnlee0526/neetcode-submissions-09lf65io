class Solution:

    def encode(self, strs: List[str]) -> str:
        res = '' # 'count#word'

        for word in strs:
            res += f'{len(word)}#{word}'

        return res


    def decode(self, s: str) -> List[str]:
        if not s: # edge case
            return []
        
        # s -> 5#Hello5#World
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            # j located at the '#'
            length = int(s[i : j]) # from i to (j - 1)
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            i = j + 1 + length

        return res