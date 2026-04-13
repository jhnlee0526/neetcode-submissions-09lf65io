class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsDict = defaultdict(int)
        for n in nums:
            if n in numsDict:
                return True
            else:
                numsDict[n] += 1
        return False