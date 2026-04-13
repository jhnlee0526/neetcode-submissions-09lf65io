class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapq.heapify(intervals)
        res = []

        while intervals:
            start, end = heapq.heappop(intervals)

            if not res or start > res[-1][1]:
                res.append([start, end])
            else:
                res[-1][1] = max(end, res[-1][1])

        return res