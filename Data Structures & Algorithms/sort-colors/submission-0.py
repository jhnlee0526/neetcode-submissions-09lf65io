class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # [insertion sort]
        #   time: Best - O(n) already sorted, Worst - O(n^2)
        #   space: O(1)
        def insertionSort(nums):
            for i in range(0, len(nums)):
                j = i - 1
                while j >= 0 and nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    j -= 1
            return 

        insertionSort(nums)