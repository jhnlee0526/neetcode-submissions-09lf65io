class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap
        #   Time : O(n)
        #   Space: O(n)

        seen = {}   # {num : index, ..}
        for i, num in enumerate(nums):
            other_num = target - num
            if other_num in seen:
                return [seen[other_num], i]
            seen[num] = i