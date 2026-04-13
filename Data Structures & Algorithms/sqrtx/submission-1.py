class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        #   time : O(log n)
        #   space: O(1)

        l, r = 1, x
        while l <= r:
            m = l + (r - l) // 2
            
            if m ** 2 <= x:
                l = m + 1
            else:
                r = m - 1
            
        return r
        # Last-true (most): return r
        # First-true (least): return l
