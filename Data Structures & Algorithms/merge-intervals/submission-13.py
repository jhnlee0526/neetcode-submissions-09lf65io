class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        heapq.heapify(intervals)

        while intervals:
            start, end = heapq.heappop(intervals)
            if not res or start > res[-1][1]:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)

        return res