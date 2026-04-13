class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #   Time : O(n) - visits each number once
        #   Space: O(n) - hashset
        
        # edge case
        if not nums:
            return False

        numMap = set()  # {num1, num2, ..}
        
        for num in nums:
            if num in numMap:
                return True
            numMap.add(num)
        
        return False
        