class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            rob1 = max money if you skipped the previous house (i.e., two houses ago)
            rob2 = max money if you considered up to the previous house
                 = The BEST amount so far including or skipping the previous house
        """
        rob1, rob2 = 0, 0
        for curHouse in nums:
            rob1, rob2 = rob2, max(rob1 + curHouse, rob2)
        
        return rob2