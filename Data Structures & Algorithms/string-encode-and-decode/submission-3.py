class Solution:
    # time complexity : O(n)
    def encode(self, strs: List[str]) -> str:
        res = '' 
        for curStr in strs:
            res += str(len(curStr)) + '#' + curStr
        return res # '4#neet4#code4#love3#you'

    # time complexity : O(n)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # First, find the position of the delimiter '#'
            while s[j] != '#':
                j += 1
            strLength = int(s[i : j])  # Now it's safe to convert to int
            res.append(s[j + 1 : j + 1 + strLength])  # Extract the string
            i = j + 1 + strLength  # Move to the next encoded string

        return res