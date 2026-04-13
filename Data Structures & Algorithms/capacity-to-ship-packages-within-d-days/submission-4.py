class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search

        l, r = max(weights), sum(weights)
        res = r     # start from the upper bound

        while l <= r:
            m = (l + r) // 2
            requiredDays = 1    # start with day 1
            totalW = 0

            # set requiredDay and totalW
            for curW in weights:
                if totalW + curW > m:   # If I try to add this package to today's ship and it exceeds the limit, I must wait and load it tomorrow.
                    requiredDays += 1
                    totalW = 0
                totalW += curW          # still load the current weight, since every package must be shipped in order.
            
            if requiredDays <= days:    # If current capacity works within the day limit, try smaller capacity
                res = m
                r = m - 1
            else:
                l = m + 1
            
        return res