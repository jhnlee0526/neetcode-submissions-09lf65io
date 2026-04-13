class Solution:
    def climbStairs(self, n: int) -> int:
        ## dp: bottom up (space optimized)
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one