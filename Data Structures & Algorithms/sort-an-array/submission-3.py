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

        ## Insertion Sort: time O(n^2), space O(1)
        # for i in range(1, len(nums)):
        #     j = i - 1
        #     while j >= 0 and nums[j] > nums[j + 1]:
        #         nums[j], nums[j + 1] = nums[j + 1], nums[j]
        #         j -= 1
        # return nums

        ## Merge Sort: time O(n*logn), space O(1)
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