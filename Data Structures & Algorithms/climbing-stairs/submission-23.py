class Solution:
    def climbStairs(self, n: int) -> int:
        # dp - bottom up **space optimized**
        # time : O(n)
        # space: O(1)
        
        if n <= 2: # edge case
            return n

        one = 1
        two = 2

        for i in range(3, n + 1):   # 3 ~ n
            one, two = two, one + two
        
        return two


        # dp - bottom up **space optimized**
        # time : O(n)
        # space: O(1)
        
        if n <= 2: # edge case
            return n

        one = 1
        two = 2

        for i in range(3, n + 1):   # 3 ~ n
            one, two = two, one + two
        
        return two
