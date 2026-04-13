class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## binary search 
        l = 1
        r = max(piles)
        minPile = r

        while l <= r:
            k = (l + r) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                minPile = min(minPile, k)
                r = k - 1
            else:
                l = k + 1
            
        return minPile
