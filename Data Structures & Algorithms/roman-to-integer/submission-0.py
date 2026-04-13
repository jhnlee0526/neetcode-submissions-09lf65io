class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping Roman numerals (single & pairs) to integers
        symMap = {
            'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
            'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
            'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
            'M': 1000
        }

        res = 0
        i = 0

        while i < len(s):
            # Check if the next two characters form a valid symbol
            if i + 1 < len(s) and s[i:i+2] in symMap:
                res += symMap[s[i:i+2]]
                i += 2
            else:
                # Otherwise just use the single character
                res += symMap[s[i]]
                i += 1

        return res
