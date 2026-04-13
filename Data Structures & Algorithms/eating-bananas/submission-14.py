class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        #   time : O(n logM) - n = length of piles, M = max(piles)
        #   space: O(1)

        l, r = 1, max(piles)    # <-- start at 1

        while l <= r:
            midP = l + (r - l) // 2

            hours = 0
            for eachP in piles:
                hours += math.ceil(eachP / midP)
            
            if hours <= h:
                r = midP - 1
            else:
                l = midP + 1
        
        return l