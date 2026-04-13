class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## Using Hash Set:
        #### time : O(n)
        #### space: 0(n)
        numset = set(nums)
        longest = 0

        for item in numset:
            # only start counting if it's the start of the sequence
            if (item - 1) not in numset:
                curItem = item
                length = 1
                
                while item + length in numset:
                    curItem += 1
                    length += 1
                    
                longest = max(longest, length)
        
        return longest
