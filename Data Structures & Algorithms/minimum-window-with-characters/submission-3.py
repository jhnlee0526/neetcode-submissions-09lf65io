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

            
