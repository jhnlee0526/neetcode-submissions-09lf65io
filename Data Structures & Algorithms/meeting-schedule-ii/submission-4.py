"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # [Two pointers]
        ## time : O(n log n) - sorting
        ## space: O(n)
        
        # Create 'maxCnt' for result
        # Create 'resCnt' for tracking meeting count
        # Create 'ptS' & 'ptE' for two pointers
        # Have separated sorted lists for each starts and ends
        # Run a while loop until ptS is valid

        maxCnt = 0
        resCnt = 0
        ptS = ptE = 0

        starts = sorted([each.start for each in intervals])
        ends = sorted([each.end for each in intervals])

        while ptS < len(starts):
            if starts[ptS] < ends[ptE]: # new meetings starting
                resCnt += 1
                ptS += 1
            else:                       # a meeting has ended
                resCnt -= 1
                ptE += 1
            
            maxCnt = max(maxCnt, resCnt)# find the max count
        
        return maxCnt