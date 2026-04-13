class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # [Sliding Window]
        #   time : O(n + m)  -> n = len(s), m = len(t)
        #   space: O(m)      -> for Counter(t) and window dictionary

        # edge case:
        if t == '':
            return ''
        
        cntT = Counter(t)           # hashmap for t, {char: cnt, }
        window = {}                 # window hashmap for current window in s

        # To track the best (smallest) window seen so far
        shortestIndices = [-1, -1]
        shortestIndicesLen = float('inf')

        have, need = 0, len(cntT)   # have = # of characters met, need = total unique characters in t

        l = 0                       # left pointer
        for r in range(len(s)):     # right pointer expands the window
            char = s[r]
            window[char] = window.get(char, 0) + 1

            # If current char matches the required count from t, increment 'have'
            if char in cntT and window[char] == cntT[char]:
                have += 1

            # Try to shrink the window from the left while it satisfies the condition
            while have == need:
                if (r - l + 1) < shortestIndicesLen:            # Update result if current window is SMALLER than previously found one
                    shortestIndices = [l, r]
                    shortestIndicesLen = r - l + 1

                # Shrink / Sliding window
                window[s[l]] -= 1                               # Remove the leftmost character from the window
                if s[l] in cntT and window[s[l]] < cntT[s[l]]:  # If removing it makes the window invalid, decrement 'have'
                    have -= 1
                l += 1                                          # move left pointer to shrink window

        # unpack final best window indices
        l, r = shortestIndices

        return s[l : r + 1] if shortestIndicesLen != float('inf') else ''

######################################################
        # [Brute Force]
        #   time : O(n² * m)    - All substrings (n^2) × character check (m)
        #   space: O(m)         - Hash maps for t and current window

        # edge case
        if t == '':
            return ''

        cntT = Counter(t)                                   # hashmap for t, {char: cnt, }

        # "shortestIndices" as [start_index, end_index]
        shortestIndices = [-1, -1]
        shortestIndicesLen = float('inf')

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
            
                # If "shortestIndices" is valid and shorter than previous shortest, update result
                if flag and (j - i + 1) < shortestIndicesLen:
                    shortestIndices = [i , j]
                    shortestIndicesLen = j - i + 1
        
        # Unpack "shortestIndices" indices
        l, r = shortestIndices
    
        return s[l : r + 1] if shortestIndicesLen != float('inf') else ''
