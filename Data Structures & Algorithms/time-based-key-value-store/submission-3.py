class TimeMap:

    def __init__(self):
        self.map = {} # {key : [value, timestamp], }


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        res = ''
        vals = self.map.get(key, []) # [[val, timestamps], ..]

        # binary search
        l, r = 0, len(vals) - 1
        while l <= r:
            m = l + (r - l) // 2
            
            if vals[m][1] <= timestamp:
                res = vals[m][0]
                l = m + 1
            else:
                r = m - 1

        return res

        
