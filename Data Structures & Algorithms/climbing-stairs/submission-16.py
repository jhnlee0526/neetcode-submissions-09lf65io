class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: #edge case
            return n

        one = 1 # way to reach step 1
        two = 2 # way to reach step 2
        
        for i in range(3, n + 1): # start from step3 up to (n + 1)
            one, two = two, one + two
        
        return two