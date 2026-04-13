class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # bineary search
        l = 1
        r = max(piles)
        minPiles = r # res

        while l <= r:
            k = (l + r) // 2 # avgPiles
            hours = 0

            # calculate hours thru piles
            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                minPiles = min(minPiles, k)
                r = k - 1
            else:
                l = k + 1

        return minPiles

            
