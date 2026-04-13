class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for n in nums:
            if dict.get(n, 0) == 1:
                return True
            dict[n] = dict.get(n, 0) + 1
        return False