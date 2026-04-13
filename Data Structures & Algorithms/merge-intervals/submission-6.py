class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ## [Greedy] avoiding sorting to get better than O(n logn) time
        #### time : O(n + max_val)
        #### space: O(max_val), the mp array increases memory use depending on interval spread
        
        # Step 1: Find the maximum starting value in the intervals
        # This determines the size of the `mp` array that tracks interval end points.
        max_val = max(interval[0] for interval in intervals)  # O(n) time complexity

        # Step 2: Create a mapping array (`mp`) initialized to zeros.
        # `mp[start]` will store the maximum end point encountered for that start index.
        mp = [0] * (max_val + 1)  # Space complexity: O(max_val)

        # Step 3: Populate the `mp` array with the highest end seen for each start point.
        for start, end in intervals:  # Iterates over intervals → O(n) time
            mp[start] = max(end + 1, mp[start])  # Store max end + 1 for merging

        # Step 4: Iterate over the `mp` array and merge intervals greedily.
        res = []  # Stores the merged intervals
        have = -1  # Keeps track of the furthest end in an active merge
        interval_start = -1  # Stores the beginning of the current merged interval
        
        for i in range(len(mp)):  # Iterate through all possible start values (O(max_val))
            if mp[i] != 0:  # If we encounter a valid interval start
                if interval_start == -1:  # If no merge in progress, start a new one
                    interval_start = i
                have = max(mp[i] - 1, have)  # Update the furthest reach of the merge

            if have == i:  # If we reach the end of a merged segment
                res.append([interval_start, have])  # Save the merged interval
                have = -1  # Reset merging state
                interval_start = -1  # Reset start index

        # Step 5: If there's an unfinished interval left after iteration, store it.
        if interval_start != -1:
            res.append([interval_start, have])

        return res


        
        ## [Sorting]
        #### time : O(n logn)
        #### space: O(n) for the output list

    #     # intervals.sort(key=lambda each: each[0]) # time O(n logn)
    #     self.mergeSort(intervals, 0, len(intervals) - 1) # time O(n logn)
    #     res = [intervals[0]]
        
    #     for start, end in intervals[1:]:
    #         lastEnd = res[-1][1] #res[-1] is the last item on the list
    #         if lastEnd >= start:
    #             res[-1][1] = max(lastEnd, end) # [1, 5], [2, 4] -> [1, 5]
    #         else:
    #             res.append([start, end])
        
    #     return res

    # # MERGE SORT : time O(n logn) 
    # def mergeSort(self, arr, l, r):
    #     if l >= r:
    #         return
    #     m = (l + r) // 2
    #     self.mergeSort(arr, l, m)
    #     self.mergeSort(arr, m + 1, r)
    #     self.mergeLists(arr, l, m, r)

    # def mergeLists(self, arr, l, m, r):
    #     L = arr[l : m + 1]
    #     R = arr[m + 1 : r + 1]

    #     i, j = 0, 0
    #     k = l
    #     while i < len(L) and j < len(R):
    #         if L[i][0] <= R[j][0]:
    #             arr[k] = L[i]
    #             i += 1
    #         else:
    #             arr[k] = R[j]
    #             j += 1
    #         k += 1
        
    #     while i < len(L):
    #         arr[k] = L[i]
    #         i += 1
    #         k += 1
    #     while j < len(R):
    #         arr[k] = R[j]
    #         j += 1
    #         k += 1
