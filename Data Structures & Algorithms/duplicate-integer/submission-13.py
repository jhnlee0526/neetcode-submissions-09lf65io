class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            if num not in numSet:
                numSet.add(num)
            else:
                return True
        
        return False
