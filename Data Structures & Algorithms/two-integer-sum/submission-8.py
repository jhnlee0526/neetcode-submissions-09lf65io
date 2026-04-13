class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            otherNum = target - num
            if otherNum in hashmap:
                # return [i, hashmap.get(otherNum)] if num < otherNum else [hashmap.get(otherNum), i]
                return [hashmap.get(otherNum), i]
            hashmap[num] = i
        return []