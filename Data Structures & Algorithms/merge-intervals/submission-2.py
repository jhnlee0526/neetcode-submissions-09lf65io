class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda each: each[0]) # time O(n logn)
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = res[-1][1] #res[-1] is the last item on the list
            if lastEnd >= start:
                res[-1][1] = max(lastEnd, end) # [1, 5], [2, 4] -> [1, 5]
            else:
                res.append([start, end])
        
        return res
        
                
