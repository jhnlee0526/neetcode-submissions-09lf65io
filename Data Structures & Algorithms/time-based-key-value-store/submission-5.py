class TimeMap:

    def __init__(self):
        self.map = {}   # {key : [(value, timestamp), ...], ...}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # [binary search] for latest value with timestamp ≤ target
        #   Time : O(log n)
        #   Space: O(1)

        res = ''
        valsList = self.map.get(key, [])    # [(value, timestamp), ...]

        l, r = 0, len(valsList) - 1
        while l <= r:
            m = l + (r - l) // 2
            
            if valsList[m][1] <= timestamp:
                res = valsList[m][0]        # candidate value
                l = m + 1                   # search right for newer timestamp
            else:
                r = m - 1                   # search left
        
        return res


        
        
