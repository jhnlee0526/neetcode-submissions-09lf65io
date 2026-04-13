class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # time : O(n logn)
        # space: O(n)
        
        # minheap 
        # loop to get the res

        mergedIntervals = []
        heapq.heapify(intervals)                            # O(n)

        while intervals:                                    # O(n) -> O(n log n)
            curStart, curEnd = heapq.heappop(intervals)     # O(log n)
            if (
                len(mergedIntervals) > 0 and
                mergedIntervals[-1][1] >= curStart
            ):
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1], curEnd)
            else:
                mergedIntervals.append([curStart, curEnd])

        return mergedIntervals