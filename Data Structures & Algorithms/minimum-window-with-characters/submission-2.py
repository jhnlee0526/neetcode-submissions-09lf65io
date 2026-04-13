class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # [Brute Force]
        #   time : O(n² * m)    - All substrings (n^2) × character check (m)
        #   space: O(m)         - Hash maps for t and current window

        # edge case
        if t == '':
            return ''

        cntT = Counter(t)                                   # hashmap for t, {char: cnt, }

        # "window" as [start_index, end_index]
        window = [-1, -1]
        windowLen = float('inf')

        for i in range(len(s)):                             # O(n)
            # set up the cntS hashmap
            cntS = {}                                       # hashmap for 's' string, {char: cnt, }
            for j in range(i, len(s)):                      # O(n)
                cntS[s[j]] = cntS.get(s[j], 0) + 1

                # Check if current window covers all characters in 'eachT'
                flag = True
                for eachT in cntT.keys():                   # O(m)
                    if cntS.get(eachT, 0) < cntT[eachT]:    # Not enough of character 'eachT' in the window
                        flag = False
                        break
            
                # If window is valid and shorter than previous shortest, update result
                if flag and (j - i + 1) < windowLen:
                    window = [i , j]
                    windowLen = j - i + 1
        
        # Unpack "window" indices
        l, r = window
    
        return s[l : r + 1] if windowLen != float('inf') else ''

            