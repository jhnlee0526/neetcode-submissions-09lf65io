class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # [Sum Trick]
        ## time : O(n) 
        ## space: O(1)

        # Total numbers from 0 to n (inclusive)
        total_count = len(nums)
        '''
            Expected sum of all numbers from 0 to n using Gauss' formula:
            0 + 1 + 2 + ... + n = n * (n + 1) // 2
            This comes from pairing numbers from opposite ends:
            (0 + n), (1 + n-1), (2 + n-2), ... all equal (n + 0)
            There are (n + 1) numbers total, and the average value is n / 2
            So the sum is: number of terms * average = (n + 1) * n // 2
        '''
        # expected_sum = sum(range(total_count + 1)) # 0 ~ (total_count + 1)
        expected_sum = total_count * (total_count + 1) // 2

        # Actual sum of the numbers provided (with one missing)
        actual_sum = sum(nums)

        # The missing number is just the difference
        missing = expected_sum - actual_sum

        return missing