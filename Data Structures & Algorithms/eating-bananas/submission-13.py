class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search on eating speed K
        # time:  O(n · log M), where n = len(piles), M = max(piles)
        # space: O(1)

        # speed must be at least 1, at most the largest pile
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2

            # compute hours needed at speed = mid
            hours = 0
            for pile in piles:
                # ceil(pile / mid) without floating point
                hours += (pile + mid - 1) // mid

            # if we can finish within H hours, try slower
            if hours <= h:
                r = mid - 1
            else:
                # too slow—need to increase speed
                l = mid + 1

        # when loop ends, l is the smallest valid speed
        return l
