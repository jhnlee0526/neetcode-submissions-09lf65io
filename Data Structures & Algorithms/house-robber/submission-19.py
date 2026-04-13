class Solution:
    def rob(self, nums: List[int]) -> int:
        # ✅ Bottom-Up DP — OPTIMAL SPACE (O(1))
        #   Time : O(n) — iterate through all houses once
        #   Space: O(1) — only two variables tracked

        rob1 = 0  # max money robbed from houses 0 to i-2
        rob2 = 0  # max money robbed from houses 0 to i-1

        # Compute max if we rob this house (rob1 + amount) vs skip it (rob2)
        for amount in nums:
            rob1, rob2 = rob2, max(rob2, rob1 + amount)
            ''' After this line:
                - rob1 becomes previous rob2 (i-1)
                - rob2 becomes MAX MONEY robbed up to current house (i) '''

        # rob2 now holds the max money robbed from all houses
        return rob2