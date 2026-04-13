class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            if (num - 1) not in numset: # only start counting if it's the start of the sequence
                currentItem = num
                length = 1
                while num + length in numset: #
                    currentItem += 1
                    length += 1
                longest = max(longest, length)

        return longest

