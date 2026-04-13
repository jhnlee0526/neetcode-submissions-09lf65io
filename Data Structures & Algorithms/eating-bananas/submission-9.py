class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        L, R = 1, max(piles)
        minPiles = R # start at the upperbound

        while L <= R:
            m = (L + R) // 2
            hours = 0

            for pile in piles: # calculate hours through piles
                # Round up since partial piles take a whole hour
                hours += math.ceil(pile / m)
            
            if hours <= h: # If you can finish in 'h' hours or less, try a slower speed
                minPiles = min(minPiles, m)
                R = m - 1 # Try smaller k
            else:
                L = m + 1 # Try larger k to speed up eating

        return minPiles