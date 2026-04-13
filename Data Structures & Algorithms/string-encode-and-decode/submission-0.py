class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f'{len(s)}#{s}' for s in strs)
        # 4#neet4#code4#love3#you

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): # 4#neet4#code4#love3#you
            # Find the position of the delimiter '#'
            j = s.index('#', i)
            # Get the length of the next string
            leng = int(s[i:j]) # 4
            # Move the pointer to the start of the string after the '#'
            i = j + 1
            # Extract the string using the length
            res.append(s[i:i + leng])
            # Move the pointer past the current string
            i += leng
        return res
