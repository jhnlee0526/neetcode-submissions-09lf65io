# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # binary search
        #   time : O(log n)
        #   space: O(1)

        l, r = 1, n
        while l <= r:
            m = l + (r - l) // 2

            guessPick = guess(m)

            if guessPick > 0:
                l = m + 1
            elif guessPick < 0:
                r = m - 1
            else:
                return m
        