class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0

        for num in numSet:
            if num - 1 not in numSet:
                curVal = num
                curLength = 1

                while num + curLength in numSet: ##
                    curVal += 1
                    curLength += 1
                
                maxLength = max(maxLength, curLength)

        return maxLength