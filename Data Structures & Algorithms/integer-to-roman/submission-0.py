class Solution:
    def intToRoman(self, num: int) -> str:
        # Time: O(1) — constant time since the loop iterates over a fixed symbol list (13 elements)
        # Space: O(1) — result string is bounded for num <= 3999
        symbols = [
            ['I', 1], ['IV', 4], ['V', 5], ['IX', 9], 
            ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], 
            ['C', 100], ['CD', 400], ['D', 500], ['CM', 900], 
            ['M', 1000]
        ]

        res = ""
        for curSym, curVal in reversed(symbols):  # iterate from largest to smallest
            cnt = num // curVal  # how many times curVal fits into num
            if cnt:
                res += curSym * cnt  # append the symbol cnt times
                num %= curVal  # reduce num by used value

        return res