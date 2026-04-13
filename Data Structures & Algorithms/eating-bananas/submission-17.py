class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        #   Time :
        #   Space:

        l, r = 1, max(piles)
        while l <= r:
            m = l + (r - l) // 2

            hours = 0
            for curPile in piles:
                hours += math.ceil(curPile / m)   # cur pile / mid pile
            
            if hours <= h:   # finished within time -> go slower
                r = m - 1
            else:           # finished later -> go faster
                l = m + 1
        
        return l