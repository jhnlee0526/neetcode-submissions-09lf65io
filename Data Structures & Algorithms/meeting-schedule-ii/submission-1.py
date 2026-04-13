class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # [Two Pointers] with sorting
        # Time: O(n log n) — for sorting start and end times
        # Space: O(n) — storing sorted start and end arrays

        # Extract and sort all start and end times
        starts = sorted([each.start for each in intervals])
        ends = sorted([each.end for each in intervals])

        maxCnt = curCnt = 0
        ptS = ptE = 0  # Pointers to iterate through starts and ends

        while ptS < len(intervals):
            if starts[ptS] < ends[ptE]:
                # A new meeting is starting before the earliest one ends
                curCnt += 1
                ptS += 1
            else:
                # A meeting ended — room freed up
                curCnt -= 1
                ptE += 1

            maxCnt = max(maxCnt, curCnt)  # Track peak room usage

        return maxCnt