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
        
        # [merge sort] "recursivly"
        #   time : Best - O(n*logn), Worst - O(n*logn)
        #   space: O(n)
        def mergeSort(nums, l, r):
            if l >= r:
                return
            m = (l + r) // 2
            mergeSort(nums, l, m)
            mergeSort(nums, m + 1, r)
            merge(nums, l, m, r)
        
        def merge(nums, l, m, r):
            numsL = nums[l : m + 1]
            numsR = nums[m + 1 : r + 1]
            i = 0
            j = 0
            k = l
            while i < len(numsL) and j < len(numsR):
                if numsL[i] <= numsR[j]:
                    nums[k] = numsL[i]
                    i += 1
                else:
                    nums[k] = numsR[j]
                    j += 1
                k += 1
            while i < len(numsL):
                nums[k] = numsL[i]
                i += 1
                k += 1
            while j < len(numsR):
                nums[k] = numsR[j]
                j += 1
                k += 1

        # **[quick sort partition]: "ONE PASS SOLUTION" **
        #   time : O(n)
        #   space: O(1)
        def quickSortPartition(nums, l, r):
            i = l
            while i <= r:
                if nums[i] == 0:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
                elif nums[i] == 2:
                    nums[r], nums[i] = nums[i], nums[r]
                    r -= 1
                    i -= 1
                i += 1
            return

        ## Invocations for sorting
        # insertionSort(nums)
        # quickSort(nums, 0, len(nums) - 1)
        # mergeSort(nums, 0, len(nums) - 1)
        quickSortPartition(nums, 0, len(nums) - 1)