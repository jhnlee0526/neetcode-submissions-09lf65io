class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = defaultdict(int)
        for n in nums:
            if dict[n] == 1:
                return True
            dict[n] += 1
        return False