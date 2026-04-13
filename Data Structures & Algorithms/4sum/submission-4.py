class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ## four pointers (two pointers)
        #### time : O(n^2) = O(n logn) + O(n^2)
        #### space: O(m) for the output ~ O(1)
        res = []

        ## Sorting O(n logn)
        # nums.sort()
        sortedNums = self.mergeSort(nums, 0, len(nums) - 1)

        for i in range(len(sortedNums)):
            # skip to the next if the current val is the same as the previous
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue
            
            for j in range(i + 1, len(sortedNums)):
                # skip to the next if the current val is the same as the previous
                if j > i + 1 and sortedNums[j] == sortedNums[j - 1]:
                    continue
                
                l = j + 1
                r = len(sortedNums) - 1
                while l < r:
                    sum = sortedNums[i] + sortedNums[j] + sortedNums[l] + sortedNums[r]
                    if sum > target:
                        r -= 1
                    elif sum < target:
                        l += 1
                    else:
                        res.append([sortedNums[i], sortedNums[j], sortedNums[l], sortedNums[r]])
                        l += 1
                        # skip to the next if the current val is the same as the previous
                        while l < r and sortedNums[l] == sortedNums[l - 1]:
                            l += 1  
        return res


    # def mergeSort(self, arr: List[int], l: int , r: int) -> List[int]:
    def mergeSort(self, arr, l , r):
        if l >= r:
            return arr
        m = (l + r) // 2
        self.mergeSort(arr, l, m)
        self.mergeSort(arr, m + 1, r)
        self.merge(arr, l, m, r)
        return arr

    
    def merge(self, arr: List[int], l: int, m: int, r: int):
        L = arr[l : m + 1]
        R = arr[m + 1 : r + 1]

        i, j, k = 0, 0, l
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

            