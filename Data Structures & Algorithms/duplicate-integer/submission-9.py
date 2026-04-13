class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force O(n^2)
        p1 = 0
        while p1 < len(nums):
            p2 = p1 + 1
            while p2 < len(nums):
                if nums[p1] == nums[p2]:
                    return True
                else: 
                    p2 += 1
            p1 += 1
        return False
