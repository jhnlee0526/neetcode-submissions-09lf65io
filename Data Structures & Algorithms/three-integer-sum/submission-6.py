class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## three pointers
        #### time : O(n^2) : sorting O(n logn) + nested loops O(n^2)
        #### space: O(m) for the output list
        res = []
        # nums.sort() # time : O(n logn)
        sortedNums = self.mergeSort(nums, 0, len(nums) - 1) # time : O(n logn)
        
        for i in range(len(sortedNums)):
            # if current val is the same as the previous val, skip to the next
            if i> 0 and sortedNums[i] == sortedNums[i - 1]:
                continue
            
            l = i + 1
            r = len(sortedNums) - 1
            while l < r:
                sum = sortedNums[i] + sortedNums[l] + sortedNums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([sortedNums[i], sortedNums[l], sortedNums[r]])
                    l += 1 # move just one pt
                    # skip to the next when the current val is the same as the previous one.
                    while l < r and sortedNums[l] == sortedNums[l - 1]:
                        l += 1     
        return res


    # mergeSort(recursive) : time O(n logn), space O(n)
    def mergeSort(self, nums: List[int], l: int, r: int) -> List[int]:
        # base case
        if l >= r:
            return nums
        # devide in half
        m = (l + r) // 2 
        self.mergeSort(nums, l, m)
        self.mergeSort(nums, m + 1, r)
        # compare & merge those two again
        self.merge(nums, l, m, r)
        return nums


    # helper function for merging
    def merge(self, nums: List[int], l: int, m: int, r: int):
        L = nums[l : m + 1]
        R = nums[m + 1 : r + 1]

        i, j, k = 0, 0, l
        # comparing two lists: L v. R
        while i < len(L) and j < len(R): 
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
        
        # adding left-overs
        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1
