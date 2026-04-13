class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniquePt = 1
        for scannerPt in range(1, len(nums)):
            # compare the val at scannerPt with the previous val
            if nums[scannerPt] != nums[scannerPt - 1]:
                nums[uniquePt] = nums[scannerPt]
                uniquePt += 1
        
        return uniquePt