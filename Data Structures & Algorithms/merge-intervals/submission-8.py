class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]

        for curStart, curEnd in intervals:
            lastEnd = res[-1][1]
            if lastEnd >= curStart:
                res[-1][1] = max(lastEnd, curEnd)
            else:
                res.append([curStart, curEnd])

        return res