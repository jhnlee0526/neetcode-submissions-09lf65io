class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search
        ## ⏱️ Time: O(n · log m)
        ''' - n = number of piles
            - m = max number of bananas in a pile
            - We binary search over Koko's speed (1 to max pile size)
            - For each guess, we scan every pile → total cost = log(m) * n'''
        ## 📦 Space: O(1)
        ''' - We're just using a few variables — no extra memory based on input size'''

        L, R = 1, max(piles)
        minPile = R     # starting from the upperbound

        while L <= R:
            m = (L + R) // 2
            
            # Set up for the hours through piles
            hours = 0
            for curPile in piles:
                hours += math.ceil(curPile / m)
            
            if hours <= h:
                minPile = min(minPile, m)
                R = m - 1
            else:
                L = m + 1

        return minPile