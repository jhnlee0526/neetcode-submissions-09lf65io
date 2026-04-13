class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # [insertion sort] "iteratively"
        #   time : Best - O(n) already sorted, Worst - O(n^2)
        #   space: O(1)
        def insertionSort(nums):
            for i in range(0, len(nums)):
                j = i - 1
                while j >= 0 and nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    j -= 1
            return 

        # [quick sort] "recursively"
        #   time : Best - O(n*logn), Worst - O(n^2) already sorted
        #   space: O(logn)
        def quickSort(nums, l, r):
            if l >= r:
                return
            pivot = nums[r]
            leftPt = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[leftPt], nums[i] = nums[i], nums[leftPt]
                    leftPt += 1
            nums[leftPt], nums[r] = nums[r], nums[leftPt]
            quickSort(nums, l, leftPt - 1)
            quickSort(nums, leftPt + 1, r)
            

        ## Invocations for sorting
        # insertionSort(nums)
        quickSort(nums, 0, len(nums) - 1)