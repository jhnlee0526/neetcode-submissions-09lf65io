class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hashset (better)
        #   Time : O(n)
        #   Space: O(n)

        if len(nums) <= 1:
            return False
        
        numset = set()
        for num in nums:
            if num in numset:
                return True
            numset.add(num)
        
        return False

        #------------------------
        # Hashset
        #   Time : O(n)
        #   Space: O(n)

        # edge case
        if len(nums) <= 1:
            return False
        
        numset = set(nums)
        return True if len(numset) != len(nums) else False
        

