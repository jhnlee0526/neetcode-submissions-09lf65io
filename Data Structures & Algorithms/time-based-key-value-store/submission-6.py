class TimeMap:

    def __init__(self):
        # {key : string+timestamp list, key : [(value, timestamps), ..], ..}
        self.timeMap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        # Binary Search
        #   time : O(log n)
        #   space: O(1)
        
        foundValue = ""

        vals = self.timeMap.get(key, []) #  [(value, timestamps), ..]
        
        l, r = 0, len(vals) - 1
        while l <= r:
            m = l + (r - l) // 2

            if vals[m][1] <= timestamp:
                foundValue = vals[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return foundValue

