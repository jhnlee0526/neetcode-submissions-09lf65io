class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ## [Sorting]
        #### time : O(n logn)
        #### space: O(n) for the output list

        # intervals.sort(key=lambda each: each[0]) # time O(n logn)
        self.mergeSort(intervals, 0, len(intervals) - 1) # time O(n logn)
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = res[-1][1] #res[-1] is the last item on the list
            if lastEnd >= start:
                res[-1][1] = max(lastEnd, end) # [1, 5], [2, 4] -> [1, 5]
            else:
                res.append([start, end])
        
        return res

    # MERGE SORT : time O(n logn) 
    def mergeSort(self, arr, l, r):
        if l >= r:
            return
        m = (l + r) // 2
        self.mergeSort(arr, l, m)
        self.mergeSort(arr, m + 1, r)
        self.mergeLists(arr, l, m, r)

    def mergeLists(self, arr, l, m, r):
        L = arr[l : m + 1]
        R = arr[m + 1 : r + 1]

        i, j = 0, 0
        k = l
        while i < len(L) and j < len(R):
            if L[i][0] <= R[j][0]:
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
