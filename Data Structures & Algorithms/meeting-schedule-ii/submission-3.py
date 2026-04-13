"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        maxCount = 0    # result
        curCount = 0
        ptS, ptE = 0, 0 # two pointer

        # separate 'intervals' into two lists (starts & ends), and sort them
        starts = sorted([each.start for each in intervals])
        ends = sorted([each.end for each in intervals])

        while ptS < len(starts):
            if starts[ptS] < ends[ptE]:         # A new meeting is starting before the earliest one ends
                curCount += 1
                ptS += 1
            else:                               # A meeting ended — room freed up
                curCount -= 1
                ptE += 1
            maxCount = max(maxCount, curCount)  # Track peak room usage

        return maxCount