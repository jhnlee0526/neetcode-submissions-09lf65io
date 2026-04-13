class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minPile = r

        while l <= r:
            k = (l + r) // 2
            totalHours = 0

            for pile in piles:
                totalHours += math.ceil(pile / k)
            
            if totalHours <= h:
                minPile = min(minPile, k)
                r = k - 1
            else:
                l = k + 1
            
        return minPile