class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #   Time : O(n)
        #   Space: O(n)

        max_length = 0

        num_set = set(nums) # {num, ..}
        for num in nums:
            cur_length = 0

            if num - 1 not in num_set:
                cur_length = 1
                while num + cur_length in num_set:
                    cur_length += 1
                
            max_length = max(max_length, cur_length)

        return max_length
