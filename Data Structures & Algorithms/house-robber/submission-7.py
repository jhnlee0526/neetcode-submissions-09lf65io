class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for curHouse in nums:
            rob1, rob2 = rob2, max(curHouse + rob1, rob2)
        
        return rob2