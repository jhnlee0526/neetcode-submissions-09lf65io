class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #   Time : O(n)
        #   Space: O(n)

        numSet = set(nums)  # {num, ..}
        maxLength = 0

        for num in nums:
            curLength = 0
            if num - 1 not in numSet:   ##
                curLength = 1
                while num + curLength in numSet:
                    curLength += 1
            maxLength = max(maxLength, curLength)

        return maxLength