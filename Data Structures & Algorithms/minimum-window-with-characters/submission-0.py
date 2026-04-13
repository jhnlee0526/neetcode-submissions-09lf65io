class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # [Brute Force]
        # time : O(n² * m)	- All substrings (n^2) × character check (m)
        # space: O(m) - Hash maps for t and current window

        if t == '':     # edge case
            return ''
        
        resLen = []
        cntT = Counter(t)   # hashmap for 't' string, {char: cnt, }
        
        # "window" as [start_index, end_index]
        shortestStr = [-1, -1]
        shortestStrLen = float('inf')

        for i in range(len(s)):         # time : O(n)
            cntS = {}
            for j in range(i, len(s)):  # time : O(n)
                cntS[s[j]] = 1 + cntS.get(s[j], 0)

                # Check if current window covers all characters in 't'
                flag = True
                for c in cntT:          # time : O(m)
                    # Not enough of character 'c' in the window
                    if cntS.get(c, 0) < cntT[c]:
                        flag = False
                        break

                # If window is valid and shorter than previous shortest, update result
                if flag and (j - i + 1) < shortestStrLen:
                    shortestStr = [i, j]
                    shortestStrLen = j - i + 1

        # update the "window"
        l, r = shortestStr

        # If we found a valid window, return it; otherwise, return empty string
        return s[l : r + 1] if shortestStrLen != float('inf') else ''
