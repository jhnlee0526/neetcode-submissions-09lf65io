class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ## Brute Force : time O(n^2) space O(1)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             j += 1
        #     i += 1
        # return nums


        ## Insertion Sort: "iteratively" 
        #### time - Best(already sorted): O(n), WorstO(n^2)
        #### space O(1)
        # for i in range(1, len(nums)):
        #     j = i - 1
        #     while j >= 0 and nums[j] > nums[j + 1]:
        #         nums[j], nums[j + 1] = nums[j + 1], nums[j]
        #         j -= 1
        # return nums
        

        ## Quick Sort (UNSTABLE): "recursively" 
        #### time - Average: O(n log n), Worst: O(n²) (when pivot is always min/max — e.g., sorted input)
        #### space - Best/Average: O(log n), Worst: O(n) due to call stacks
        # def quickSort(nums, l, r):
        #     if l >= r:
        #         return
        #     pivot = nums[r]
        #     leftPt = l # pointer for swapping
        #     for i in range(l, r):
        #         if nums[i] < pivot:
        #             nums[i], nums[leftPt] = nums[leftPt], nums[i]
        #             leftPt += 1
        #     nums[r], nums[leftPt] = nums[leftPt], nums[r]

        #     quickSort(nums, l, leftPt - 1)
        #     quickSort(nums, leftPt + 1, r)

        # quickSort(nums, 0, len(nums) - 1)
        # return nums


        ## Merge Sort (STABLE): "recursively" time O(n*logn), space O(n)
        def mergeSort(nums, l, r):
            if l >= r: # base case
                return
            
            m = (l + r) // 2
            # device & conquer
            mergeSort(nums, l, m)
            mergeSort(nums, m + 1, r)
            merge(nums, l, m, r)

        def merge(nums, l, m, r):
            L = nums[l : m + 1]
            R = nums[m + 1 : r + 1]

            i = 0
            j = 0
            k = l
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1
            
            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1
            
            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1
        
        mergeSort(nums, 0, len(nums) - 1) # Invocation of the mergeSort()
        return nums