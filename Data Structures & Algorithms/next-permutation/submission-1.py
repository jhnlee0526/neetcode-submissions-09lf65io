class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [ O(n) In-Place Version ]
        ## time : O(n)
        ## space: O(1)
        """
        🚫 Not Greedy
            - Greedy means making the best local decision at every step to reach a global optimum.
            - In nextPermutation, we don’t choose the “best” number to swap at every index — instead, we find a specific pivot point, do one targeted swap, and then reverse a suffix.
            - It’s more like following a recipe than following instincts.
        🚫 Not BFS
            - BFS is about exploring all possibilities level by level (like with permutations or coin change).
            - Here, we aren’t exploring all permutations — we’re making one surgical transformation to go to the very next permutation in lexicographic order.
        """

        # Step 1: find the pivot index
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: find the number just larger than nums[i] after index i
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap them
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: reverse the suffix starting at i+1
        l, r = i + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        


        