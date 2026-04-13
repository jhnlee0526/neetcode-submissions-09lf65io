class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        heapq.heapify(intervals) # minheap

        while intervals:
            start, end = heapq.heappop(intervals)
            if len(res) > 0 and start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)

            else:
                res.append([start, end])

        return res