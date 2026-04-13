class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        #   time : O(p * log b) : p - # of piles, b - # of banana
        #   space: O(1)

        l, r = 1, max(piles)
        minPile = r ##

        while l <= r:
            m = l + (r - l) // 2    # mid piles

            hours = 0
            for eachP in piles:
                hours += math.ceil(eachP / m)
            
            if hours <= h:
                minPile = min(minPile, m) ##
                r = m - 1
            else:
                l = m + 1
            
        return minPile
