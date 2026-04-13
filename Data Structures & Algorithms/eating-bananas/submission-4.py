class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minPile = r

        while l <= r:
            k = (l + r) // 2
            totalHours = 0

            for curPile in piles:
                totalHours += math.ceil(curPile / k)
            
            if totalHours <= h:
                minPile = min(minPile, k)
                r = k - 1
            else:
                l = k + 1
            
        return minPile