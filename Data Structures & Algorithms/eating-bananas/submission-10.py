class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search

        L, R = 1, max(piles)
        minPiles = R

        while L <= R:
            m = (L + R) // 2
            
            # set up for the hours thru piles
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)    # partially eat also counts as 1 hour
            
            if hours <= h: # if hours take 'h' hours or less, update minPiles, and keep try slower speed(eat less)
                minPiles = min(minPiles, m)
                R = m - 1
            else:
                L = m + 1
            
        return minPiles




        return minPiles