class Solution:
    def reverse(self, x: int) -> int:
        # Input example:
        # x = 123 → we want to reverse digits to get 321

        # Define bounds for 32-bit signed integers:
        minInt = -1 << 31         # = -2,147,483,648
        maxInt = (1 << 31) - 1    # =  2,147,483,647

        res = 0  # Initialize reversed number

        while x:
            # Step 1: Take last digit from x
            # First iteration: x = 123 → digit = 123 % 10 = 3
            digit = int(math.fmod(x, 10))
            '''x % 10 behaves weirdly with negative numbers — the result is always non-negative.'''
            # digit = x % 10

            # Step 2: Chop off the last digit
            # x = 123 // 10 = 12
            x = int(x / 10)
            '''x // 10 behaves weirdly with negative numbers'''
            

            # Step 3: Check if res will overflow after adding digit
            # Example: res = 0 → safe to proceed
            if (
                res > maxInt // 10 or
                (res == maxInt // 10 and digit > maxInt % 10)
            ):
                return 0  # Overflow check failed

            if (
                res < minInt // 10 or
                (res == minInt // 10 and digit < minInt % 10)
            ):
                return 0  # Underflow check failed

            # Step 4: Build the reversed number
            # res = res * 10 + digit → res = 0 * 10 + 3 = 3
            res = (res * 10) + digit

            # Loop continues:
            # Next iteration: x = 12 → digit = 2 → res = 3 * 10 + 2 = 32
            # Next iteration: x = 1 → digit = 1 → res = 32 * 10 + 1 = 321

        return res  # Final reversed integer
